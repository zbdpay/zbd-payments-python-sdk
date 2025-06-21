# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInternalTransfer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_initiate(self, client: ZbdPayments) -> None:
        internal_transfer = client.internal_transfer.initiate()
        assert internal_transfer is None

    @pytest.mark.skip()
    @parametrize
    def test_method_initiate_with_all_params(self, client: ZbdPayments) -> None:
        internal_transfer = client.internal_transfer.initiate(
            amount="string",
            receiver_wallet_id="string",
        )
        assert internal_transfer is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_initiate(self, client: ZbdPayments) -> None:
        response = client.internal_transfer.with_raw_response.initiate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_transfer = response.parse()
        assert internal_transfer is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_initiate(self, client: ZbdPayments) -> None:
        with client.internal_transfer.with_streaming_response.initiate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_transfer = response.parse()
            assert internal_transfer is None

        assert cast(Any, response.is_closed) is True


class TestAsyncInternalTransfer:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_initiate(self, async_client: AsyncZbdPayments) -> None:
        internal_transfer = await async_client.internal_transfer.initiate()
        assert internal_transfer is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_initiate_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        internal_transfer = await async_client.internal_transfer.initiate(
            amount="string",
            receiver_wallet_id="string",
        )
        assert internal_transfer is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_initiate(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.internal_transfer.with_raw_response.initiate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internal_transfer = await response.parse()
        assert internal_transfer is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_initiate(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.internal_transfer.with_streaming_response.initiate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internal_transfer = await response.parse()
            assert internal_transfer is None

        assert cast(Any, response.is_closed) is True
