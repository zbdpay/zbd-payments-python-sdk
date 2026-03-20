# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import lightning_static_charge_create_params, lightning_static_charge_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["LightningStaticChargesResource", "AsyncLightningStaticChargesResource"]


class LightningStaticChargesResource(SyncAPIResource):
    """Lightning Charges endpoints"""

    @cached_property
    def with_raw_response(self) -> LightningStaticChargesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LightningStaticChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LightningStaticChargesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return LightningStaticChargesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allowed_slots: float | Omit = omit,
        callback_url: str | Omit = omit,
        description: str | Omit = omit,
        identifier: str | Omit = omit,
        internal_id: str | Omit = omit,
        max_amount: str | Omit = omit,
        min_amount: str | Omit = omit,
        success_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Start accepting payments on Lightning with Static QR codes.

        Args:
          allowed_slots: Number of payments this Static Charge can accept

          callback_url: The endpoint ZBD will POST Charge updates to

          description: Note or comment for this Static Charge (visible to payer)

          identifier: Used for Custom Lightning Addresses (see guide)

          internal_id: Open metadata string property

          max_amount: Maximum allowed amount for the Static Charge -> in millisatoshis

          min_amount: Minimum allowed amount for the Static Charge -> in millisatoshis

          success_message: Message displayed to the payer AFTER payment settles. Maximum of 144 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/static-charges",
            body=maybe_transform(
                {
                    "allowed_slots": allowed_slots,
                    "callback_url": callback_url,
                    "description": description,
                    "identifier": identifier,
                    "internal_id": internal_id,
                    "max_amount": max_amount,
                    "min_amount": min_amount,
                    "success_message": success_message,
                },
                lightning_static_charge_create_params.LightningStaticChargeCreateParams,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve all data about a single Static Charge.

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
            path_template("/v0/static-charges/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        allowed_slots: float | Omit = omit,
        callback_url: str | Omit = omit,
        description: str | Omit = omit,
        internal_id: str | Omit = omit,
        max_amount: str | Omit = omit,
        min_amount: str | Omit = omit,
        success_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Change the configuration of a Static Charge QR code.

        Args:
          allowed_slots: Number of payments this Static Charge can accept

          callback_url: The endpoint ZBD will POST Charge updates to

          description: Note or comment for this Static Charge (visible to payer)

          internal_id: Open metadata string property

          max_amount: Maximum allowed amount for the Static Charge -> in millisatoshis

          min_amount: Minimum allowed amount for the Static Charge -> in millisatoshis

          success_message: Message displayed to the payer AFTER payment settles

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/v0/static-charges/{id}", id=id),
            body=maybe_transform(
                {
                    "allowed_slots": allowed_slots,
                    "callback_url": callback_url,
                    "description": description,
                    "internal_id": internal_id,
                    "max_amount": max_amount,
                    "min_amount": min_amount,
                    "success_message": success_message,
                },
                lightning_static_charge_update_params.LightningStaticChargeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLightningStaticChargesResource(AsyncAPIResource):
    """Lightning Charges endpoints"""

    @cached_property
    def with_raw_response(self) -> AsyncLightningStaticChargesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLightningStaticChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLightningStaticChargesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncLightningStaticChargesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allowed_slots: float | Omit = omit,
        callback_url: str | Omit = omit,
        description: str | Omit = omit,
        identifier: str | Omit = omit,
        internal_id: str | Omit = omit,
        max_amount: str | Omit = omit,
        min_amount: str | Omit = omit,
        success_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Start accepting payments on Lightning with Static QR codes.

        Args:
          allowed_slots: Number of payments this Static Charge can accept

          callback_url: The endpoint ZBD will POST Charge updates to

          description: Note or comment for this Static Charge (visible to payer)

          identifier: Used for Custom Lightning Addresses (see guide)

          internal_id: Open metadata string property

          max_amount: Maximum allowed amount for the Static Charge -> in millisatoshis

          min_amount: Minimum allowed amount for the Static Charge -> in millisatoshis

          success_message: Message displayed to the payer AFTER payment settles. Maximum of 144 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/static-charges",
            body=await async_maybe_transform(
                {
                    "allowed_slots": allowed_slots,
                    "callback_url": callback_url,
                    "description": description,
                    "identifier": identifier,
                    "internal_id": internal_id,
                    "max_amount": max_amount,
                    "min_amount": min_amount,
                    "success_message": success_message,
                },
                lightning_static_charge_create_params.LightningStaticChargeCreateParams,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve all data about a single Static Charge.

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
            path_template("/v0/static-charges/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        allowed_slots: float | Omit = omit,
        callback_url: str | Omit = omit,
        description: str | Omit = omit,
        internal_id: str | Omit = omit,
        max_amount: str | Omit = omit,
        min_amount: str | Omit = omit,
        success_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Change the configuration of a Static Charge QR code.

        Args:
          allowed_slots: Number of payments this Static Charge can accept

          callback_url: The endpoint ZBD will POST Charge updates to

          description: Note or comment for this Static Charge (visible to payer)

          internal_id: Open metadata string property

          max_amount: Maximum allowed amount for the Static Charge -> in millisatoshis

          min_amount: Minimum allowed amount for the Static Charge -> in millisatoshis

          success_message: Message displayed to the payer AFTER payment settles

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/v0/static-charges/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "allowed_slots": allowed_slots,
                    "callback_url": callback_url,
                    "description": description,
                    "internal_id": internal_id,
                    "max_amount": max_amount,
                    "min_amount": min_amount,
                    "success_message": success_message,
                },
                lightning_static_charge_update_params.LightningStaticChargeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LightningStaticChargesResourceWithRawResponse:
    def __init__(self, lightning_static_charges: LightningStaticChargesResource) -> None:
        self._lightning_static_charges = lightning_static_charges

        self.create = to_raw_response_wrapper(
            lightning_static_charges.create,
        )
        self.retrieve = to_raw_response_wrapper(
            lightning_static_charges.retrieve,
        )
        self.update = to_raw_response_wrapper(
            lightning_static_charges.update,
        )


class AsyncLightningStaticChargesResourceWithRawResponse:
    def __init__(self, lightning_static_charges: AsyncLightningStaticChargesResource) -> None:
        self._lightning_static_charges = lightning_static_charges

        self.create = async_to_raw_response_wrapper(
            lightning_static_charges.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            lightning_static_charges.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            lightning_static_charges.update,
        )


class LightningStaticChargesResourceWithStreamingResponse:
    def __init__(self, lightning_static_charges: LightningStaticChargesResource) -> None:
        self._lightning_static_charges = lightning_static_charges

        self.create = to_streamed_response_wrapper(
            lightning_static_charges.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            lightning_static_charges.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            lightning_static_charges.update,
        )


class AsyncLightningStaticChargesResourceWithStreamingResponse:
    def __init__(self, lightning_static_charges: AsyncLightningStaticChargesResource) -> None:
        self._lightning_static_charges = lightning_static_charges

        self.create = async_to_streamed_response_wrapper(
            lightning_static_charges.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            lightning_static_charges.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            lightning_static_charges.update,
        )
