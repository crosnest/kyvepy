# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kyve.query.v1beta1 import bundles_pb2 as kyve_dot_query_dot_v1beta1_dot_bundles__pb2


class QueryBundlesStub(object):
  """QueryDelegation contains all rpc requests related to direct delegation data
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FinalizedBundles = channel.unary_unary(
        '/kyve.query.v1beta1.QueryBundles/FinalizedBundles',
        request_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundlesRequest.SerializeToString,
        response_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundlesResponse.FromString,
        )
    self.FinalizedBundle = channel.unary_unary(
        '/kyve.query.v1beta1.QueryBundles/FinalizedBundle',
        request_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundleRequest.SerializeToString,
        response_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundleResponse.FromString,
        )
    self.FinalizedBundlesByHeight = channel.unary_unary(
        '/kyve.query.v1beta1.QueryBundles/FinalizedBundlesByHeight',
        request_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundlesByHeightRequest.SerializeToString,
        response_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundlesByHeightResponse.FromString,
        )
    self.CurrentVoteStatus = channel.unary_unary(
        '/kyve.query.v1beta1.QueryBundles/CurrentVoteStatus',
        request_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCurrentVoteStatusRequest.SerializeToString,
        response_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCurrentVoteStatusResponse.FromString,
        )
    self.CanValidate = channel.unary_unary(
        '/kyve.query.v1beta1.QueryBundles/CanValidate',
        request_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanValidateRequest.SerializeToString,
        response_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanValidateResponse.FromString,
        )
    self.CanPropose = channel.unary_unary(
        '/kyve.query.v1beta1.QueryBundles/CanPropose',
        request_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanProposeRequest.SerializeToString,
        response_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanProposeResponse.FromString,
        )
    self.CanVote = channel.unary_unary(
        '/kyve.query.v1beta1.QueryBundles/CanVote',
        request_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanVoteRequest.SerializeToString,
        response_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanVoteResponse.FromString,
        )


class QueryBundlesServicer(object):
  """QueryDelegation contains all rpc requests related to direct delegation data
  """

  def FinalizedBundles(self, request, context):
    """FinalizedBundles ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FinalizedBundle(self, request, context):
    """FinalizedBundle ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FinalizedBundlesByHeight(self, request, context):
    """Queries the bundle which contains the data given height
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CurrentVoteStatus(self, request, context):
    """CurrentVoteStatus ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CanValidate(self, request, context):
    """CanValidate ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CanPropose(self, request, context):
    """CanPropose ...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CanVote(self, request, context):
    """CanVote checks if voter on pool can still vote for the given bundle
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QueryBundlesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FinalizedBundles': grpc.unary_unary_rpc_method_handler(
          servicer.FinalizedBundles,
          request_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundlesRequest.FromString,
          response_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundlesResponse.SerializeToString,
      ),
      'FinalizedBundle': grpc.unary_unary_rpc_method_handler(
          servicer.FinalizedBundle,
          request_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundleRequest.FromString,
          response_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundleResponse.SerializeToString,
      ),
      'FinalizedBundlesByHeight': grpc.unary_unary_rpc_method_handler(
          servicer.FinalizedBundlesByHeight,
          request_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundlesByHeightRequest.FromString,
          response_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryFinalizedBundlesByHeightResponse.SerializeToString,
      ),
      'CurrentVoteStatus': grpc.unary_unary_rpc_method_handler(
          servicer.CurrentVoteStatus,
          request_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCurrentVoteStatusRequest.FromString,
          response_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCurrentVoteStatusResponse.SerializeToString,
      ),
      'CanValidate': grpc.unary_unary_rpc_method_handler(
          servicer.CanValidate,
          request_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanValidateRequest.FromString,
          response_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanValidateResponse.SerializeToString,
      ),
      'CanPropose': grpc.unary_unary_rpc_method_handler(
          servicer.CanPropose,
          request_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanProposeRequest.FromString,
          response_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanProposeResponse.SerializeToString,
      ),
      'CanVote': grpc.unary_unary_rpc_method_handler(
          servicer.CanVote,
          request_deserializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanVoteRequest.FromString,
          response_serializer=kyve_dot_query_dot_v1beta1_dot_bundles__pb2.QueryCanVoteResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kyve.query.v1beta1.QueryBundles', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
