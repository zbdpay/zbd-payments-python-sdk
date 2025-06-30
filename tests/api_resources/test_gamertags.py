# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGamertags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_charge(self, client: ZbdPayments) -> None:
        gamertag = client.gamertags.create_charge()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_charge_with_all_params(self, client: ZbdPayments) -> None:
        gamertag = client.gamertags.create_charge(
            amount="string",
            callback_url="string",
            description="string",
            expires_in=0,
            gamertag="string",
            internal_id="string",
        )
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_charge(self, client: ZbdPayments) -> None:
        response = client.gamertags.with_raw_response.create_charge()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gamertag = response.parse()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_charge(self, client: ZbdPayments) -> None:
        with client.gamertags.with_streaming_response.create_charge() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gamertag = response.parse()
            assert gamertag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_gamertag(self, client: ZbdPayments) -> None:
        gamertag = client.gamertags.retrieve_by_gamertag(
            "gamertag",
        )
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_gamertag(self, client: ZbdPayments) -> None:
        response = client.gamertags.with_raw_response.retrieve_by_gamertag(
            "gamertag",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gamertag = response.parse()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_gamertag(self, client: ZbdPayments) -> None:
        with client.gamertags.with_streaming_response.retrieve_by_gamertag(
            "gamertag",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gamertag = response.parse()
            assert gamertag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_by_gamertag(self, client: ZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gamertag` but received ''"):
            client.gamertags.with_raw_response.retrieve_by_gamertag(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_zbd_id(self, client: ZbdPayments) -> None:
        gamertag = client.gamertags.retrieve_by_zbd_id(
            "id",
        )
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_zbd_id(self, client: ZbdPayments) -> None:
        response = client.gamertags.with_raw_response.retrieve_by_zbd_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gamertag = response.parse()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_zbd_id(self, client: ZbdPayments) -> None:
        with client.gamertags.with_streaming_response.retrieve_by_zbd_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gamertag = response.parse()
            assert gamertag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_by_zbd_id(self, client: ZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gamertags.with_raw_response.retrieve_by_zbd_id(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_payment(self, client: ZbdPayments) -> None:
        gamertag = client.gamertags.retrieve_payment(
            "id",
        )
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_payment(self, client: ZbdPayments) -> None:
        response = client.gamertags.with_raw_response.retrieve_payment(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gamertag = response.parse()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_payment(self, client: ZbdPayments) -> None:
        with client.gamertags.with_streaming_response.retrieve_payment(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gamertag = response.parse()
            assert gamertag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_payment(self, client: ZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gamertags.with_raw_response.retrieve_payment(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_send_payment(self, client: ZbdPayments) -> None:
        gamertag = client.gamertags.send_payment()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_method_send_payment_with_all_params(self, client: ZbdPayments) -> None:
        gamertag = client.gamertags.send_payment(
            amount="string",
            description="string",
            gamertag="string",
        )
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_send_payment(self, client: ZbdPayments) -> None:
        response = client.gamertags.with_raw_response.send_payment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gamertag = response.parse()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_send_payment(self, client: ZbdPayments) -> None:
        with client.gamertags.with_streaming_response.send_payment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gamertag = response.parse()
            assert gamertag is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGamertags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_charge(self, async_client: AsyncZbdPayments) -> None:
        gamertag = await async_client.gamertags.create_charge()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_charge_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        gamertag = await async_client.gamertags.create_charge(
            amount="string",
            callback_url="string",
            description="string",
            expires_in=0,
            gamertag="string",
            internal_id="string",
        )
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_charge(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.gamertags.with_raw_response.create_charge()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gamertag = await response.parse()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_charge(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.gamertags.with_streaming_response.create_charge() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gamertag = await response.parse()
            assert gamertag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_gamertag(self, async_client: AsyncZbdPayments) -> None:
        gamertag = await async_client.gamertags.retrieve_by_gamertag(
            "gamertag",
        )
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_gamertag(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.gamertags.with_raw_response.retrieve_by_gamertag(
            "gamertag",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gamertag = await response.parse()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_gamertag(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.gamertags.with_streaming_response.retrieve_by_gamertag(
            "gamertag",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gamertag = await response.parse()
            assert gamertag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_by_gamertag(self, async_client: AsyncZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gamertag` but received ''"):
            await async_client.gamertags.with_raw_response.retrieve_by_gamertag(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_zbd_id(self, async_client: AsyncZbdPayments) -> None:
        gamertag = await async_client.gamertags.retrieve_by_zbd_id(
            "id",
        )
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_zbd_id(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.gamertags.with_raw_response.retrieve_by_zbd_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gamertag = await response.parse()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_zbd_id(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.gamertags.with_streaming_response.retrieve_by_zbd_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gamertag = await response.parse()
            assert gamertag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_by_zbd_id(self, async_client: AsyncZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gamertags.with_raw_response.retrieve_by_zbd_id(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_payment(self, async_client: AsyncZbdPayments) -> None:
        gamertag = await async_client.gamertags.retrieve_payment(
            "id",
        )
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_payment(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.gamertags.with_raw_response.retrieve_payment(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gamertag = await response.parse()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_payment(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.gamertags.with_streaming_response.retrieve_payment(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gamertag = await response.parse()
            assert gamertag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_payment(self, async_client: AsyncZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gamertags.with_raw_response.retrieve_payment(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_send_payment(self, async_client: AsyncZbdPayments) -> None:
        gamertag = await async_client.gamertags.send_payment()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_send_payment_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        gamertag = await async_client.gamertags.send_payment(
            amount="string",
            description="string",
            gamertag="string",
        )
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_send_payment(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.gamertags.with_raw_response.send_payment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gamertag = await response.parse()
        assert gamertag is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_send_payment(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.gamertags.with_streaming_response.send_payment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gamertag = await response.parse()
            assert gamertag is None

        assert cast(Any, response.is_closed) is True
