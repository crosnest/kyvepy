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

"""Osmosis tx test."""

from c4epy.aerial.client import LedgerClient
from c4epy.aerial.wallet import LocalWallet

from tests.integration.osmosis_testnet.net_config import FaucetMixIn, NET_CONFIG
from tests.integration.test_tx import TestTx as BaseTestTx


class TestTx(BaseTestTx, FaucetMixIn):
    """Osmosis Transaction test

    :param BaseTestTx: Base test transaction
    :param FaucetMixIn: Osmosis testnet Faucet config
    """

    COIN = "uosmo"
    GAS_LIMIT = 120000
    PREFIX = "osmo"

    def get_wallet_1(self):
        wallet = LocalWallet.generate(prefix=self.PREFIX)
        self.ask_funds(wallet)
        return wallet

    def get_wallet_2(self):
        return LocalWallet.generate(prefix=self.PREFIX)

    def get_ledger(self):
        return LedgerClient(NET_CONFIG)