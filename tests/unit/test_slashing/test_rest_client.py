# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
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
"""Tests for REST implementation of Slashing."""
from typing import Dict, Tuple
from unittest import TestCase

from c4epy.common.utils import json_encode
from c4epy.protos.cosmos.slashing.v1beta1 import (
    QueryParamsResponse,
    QuerySigningInfoRequest,
    QuerySigningInfoResponse,
    QuerySigningInfosRequest,
    QuerySigningInfosResponse,
)
from c4epy.slashing.rest_client import SlashingRestClient

from tests.helpers import MockRestClient


class SlashingRestClientTestCase(TestCase):
    """Test case for SlashingRestClient class."""

    REST_CLIENT = SlashingRestClient

    def make_clients(
        self, response_content: Dict
    ) -> Tuple[MockRestClient, SlashingRestClient]:
        """
        Make  mock client and rest client api for specific content.

        :param response_content: dict
        :return: rest client instance
        """
        mock_client = MockRestClient(json_encode(response_content).encode("utf-8"))
        rest_client = self.REST_CLIENT(mock_client)
        return mock_client, rest_client

    def test_Params(self):
        """Test Params method."""
        content = {
            "params": {
                "signed_blocks_window": "12",
                "min_signed_per_window": "MTI=",
                "downtime_jail_duration": "12s",
                "slash_fraction_double_sign": "MTI=",
                "slash_fraction_downtime": "MTI=",
            }
        }
        mock_client, slashing = self.make_clients(content)
        expected_response = QueryParamsResponse().from_dict(content)

        assert slashing.Params() == expected_response
        assert mock_client.last_base_url == "/cosmos/slashing/v1beta1/params"

    def test_SigningInfo(self):
        """Test SigningInfo method."""
        content = {
            "val_signing_info": {
                "address": "string",
                "start_height": "1",
                "index_offset": "1",
                "jailed_until": "2022-03-22T11:14:55.544Z",
                "tombstoned": True,
                "missed_blocks_counter": "1",
            }
        }
        mock_client, slashing = self.make_clients(content)
        expected_response = QuerySigningInfoResponse().from_dict(content)

        assert (
            slashing.SigningInfo(QuerySigningInfoRequest(cons_address="some_addr"))
            == expected_response
        )
        assert (
            mock_client.last_base_url
            == "/cosmos/slashing/v1beta1/signing_infos/some_addr"
        )

    def test_SigningInfos(self):
        """Test SigningInfos method."""
        content = {
            "info": [
                {
                    "address": "string",
                    "start_height": "1",
                    "index_offset": "1",
                    "jailed_until": "2022-03-22T11:15:53.940Z",
                    "tombstoned": True,
                    "missed_blocks_counter": "1",
                }
            ],
            "pagination": {"next_key": "c3RyaW5n", "total": "1"},
        }
        mock_client, slashing = self.make_clients(content)
        expected_response = QuerySigningInfosResponse().from_dict(content)

        assert slashing.SigningInfos(QuerySigningInfosRequest()) == expected_response
        assert mock_client.last_base_url == "/cosmos/slashing/v1beta1/signing_infos"
