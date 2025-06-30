# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import withdrawal_request_create_params
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

__all__ = ["WithdrawalRequestsResource", "AsyncWithdrawalRequestsResource"]


class WithdrawalRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WithdrawalRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WithdrawalRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WithdrawalRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return WithdrawalRequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expires_in: float | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Start creating Bitcoin voucher QR codes.

        Args:
          amount: The amount for the Withdrawal Request -> in millisatoshis

          callback_url: The endpoint ZBD will POST Charge updates to

          description: Note or comment for this Withdrawal Request

          expires_in: Time until Withdrawal Request expiration -> in seconds

          internal_id: Open metadata string property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/withdrawal-requests",
            body=maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "description": description,
                    "expires_in": expires_in,
                    "internal_id": internal_id,
                },
                withdrawal_request_create_params.WithdrawalRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Retrieve all data about a single Withdrawal Request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v0/withdrawal-requests/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWithdrawalRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWithdrawalRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWithdrawalRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWithdrawalRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncWithdrawalRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expires_in: float | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Start creating Bitcoin voucher QR codes.

        Args:
          amount: The amount for the Withdrawal Request -> in millisatoshis

          callback_url: The endpoint ZBD will POST Charge updates to

          description: Note or comment for this Withdrawal Request

          expires_in: Time until Withdrawal Request expiration -> in seconds

          internal_id: Open metadata string property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/withdrawal-requests",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "description": description,
                    "expires_in": expires_in,
                    "internal_id": internal_id,
                },
                withdrawal_request_create_params.WithdrawalRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Retrieve all data about a single Withdrawal Request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v0/withdrawal-requests/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WithdrawalRequestsResourceWithRawResponse:
    def __init__(self, withdrawal_requests: WithdrawalRequestsResource) -> None:
        self._withdrawal_requests = withdrawal_requests

        self.create = to_raw_response_wrapper(
            withdrawal_requests.create,
        )
        self.retrieve = to_raw_response_wrapper(
            withdrawal_requests.retrieve,
        )


class AsyncWithdrawalRequestsResourceWithRawResponse:
    def __init__(self, withdrawal_requests: AsyncWithdrawalRequestsResource) -> None:
        self._withdrawal_requests = withdrawal_requests

        self.create = async_to_raw_response_wrapper(
            withdrawal_requests.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            withdrawal_requests.retrieve,
        )


class WithdrawalRequestsResourceWithStreamingResponse:
    def __init__(self, withdrawal_requests: WithdrawalRequestsResource) -> None:
        self._withdrawal_requests = withdrawal_requests

        self.create = to_streamed_response_wrapper(
            withdrawal_requests.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            withdrawal_requests.retrieve,
        )


class AsyncWithdrawalRequestsResourceWithStreamingResponse:
    def __init__(self, withdrawal_requests: AsyncWithdrawalRequestsResource) -> None:
        self._withdrawal_requests = withdrawal_requests

        self.create = async_to_streamed_response_wrapper(
            withdrawal_requests.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            withdrawal_requests.retrieve,
        )
