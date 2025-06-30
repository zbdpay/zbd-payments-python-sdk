# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLightningAddress:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_charge(self, client: ZbdPayments) -> None:
        lightning_address = client.lightning_address.create_charge()
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_charge_with_all_params(self, client: ZbdPayments) -> None:
        lightning_address = client.lightning_address.create_charge(
            amount="string",
            description="string",
            lnaddress="string",
        )
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_charge(self, client: ZbdPayments) -> None:
        response = client.lightning_address.with_raw_response.create_charge()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_address = response.parse()
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_charge(self, client: ZbdPayments) -> None:
        with client.lightning_address.with_streaming_response.create_charge() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_address = response.parse()
            assert lightning_address is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_send_payment(self, client: ZbdPayments) -> None:
        lightning_address = client.lightning_address.send_payment()
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    def test_method_send_payment_with_all_params(self, client: ZbdPayments) -> None:
        lightning_address = client.lightning_address.send_payment(
            amount="string",
            callback_url="string",
            comment="string",
            internal_id="string",
            ln_address="string",
        )
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_send_payment(self, client: ZbdPayments) -> None:
        response = client.lightning_address.with_raw_response.send_payment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_address = response.parse()
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_send_payment(self, client: ZbdPayments) -> None:
        with client.lightning_address.with_streaming_response.send_payment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_address = response.parse()
            assert lightning_address is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_validate(self, client: ZbdPayments) -> None:
        lightning_address = client.lightning_address.validate(
            "address",
        )
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate(self, client: ZbdPayments) -> None:
        response = client.lightning_address.with_raw_response.validate(
            "address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_address = response.parse()
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate(self, client: ZbdPayments) -> None:
        with client.lightning_address.with_streaming_response.validate(
            "address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_address = response.parse()
            assert lightning_address is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_validate(self, client: ZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.lightning_address.with_raw_response.validate(
                "",
            )


class TestAsyncLightningAddress:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_charge(self, async_client: AsyncZbdPayments) -> None:
        lightning_address = await async_client.lightning_address.create_charge()
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_charge_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        lightning_address = await async_client.lightning_address.create_charge(
            amount="string",
            description="string",
            lnaddress="string",
        )
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_charge(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.lightning_address.with_raw_response.create_charge()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_address = await response.parse()
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_charge(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.lightning_address.with_streaming_response.create_charge() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_address = await response.parse()
            assert lightning_address is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_send_payment(self, async_client: AsyncZbdPayments) -> None:
        lightning_address = await async_client.lightning_address.send_payment()
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_send_payment_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        lightning_address = await async_client.lightning_address.send_payment(
            amount="string",
            callback_url="string",
            comment="string",
            internal_id="string",
            ln_address="string",
        )
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_send_payment(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.lightning_address.with_raw_response.send_payment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_address = await response.parse()
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_send_payment(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.lightning_address.with_streaming_response.send_payment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_address = await response.parse()
            assert lightning_address is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate(self, async_client: AsyncZbdPayments) -> None:
        lightning_address = await async_client.lightning_address.validate(
            "address",
        )
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.lightning_address.with_raw_response.validate(
            "address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_address = await response.parse()
        assert lightning_address is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.lightning_address.with_streaming_response.validate(
            "address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_address = await response.parse()
            assert lightning_address is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.lightning_address.with_raw_response.validate(
                "",
            )
