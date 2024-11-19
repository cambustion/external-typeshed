from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from .preflowpush import preflow_push

__all__ = ["maximum_flow", "maximum_flow_value", "minimum_cut", "minimum_cut_value"]

default_flow_func = preflow_push

@_dispatchable
def maximum_flow(flowG, _s, _t, capacity: str = "capacity", flow_func: Incomplete | None = None, **kwargs): ...
@_dispatchable
def maximum_flow_value(flowG, _s, _t, capacity: str = "capacity", flow_func: Incomplete | None = None, **kwargs): ...
@_dispatchable
def minimum_cut(flowG, _s, _t, capacity: str = "capacity", flow_func: Incomplete | None = None, **kwargs): ...
@_dispatchable
def minimum_cut_value(flowG, _s, _t, capacity: str = "capacity", flow_func: Incomplete | None = None, **kwargs): ...
