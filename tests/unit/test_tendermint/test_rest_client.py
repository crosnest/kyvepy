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
"""Tests for REST implementation of Cosmos Base Tendermint."""
from typing import Dict, Tuple
from unittest import TestCase

from c4epy.common.utils import json_encode
from c4epy.protos.cosmos.base.tendermint.v1beta1 import (
    GetBlockByHeightRequest,
    GetBlockByHeightResponse,
    GetLatestBlockRequest,
    GetLatestBlockResponse,
    GetLatestValidatorSetRequest,
    GetLatestValidatorSetResponse,
    GetNodeInfoRequest,
    GetNodeInfoResponse,
    GetSyncingRequest,
    GetSyncingResponse,
    GetValidatorSetByHeightRequest,
    GetValidatorSetByHeightResponse,
)
from c4epy.tendermint.rest_client import CosmosBaseTendermintRestClient

from tests.helpers import MockRestClient


TYPE = {
    "@type": "type.googleapis.com/google.protobuf.Int32Value",
    "value": "NDI=",
}


class CosmosBaseTendermintRestClientTestCase(TestCase):
    """Test case for CosmosBaseTendermintRestClient class."""

    REST_CLIENT = CosmosBaseTendermintRestClient

    def make_clients(
        self, response_content: Dict
    ) -> Tuple[MockRestClient, CosmosBaseTendermintRestClient]:
        """
        Make  mock client and rest client api for specific content.

        :param response_content: dict
        :return: rest client instance
        """
        mock_client = MockRestClient(json_encode(response_content).encode("utf-8"))
        rest_client = self.REST_CLIENT(mock_client)
        return mock_client, rest_client

    def test_GetNodeInfo(self):
        """Test GetNodeInfo method."""
        content = {
            "default_node_info": {
                "protocol_version": {
                    "p2p": "12",
                    "block": "12",
                    "app": "12",
                },
                "default_node_id": "string",
                "listen_addr": "string",
                "network": "string",
                "version": "string",
                "channels": "c3RyaW5n",
                "moniker": "string",
                "other": {"tx_index": "string", "rpc_address": "string"},
            },
            "application_version": {
                "name": "string",
                "app_name": "string",
                "version": "string",
                "git_commit": "string",
                "build_tags": "string",
                "go_version": "string",
                "build_deps": [{"path": "string", "version": "string", "sum": "12"}],
            },
        }
        mock_client, rest_client = self.make_clients(content)
        expected_response = GetNodeInfoResponse().from_dict(content)

        assert rest_client.GetNodeInfo(GetNodeInfoRequest()) == expected_response
        assert mock_client.last_base_url == "/cosmos/base/tendermint/v1beta1/node_info"

    def test_GetSyncing(self):
        """Test GetSyncing method."""
        content = {"syncing": True}
        mock_client, rest_client = self.make_clients(content)
        expected_response = GetSyncingResponse().from_dict(content)

        assert rest_client.GetSyncing(GetSyncingRequest()) == expected_response
        assert mock_client.last_base_url == "/cosmos/base/tendermint/v1beta1/syncing"

    def test_GetLatestBlock(self):
        """Test GetLatestBlock method."""
        content = {
            "block_id": {
                "hash": "c3RyaW5n",
                "part_set_header": {"total": 0, "hash": "c3RyaW5n"},
            },
            "block": {
                "header": {
                    "version": {"block": "12", "app": "12"},
                    "chain_id": "string",
                    "height": "12",
                    "time": "2022-03-29T10:21:54.568Z",
                    "last_block_id": {
                        "hash": "c3RyaW5n",
                        "part_set_header": {"total": 0, "hash": "c3RyaW5n"},
                    },
                    "last_commit_hash": "c3RyaW5n",
                    "data_hash": "c3RyaW5n",
                    "validators_hash": "c3RyaW5n",
                    "next_validators_hash": "c3RyaW5n",
                    "consensus_hash": "c3RyaW5n",
                    "app_hash": "c3RyaW5n",
                    "last_results_hash": "c3RyaW5n",
                    "evidence_hash": "c3RyaW5n",
                    "proposer_address": "c3RyaW5n",
                },
                "data": {"txs": ["c3RyaW5n"]},
                "evidence": {"evidence": []},
                "last_commit": {
                    "height": "12",
                    "round": 0,
                    "block_id": {
                        "hash": "c3RyaW5n",
                        "part_set_header": {"total": 0, "hash": "c3RyaW5n"},
                    },
                    "signatures": [
                        {
                            "block_id_flag": "BLOCK_ID_FLAG_UNKNOWN",
                            "validator_address": "c3RyaW5n",
                            "timestamp": "2022-03-29T10:21:54.569Z",
                            "signature": "c3RyaW5n",
                        }
                    ],
                },
            },
        }
        mock_client, rest_client = self.make_clients(content)
        expected_response = GetLatestBlockResponse().from_dict(content)

        assert rest_client.GetLatestBlock(GetLatestBlockRequest()) == expected_response
        assert (
            mock_client.last_base_url == "/cosmos/base/tendermint/v1beta1/blocks/latest"
        )

    def test_GetBlockByHeight(self):
        """Test GetBlockByHeight method."""
        content = {
            "block_id": {
                "hash": "c3RyaW5n",
                "part_set_header": {"total": 0, "hash": "c3RyaW5n"},
            },
            "block": {
                "header": {
                    "version": {"block": "12", "app": "12"},
                    "chain_id": "string",
                    "height": "12",
                    "time": "2022-03-29T10:27:01.686Z",
                    "last_block_id": {
                        "hash": "c3RyaW5n",
                        "part_set_header": {"total": 0, "hash": "c3RyaW5n"},
                    },
                    "last_commit_hash": "c3RyaW5n",
                    "data_hash": "c3RyaW5n",
                    "validators_hash": "c3RyaW5n",
                    "next_validators_hash": "c3RyaW5n",
                    "consensus_hash": "c3RyaW5n",
                    "app_hash": "c3RyaW5n",
                    "last_results_hash": "c3RyaW5n",
                    "evidence_hash": "c3RyaW5n",
                    "proposer_address": "c3RyaW5n",
                },
                "data": {"txs": ["c3RyaW5n"]},
                "evidence": {"evidence": []},
                "last_commit": {
                    "height": "12",
                    "round": 0,
                    "block_id": {
                        "hash": "c3RyaW5n",
                        "part_set_header": {"total": 0, "hash": "c3RyaW5n"},
                    },
                    "signatures": [
                        {
                            "block_id_flag": "BLOCK_ID_FLAG_UNKNOWN",
                            "validator_address": "c3RyaW5n",
                            "timestamp": "2022-03-29T10:27:01.687Z",
                            "signature": "c3RyaW5n",
                        }
                    ],
                },
            },
        }
        mock_client, rest_client = self.make_clients(content)
        expected_response = GetBlockByHeightResponse().from_dict(content)

        assert (
            rest_client.GetBlockByHeight(GetBlockByHeightRequest(height=123))
            == expected_response
        )
        assert mock_client.last_base_url == "/cosmos/base/tendermint/v1beta1/blocks/123"

    def test_GetLatestValidatorSet(self):
        """Test GetLatestValidatorSet method."""
        content = {
            "block_height": "12",
            "validators": [
                {
                    "address": "c3RyaW5n",
                    "pub_key": TYPE,
                    "voting_power": "12",
                    "proposer_priority": "12",
                }
            ],
            "pagination": {"next_key": "c3RyaW5n", "total": "12"},
        }
        mock_client, rest_client = self.make_clients(content)
        expected_response = GetLatestValidatorSetResponse().from_dict(content)

        assert (
            rest_client.GetLatestValidatorSet(GetLatestValidatorSetRequest())
            == expected_response
        )
        assert (
            mock_client.last_base_url
            == "/cosmos/base/tendermint/v1beta1/validatorsets/latest"
        )

    def test_GetValidatorSetByHeight(self):
        """Test GetValidatorSetByHeight method."""
        content = {
            "block_height": "12",
            "validators": [
                {
                    "address": "string",
                    "pub_key": TYPE,
                    "voting_power": "12",
                    "proposer_priority": "12",
                }
            ],
            "pagination": {"next_key": "c3RyaW5n", "total": "12"},
        }
        mock_client, rest_client = self.make_clients(content)
        expected_response = GetValidatorSetByHeightResponse().from_dict(content)

        assert (
            rest_client.GetValidatorSetByHeight(
                GetValidatorSetByHeightRequest(height=123)
            )
            == expected_response
        )
        assert (
            mock_client.last_base_url
            == "/cosmos/base/tendermint/v1beta1/validatorsets/123"
        )
