################################################################################
## GENERATED FILE INFO
##
## Template Source: training/python/split_embedding_codegen_lookup_invoker.template
################################################################################

__template_source_file__ = "training/python/split_embedding_codegen_lookup_invoker.template"

#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# pyre-ignore-all-errors

import torch
from .lookup_args import *






def invoke(
    common_args: CommonArgs,
    optimizer_args: OptimizerArgs,
    momentum1: Momentum,
    prev_iter: Momentum,
    row_counter: Momentum,
    iter: int,
    max_counter: float,
    apply_global_weight_decay: bool = False,
    gwd_lower_bound: float = 0.0,
    mixed_D: bool = True,
) -> torch.Tensor:
    # host_weights is only used for CPU training
    use_cpu = common_args.host_weights.numel() > 0
    vbe_metadata = common_args.vbe_metadata

    # pack weights
    weights = [
        common_args.dev_weights,
        common_args.uvm_weights,
        common_args.weights_placements,
        common_args.weights_offsets,
        common_args.lxu_cache_weights,
    ] if not use_cpu else [
        common_args.host_weights,
        common_args.weights_placements,
        common_args.weights_offsets,
    ]
    dict_aux_tensor: Dict[str, Optional[torch.Tensor]] = {
        "B_offsets": vbe_metadata.B_offsets,
        "vbe_output_offsets_feature_rank": vbe_metadata.output_offsets_feature_rank,
        "vbe_B_offsets_rank_per_feature": vbe_metadata.B_offsets_rank_per_feature,
        "lxu_cache_locations": common_args.lxu_cache_locations,
        "uvm_cache_stats": common_args.uvm_cache_stats,
    }

    dict_aux_int: Dict[str, int] = {
        "iter": iter, 
        "info_B_num_bits": common_args.info_B_num_bits, 
        "info_B_mask": common_args.info_B_mask,
    }
    
    dict_aux_float: Dict[str, float] = {
        "gwd_lower_bound": gwd_lower_bound,
    }

    dict_aux_bool: Dict[str, bool] = {
        "is_experimental_tbe": common_args.is_experimental,
        "use_uniq_cache_locations_bwd": common_args.use_uniq_cache_locations_bwd,
        "use_homogeneous_placements": common_args.use_homogeneous_placements,
        "apply_global_weight_decay": apply_global_weight_decay,
        "mixed_D": mixed_D,
    }
    dict_optim_int: Dict[str, int] = {}
    dict_optim_float: Dict[str, float] = {}
    dict_optim_bool: Dict[str, bool] = {}

    # Explicitly pass only prev_iter_dev for global weight decay, unless it already exists in optim arg
    dict_aux_tensor["prev_iter_dev"] = prev_iter.dev
    

    # optimizer_args # if optimizer == none
    dict_aux_bool["gradient_clipping"] = optimizer_args.gradient_clipping
    dict_aux_float["max_gradient"] = optimizer_args.max_gradient
    dict_aux_bool["stochastic_rounding"] = optimizer_args.stochastic_rounding
    dict_optim_float["eps"] = optimizer_args.eps
    dict_optim_float["weight_decay"] = optimizer_args.weight_decay
    dict_optim_int["weight_decay_mode"] = optimizer_args.weight_decay_mode
    dict_optim_int["counter_halflife"] = optimizer_args.counter_halflife
    dict_optim_int["adjustment_iter"] = optimizer_args.adjustment_iter
    dict_optim_float["adjustment_ub"] = optimizer_args.adjustment_ub
    dict_optim_int["learning_rate_mode"] = optimizer_args.learning_rate_mode
    dict_optim_int["grad_sum_decay"] = optimizer_args.grad_sum_decay
    dict_optim_float["tail_id_threshold"] = optimizer_args.tail_id_threshold
    dict_optim_int["is_tail_id_thresh_ratio"] = optimizer_args.is_tail_id_thresh_ratio
    dict_optim_float["weight_norm_coefficient"] = optimizer_args.weight_norm_coefficient
    dict_optim_float["lower_bound"] = optimizer_args.lower_bound
    dict_optim_int["regularization_mode"] = optimizer_args.regularization_mode
    dict_optim_float["max_counter"] = max_counter
    
    momentum1_list = [
        momentum1.dev,
        momentum1.uvm,
        momentum1.placements,
        momentum1.offsets,
    ] if not use_cpu else [
        momentum1.host,
        momentum1.placements,
        momentum1.offsets,
    ] if momentum1 is not None else None
    
    prev_iter_list = [
        prev_iter.dev,
        prev_iter.uvm,
        prev_iter.placements,
        prev_iter.offsets,
    ] if not use_cpu else [
        prev_iter.host,
        prev_iter.placements,
        prev_iter.offsets,
    ] if prev_iter is not None else None
    
    row_counter_list = [
        row_counter.dev,
        row_counter.uvm,
        row_counter.placements,
        row_counter.offsets,
    ] if not use_cpu else [
        row_counter.host,
        row_counter.placements,
        row_counter.offsets,
    ] if row_counter is not None else None

    
    aux_tensor: List[Optional[torch.Tensor]] = []
    assert "B_offsets" in dict_aux_tensor, (
        "B_offsets must be in dict_aux_tensor. "
        "Please check the frontend and backend version. "
    )
    aux_tensor.append(dict_aux_tensor["B_offsets"])
    assert "vbe_output_offsets_feature_rank" in dict_aux_tensor, (
        "vbe_output_offsets_feature_rank must be in dict_aux_tensor. "
        "Please check the frontend and backend version. "
    )
    aux_tensor.append(dict_aux_tensor["vbe_output_offsets_feature_rank"])
    assert "vbe_B_offsets_rank_per_feature" in dict_aux_tensor, (
        "vbe_B_offsets_rank_per_feature must be in dict_aux_tensor. "
        "Please check the frontend and backend version. "
    )
    aux_tensor.append(dict_aux_tensor["vbe_B_offsets_rank_per_feature"])
    assert "lxu_cache_locations" in dict_aux_tensor, (
        "lxu_cache_locations must be in dict_aux_tensor. "
        "Please check the frontend and backend version. "
    )
    aux_tensor.append(dict_aux_tensor["lxu_cache_locations"])
    assert "uvm_cache_stats" in dict_aux_tensor, (
        "uvm_cache_stats must be in dict_aux_tensor. "
        "Please check the frontend and backend version. "
    )
    aux_tensor.append(dict_aux_tensor["uvm_cache_stats"])
    assert "prev_iter_dev" in dict_aux_tensor, (
        "prev_iter_dev must be in dict_aux_tensor. "
        "Please check the frontend and backend version. "
    )
    aux_tensor.append(dict_aux_tensor["prev_iter_dev"])
    
    aux_int: List[int] = []
    assert "iter" in dict_aux_int, (
        "iter must be in dict_aux_int. "
        "Please check the frontend and backend version. "
    )
    aux_int.append(dict_aux_int["iter"])
    assert "info_B_num_bits" in dict_aux_int, (
        "info_B_num_bits must be in dict_aux_int. "
        "Please check the frontend and backend version. "
    )
    aux_int.append(dict_aux_int["info_B_num_bits"])
    assert "info_B_mask" in dict_aux_int, (
        "info_B_mask must be in dict_aux_int. "
        "Please check the frontend and backend version. "
    )
    aux_int.append(dict_aux_int["info_B_mask"])
    
    aux_float: List[float] = []
    assert "gwd_lower_bound" in dict_aux_float, (
        "gwd_lower_bound must be in dict_aux_float. "
        "Please check the frontend and backend version. "
    )
    aux_float.append(dict_aux_float["gwd_lower_bound"])
    assert "max_gradient" in dict_aux_float, (
        "max_gradient must be in dict_aux_float. "
        "Please check the frontend and backend version. "
    )
    aux_float.append(dict_aux_float["max_gradient"])
    
    aux_bool: List[bool] = []
    assert "is_experimental_tbe" in dict_aux_bool, (
        "is_experimental_tbe must be in dict_aux_bool. "
        "Please check the frontend and backend version. "
    )
    aux_bool.append(dict_aux_bool["is_experimental_tbe"])
    assert "use_uniq_cache_locations_bwd" in dict_aux_bool, (
        "use_uniq_cache_locations_bwd must be in dict_aux_bool. "
        "Please check the frontend and backend version. "
    )
    aux_bool.append(dict_aux_bool["use_uniq_cache_locations_bwd"])
    assert "use_homogeneous_placements" in dict_aux_bool, (
        "use_homogeneous_placements must be in dict_aux_bool. "
        "Please check the frontend and backend version. "
    )
    aux_bool.append(dict_aux_bool["use_homogeneous_placements"])
    assert "apply_global_weight_decay" in dict_aux_bool, (
        "apply_global_weight_decay must be in dict_aux_bool. "
        "Please check the frontend and backend version. "
    )
    aux_bool.append(dict_aux_bool["apply_global_weight_decay"])
    assert "gradient_clipping" in dict_aux_bool, (
        "gradient_clipping must be in dict_aux_bool. "
        "Please check the frontend and backend version. "
    )
    aux_bool.append(dict_aux_bool["gradient_clipping"])
    assert "stochastic_rounding" in dict_aux_bool, (
        "stochastic_rounding must be in dict_aux_bool. "
        "Please check the frontend and backend version. "
    )
    aux_bool.append(dict_aux_bool["stochastic_rounding"])
    assert "mixed_D" in dict_aux_bool, (
        "mixed_D must be in dict_aux_bool. "
        "Please check the frontend and backend version. "
    )
    aux_bool.append(dict_aux_bool["mixed_D"])

    # optim_int
    optim_int: List[int] = []
    optim_int.append(dict_optim_int["counter_halflife"])
    optim_int.append(dict_optim_int["adjustment_iter"])
    optim_int.append(dict_optim_int["learning_rate_mode"])
    optim_int.append(dict_optim_int["weight_decay_mode"])
    optim_int.append(dict_optim_int["grad_sum_decay"])
    optim_int.append(dict_optim_int["is_tail_id_thresh_ratio"])
    optim_int.append(dict_optim_int["regularization_mode"])
    # optim_float
    # ['momentum1', 'prev_iter', 'row_counter', 'learning_rate_tensor', 'optim_int', 'optim_float']
    optim_float: List[float] = []
    optim_float.append(dict_optim_float["eps"])
    optim_float.append(dict_optim_float["weight_decay"])
    optim_float.append(dict_optim_float["adjustment_ub"])
    optim_float.append(dict_optim_float["max_counter"])
    optim_float.append(dict_optim_float["tail_id_threshold"])
    optim_float.append(dict_optim_float["weight_norm_coefficient"])
    optim_float.append(dict_optim_float["lower_bound"])
    # optim_bool 

    return torch.ops.fbgemm.split_embedding_codegen_lookup_rowwise_adagrad_with_counter_function_pt2(
        # common_args
        placeholder_autograd_tensor=common_args.placeholder_autograd_tensor,
        # weights
        weights=weights,
        D_offsets=common_args.D_offsets,
        total_D=common_args.total_D,
        max_D=common_args.max_D,
        hash_size_cumsum=common_args.hash_size_cumsum,
        total_hash_size_bits=common_args.total_hash_size_bits,
        indices=common_args.indices,
        offsets=common_args.offsets,
        pooling_mode=common_args.pooling_mode,
        indice_weights=common_args.indice_weights,
        feature_requires_grad=common_args.feature_requires_grad,
        output_dtype=common_args.output_dtype,
        # VBE metadata
        max_B=vbe_metadata.max_B,
        max_B_feature_rank=vbe_metadata.max_B_feature_rank,
        vbe_output_size=vbe_metadata.output_size,
        # aux_tensor
        aux_tensor=aux_tensor,
        # aux_int
        aux_int=aux_int,
        # aux_float
        aux_float=aux_float,
        # aux_bool
        aux_bool=aux_bool,
        learning_rate_tensor=common_args.learning_rate_tensor,

        # momentum1
        momentum1 = momentum1_list,
        # momentum2
        # prev_iter
        prev_iter=prev_iter_list,
        # row_counter
        row_counter=row_counter_list,
        # optim_tensor
        # optim_int
        optim_int=optim_int,
        # optim_float
        optim_float=optim_float,
        # optim_bool
        # optim symint args
        # total_unique_indices
    )