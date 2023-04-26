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

"""Tests for REST implementation of cfeminter."""

import unittest

import pytest
from google.protobuf.json_format import ParseDict

from kyvepy.cfeminter.rest_client import CfeMinterRestClient
from kyvepy.common.utils import json_encode
from kyvepy.protos.kyvechain.cfeminter.query_pb2 import (
    QueryInflationRequest,
    QueryInflationResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QueryStateRequest,
    QueryStateResponse,
)

from tests.helpers import MockRestClient


class CfeMinterRestClientTestCase(unittest.TestCase):
    """Test case for CfeMinter module."""

    @pytest.mark.skip()
    @staticmethod
    def test_query_inflation():
        """Test query minter for positive value."""
        content = {"inflation": "0.019935838916075397"}
        expected_response = ParseDict(content, QueryInflationResponse())

        mock_client = MockRestClient(json_encode(content))
        minter = CfeMinterRestClient(mock_client)

        assert minter.Inflation(QueryInflationRequest()) == expected_response
        assert mock_client.last_base_url == "/kyve/minter/v1beta1/inflation"

    @pytest.mark.skip()
    @staticmethod
    def test_query_state():
        """Test query account for positive result."""
        expected_content = {
            "minter_state": {
                "sequence_id": 1,
                "amount_minted": "1038506205638",
                "remainder_to_mint": "0.174259132506908003",
                "last_mint_block_time": "2023-04-05T21:56:35.429380906Z",
                "remainder_from_previous_minter": "0.000000000000000000",
            },
            "state_history": [],
        }
        expected_response = ParseDict(expected_content, QueryStateResponse())

        mock_client = MockRestClient(json_encode(expected_content))
        minter = CfeMinterRestClient(mock_client)

        assert minter.State(QueryStateRequest()) == expected_response
        assert mock_client.last_base_url == "/kyve/minter/v1beta1/state"

    @staticmethod
    def test_query_params():
        """Test query params for positive result."""
        content = {
            "params": {
                "mint_denom": "ukyve",
                "start_time": "2023-02-17T12:00:00Z",
                "minters": [
                    {
                        "sequence_id": 1,
                        "end_time": None,
                        "config": {
                            "@type": "/chain4energy.kyvechain.cfeminter.ExponentialStepMinting",
                            "step_duration": "126230400s",
                            "amount": "32000000000000",
                            "amount_multiplier": "0.500000000000000000",
                        },
                    }
                ],
            }
        }
        expected_response = ParseDict(content, QueryParamsResponse())

        mock_client = MockRestClient(json_encode(content))
        minter = CfeMinterRestClient(mock_client)

        assert minter.Params(QueryParamsRequest()) == expected_response
        assert mock_client.last_base_url == "/kyve/minter/v1beta1/params"
