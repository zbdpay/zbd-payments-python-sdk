# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLightningPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ZbdPayments) -> None:
        lightning_payment = client.lightning_payments.retrieve(
            "id",
        )
        assert lightning_payment is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ZbdPayments) -> None:
        response = client.lightning_payments.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_payment = response.parse()
        assert lightning_payment is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ZbdPayments) -> None:
        with client.lightning_payments.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_payment = response.parse()
            assert lightning_payment is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: ZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.lightning_payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_send(self, client: ZbdPayments) -> None:
        lightning_payment = client.lightning_payments.send()
        assert lightning_payment is None

    @pytest.mark.skip()
    @parametrize
    def test_method_send_with_all_params(self, client: ZbdPayments) -> None:
        lightning_payment = client.lightning_payments.send(
            amount="string",
            callback_url="string",
            description="string",
            internal_id="string",
            invoice="string",
        )
        assert lightning_payment is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_send(self, client: ZbdPayments) -> None:
        response = client.lightning_payments.with_raw_response.send()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_payment = response.parse()
        assert lightning_payment is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_send(self, client: ZbdPayments) -> None:
        with client.lightning_payments.with_streaming_response.send() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_payment = response.parse()
            assert lightning_payment is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLightningPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZbdPayments) -> None:
        lightning_payment = await async_client.lightning_payments.retrieve(
            "id",
        )
        assert lightning_payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.lightning_payments.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_payment = await response.parse()
        assert lightning_payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.lightning_payments.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_payment = await response.parse()
            assert lightning_payment is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.lightning_payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_send(self, async_client: AsyncZbdPayments) -> None:
        lightning_payment = await async_client.lightning_payments.send()
        assert lightning_payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        lightning_payment = await async_client.lightning_payments.send(
            amount="string",
            callback_url="string",
            description="string",
            internal_id="string",
            invoice="string",
        )
        assert lightning_payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.lightning_payments.with_raw_response.send()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_payment = await response.parse()
        assert lightning_payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.lightning_payments.with_streaming_response.send() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_payment = await response.parse()
            assert lightning_payment is None

        assert cast(Any, response.is_closed) is True
