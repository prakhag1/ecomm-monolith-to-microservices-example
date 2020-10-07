# Copyright 2020 Google LLC. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import demo_pb2 as demo__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class RecommendationServiceStub(object):
  """---------------Recommendation service----------

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListRecommendations = channel.unary_unary(
        '/RecommendationService/ListRecommendations',
        request_serializer=demo__pb2.RecommendationsRequest.SerializeToString,
        response_deserializer=demo__pb2.ListRecommendationsResponse.FromString,
        )
    self.HealthCheck = channel.unary_unary(
        '/RecommendationService/HealthCheck',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=demo__pb2.HealthStatusResponse.FromString,
        )


class RecommendationServiceServicer(object):
  """---------------Recommendation service----------

  """

  def ListRecommendations(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HealthCheck(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RecommendationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListRecommendations': grpc.unary_unary_rpc_method_handler(
          servicer.ListRecommendations,
          request_deserializer=demo__pb2.RecommendationsRequest.FromString,
          response_serializer=demo__pb2.ListRecommendationsResponse.SerializeToString,
      ),
      'HealthCheck': grpc.unary_unary_rpc_method_handler(
          servicer.HealthCheck,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=demo__pb2.HealthStatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'RecommendationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
