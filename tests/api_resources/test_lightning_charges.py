# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLightningCharges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: ZbdPayments) -> None:
        lightning_charge = client.lightning_charges.create()
        assert lightning_charge is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: ZbdPayments) -> None:
        lightning_charge = client.lightning_charges.create(
            amount="string",
            callback_url="string",
            description="string",
            expires_in=0,
            internal_id="string",
        )
        assert lightning_charge is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: ZbdPayments) -> None:
        response = client.lightning_charges.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_charge = response.parse()
        assert lightning_charge is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: ZbdPayments) -> None:
        with client.lightning_charges.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_charge = response.parse()
            assert lightning_charge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ZbdPayments) -> None:
        lightning_charge = client.lightning_charges.retrieve(
            "id",
        )
        assert lightning_charge is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ZbdPayments) -> None:
        response = client.lightning_charges.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_charge = response.parse()
        assert lightning_charge is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ZbdPayments) -> None:
        with client.lightning_charges.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_charge = response.parse()
            assert lightning_charge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: ZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.lightning_charges.with_raw_response.retrieve(
                "",
            )


class TestAsyncLightningCharges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncZbdPayments) -> None:
        lightning_charge = await async_client.lightning_charges.create()
        assert lightning_charge is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        lightning_charge = await async_client.lightning_charges.create(
            amount="string",
            callback_url="string",
            description="string",
            expires_in=0,
            internal_id="string",
        )
        assert lightning_charge is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.lightning_charges.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_charge = await response.parse()
        assert lightning_charge is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.lightning_charges.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_charge = await response.parse()
            assert lightning_charge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZbdPayments) -> None:
        lightning_charge = await async_client.lightning_charges.retrieve(
            "id",
        )
        assert lightning_charge is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.lightning_charges.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lightning_charge = await response.parse()
        assert lightning_charge is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.lightning_charges.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lightning_charge = await response.parse()
            assert lightning_charge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.lightning_charges.with_raw_response.retrieve(
                "",
            )
