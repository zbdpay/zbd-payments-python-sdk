# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVouchers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: ZbdPayments) -> None:
        voucher = client.vouchers.create()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: ZbdPayments) -> None:
        voucher = client.vouchers.create(
            amount="string",
            description="string",
        )
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: ZbdPayments) -> None:
        response = client.vouchers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = response.parse()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: ZbdPayments) -> None:
        with client.vouchers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = response.parse()
            assert voucher is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ZbdPayments) -> None:
        voucher = client.vouchers.retrieve(
            "id",
        )
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ZbdPayments) -> None:
        response = client.vouchers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = response.parse()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ZbdPayments) -> None:
        with client.vouchers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = response.parse()
            assert voucher is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: ZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vouchers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_redeem(self, client: ZbdPayments) -> None:
        voucher = client.vouchers.redeem()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_method_redeem_with_all_params(self, client: ZbdPayments) -> None:
        voucher = client.vouchers.redeem(
            code="string",
        )
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_redeem(self, client: ZbdPayments) -> None:
        response = client.vouchers.with_raw_response.redeem()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = response.parse()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_redeem(self, client: ZbdPayments) -> None:
        with client.vouchers.with_streaming_response.redeem() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = response.parse()
            assert voucher is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_revoke(self, client: ZbdPayments) -> None:
        voucher = client.vouchers.revoke()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_method_revoke_with_all_params(self, client: ZbdPayments) -> None:
        voucher = client.vouchers.revoke(
            code="string",
        )
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_revoke(self, client: ZbdPayments) -> None:
        response = client.vouchers.with_raw_response.revoke()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = response.parse()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_revoke(self, client: ZbdPayments) -> None:
        with client.vouchers.with_streaming_response.revoke() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = response.parse()
            assert voucher is None

        assert cast(Any, response.is_closed) is True


class TestAsyncVouchers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncZbdPayments) -> None:
        voucher = await async_client.vouchers.create()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        voucher = await async_client.vouchers.create(
            amount="string",
            description="string",
        )
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.vouchers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = await response.parse()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.vouchers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = await response.parse()
            assert voucher is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncZbdPayments) -> None:
        voucher = await async_client.vouchers.retrieve(
            "id",
        )
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.vouchers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = await response.parse()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.vouchers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = await response.parse()
            assert voucher is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vouchers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_redeem(self, async_client: AsyncZbdPayments) -> None:
        voucher = await async_client.vouchers.redeem()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_redeem_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        voucher = await async_client.vouchers.redeem(
            code="string",
        )
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_redeem(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.vouchers.with_raw_response.redeem()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = await response.parse()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_redeem(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.vouchers.with_streaming_response.redeem() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = await response.parse()
            assert voucher is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_revoke(self, async_client: AsyncZbdPayments) -> None:
        voucher = await async_client.vouchers.revoke()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_revoke_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        voucher = await async_client.vouchers.revoke(
            code="string",
        )
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.vouchers.with_raw_response.revoke()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = await response.parse()
        assert voucher is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.vouchers.with_streaming_response.revoke() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = await response.parse()
            assert voucher is None

        assert cast(Any, response.is_closed) is True
