# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kyve.query.v1beta1 import pools_pb2 as kyve_dot_query_dot_v1beta1_dot_pools__pb2


class QueryPoolStub(object):
  """QueryPool ...
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Pools = channel.unary_unary(
        '/kyve.query.v1beta1.QueryPool/Pools',
        request_serializer=kyve_dot_query_dot_v1beta1_dot_pools__pb2.QueryPoolsRequest.SerializeToString,
        response_deserializer=kyve_dot_query_dot_v1beta1_dot_pools__pb2.QueryPoolsResponse.FromString,
        )
    self.Pool = channel.unary_unary(
        '/kyve.query.v1beta1.QueryPool/Pool',
        request_serializer=kyve_dot_query_dot_v1beta1_dot_pools__pb2.QueryPoolRequest.SerializeToString,
        response_deserializer=kyve_dot_query_dot_v1beta1_dot_pools__pb2.QueryPoolResponse.FromString,
        )


class QueryPoolServicer(object):
  """QueryPool ...
  """

  def Pools(self, request, context):
    """Pools queries for all pools.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Pool(self, request, context):
    """Pool queries a pool by its Id.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QueryPoolServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Pools': grpc.unary_unary_rpc_method_handler(
          servicer.Pools,
          request_deserializer=kyve_dot_query_dot_v1beta1_dot_pools__pb2.QueryPoolsRequest.FromString,
          response_serializer=kyve_dot_query_dot_v1beta1_dot_pools__pb2.QueryPoolsResponse.SerializeToString,
      ),
      'Pool': grpc.unary_unary_rpc_method_handler(
          servicer.Pool,
          request_deserializer=kyve_dot_query_dot_v1beta1_dot_pools__pb2.QueryPoolRequest.FromString,
          response_serializer=kyve_dot_query_dot_v1beta1_dot_pools__pb2.QueryPoolResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kyve.query.v1beta1.QueryPool', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
