# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import lightning_payment_send_params
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

__all__ = ["LightningPaymentsResource", "AsyncLightningPaymentsResource"]


class LightningPaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LightningPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LightningPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LightningPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return LightningPaymentsResourceWithStreamingResponse(self)

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
        Retrieve all data about a single Payment.

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
            f"/v0/payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        invoice: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Start sending instant Bitcoin payments through the ZBD API.

        Args:
          amount: Amount to be paid to this Charge/Invoice -> in millisatoshis _(only valid if
              Amountless Invoice)_

          callback_url: The endpoint ZBD will POST Payment updates to

          description: Note or comment for this Payment

          internal_id: Open metadata string property

          invoice: Lightning Network Payment Request / Charge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/payments",
            body=maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "description": description,
                    "internal_id": internal_id,
                    "invoice": invoice,
                },
                lightning_payment_send_params.LightningPaymentSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLightningPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLightningPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLightningPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLightningPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncLightningPaymentsResourceWithStreamingResponse(self)

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
        Retrieve all data about a single Payment.

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
            f"/v0/payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        invoice: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Start sending instant Bitcoin payments through the ZBD API.

        Args:
          amount: Amount to be paid to this Charge/Invoice -> in millisatoshis _(only valid if
              Amountless Invoice)_

          callback_url: The endpoint ZBD will POST Payment updates to

          description: Note or comment for this Payment

          internal_id: Open metadata string property

          invoice: Lightning Network Payment Request / Charge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/payments",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "description": description,
                    "internal_id": internal_id,
                    "invoice": invoice,
                },
                lightning_payment_send_params.LightningPaymentSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LightningPaymentsResourceWithRawResponse:
    def __init__(self, lightning_payments: LightningPaymentsResource) -> None:
        self._lightning_payments = lightning_payments

        self.retrieve = to_raw_response_wrapper(
            lightning_payments.retrieve,
        )
        self.send = to_raw_response_wrapper(
            lightning_payments.send,
        )


class AsyncLightningPaymentsResourceWithRawResponse:
    def __init__(self, lightning_payments: AsyncLightningPaymentsResource) -> None:
        self._lightning_payments = lightning_payments

        self.retrieve = async_to_raw_response_wrapper(
            lightning_payments.retrieve,
        )
        self.send = async_to_raw_response_wrapper(
            lightning_payments.send,
        )


class LightningPaymentsResourceWithStreamingResponse:
    def __init__(self, lightning_payments: LightningPaymentsResource) -> None:
        self._lightning_payments = lightning_payments

        self.retrieve = to_streamed_response_wrapper(
            lightning_payments.retrieve,
        )
        self.send = to_streamed_response_wrapper(
            lightning_payments.send,
        )


class AsyncLightningPaymentsResourceWithStreamingResponse:
    def __init__(self, lightning_payments: AsyncLightningPaymentsResource) -> None:
        self._lightning_payments = lightning_payments

        self.retrieve = async_to_streamed_response_wrapper(
            lightning_payments.retrieve,
        )
        self.send = async_to_streamed_response_wrapper(
            lightning_payments.send,
        )
