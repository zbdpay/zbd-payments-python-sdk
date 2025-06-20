# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import lightning_address_send_payment_params, lightning_address_create_charge_params
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

__all__ = ["LightningAddressResource", "AsyncLightningAddressResource"]


class LightningAddressResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LightningAddressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LightningAddressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LightningAddressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return LightningAddressResourceWithStreamingResponse(self)

    def create_charge(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        lnaddress: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Generate a payment request for a Lightning Address.

        Args:
          amount: The amount for the Charge -> in millisatoshis

          description: Note or comment of this Charge

          lnaddress: The Lightning Address of the intended recipient

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/ln-address/fetch-charge",
            body=maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                    "lnaddress": lnaddress,
                },
                lightning_address_create_charge_params.LightningAddressCreateChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_payment(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        ln_address: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send instant Bitcoin payments to any Lightning Address.

        Args:
          amount: The amount for the Payment -> in millisatoshis

          callback_url: The endpoint ZBD will POST Charge updates to

          comment: Note or description of this Payment

          internal_id: Open metadata string property

          ln_address: The Lightning Address of the intended recipient (e.g. andre@zbd.gg)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/ln-address/send-payment",
            body=maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "comment": comment,
                    "internal_id": internal_id,
                    "ln_address": ln_address,
                },
                lightning_address_send_payment_params.LightningAddressSendPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def validate(
        self,
        address: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Verify the validity of a Lightning Address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v0/ln-address/validate/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLightningAddressResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLightningAddressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLightningAddressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLightningAddressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncLightningAddressResourceWithStreamingResponse(self)

    async def create_charge(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        lnaddress: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Generate a payment request for a Lightning Address.

        Args:
          amount: The amount for the Charge -> in millisatoshis

          description: Note or comment of this Charge

          lnaddress: The Lightning Address of the intended recipient

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/ln-address/fetch-charge",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                    "lnaddress": lnaddress,
                },
                lightning_address_create_charge_params.LightningAddressCreateChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_payment(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        ln_address: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send instant Bitcoin payments to any Lightning Address.

        Args:
          amount: The amount for the Payment -> in millisatoshis

          callback_url: The endpoint ZBD will POST Charge updates to

          comment: Note or description of this Payment

          internal_id: Open metadata string property

          ln_address: The Lightning Address of the intended recipient (e.g. andre@zbd.gg)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/ln-address/send-payment",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "comment": comment,
                    "internal_id": internal_id,
                    "ln_address": ln_address,
                },
                lightning_address_send_payment_params.LightningAddressSendPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def validate(
        self,
        address: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Verify the validity of a Lightning Address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v0/ln-address/validate/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LightningAddressResourceWithRawResponse:
    def __init__(self, lightning_address: LightningAddressResource) -> None:
        self._lightning_address = lightning_address

        self.create_charge = to_raw_response_wrapper(
            lightning_address.create_charge,
        )
        self.send_payment = to_raw_response_wrapper(
            lightning_address.send_payment,
        )
        self.validate = to_raw_response_wrapper(
            lightning_address.validate,
        )


class AsyncLightningAddressResourceWithRawResponse:
    def __init__(self, lightning_address: AsyncLightningAddressResource) -> None:
        self._lightning_address = lightning_address

        self.create_charge = async_to_raw_response_wrapper(
            lightning_address.create_charge,
        )
        self.send_payment = async_to_raw_response_wrapper(
            lightning_address.send_payment,
        )
        self.validate = async_to_raw_response_wrapper(
            lightning_address.validate,
        )


class LightningAddressResourceWithStreamingResponse:
    def __init__(self, lightning_address: LightningAddressResource) -> None:
        self._lightning_address = lightning_address

        self.create_charge = to_streamed_response_wrapper(
            lightning_address.create_charge,
        )
        self.send_payment = to_streamed_response_wrapper(
            lightning_address.send_payment,
        )
        self.validate = to_streamed_response_wrapper(
            lightning_address.validate,
        )


class AsyncLightningAddressResourceWithStreamingResponse:
    def __init__(self, lightning_address: AsyncLightningAddressResource) -> None:
        self._lightning_address = lightning_address

        self.create_charge = async_to_streamed_response_wrapper(
            lightning_address.create_charge,
        )
        self.send_payment = async_to_streamed_response_wrapper(
            lightning_address.send_payment,
        )
        self.validate = async_to_streamed_response_wrapper(
            lightning_address.validate,
        )
