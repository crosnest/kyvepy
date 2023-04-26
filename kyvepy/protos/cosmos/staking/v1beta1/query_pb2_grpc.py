# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from cosmos.staking.v1beta1 import query_pb2 as cosmos_dot_staking_dot_v1beta1_dot_query__pb2


class QueryStub(object):
  """Query defines the gRPC querier service.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Validators = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/Validators',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsResponse.FromString,
        )
    self.Validator = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/Validator',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorResponse.FromString,
        )
    self.ValidatorDelegations = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/ValidatorDelegations',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsResponse.FromString,
        )
    self.ValidatorUnbondingDelegations = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/ValidatorUnbondingDelegations',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsResponse.FromString,
        )
    self.Delegation = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/Delegation',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationResponse.FromString,
        )
    self.UnbondingDelegation = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/UnbondingDelegation',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationResponse.FromString,
        )
    self.DelegatorDelegations = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/DelegatorDelegations',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsResponse.FromString,
        )
    self.DelegatorUnbondingDelegations = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/DelegatorUnbondingDelegations',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsResponse.FromString,
        )
    self.Redelegations = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/Redelegations',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsResponse.FromString,
        )
    self.DelegatorValidators = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/DelegatorValidators',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.FromString,
        )
    self.DelegatorValidator = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/DelegatorValidator',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorResponse.FromString,
        )
    self.HistoricalInfo = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/HistoricalInfo',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoResponse.FromString,
        )
    self.Pool = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/Pool',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolResponse.FromString,
        )
    self.Params = channel.unary_unary(
        '/cosmos.staking.v1beta1.Query/Params',
        request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
        response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
        )


class QueryServicer(object):
  """Query defines the gRPC querier service.
  """

  def Validators(self, request, context):
    """Validators queries all validators that match the given status.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Validator(self, request, context):
    """Validator queries validator info for given validator address.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ValidatorDelegations(self, request, context):
    """ValidatorDelegations queries delegate info for given validator.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ValidatorUnbondingDelegations(self, request, context):
    """ValidatorUnbondingDelegations queries unbonding delegations of a validator.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delegation(self, request, context):
    """Delegation queries delegate info for given validator delegator pair.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnbondingDelegation(self, request, context):
    """UnbondingDelegation queries unbonding info for given validator delegator
    pair.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelegatorDelegations(self, request, context):
    """DelegatorDelegations queries all delegations of a given delegator address.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelegatorUnbondingDelegations(self, request, context):
    """DelegatorUnbondingDelegations queries all unbonding delegations of a given
    delegator address.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Redelegations(self, request, context):
    """Redelegations queries redelegations of given address.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelegatorValidators(self, request, context):
    """DelegatorValidators queries all validators info for given delegator
    address.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelegatorValidator(self, request, context):
    """DelegatorValidator queries validator info for given delegator validator
    pair.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricalInfo(self, request, context):
    """HistoricalInfo queries the historical info for given height.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Pool(self, request, context):
    """Pool queries the pool info.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Params(self, request, context):
    """Parameters queries the staking parameters.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Validators': grpc.unary_unary_rpc_method_handler(
          servicer.Validators,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsResponse.SerializeToString,
      ),
      'Validator': grpc.unary_unary_rpc_method_handler(
          servicer.Validator,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorResponse.SerializeToString,
      ),
      'ValidatorDelegations': grpc.unary_unary_rpc_method_handler(
          servicer.ValidatorDelegations,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsResponse.SerializeToString,
      ),
      'ValidatorUnbondingDelegations': grpc.unary_unary_rpc_method_handler(
          servicer.ValidatorUnbondingDelegations,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsResponse.SerializeToString,
      ),
      'Delegation': grpc.unary_unary_rpc_method_handler(
          servicer.Delegation,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationResponse.SerializeToString,
      ),
      'UnbondingDelegation': grpc.unary_unary_rpc_method_handler(
          servicer.UnbondingDelegation,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationResponse.SerializeToString,
      ),
      'DelegatorDelegations': grpc.unary_unary_rpc_method_handler(
          servicer.DelegatorDelegations,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsResponse.SerializeToString,
      ),
      'DelegatorUnbondingDelegations': grpc.unary_unary_rpc_method_handler(
          servicer.DelegatorUnbondingDelegations,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsResponse.SerializeToString,
      ),
      'Redelegations': grpc.unary_unary_rpc_method_handler(
          servicer.Redelegations,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsResponse.SerializeToString,
      ),
      'DelegatorValidators': grpc.unary_unary_rpc_method_handler(
          servicer.DelegatorValidators,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.SerializeToString,
      ),
      'DelegatorValidator': grpc.unary_unary_rpc_method_handler(
          servicer.DelegatorValidator,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorResponse.SerializeToString,
      ),
      'HistoricalInfo': grpc.unary_unary_rpc_method_handler(
          servicer.HistoricalInfo,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoResponse.SerializeToString,
      ),
      'Pool': grpc.unary_unary_rpc_method_handler(
          servicer.Pool,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolResponse.SerializeToString,
      ),
      'Params': grpc.unary_unary_rpc_method_handler(
          servicer.Params,
          request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString,
          response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cosmos.staking.v1beta1.Query', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
