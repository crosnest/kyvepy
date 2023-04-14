# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/upgrade/v1beta1/query.proto, cosmos/upgrade/v1beta1/tx.proto, cosmos/upgrade/v1beta1/upgrade.proto
# plugin: python-betterproto
import warnings
from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class Plan(betterproto.Message):
    """
    Plan specifies information about a planned upgrade and when it should
    occur.
    """

    name: str = betterproto.string_field(1)
    """
    Sets the name for the upgrade. This name will be used by the upgraded
    version of the software to apply any special "on-upgrade" commands during
    the first BeginBlock method after the upgrade is applied. It is also used
    to detect whether a software version can handle a given upgrade. If no
    upgrade handler with this name has been set in the software, it will be
    assumed that the software is out-of-date when the upgrade Time or Height is
    reached and the software will exit.
    """

    time: datetime = betterproto.message_field(2)
    """
    Deprecated: Time based upgrades have been deprecated. Time based upgrade
    logic has been removed from the SDK. If this field is not empty, an error
    will be thrown.
    """

    height: int = betterproto.int64_field(3)
    """
    The height at which the upgrade must be performed. Only used if Time is not
    set.
    """

    info: str = betterproto.string_field(4)
    """
    Any application specific upgrade info to be included on-chain such as a git
    commit that validators could automatically upgrade to
    """

    upgraded_client_state: "betterproto_lib_google_protobuf.Any" = (
        betterproto.message_field(5)
    )
    """
    Deprecated: UpgradedClientState field has been deprecated. IBC upgrade
    logic has been moved to the IBC module in the sub module 02-client. If this
    field is not empty, an error will be thrown.
    """

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.is_set("time"):
            warnings.warn("Plan.time is deprecated", DeprecationWarning)
        if self.is_set("upgraded_client_state"):
            warnings.warn(
                "Plan.upgraded_client_state is deprecated", DeprecationWarning
            )


@dataclass(eq=False, repr=False)
class SoftwareUpgradeProposal(betterproto.Message):
    """
    SoftwareUpgradeProposal is a gov Content type for initiating a software
    upgrade. Deprecated: This legacy proposal is deprecated in favor of Msg-
    based gov proposals, see MsgSoftwareUpgrade.
    """

    title: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)
    plan: "Plan" = betterproto.message_field(3)

    def __post_init__(self) -> None:
        warnings.warn("SoftwareUpgradeProposal is deprecated", DeprecationWarning)
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CancelSoftwareUpgradeProposal(betterproto.Message):
    """
    CancelSoftwareUpgradeProposal is a gov Content type for cancelling a
    software upgrade. Deprecated: This legacy proposal is deprecated in favor
    of Msg-based gov proposals, see MsgCancelUpgrade.
    """

    title: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        warnings.warn("CancelSoftwareUpgradeProposal is deprecated", DeprecationWarning)
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ModuleVersion(betterproto.Message):
    """
    ModuleVersion specifies a module and its consensus version. Since: cosmos-
    sdk 0.43
    """

    name: str = betterproto.string_field(1)
    """name of the app module"""

    version: int = betterproto.uint64_field(2)
    """consensus version of the app module"""


@dataclass(eq=False, repr=False)
class QueryCurrentPlanRequest(betterproto.Message):
    """
    QueryCurrentPlanRequest is the request type for the Query/CurrentPlan RPC
    method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryCurrentPlanResponse(betterproto.Message):
    """
    QueryCurrentPlanResponse is the response type for the Query/CurrentPlan RPC
    method.
    """

    plan: "Plan" = betterproto.message_field(1)
    """plan is the current upgrade plan."""


@dataclass(eq=False, repr=False)
class QueryAppliedPlanRequest(betterproto.Message):
    """
    QueryCurrentPlanRequest is the request type for the Query/AppliedPlan RPC
    method.
    """

    name: str = betterproto.string_field(1)
    """name is the name of the applied plan to query for."""


@dataclass(eq=False, repr=False)
class QueryAppliedPlanResponse(betterproto.Message):
    """
    QueryAppliedPlanResponse is the response type for the Query/AppliedPlan RPC
    method.
    """

    height: int = betterproto.int64_field(1)
    """height is the block height at which the plan was applied."""


@dataclass(eq=False, repr=False)
class QueryUpgradedConsensusStateRequest(betterproto.Message):
    """
    QueryUpgradedConsensusStateRequest is the request type for the
    Query/UpgradedConsensusState RPC method.
    """

    last_height: int = betterproto.int64_field(1)
    """
    last height of the current chain must be sent in request as this is the
    height under which next consensus state is stored
    """

    def __post_init__(self) -> None:
        warnings.warn(
            "QueryUpgradedConsensusStateRequest is deprecated", DeprecationWarning
        )
        super().__post_init__()


@dataclass(eq=False, repr=False)
class QueryUpgradedConsensusStateResponse(betterproto.Message):
    """
    QueryUpgradedConsensusStateResponse is the response type for the
    Query/UpgradedConsensusState RPC method.
    """

    upgraded_consensus_state: bytes = betterproto.bytes_field(2)
    """Since: cosmos-sdk 0.43"""

    def __post_init__(self) -> None:
        warnings.warn(
            "QueryUpgradedConsensusStateResponse is deprecated", DeprecationWarning
        )
        super().__post_init__()


@dataclass(eq=False, repr=False)
class QueryModuleVersionsRequest(betterproto.Message):
    """
    QueryModuleVersionsRequest is the request type for the Query/ModuleVersions
    RPC method. Since: cosmos-sdk 0.43
    """

    module_name: str = betterproto.string_field(1)
    """
    module_name is a field to query a specific module consensus version from
    state. Leaving this empty will fetch the full list of module versions from
    state
    """


@dataclass(eq=False, repr=False)
class QueryModuleVersionsResponse(betterproto.Message):
    """
    QueryModuleVersionsResponse is the response type for the
    Query/ModuleVersions RPC method. Since: cosmos-sdk 0.43
    """

    module_versions: List["ModuleVersion"] = betterproto.message_field(1)
    """
    module_versions is a list of module names with their consensus versions.
    """


@dataclass(eq=False, repr=False)
class QueryAuthorityRequest(betterproto.Message):
    """
    QueryAuthorityRequest is the request type for Query/Authority Since:
    cosmos-sdk 0.46
    """

    pass


@dataclass(eq=False, repr=False)
class QueryAuthorityResponse(betterproto.Message):
    """
    QueryAuthorityResponse is the response type for Query/Authority Since:
    cosmos-sdk 0.46
    """

    address: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MsgSoftwareUpgrade(betterproto.Message):
    """
    MsgSoftwareUpgrade is the Msg/SoftwareUpgrade request type. Since: cosmos-
    sdk 0.46
    """

    authority: str = betterproto.string_field(1)
    """authority is the address of the governance account."""

    plan: "Plan" = betterproto.message_field(2)
    """plan is the upgrade plan."""


@dataclass(eq=False, repr=False)
class MsgSoftwareUpgradeResponse(betterproto.Message):
    """
    MsgSoftwareUpgradeResponse is the Msg/SoftwareUpgrade response type. Since:
    cosmos-sdk 0.46
    """

    pass


@dataclass(eq=False, repr=False)
class MsgCancelUpgrade(betterproto.Message):
    """
    MsgCancelUpgrade is the Msg/CancelUpgrade request type. Since: cosmos-sdk
    0.46
    """

    authority: str = betterproto.string_field(1)
    """authority is the address of the governance account."""


@dataclass(eq=False, repr=False)
class MsgCancelUpgradeResponse(betterproto.Message):
    """
    MsgCancelUpgradeResponse is the Msg/CancelUpgrade response type. Since:
    cosmos-sdk 0.46
    """

    pass


class QueryStub(betterproto.ServiceStub):
    async def current_plan(
        self,
        query_current_plan_request: "QueryCurrentPlanRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryCurrentPlanResponse":
        return await self._unary_unary(
            "/cosmos.upgrade.v1beta1.Query/CurrentPlan",
            query_current_plan_request,
            QueryCurrentPlanResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def applied_plan(
        self,
        query_applied_plan_request: "QueryAppliedPlanRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAppliedPlanResponse":
        return await self._unary_unary(
            "/cosmos.upgrade.v1beta1.Query/AppliedPlan",
            query_applied_plan_request,
            QueryAppliedPlanResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def upgraded_consensus_state(
        self,
        query_upgraded_consensus_state_request: "QueryUpgradedConsensusStateRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryUpgradedConsensusStateResponse":
        return await self._unary_unary(
            "/cosmos.upgrade.v1beta1.Query/UpgradedConsensusState",
            query_upgraded_consensus_state_request,
            QueryUpgradedConsensusStateResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def module_versions(
        self,
        query_module_versions_request: "QueryModuleVersionsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryModuleVersionsResponse":
        return await self._unary_unary(
            "/cosmos.upgrade.v1beta1.Query/ModuleVersions",
            query_module_versions_request,
            QueryModuleVersionsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def authority(
        self,
        query_authority_request: "QueryAuthorityRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAuthorityResponse":
        return await self._unary_unary(
            "/cosmos.upgrade.v1beta1.Query/Authority",
            query_authority_request,
            QueryAuthorityResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def software_upgrade(
        self,
        msg_software_upgrade: "MsgSoftwareUpgrade",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgSoftwareUpgradeResponse":
        return await self._unary_unary(
            "/cosmos.upgrade.v1beta1.Msg/SoftwareUpgrade",
            msg_software_upgrade,
            MsgSoftwareUpgradeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def cancel_upgrade(
        self,
        msg_cancel_upgrade: "MsgCancelUpgrade",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgCancelUpgradeResponse":
        return await self._unary_unary(
            "/cosmos.upgrade.v1beta1.Msg/CancelUpgrade",
            msg_cancel_upgrade,
            MsgCancelUpgradeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def current_plan(
        self, query_current_plan_request: "QueryCurrentPlanRequest"
    ) -> "QueryCurrentPlanResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def applied_plan(
        self, query_applied_plan_request: "QueryAppliedPlanRequest"
    ) -> "QueryAppliedPlanResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upgraded_consensus_state(
        self,
        query_upgraded_consensus_state_request: "QueryUpgradedConsensusStateRequest",
    ) -> "QueryUpgradedConsensusStateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def module_versions(
        self, query_module_versions_request: "QueryModuleVersionsRequest"
    ) -> "QueryModuleVersionsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def authority(
        self, query_authority_request: "QueryAuthorityRequest"
    ) -> "QueryAuthorityResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_current_plan(
        self,
        stream: "grpclib.server.Stream[QueryCurrentPlanRequest, QueryCurrentPlanResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.current_plan(request)
        await stream.send_message(response)

    async def __rpc_applied_plan(
        self,
        stream: "grpclib.server.Stream[QueryAppliedPlanRequest, QueryAppliedPlanResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.applied_plan(request)
        await stream.send_message(response)

    async def __rpc_upgraded_consensus_state(
        self,
        stream: "grpclib.server.Stream[QueryUpgradedConsensusStateRequest, QueryUpgradedConsensusStateResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.upgraded_consensus_state(request)
        await stream.send_message(response)

    async def __rpc_module_versions(
        self,
        stream: "grpclib.server.Stream[QueryModuleVersionsRequest, QueryModuleVersionsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.module_versions(request)
        await stream.send_message(response)

    async def __rpc_authority(
        self,
        stream: "grpclib.server.Stream[QueryAuthorityRequest, QueryAuthorityResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.authority(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.upgrade.v1beta1.Query/CurrentPlan": grpclib.const.Handler(
                self.__rpc_current_plan,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryCurrentPlanRequest,
                QueryCurrentPlanResponse,
            ),
            "/cosmos.upgrade.v1beta1.Query/AppliedPlan": grpclib.const.Handler(
                self.__rpc_applied_plan,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAppliedPlanRequest,
                QueryAppliedPlanResponse,
            ),
            "/cosmos.upgrade.v1beta1.Query/UpgradedConsensusState": grpclib.const.Handler(
                self.__rpc_upgraded_consensus_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryUpgradedConsensusStateRequest,
                QueryUpgradedConsensusStateResponse,
            ),
            "/cosmos.upgrade.v1beta1.Query/ModuleVersions": grpclib.const.Handler(
                self.__rpc_module_versions,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryModuleVersionsRequest,
                QueryModuleVersionsResponse,
            ),
            "/cosmos.upgrade.v1beta1.Query/Authority": grpclib.const.Handler(
                self.__rpc_authority,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAuthorityRequest,
                QueryAuthorityResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def software_upgrade(
        self, msg_software_upgrade: "MsgSoftwareUpgrade"
    ) -> "MsgSoftwareUpgradeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def cancel_upgrade(
        self, msg_cancel_upgrade: "MsgCancelUpgrade"
    ) -> "MsgCancelUpgradeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_software_upgrade(
        self,
        stream: "grpclib.server.Stream[MsgSoftwareUpgrade, MsgSoftwareUpgradeResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.software_upgrade(request)
        await stream.send_message(response)

    async def __rpc_cancel_upgrade(
        self,
        stream: "grpclib.server.Stream[MsgCancelUpgrade, MsgCancelUpgradeResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.cancel_upgrade(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.upgrade.v1beta1.Msg/SoftwareUpgrade": grpclib.const.Handler(
                self.__rpc_software_upgrade,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSoftwareUpgrade,
                MsgSoftwareUpgradeResponse,
            ),
            "/cosmos.upgrade.v1beta1.Msg/CancelUpgrade": grpclib.const.Handler(
                self.__rpc_cancel_upgrade,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgCancelUpgrade,
                MsgCancelUpgradeResponse,
            ),
        }
