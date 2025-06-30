# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import util_decode_lightning_charge_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["UtilsResource", "AsyncUtilsResource"]


class UtilsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UtilsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return UtilsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UtilsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return UtilsResourceWithStreamingResponse(self)

    def check_ip_support(
        self,
        ip: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Verify if a user is coming from a supported region.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ip:
            raise ValueError(f"Expected a non-empty value for `ip` but received {ip!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v0/is-supported-region/{ip}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def decode_lightning_charge(
        self,
        *,
        invoice: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Understand the inner properties of a Charge QR code.

        Args:
          invoice: The Charge or Invoice QR code contents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/decode-invoice",
            body=maybe_transform(
                {"invoice": invoice}, util_decode_lightning_charge_params.UtilDecodeLightningChargeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_prod_ips(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get the official IP addresses of ZBD servers."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v0/prod-ips",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_btc_usd(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get the latest price for Bitcoin in US Dollars."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v0/btcusd",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUtilsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUtilsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUtilsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUtilsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncUtilsResourceWithStreamingResponse(self)

    async def check_ip_support(
        self,
        ip: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Verify if a user is coming from a supported region.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ip:
            raise ValueError(f"Expected a non-empty value for `ip` but received {ip!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v0/is-supported-region/{ip}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def decode_lightning_charge(
        self,
        *,
        invoice: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Understand the inner properties of a Charge QR code.

        Args:
          invoice: The Charge or Invoice QR code contents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/decode-invoice",
            body=await async_maybe_transform(
                {"invoice": invoice}, util_decode_lightning_charge_params.UtilDecodeLightningChargeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_prod_ips(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get the official IP addresses of ZBD servers."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v0/prod-ips",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_btc_usd(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get the latest price for Bitcoin in US Dollars."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v0/btcusd",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UtilsResourceWithRawResponse:
    def __init__(self, utils: UtilsResource) -> None:
        self._utils = utils

        self.check_ip_support = to_raw_response_wrapper(
            utils.check_ip_support,
        )
        self.decode_lightning_charge = to_raw_response_wrapper(
            utils.decode_lightning_charge,
        )
        self.list_prod_ips = to_raw_response_wrapper(
            utils.list_prod_ips,
        )
        self.retrieve_btc_usd = to_raw_response_wrapper(
            utils.retrieve_btc_usd,
        )


class AsyncUtilsResourceWithRawResponse:
    def __init__(self, utils: AsyncUtilsResource) -> None:
        self._utils = utils

        self.check_ip_support = async_to_raw_response_wrapper(
            utils.check_ip_support,
        )
        self.decode_lightning_charge = async_to_raw_response_wrapper(
            utils.decode_lightning_charge,
        )
        self.list_prod_ips = async_to_raw_response_wrapper(
            utils.list_prod_ips,
        )
        self.retrieve_btc_usd = async_to_raw_response_wrapper(
            utils.retrieve_btc_usd,
        )


class UtilsResourceWithStreamingResponse:
    def __init__(self, utils: UtilsResource) -> None:
        self._utils = utils

        self.check_ip_support = to_streamed_response_wrapper(
            utils.check_ip_support,
        )
        self.decode_lightning_charge = to_streamed_response_wrapper(
            utils.decode_lightning_charge,
        )
        self.list_prod_ips = to_streamed_response_wrapper(
            utils.list_prod_ips,
        )
        self.retrieve_btc_usd = to_streamed_response_wrapper(
            utils.retrieve_btc_usd,
        )


class AsyncUtilsResourceWithStreamingResponse:
    def __init__(self, utils: AsyncUtilsResource) -> None:
        self._utils = utils

        self.check_ip_support = async_to_streamed_response_wrapper(
            utils.check_ip_support,
        )
        self.decode_lightning_charge = async_to_streamed_response_wrapper(
            utils.decode_lightning_charge,
        )
        self.list_prod_ips = async_to_streamed_response_wrapper(
            utils.list_prod_ips,
        )
        self.retrieve_btc_usd = async_to_streamed_response_wrapper(
            utils.retrieve_btc_usd,
        )
