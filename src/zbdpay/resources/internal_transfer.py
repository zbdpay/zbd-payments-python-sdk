# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import internal_transfer_initiate_params
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

__all__ = ["InternalTransferResource", "AsyncInternalTransferResource"]


class InternalTransferResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InternalTransferResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return InternalTransferResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InternalTransferResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return InternalTransferResourceWithStreamingResponse(self)

    def initiate(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        receiver_wallet_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Performs a transfer of funds between two Projects.

        Args:
          amount: The amount to be transferred -> in millisatoshis

          receiver_wallet_id: The Wallet ID of the recipient Project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/internal-transfer",
            body=maybe_transform(
                {
                    "amount": amount,
                    "receiver_wallet_id": receiver_wallet_id,
                },
                internal_transfer_initiate_params.InternalTransferInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInternalTransferResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInternalTransferResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncInternalTransferResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInternalTransferResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncInternalTransferResourceWithStreamingResponse(self)

    async def initiate(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        receiver_wallet_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Performs a transfer of funds between two Projects.

        Args:
          amount: The amount to be transferred -> in millisatoshis

          receiver_wallet_id: The Wallet ID of the recipient Project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/internal-transfer",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "receiver_wallet_id": receiver_wallet_id,
                },
                internal_transfer_initiate_params.InternalTransferInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InternalTransferResourceWithRawResponse:
    def __init__(self, internal_transfer: InternalTransferResource) -> None:
        self._internal_transfer = internal_transfer

        self.initiate = to_raw_response_wrapper(
            internal_transfer.initiate,
        )


class AsyncInternalTransferResourceWithRawResponse:
    def __init__(self, internal_transfer: AsyncInternalTransferResource) -> None:
        self._internal_transfer = internal_transfer

        self.initiate = async_to_raw_response_wrapper(
            internal_transfer.initiate,
        )


class InternalTransferResourceWithStreamingResponse:
    def __init__(self, internal_transfer: InternalTransferResource) -> None:
        self._internal_transfer = internal_transfer

        self.initiate = to_streamed_response_wrapper(
            internal_transfer.initiate,
        )


class AsyncInternalTransferResourceWithStreamingResponse:
    def __init__(self, internal_transfer: AsyncInternalTransferResource) -> None:
        self._internal_transfer = internal_transfer

        self.initiate = async_to_streamed_response_wrapper(
            internal_transfer.initiate,
        )
