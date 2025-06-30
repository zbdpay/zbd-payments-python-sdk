# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["WalletResource", "AsyncWalletResource"]


class WalletResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WalletResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WalletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WalletResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return WalletResourceWithStreamingResponse(self)

    def retrieve_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Retrieve all data about a ZBD Project's Wallet."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v0/wallet",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWalletResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWalletResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWalletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWalletResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncWalletResourceWithStreamingResponse(self)

    async def retrieve_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Retrieve all data about a ZBD Project's Wallet."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v0/wallet",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WalletResourceWithRawResponse:
    def __init__(self, wallet: WalletResource) -> None:
        self._wallet = wallet

        self.retrieve_balance = to_raw_response_wrapper(
            wallet.retrieve_balance,
        )


class AsyncWalletResourceWithRawResponse:
    def __init__(self, wallet: AsyncWalletResource) -> None:
        self._wallet = wallet

        self.retrieve_balance = async_to_raw_response_wrapper(
            wallet.retrieve_balance,
        )


class WalletResourceWithStreamingResponse:
    def __init__(self, wallet: WalletResource) -> None:
        self._wallet = wallet

        self.retrieve_balance = to_streamed_response_wrapper(
            wallet.retrieve_balance,
        )


class AsyncWalletResourceWithStreamingResponse:
    def __init__(self, wallet: AsyncWalletResource) -> None:
        self._wallet = wallet

        self.retrieve_balance = async_to_streamed_response_wrapper(
            wallet.retrieve_balance,
        )
