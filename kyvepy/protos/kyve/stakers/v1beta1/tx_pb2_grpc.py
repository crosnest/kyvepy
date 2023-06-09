# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kyve.stakers.v1beta1 import tx_pb2 as kyve_dot_stakers_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
  """Msg defines the Msg service.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateStaker = channel.unary_unary(
        '/kyve.stakers.v1beta1.Msg/CreateStaker',
        request_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgCreateStaker.SerializeToString,
        response_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgCreateStakerResponse.FromString,
        )
    self.UpdateMetadata = channel.unary_unary(
        '/kyve.stakers.v1beta1.Msg/UpdateMetadata',
        request_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateMetadata.SerializeToString,
        response_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateMetadataResponse.FromString,
        )
    self.UpdateCommission = channel.unary_unary(
        '/kyve.stakers.v1beta1.Msg/UpdateCommission',
        request_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateCommission.SerializeToString,
        response_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateCommissionResponse.FromString,
        )
    self.JoinPool = channel.unary_unary(
        '/kyve.stakers.v1beta1.Msg/JoinPool',
        request_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgJoinPool.SerializeToString,
        response_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgJoinPoolResponse.FromString,
        )
    self.LeavePool = channel.unary_unary(
        '/kyve.stakers.v1beta1.Msg/LeavePool',
        request_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgLeavePool.SerializeToString,
        response_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgLeavePoolResponse.FromString,
        )
    self.UpdateParams = channel.unary_unary(
        '/kyve.stakers.v1beta1.Msg/UpdateParams',
        request_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
        response_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
        )


class MsgServicer(object):
  """Msg defines the Msg service.
  """

  def CreateStaker(self, request, context):
    """CreateStaker ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateMetadata(self, request, context):
    """UpdateMetadata ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateCommission(self, request, context):
    """UpdateCommission ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def JoinPool(self, request, context):
    """JoinPool ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LeavePool(self, request, context):
    """LeavePool ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateParams(self, request, context):
    """UpdateParams defines a governance operation for updating the x/stakers module
    parameters. The authority is hard-coded to the x/gov module account.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateStaker': grpc.unary_unary_rpc_method_handler(
          servicer.CreateStaker,
          request_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgCreateStaker.FromString,
          response_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgCreateStakerResponse.SerializeToString,
      ),
      'UpdateMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateMetadata,
          request_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateMetadata.FromString,
          response_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateMetadataResponse.SerializeToString,
      ),
      'UpdateCommission': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateCommission,
          request_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateCommission.FromString,
          response_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateCommissionResponse.SerializeToString,
      ),
      'JoinPool': grpc.unary_unary_rpc_method_handler(
          servicer.JoinPool,
          request_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgJoinPool.FromString,
          response_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgJoinPoolResponse.SerializeToString,
      ),
      'LeavePool': grpc.unary_unary_rpc_method_handler(
          servicer.LeavePool,
          request_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgLeavePool.FromString,
          response_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgLeavePoolResponse.SerializeToString,
      ),
      'UpdateParams': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateParams,
          request_deserializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.FromString,
          response_serializer=kyve_dot_stakers_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kyve.stakers.v1beta1.Msg', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
