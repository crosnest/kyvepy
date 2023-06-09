# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from cosmos.auth.v1beta1 import query_pb2 as cosmos_dot_auth_dot_v1beta1_dot_query__pb2


class QueryStub(object):
  """Query defines the gRPC querier service.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Accounts = channel.unary_unary(
        '/cosmos.auth.v1beta1.Query/Accounts',
        request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.SerializeToString,
        response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.FromString,
        )
    self.Account = channel.unary_unary(
        '/cosmos.auth.v1beta1.Query/Account',
        request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.SerializeToString,
        response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.FromString,
        )
    self.AccountAddressByID = channel.unary_unary(
        '/cosmos.auth.v1beta1.Query/AccountAddressByID',
        request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountAddressByIDRequest.SerializeToString,
        response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountAddressByIDResponse.FromString,
        )
    self.Params = channel.unary_unary(
        '/cosmos.auth.v1beta1.Query/Params',
        request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
        response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
        )
    self.ModuleAccounts = channel.unary_unary(
        '/cosmos.auth.v1beta1.Query/ModuleAccounts',
        request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsRequest.SerializeToString,
        response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsResponse.FromString,
        )
    self.ModuleAccountByName = channel.unary_unary(
        '/cosmos.auth.v1beta1.Query/ModuleAccountByName',
        request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountByNameRequest.SerializeToString,
        response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountByNameResponse.FromString,
        )
    self.Bech32Prefix = channel.unary_unary(
        '/cosmos.auth.v1beta1.Query/Bech32Prefix',
        request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixRequest.SerializeToString,
        response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixResponse.FromString,
        )
    self.AddressBytesToString = channel.unary_unary(
        '/cosmos.auth.v1beta1.Query/AddressBytesToString',
        request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringRequest.SerializeToString,
        response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringResponse.FromString,
        )
    self.AddressStringToBytes = channel.unary_unary(
        '/cosmos.auth.v1beta1.Query/AddressStringToBytes',
        request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesRequest.SerializeToString,
        response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesResponse.FromString,
        )


class QueryServicer(object):
  """Query defines the gRPC querier service.
  """

  def Accounts(self, request, context):
    """Accounts returns all the existing accounts

    Since: cosmos-sdk 0.43
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Account(self, request, context):
    """Account returns account details based on address.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AccountAddressByID(self, request, context):
    """AccountAddressByID returns account address based on account number.

    Since: cosmos-sdk 0.46.2
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Params(self, request, context):
    """Params queries all parameters.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModuleAccounts(self, request, context):
    """ModuleAccounts returns all the existing module accounts.

    Since: cosmos-sdk 0.46
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModuleAccountByName(self, request, context):
    """ModuleAccountByName returns the module account info by module name
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Bech32Prefix(self, request, context):
    """Bech32Prefix queries bech32Prefix

    Since: cosmos-sdk 0.46
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddressBytesToString(self, request, context):
    """AddressBytesToString converts Account Address bytes to string

    Since: cosmos-sdk 0.46
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddressStringToBytes(self, request, context):
    """AddressStringToBytes converts Address string to bytes

    Since: cosmos-sdk 0.46
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Accounts': grpc.unary_unary_rpc_method_handler(
          servicer.Accounts,
          request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.FromString,
          response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.SerializeToString,
      ),
      'Account': grpc.unary_unary_rpc_method_handler(
          servicer.Account,
          request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.FromString,
          response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.SerializeToString,
      ),
      'AccountAddressByID': grpc.unary_unary_rpc_method_handler(
          servicer.AccountAddressByID,
          request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountAddressByIDRequest.FromString,
          response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountAddressByIDResponse.SerializeToString,
      ),
      'Params': grpc.unary_unary_rpc_method_handler(
          servicer.Params,
          request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString,
          response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString,
      ),
      'ModuleAccounts': grpc.unary_unary_rpc_method_handler(
          servicer.ModuleAccounts,
          request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsRequest.FromString,
          response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsResponse.SerializeToString,
      ),
      'ModuleAccountByName': grpc.unary_unary_rpc_method_handler(
          servicer.ModuleAccountByName,
          request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountByNameRequest.FromString,
          response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountByNameResponse.SerializeToString,
      ),
      'Bech32Prefix': grpc.unary_unary_rpc_method_handler(
          servicer.Bech32Prefix,
          request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixRequest.FromString,
          response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixResponse.SerializeToString,
      ),
      'AddressBytesToString': grpc.unary_unary_rpc_method_handler(
          servicer.AddressBytesToString,
          request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringRequest.FromString,
          response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringResponse.SerializeToString,
      ),
      'AddressStringToBytes': grpc.unary_unary_rpc_method_handler(
          servicer.AddressStringToBytes,
          request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesRequest.FromString,
          response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cosmos.auth.v1beta1.Query', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
