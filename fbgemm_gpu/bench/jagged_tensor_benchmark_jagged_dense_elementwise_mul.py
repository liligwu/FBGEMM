# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import logging

import click
import fbgemm_gpu
import torch

logging.basicConfig(level=logging.DEBUG)

# pyre-fixme[16]: Module `fbgemm_gpu` has no attribute `open_source`.
open_source: bool = getattr(fbgemm_gpu, "open_source", False)

if open_source:
    # pyre-ignore[21]
    from bench_utils import benchmark_torch_function
else:
    from fbgemm_gpu.bench.bench_utils import benchmark_torch_function

    torch.ops.load_library("//deeplearning/fbgemm/fbgemm_gpu:sparse_ops")
    torch.ops.load_library("//deeplearning/fbgemm/fbgemm_gpu:sparse_ops_cpu")


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option("--batch-size", type=int, default=128)
@click.option("--embedding-dim", type=int, default=128)
@click.option("--max-len", type=int, default=128)
@click.option("--elem-type", type=str, default="half")
def device(
    batch_size: int,
    embedding_dim: int,
    max_len: int,
    elem_type: str,
) -> None:
    lengths = torch.randint(max_len, size=(batch_size,))
    total_lengths = lengths.sum().item()
    offsets = torch.ops.fbgemm.asynchronous_complete_cumsum(lengths)

    dtype = (
        torch.float16
        if elem_type == "half" or elem_type == "float16"
        else torch.float32
    )

    # pyre-fixme[6]: For 1st param expected `int` but got `Union[bool, float, int]`.
    values_2d = torch.rand(total_lengths, embedding_dim, dtype=dtype)

    if torch.cuda.is_available():
        offsets = offsets.cuda()
        values_2d = values_2d.cuda()

    output = torch.load('jagged_to_dense_output.pt')
    offsets_nbytes = offsets.numel() * offsets.element_size()
    values_nbytes = values_2d.numel() * values_2d.element_size()
    dense_nbytes = output.numel() * output.element_size()

    num_bytes = offsets_nbytes + values_nbytes + dense_nbytes

    time, jagged_output = benchmark_torch_function(
        torch.ops.fbgemm.jagged_dense_elementwise_mul,
        (values_2d, [offsets], output),
        iters=1000,
    )
    num_bytes = offsets_nbytes + 3 * values_nbytes
    logging.info(
        f"jagged_dense_elementwise_mul {time} sec {num_bytes / time / 1e9} GB/s"
    )

if __name__ == "__main__":
    cli()
