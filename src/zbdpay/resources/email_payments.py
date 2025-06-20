# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import email_payment_send_params
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

__all__ = ["EmailPaymentsResource", "AsyncEmailPaymentsResource"]


class EmailPaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EmailPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return EmailPaymentsResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send instant Bitcoin payments to any email.

        Args:
          amount: The amount for the Payment -> in millisatoshis

          comment: Note / description of this Payment (may be shown to recipient)

          email: The Email of the intended recipient (e.g. info@zebedee.io)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/email/send-payment",
            body=maybe_transform(
                {
                    "amount": amount,
                    "comment": comment,
                    "email": email,
                },
                email_payment_send_params.EmailPaymentSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEmailPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncEmailPaymentsResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send instant Bitcoin payments to any email.

        Args:
          amount: The amount for the Payment -> in millisatoshis

          comment: Note / description of this Payment (may be shown to recipient)

          email: The Email of the intended recipient (e.g. info@zebedee.io)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/email/send-payment",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "comment": comment,
                    "email": email,
                },
                email_payment_send_params.EmailPaymentSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EmailPaymentsResourceWithRawResponse:
    def __init__(self, email_payments: EmailPaymentsResource) -> None:
        self._email_payments = email_payments

        self.send = to_raw_response_wrapper(
            email_payments.send,
        )


class AsyncEmailPaymentsResourceWithRawResponse:
    def __init__(self, email_payments: AsyncEmailPaymentsResource) -> None:
        self._email_payments = email_payments

        self.send = async_to_raw_response_wrapper(
            email_payments.send,
        )


class EmailPaymentsResourceWithStreamingResponse:
    def __init__(self, email_payments: EmailPaymentsResource) -> None:
        self._email_payments = email_payments

        self.send = to_streamed_response_wrapper(
            email_payments.send,
        )


class AsyncEmailPaymentsResourceWithStreamingResponse:
    def __init__(self, email_payments: AsyncEmailPaymentsResource) -> None:
        self._email_payments = email_payments

        self.send = async_to_streamed_response_wrapper(
            email_payments.send,
        )
