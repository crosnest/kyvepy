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

"""Implementation of cfesignature interface using REST."""


from c4epy.cfesignature.interface import CfeSignature
from c4epy.common.rest_client import RestClient
from c4epy.protos.chain4energy.c4echain.cfesignature import (
    QueryCreateReferenceIdRequest,
    QueryCreateReferenceIdResponse,
    QueryCreateReferencePayloadLinkRequest,
    QueryCreateReferencePayloadLinkResponse,
    QueryCreateStorageKeyRequest,
    QueryCreateStorageKeyResponse,
    QueryGetAccountInfoRequest,
    QueryGetAccountInfoResponse,
    QueryGetReferencePayloadLinkRequest,
    QueryGetReferencePayloadLinkResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QueryVerifyReferencePayloadLinkRequest,
    QueryVerifyReferencePayloadLinkResponse,
    QueryVerifySignatureRequest,
    QueryVerifySignatureResponse,
)


class CfeSignatureRestClient(CfeSignature):
    """cfeminter REST client."""

    API_URL = "/c4e/signature/v1beta1"

    def __init__(self, rest_api: RestClient):
        """
        Initialize signature rest client.

        :param rest_api: RestClient api
        """
        self._rest_api = rest_api

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """
        Parameters queries the parameters of the module.

        :param request: QueryParamsRequest

        :return: QueryParamsResponse
        """
        json_response = self._rest_api.get(f"{self.API_URL}/params")
        return QueryParamsResponse().from_json(json_response)

    def CreateReferenceId(
        self, request: QueryCreateReferenceIdRequest
    ) -> QueryCreateReferenceIdResponse:
        """
        Query a list of CreateReferenceId items.

        :param request: QueryCreateReferenceIdRequest

        :return: QueryCreateReferenceIdResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/create_reference_id/{request.creator}"
        )
        return QueryCreateReferenceIdResponse().from_json(json_response)

    def CreateStorageKey(
        self, request: QueryCreateStorageKeyRequest
    ) -> QueryCreateStorageKeyResponse:
        """
        Query a list of CreateStorageKey items.

        :param request: QueryCreateStorageKeyRequest

        :return: QueryCreateStorageKeyResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/create_storage_key/{request.target_acc_address}/{request.reference_id}"
        )
        return QueryCreateStorageKeyResponse().from_json(json_response)

    def CreateReferencePayloadLink(
        self, request: QueryCreateReferencePayloadLinkRequest
    ) -> QueryCreateReferencePayloadLinkResponse:
        """
        Query a list of CreateReferencePayloadLink items.

        :param request: QueryCreateReferencePayloadLinkRequest

        :return: QueryCreateReferencePayloadLinkResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/create_reference_payload_link/{request.reference_id}/{request.payload_hash}"
        )
        return QueryCreateReferencePayloadLinkResponse().from_json(json_response)

    def VerifySignature(
        self, request: QueryVerifySignatureRequest
    ) -> QueryVerifySignatureResponse:
        """
        Query a list of State items.

        :param request: QueryVerifySignatureRequest

        :return: QueryVerifySignatureResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/verify_signature/{request.reference_id}/{request.target_acc_address}"
        )
        return QueryVerifySignatureResponse().from_json(json_response)

    def GetAccountInfo(
        self, request: QueryGetAccountInfoRequest
    ) -> QueryGetAccountInfoResponse:
        """
        Query a list of GetAccountInfo items.

        :param request: QueryGetAccountInfoRequest

        :return: QueryGetAccountInfoResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/get_account_info/{request.acc_address_string}"
        )
        return QueryGetAccountInfoResponse().from_json(json_response)

    def VerifyReferencePayloadLink(
        self, request: QueryVerifyReferencePayloadLinkRequest
    ) -> QueryVerifyReferencePayloadLinkResponse:
        """
        Query a list of VerifyReferencePayloadLink items.

        :param request: QueryVerifyReferencePayloadLinkRequest

        :return: QueryVerifyReferencePayloadLinkResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/verify_reference_payload_link/{request.reference_id}/{request.payload_hash}"
        )
        return QueryVerifyReferencePayloadLinkResponse().from_json(json_response)

    def GetReferencePayloadLink(
        self, request: QueryGetReferencePayloadLinkRequest
    ) -> QueryGetReferencePayloadLinkResponse:
        """
        Query a list of GetReferencePayloadLink items.

        :param request: QueryGetReferencePayloadLinkRequest

        :return: QueryGetReferencePayloadLinkResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/get_reference_payload_link/{request.reference_id}"
        )
        return QueryGetReferencePayloadLinkResponse().from_json(json_response)
