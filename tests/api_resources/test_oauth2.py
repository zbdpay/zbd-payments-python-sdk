# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOauth2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_authorization_url(self, client: ZbdPayments) -> None:
        oauth2 = client.oauth2.create_authorization_url()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_authorization_url(self, client: ZbdPayments) -> None:
        response = client.oauth2.with_raw_response.create_authorization_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = response.parse()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_authorization_url(self, client: ZbdPayments) -> None:
        with client.oauth2.with_streaming_response.create_authorization_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = response.parse()
            assert oauth2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_refresh_token(self, client: ZbdPayments) -> None:
        oauth2 = client.oauth2.refresh_token()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_refresh_token(self, client: ZbdPayments) -> None:
        response = client.oauth2.with_raw_response.refresh_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = response.parse()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_refresh_token(self, client: ZbdPayments) -> None:
        with client.oauth2.with_streaming_response.refresh_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = response.parse()
            assert oauth2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_user_data(self, client: ZbdPayments) -> None:
        oauth2 = client.oauth2.retrieve_user_data()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_user_data_with_all_params(self, client: ZbdPayments) -> None:
        oauth2 = client.oauth2.retrieve_user_data(
            usertoken="usertoken",
        )
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_user_data(self, client: ZbdPayments) -> None:
        response = client.oauth2.with_raw_response.retrieve_user_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = response.parse()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_user_data(self, client: ZbdPayments) -> None:
        with client.oauth2.with_streaming_response.retrieve_user_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = response.parse()
            assert oauth2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_wallet_data(self, client: ZbdPayments) -> None:
        oauth2 = client.oauth2.retrieve_wallet_data()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_wallet_data_with_all_params(self, client: ZbdPayments) -> None:
        oauth2 = client.oauth2.retrieve_wallet_data(
            usertoken="usertoken",
        )
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_wallet_data(self, client: ZbdPayments) -> None:
        response = client.oauth2.with_raw_response.retrieve_wallet_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = response.parse()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_wallet_data(self, client: ZbdPayments) -> None:
        with client.oauth2.with_streaming_response.retrieve_wallet_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = response.parse()
            assert oauth2 is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOauth2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_authorization_url(self, async_client: AsyncZbdPayments) -> None:
        oauth2 = await async_client.oauth2.create_authorization_url()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_authorization_url(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.oauth2.with_raw_response.create_authorization_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = await response.parse()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_authorization_url(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.oauth2.with_streaming_response.create_authorization_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = await response.parse()
            assert oauth2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_refresh_token(self, async_client: AsyncZbdPayments) -> None:
        oauth2 = await async_client.oauth2.refresh_token()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_refresh_token(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.oauth2.with_raw_response.refresh_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = await response.parse()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_refresh_token(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.oauth2.with_streaming_response.refresh_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = await response.parse()
            assert oauth2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_user_data(self, async_client: AsyncZbdPayments) -> None:
        oauth2 = await async_client.oauth2.retrieve_user_data()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_user_data_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        oauth2 = await async_client.oauth2.retrieve_user_data(
            usertoken="usertoken",
        )
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_user_data(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.oauth2.with_raw_response.retrieve_user_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = await response.parse()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_user_data(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.oauth2.with_streaming_response.retrieve_user_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = await response.parse()
            assert oauth2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_wallet_data(self, async_client: AsyncZbdPayments) -> None:
        oauth2 = await async_client.oauth2.retrieve_wallet_data()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_wallet_data_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        oauth2 = await async_client.oauth2.retrieve_wallet_data(
            usertoken="usertoken",
        )
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_wallet_data(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.oauth2.with_raw_response.retrieve_wallet_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = await response.parse()
        assert oauth2 is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_wallet_data(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.oauth2.with_streaming_response.retrieve_wallet_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = await response.parse()
            assert oauth2 is None

        assert cast(Any, response.is_closed) is True
