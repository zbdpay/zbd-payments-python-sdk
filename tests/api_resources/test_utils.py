# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from zbdpay import ZbdPayments, AsyncZbdPayments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUtils:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check_ip_support(self, client: ZbdPayments) -> None:
        util = client.utils.check_ip_support(
            "ip",
        )
        assert util is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check_ip_support(self, client: ZbdPayments) -> None:
        response = client.utils.with_raw_response.check_ip_support(
            "ip",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = response.parse()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check_ip_support(self, client: ZbdPayments) -> None:
        with client.utils.with_streaming_response.check_ip_support(
            "ip",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = response.parse()
            assert util is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_check_ip_support(self, client: ZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip` but received ''"):
            client.utils.with_raw_response.check_ip_support(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_decode_lightning_charge(self, client: ZbdPayments) -> None:
        util = client.utils.decode_lightning_charge()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    def test_method_decode_lightning_charge_with_all_params(self, client: ZbdPayments) -> None:
        util = client.utils.decode_lightning_charge(
            invoice="string",
        )
        assert util is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_decode_lightning_charge(self, client: ZbdPayments) -> None:
        response = client.utils.with_raw_response.decode_lightning_charge()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = response.parse()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_decode_lightning_charge(self, client: ZbdPayments) -> None:
        with client.utils.with_streaming_response.decode_lightning_charge() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = response.parse()
            assert util is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_prod_ips(self, client: ZbdPayments) -> None:
        util = client.utils.list_prod_ips()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_prod_ips(self, client: ZbdPayments) -> None:
        response = client.utils.with_raw_response.list_prod_ips()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = response.parse()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_prod_ips(self, client: ZbdPayments) -> None:
        with client.utils.with_streaming_response.list_prod_ips() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = response.parse()
            assert util is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_btc_usd(self, client: ZbdPayments) -> None:
        util = client.utils.retrieve_btc_usd()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_btc_usd(self, client: ZbdPayments) -> None:
        response = client.utils.with_raw_response.retrieve_btc_usd()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = response.parse()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_btc_usd(self, client: ZbdPayments) -> None:
        with client.utils.with_streaming_response.retrieve_btc_usd() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = response.parse()
            assert util is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUtils:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_check_ip_support(self, async_client: AsyncZbdPayments) -> None:
        util = await async_client.utils.check_ip_support(
            "ip",
        )
        assert util is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check_ip_support(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.utils.with_raw_response.check_ip_support(
            "ip",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = await response.parse()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check_ip_support(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.utils.with_streaming_response.check_ip_support(
            "ip",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = await response.parse()
            assert util is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_check_ip_support(self, async_client: AsyncZbdPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip` but received ''"):
            await async_client.utils.with_raw_response.check_ip_support(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_decode_lightning_charge(self, async_client: AsyncZbdPayments) -> None:
        util = await async_client.utils.decode_lightning_charge()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_decode_lightning_charge_with_all_params(self, async_client: AsyncZbdPayments) -> None:
        util = await async_client.utils.decode_lightning_charge(
            invoice="string",
        )
        assert util is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_decode_lightning_charge(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.utils.with_raw_response.decode_lightning_charge()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = await response.parse()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_decode_lightning_charge(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.utils.with_streaming_response.decode_lightning_charge() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = await response.parse()
            assert util is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_prod_ips(self, async_client: AsyncZbdPayments) -> None:
        util = await async_client.utils.list_prod_ips()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_prod_ips(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.utils.with_raw_response.list_prod_ips()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = await response.parse()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_prod_ips(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.utils.with_streaming_response.list_prod_ips() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = await response.parse()
            assert util is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_btc_usd(self, async_client: AsyncZbdPayments) -> None:
        util = await async_client.utils.retrieve_btc_usd()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_btc_usd(self, async_client: AsyncZbdPayments) -> None:
        response = await async_client.utils.with_raw_response.retrieve_btc_usd()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = await response.parse()
        assert util is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_btc_usd(self, async_client: AsyncZbdPayments) -> None:
        async with async_client.utils.with_streaming_response.retrieve_btc_usd() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = await response.parse()
            assert util is None

        assert cast(Any, response.is_closed) is True
