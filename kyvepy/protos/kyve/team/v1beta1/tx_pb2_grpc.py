# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kyve.team.v1beta1 import tx_pb2 as kyve_dot_team_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
  """Msg defines the Msg service.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ClaimUnlocked = channel.unary_unary(
        '/kyve.team.v1beta1.Msg/ClaimUnlocked',
        request_serializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimUnlocked.SerializeToString,
        response_deserializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimUnlockedResponse.FromString,
        )
    self.Clawback = channel.unary_unary(
        '/kyve.team.v1beta1.Msg/Clawback',
        request_serializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClawback.SerializeToString,
        response_deserializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClawbackResponse.FromString,
        )
    self.CreateTeamVestingAccount = channel.unary_unary(
        '/kyve.team.v1beta1.Msg/CreateTeamVestingAccount',
        request_serializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgCreateTeamVestingAccount.SerializeToString,
        response_deserializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgCreateTeamVestingAccountResponse.FromString,
        )
    self.ClaimAuthorityRewards = channel.unary_unary(
        '/kyve.team.v1beta1.Msg/ClaimAuthorityRewards',
        request_serializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimAuthorityRewards.SerializeToString,
        response_deserializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimAuthorityRewardsResponse.FromString,
        )
    self.ClaimAccountRewards = channel.unary_unary(
        '/kyve.team.v1beta1.Msg/ClaimAccountRewards',
        request_serializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimAccountRewards.SerializeToString,
        response_deserializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimAccountRewardsResponse.FromString,
        )


class MsgServicer(object):
  """Msg defines the Msg service.
  """

  def ClaimUnlocked(self, request, context):
    """ClaimUnlocked ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Clawback(self, request, context):
    """Clawback ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateTeamVestingAccount(self, request, context):
    """CreateTeamVestingAccount ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClaimAuthorityRewards(self, request, context):
    """ClaimAuthorityRewards ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClaimAccountRewards(self, request, context):
    """ClaimInflationRewards ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ClaimUnlocked': grpc.unary_unary_rpc_method_handler(
          servicer.ClaimUnlocked,
          request_deserializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimUnlocked.FromString,
          response_serializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimUnlockedResponse.SerializeToString,
      ),
      'Clawback': grpc.unary_unary_rpc_method_handler(
          servicer.Clawback,
          request_deserializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClawback.FromString,
          response_serializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClawbackResponse.SerializeToString,
      ),
      'CreateTeamVestingAccount': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTeamVestingAccount,
          request_deserializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgCreateTeamVestingAccount.FromString,
          response_serializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgCreateTeamVestingAccountResponse.SerializeToString,
      ),
      'ClaimAuthorityRewards': grpc.unary_unary_rpc_method_handler(
          servicer.ClaimAuthorityRewards,
          request_deserializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimAuthorityRewards.FromString,
          response_serializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimAuthorityRewardsResponse.SerializeToString,
      ),
      'ClaimAccountRewards': grpc.unary_unary_rpc_method_handler(
          servicer.ClaimAccountRewards,
          request_deserializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimAccountRewards.FromString,
          response_serializer=kyve_dot_team_dot_v1beta1_dot_tx__pb2.MsgClaimAccountRewardsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kyve.team.v1beta1.Msg', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
