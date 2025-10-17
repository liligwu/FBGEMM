################################################################################
## GENERATED FILE INFO
##
## Template Source: training/python/__init__.template
################################################################################

__template_source_file__ = "training/python/__init__.template"

#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import warnings

# TBE optimizers
import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_args as lookup_args  # noqa: F401
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_adagrad as lookup_adagrad  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_adagrad
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_adam as lookup_adam  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_adam
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_lamb as lookup_lamb  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_lamb
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_lars_sgd as lookup_lars_sgd  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_lars_sgd
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_partial_rowwise_adam as lookup_partial_rowwise_adam  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_partial_rowwise_adam
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_partial_rowwise_lamb as lookup_partial_rowwise_lamb  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_partial_rowwise_lamb
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_rowwise_adagrad as lookup_rowwise_adagrad  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_rowwise_adagrad
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_rowwise_adagrad_with_counter as lookup_rowwise_adagrad_with_counter  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_rowwise_adagrad_with_counter
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_sgd as lookup_sgd  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_sgd
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_none as lookup_none  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_none
        \033[0m""",
        DeprecationWarning,
    )

# SSD TBE optimizers
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_args_ssd as lookup_args_ssd  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_args_ssd
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_adam_ssd as lookup_adam_ssd  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_adam_ssd
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_partial_rowwise_adam_ssd as lookup_partial_rowwise_adam_ssd  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_partial_rowwise_adam_ssd
        \033[0m""",
        DeprecationWarning,
    )
    
try:
    # Import is placed under a try-except bc the op is experimental and can be 
    # removed/updated in the future
    import fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_rowwise_adagrad_ssd as lookup_rowwise_adagrad_ssd  # noqa: F401
except:
    warnings.warn(
        f"""\033[93m
        Failed to import: fbgemm_gpu.split_embedding_codegen_lookup_invokers.lookup_rowwise_adagrad_ssd
        \033[0m""",
        DeprecationWarning,
    )