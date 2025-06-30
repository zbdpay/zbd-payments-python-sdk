# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWithdrawalRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: ZbdPayments) -> None:
        withdrawal_request = client.withdrawal_requests.create()
        assert withdrawal_request is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: ZbdPayments) -> None:
        withdrawal_request = client.withdrawal_requests.create(
            amount="string",
            callback_url="string",
            description="string",
            expires_in=0,
            internal_id="string",
        )
        assert withdrawal_request is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: ZbdPayments) -> None:
        response = client.withdrawal_requests.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        withdrawal_request = response.parse()
        assert withdrawal_request is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: ZbdPayments) -> None:
        with client.withdrawal_requests.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            withdrawal_request = response.parse()
            assert withdrawal_request is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ZbdPayments) -> None:
        withdrawal_request = client.withdrawal_requests.retrieve(
            "id",
        )
        assert withdrawal_request is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ZbdPayments) -> None:
        response = client.withdrawal_requests.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        withdrawal_request = response.parse()
        assert withdrawal_request is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ZbdPayments) -> None:
        with client.withdrawal_requests.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            withdrawal_request = response.parse()
            assert withdrawal_request is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: ZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.withdrawal_requests.with_raw_response.retrieve(
                "",
            )


class TestAsyncWithdrawalRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncZbdPayments) -> None:
        withdrawal_request = await async_client.withdrawal_requests.create()
        assert withdrawal_request is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        withdrawal_request = await async_client.withdrawal_requests.create(
            amount="string",
            callback_url="string",
            description="string",
            expires_in=0,
            internal_id="string",
        )
        assert withdrawal_request is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.withdrawal_requests.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        withdrawal_request = await response.parse()
        assert withdrawal_request is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.withdrawal_requests.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            withdrawal_request = await response.parse()
            assert withdrawal_request is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZbdPayments) -> None:
        withdrawal_request = await async_client.withdrawal_requests.retrieve(
            "id",
        )
        assert withdrawal_request is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.withdrawal_requests.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        withdrawal_request = await response.parse()
        assert withdrawal_request is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.withdrawal_requests.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            withdrawal_request = await response.parse()
            assert withdrawal_request is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.withdrawal_requests.with_raw_response.retrieve(
                "",
            )
