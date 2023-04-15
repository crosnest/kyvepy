# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2022-2023 Cros Nest B.V. Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Implementation of cfedistributor interface using REST."""

from c4epy.cfeminter.interface import CfeMinter
from c4epy.common.rest_client import RestClient
from c4epy.protos.chain4energy.c4echain.cfeminter import (
    QueryInflationRequest,
    QueryInflationResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QueryStateRequest,
    QueryStateResponse,
)


class CfeMinterRestClient(CfeMinter):
    """cfeminter REST client."""

    API_URL = "/c4e/minter/v1beta1"

    def __init__(self, rest_api: RestClient):
        """
        Initialize minter rest client.

        :param rest_api: RestClient api
        """
        self._rest_api = rest_api

    def Inflation(self, request: QueryInflationRequest) -> QueryInflationResponse:
        """
        Query a list of Inflation items.

        :param request: QueryInflationRequest

        :return: QueryInflationResponse
        """
        json_response = self._rest_api.get(f"{self.API_URL}/inflation")
        return QueryInflationResponse().from_json(json_response)

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """
        Parameters queries the parameters of the module.

        :param request: QueryParamsRequest

        :return: QueryParamsResponse
        """
        json_response = self._rest_api.get(f"{self.API_URL}/params")
        return QueryParamsResponse().from_json(json_response)

    def State(self, request: QueryStateRequest) -> QueryStateResponse:
        """
        Query a list of States items.

        :param request: QueryStateRequest

        :return: QueryStatesResponse
        """
        json_response = self._rest_api.get(f"{self.API_URL}/state")
        return QueryStateResponse().from_json(json_response)
