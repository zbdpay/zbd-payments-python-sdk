# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWallet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_balance(self, client: ZbdPayments) -> None:
        wallet = client.wallet.retrieve_balance()
        assert wallet is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_balance(self, client: ZbdPayments) -> None:
        response = client.wallet.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert wallet is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_balance(self, client: ZbdPayments) -> None:
        with client.wallet.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert wallet is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWallet:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncZbdPayments) -> None:
        wallet = await async_client.wallet.retrieve_balance()
        assert wallet is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.wallet.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert wallet is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.wallet.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert wallet is None

        assert cast(Any, response.is_closed) is True
