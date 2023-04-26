# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2


class ABCIApplicationStub(object):
  """----------------------------------------
  Service Definition

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Echo = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/Echo',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestEcho.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseEcho.FromString,
        )
    self.Flush = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/Flush',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestFlush.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseFlush.FromString,
        )
    self.Info = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/Info',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestInfo.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseInfo.FromString,
        )
    self.SetOption = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/SetOption',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestSetOption.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseSetOption.FromString,
        )
    self.DeliverTx = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/DeliverTx',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestDeliverTx.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseDeliverTx.FromString,
        )
    self.CheckTx = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/CheckTx',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestCheckTx.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseCheckTx.FromString,
        )
    self.Query = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/Query',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestQuery.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseQuery.FromString,
        )
    self.Commit = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/Commit',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestCommit.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseCommit.FromString,
        )
    self.InitChain = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/InitChain',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestInitChain.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseInitChain.FromString,
        )
    self.BeginBlock = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/BeginBlock',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestBeginBlock.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseBeginBlock.FromString,
        )
    self.EndBlock = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/EndBlock',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestEndBlock.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseEndBlock.FromString,
        )
    self.ListSnapshots = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/ListSnapshots',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestListSnapshots.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseListSnapshots.FromString,
        )
    self.OfferSnapshot = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/OfferSnapshot',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestOfferSnapshot.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseOfferSnapshot.FromString,
        )
    self.LoadSnapshotChunk = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/LoadSnapshotChunk',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestLoadSnapshotChunk.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseLoadSnapshotChunk.FromString,
        )
    self.ApplySnapshotChunk = channel.unary_unary(
        '/tendermint.abci.ABCIApplication/ApplySnapshotChunk',
        request_serializer=tendermint_dot_abci_dot_types__pb2.RequestApplySnapshotChunk.SerializeToString,
        response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseApplySnapshotChunk.FromString,
        )


class ABCIApplicationServicer(object):
  """----------------------------------------
  Service Definition

  """

  def Echo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Flush(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Info(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetOption(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeliverTx(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckTx(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Commit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InitChain(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BeginBlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EndBlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListSnapshots(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def OfferSnapshot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LoadSnapshotChunk(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ApplySnapshotChunk(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ABCIApplicationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Echo': grpc.unary_unary_rpc_method_handler(
          servicer.Echo,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestEcho.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseEcho.SerializeToString,
      ),
      'Flush': grpc.unary_unary_rpc_method_handler(
          servicer.Flush,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestFlush.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseFlush.SerializeToString,
      ),
      'Info': grpc.unary_unary_rpc_method_handler(
          servicer.Info,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestInfo.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseInfo.SerializeToString,
      ),
      'SetOption': grpc.unary_unary_rpc_method_handler(
          servicer.SetOption,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestSetOption.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseSetOption.SerializeToString,
      ),
      'DeliverTx': grpc.unary_unary_rpc_method_handler(
          servicer.DeliverTx,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestDeliverTx.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseDeliverTx.SerializeToString,
      ),
      'CheckTx': grpc.unary_unary_rpc_method_handler(
          servicer.CheckTx,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestCheckTx.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseCheckTx.SerializeToString,
      ),
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestQuery.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseQuery.SerializeToString,
      ),
      'Commit': grpc.unary_unary_rpc_method_handler(
          servicer.Commit,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestCommit.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseCommit.SerializeToString,
      ),
      'InitChain': grpc.unary_unary_rpc_method_handler(
          servicer.InitChain,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestInitChain.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseInitChain.SerializeToString,
      ),
      'BeginBlock': grpc.unary_unary_rpc_method_handler(
          servicer.BeginBlock,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestBeginBlock.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseBeginBlock.SerializeToString,
      ),
      'EndBlock': grpc.unary_unary_rpc_method_handler(
          servicer.EndBlock,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestEndBlock.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseEndBlock.SerializeToString,
      ),
      'ListSnapshots': grpc.unary_unary_rpc_method_handler(
          servicer.ListSnapshots,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestListSnapshots.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseListSnapshots.SerializeToString,
      ),
      'OfferSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.OfferSnapshot,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestOfferSnapshot.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseOfferSnapshot.SerializeToString,
      ),
      'LoadSnapshotChunk': grpc.unary_unary_rpc_method_handler(
          servicer.LoadSnapshotChunk,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestLoadSnapshotChunk.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseLoadSnapshotChunk.SerializeToString,
      ),
      'ApplySnapshotChunk': grpc.unary_unary_rpc_method_handler(
          servicer.ApplySnapshotChunk,
          request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestApplySnapshotChunk.FromString,
          response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseApplySnapshotChunk.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tendermint.abci.ABCIApplication', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
