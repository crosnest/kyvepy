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
"""Implementation of Gov interface using REST."""

from google.protobuf.json_format import Parse

from c4epy.common.rest_client import RestClient
from c4epy.gov.interface import Gov
from c4epy.protos.cosmos.gov.v1beta1 import (
    QueryDepositRequest,
    QueryDepositResponse,
    QueryDepositsRequest,
    QueryDepositsResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QueryProposalRequest,
    QueryProposalResponse,
    QueryProposalsRequest,
    QueryProposalsResponse,
    QueryTallyResultRequest,
    QueryTallyResultResponse,
    QueryVoteRequest,
    QueryVoteResponse,
    QueryVotesRequest,
    QueryVotesResponse,
)


class GovRestClient(Gov):
    """Gov REST client."""

    API_URL = "/cosmos/gov/v1beta1"

    def __init__(self, rest_api: RestClient) -> None:
        """
        Initialize.

        :param rest_api: RestClient api
        """
        self._rest_api = rest_api

    def Proposal(self, request: QueryProposalRequest) -> QueryProposalResponse:
        """
        Proposal queries proposal details based on ProposalID.

        :param request: QueryProposalRequest with proposal id

        :return: QueryProposalResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}",
        )
        return QueryProposalResponse().from_json(json_response)

    def Proposals(self, request: QueryProposalsRequest) -> QueryProposalsResponse:
        """
        Proposals queries all proposals based on given status.

        :param request: QueryProposalsRequest

        :return: QueryProposalsResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/",
            request,
        )
        return QueryProposalsResponse().from_json(json_response)

    def Vote(self, request: QueryVoteRequest) -> QueryVoteResponse:
        """
        Vote queries voted information based on proposalID, voterAddr.

        :param request: QueryVoteRequest with voter and proposal id

        :return: QueryVoteResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}/votes/{request.voter}"
        )
        return QueryVoteResponse().from_json(json_response)

    def Votes(self, request: QueryVotesRequest) -> QueryVotesResponse:
        """
        Votes queries votes of a given proposal.

        :param request: QueryVotesResponse with proposal id

        :return: QueryVotesResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}/votes/",
            request,
            ["proposalID"],
        )
        return QueryVotesResponse().from_json(json_response)

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """
        Params queries all parameters of the gov module.

        :param request: QueryParamsRequest with params_type

        :return: QueryParamsResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/params/{request.params_type}"
        )
        return QueryParamsResponse().from_json(json_response)

    def Deposit(self, request: QueryDepositRequest) -> QueryDepositResponse:
        """
        Deposit queries single deposit information based proposalID, depositAddr.

        :param request: QueryDepositRequest with depositor and proposal_id

        :return: QueryDepositResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}/deposits/{request.depositor}"
        )
        return QueryDepositResponse().from_json(json_response)

    def Deposits(self, request: QueryDepositsRequest) -> QueryDepositsResponse:
        """Deposits queries all deposits of a single proposal.

        :param request: QueryDepositsRequest with proposal_id

        :return: QueryDepositsResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}/deposits/",
            request,
            ["proposalID"],
        )
        return QueryDepositsResponse().from_json(json_response)

    def TallyResult(self, request: QueryTallyResultRequest) -> QueryTallyResultResponse:
        """
        Tally Result queries the tally of a proposal vote.

        :param request: QueryTallyResultRequest with proposal_id

        :return: QueryTallyResultResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/proposals/{request.proposal_id}/tally"
        )
        return QueryTallyResultResponse().from_json(json_response)
