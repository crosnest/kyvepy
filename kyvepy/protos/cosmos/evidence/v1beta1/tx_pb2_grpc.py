# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from cosmos.evidence.v1beta1 import tx_pb2 as cosmos_dot_evidence_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
  """Msg defines the evidence Msg service.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SubmitEvidence = channel.unary_unary(
        '/cosmos.evidence.v1beta1.Msg/SubmitEvidence',
        request_serializer=cosmos_dot_evidence_dot_v1beta1_dot_tx__pb2.MsgSubmitEvidence.SerializeToString,
        response_deserializer=cosmos_dot_evidence_dot_v1beta1_dot_tx__pb2.MsgSubmitEvidenceResponse.FromString,
        )


class MsgServicer(object):
  """Msg defines the evidence Msg service.
  """

  def SubmitEvidence(self, request, context):
    """SubmitEvidence submits an arbitrary Evidence of misbehavior such as equivocation or
    counterfactual signing.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SubmitEvidence': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitEvidence,
          request_deserializer=cosmos_dot_evidence_dot_v1beta1_dot_tx__pb2.MsgSubmitEvidence.FromString,
          response_serializer=cosmos_dot_evidence_dot_v1beta1_dot_tx__pb2.MsgSubmitEvidenceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cosmos.evidence.v1beta1.Msg', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
