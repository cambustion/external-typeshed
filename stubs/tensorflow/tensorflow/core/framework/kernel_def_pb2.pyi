"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.core.framework.attr_value_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class KernelDef(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class AttrConstraint(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        ALLOWED_VALUES_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Name of an attr from the Op."""
        @property
        def allowed_values(self) -> tensorflow.core.framework.attr_value_pb2.AttrValue:
            """A list of values that this kernel supports for this attr.
            Like OpDef.AttrDef.allowed_values, except for kernels instead of Ops.
            """

        def __init__(
            self,
            *,
            name: builtins.str | None = ...,
            allowed_values: tensorflow.core.framework.attr_value_pb2.AttrValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["allowed_values", b"allowed_values"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["allowed_values", b"allowed_values", "name", b"name"]) -> None: ...

    OP_FIELD_NUMBER: builtins.int
    DEVICE_TYPE_FIELD_NUMBER: builtins.int
    CONSTRAINT_FIELD_NUMBER: builtins.int
    HOST_MEMORY_ARG_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    PRIORITY_FIELD_NUMBER: builtins.int
    op: builtins.str
    """Must match the name of an Op."""
    device_type: builtins.str
    """Type of device this kernel runs on."""
    label: builtins.str
    """This allows experimental kernels to be registered for an op that
    won't be used unless the user specifies a "_kernel" attr with
    value matching this.
    """
    priority: builtins.int
    """Prioritization of kernel amongst different devices. By default we assume
    priority is 0. The higher the priority the better. By default (i.e. if
    this is not set), we prefer GPU kernels over CPU.
    """
    @property
    def constraint(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KernelDef.AttrConstraint]: ...
    @property
    def host_memory_arg(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Names of the Op's input_/output_args that reside in host memory
        instead of device memory.
        """

    def __init__(
        self,
        *,
        op: builtins.str | None = ...,
        device_type: builtins.str | None = ...,
        constraint: collections.abc.Iterable[global___KernelDef.AttrConstraint] | None = ...,
        host_memory_arg: collections.abc.Iterable[builtins.str] | None = ...,
        label: builtins.str | None = ...,
        priority: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["constraint", b"constraint", "device_type", b"device_type", "host_memory_arg", b"host_memory_arg", "label", b"label", "op", b"op", "priority", b"priority"]) -> None: ...

global___KernelDef = KernelDef

@typing.final
class KernelList(google.protobuf.message.Message):
    """A collection of KernelDefs"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KERNEL_FIELD_NUMBER: builtins.int
    @property
    def kernel(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KernelDef]: ...
    def __init__(
        self,
        *,
        kernel: collections.abc.Iterable[global___KernelDef] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["kernel", b"kernel"]) -> None: ...

global___KernelList = KernelList
