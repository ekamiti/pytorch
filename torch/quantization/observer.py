# flake8: noqa: F401
r"""
This file is in the process of migration to `torch/ao/quantization`, and
is kept here for compatibility while the migration process is ongoing.
If you are adding a new entry/functionality, please, add it to the
`torch/ao/quantization/observer.py`, while adding an import statement
here.
"""
from torch.ao.quantization import observer as __orig_mod
from torch.utils._ao_migration_utils import (
    _import_names_with_prefix,
    _get_module_getattr_override,
)

_deprecated_names = [
    "_PartialWrapper",
    "_with_args",
    "_with_callable_args",
    "ABC",
    "ObserverBase",
    "_ObserverBase",
    "MinMaxObserver",
    "MovingAverageMinMaxObserver",
    "PerChannelMinMaxObserver",
    "MovingAveragePerChannelMinMaxObserver",
    "HistogramObserver",
    "PlaceholderObserver",
    "RecordingObserver",
    "NoopObserver",
    "_is_activation_post_process",
    "_is_per_channel_script_obs_instance",
    "get_observer_state_dict",
    "load_observer_state_dict",
    "default_observer",
    "default_placeholder_observer",
    "default_debug_observer",
    "default_weight_observer",
    "default_histogram_observer",
    "default_per_channel_weight_observer",
    "default_dynamic_quant_observer",
    "default_float_qparams_observer",
]

_import_names_with_prefix(__name__, __orig_mod, _deprecated_names)
__getattr__ = _get_module_getattr_override(__name__, _deprecated_names)
