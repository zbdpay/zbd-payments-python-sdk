# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_send(self, client: ZbdPayments) -> None:
        email_payment = client.email_payments.send()
        assert email_payment is None

    @pytest.mark.skip()
    @parametrize
    def test_method_send_with_all_params(self, client: ZbdPayments) -> None:
        email_payment = client.email_payments.send(
            amount="string",
            comment="string",
            email="string",
        )
        assert email_payment is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_send(self, client: ZbdPayments) -> None:
        response = client.email_payments.with_raw_response.send()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_payment = response.parse()
        assert email_payment is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_send(self, client: ZbdPayments) -> None:
        with client.email_payments.with_streaming_response.send() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_payment = response.parse()
            assert email_payment is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEmailPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_send(self, async_client: AsyncZbdPayments) -> None:
        email_payment = await async_client.email_payments.send()
        assert email_payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        email_payment = await async_client.email_payments.send(
            amount="string",
            comment="string",
            email="string",
        )
        assert email_payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.email_payments.with_raw_response.send()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_payment = await response.parse()
        assert email_payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.email_payments.with_streaming_response.send() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_payment = await response.parse()
            assert email_payment is None

        assert cast(Any, response.is_closed) is True
