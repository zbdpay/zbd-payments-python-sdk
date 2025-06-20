# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import keysend_payment_send_params
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

__all__ = ["KeysendPaymentsResource", "AsyncKeysendPaymentsResource"]


class KeysendPaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysendPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return KeysendPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysendPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return KeysendPaymentsResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        pubkey: str | NotGiven = NOT_GIVEN,
        tlv_records: List[str] | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Start sending Keysend payments on the Lightning Network.

        Args:
          amount: The amount for the Payment -> in millisatoshis

          callback_url: The endpoint ZBD will POST Keysend Payment updates to

          metadata: Open metadata object property

          pubkey: The Public Key for the destination Lightning node

          tlv_records: List of TLV records <Expandable title="tlvRecord" defaultOpen>
              <ParamField body="type" type="number" initialValue={123456}> type of the TLV
              record

          value: value of the TLV record (hex encoded string)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/keysend-payment",
            body=maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "metadata": metadata,
                    "pubkey": pubkey,
                    "tlv_records": tlv_records,
                    "value": value,
                },
                keysend_payment_send_params.KeysendPaymentSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncKeysendPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysendPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncKeysendPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysendPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncKeysendPaymentsResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        pubkey: str | NotGiven = NOT_GIVEN,
        tlv_records: List[str] | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Start sending Keysend payments on the Lightning Network.

        Args:
          amount: The amount for the Payment -> in millisatoshis

          callback_url: The endpoint ZBD will POST Keysend Payment updates to

          metadata: Open metadata object property

          pubkey: The Public Key for the destination Lightning node

          tlv_records: List of TLV records <Expandable title="tlvRecord" defaultOpen>
              <ParamField body="type" type="number" initialValue={123456}> type of the TLV
              record

          value: value of the TLV record (hex encoded string)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/keysend-payment",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "metadata": metadata,
                    "pubkey": pubkey,
                    "tlv_records": tlv_records,
                    "value": value,
                },
                keysend_payment_send_params.KeysendPaymentSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class KeysendPaymentsResourceWithRawResponse:
    def __init__(self, keysend_payments: KeysendPaymentsResource) -> None:
        self._keysend_payments = keysend_payments

        self.send = to_raw_response_wrapper(
            keysend_payments.send,
        )


class AsyncKeysendPaymentsResourceWithRawResponse:
    def __init__(self, keysend_payments: AsyncKeysendPaymentsResource) -> None:
        self._keysend_payments = keysend_payments

        self.send = async_to_raw_response_wrapper(
            keysend_payments.send,
        )


class KeysendPaymentsResourceWithStreamingResponse:
    def __init__(self, keysend_payments: KeysendPaymentsResource) -> None:
        self._keysend_payments = keysend_payments

        self.send = to_streamed_response_wrapper(
            keysend_payments.send,
        )


class AsyncKeysendPaymentsResourceWithStreamingResponse:
    def __init__(self, keysend_payments: AsyncKeysendPaymentsResource) -> None:
        self._keysend_payments = keysend_payments

        self.send = async_to_streamed_response_wrapper(
            keysend_payments.send,
        )
