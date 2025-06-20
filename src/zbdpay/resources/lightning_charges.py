# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import lightning_charge_create_params
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

__all__ = ["LightningChargesResource", "AsyncLightningChargesResource"]


class LightningChargesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LightningChargesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LightningChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LightningChargesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return LightningChargesResourceWithStreamingResponse(self)

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
        Start receiving instant Bitcoin payments through the ZBD API.

        Args:
          amount: The amount for the Charge -> in millisatoshis

          callback_url: The endpoint ZBD will POST Charge updates to

          description: Note or comment for this Charge (visible to payer)

          expires_in: Time until Charge expiration -> in seconds

          internal_id: Open metadata string property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/charges",
            body=maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "description": description,
                    "expires_in": expires_in,
                    "internal_id": internal_id,
                },
                lightning_charge_create_params.LightningChargeCreateParams,
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
        Retrieve all data about a single Charge.

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
            f"/v0/charges/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLightningChargesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLightningChargesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLightningChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLightningChargesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncLightningChargesResourceWithStreamingResponse(self)

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
        Start receiving instant Bitcoin payments through the ZBD API.

        Args:
          amount: The amount for the Charge -> in millisatoshis

          callback_url: The endpoint ZBD will POST Charge updates to

          description: Note or comment for this Charge (visible to payer)

          expires_in: Time until Charge expiration -> in seconds

          internal_id: Open metadata string property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/charges",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "description": description,
                    "expires_in": expires_in,
                    "internal_id": internal_id,
                },
                lightning_charge_create_params.LightningChargeCreateParams,
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
        Retrieve all data about a single Charge.

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
            f"/v0/charges/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LightningChargesResourceWithRawResponse:
    def __init__(self, lightning_charges: LightningChargesResource) -> None:
        self._lightning_charges = lightning_charges

        self.create = to_raw_response_wrapper(
            lightning_charges.create,
        )
        self.retrieve = to_raw_response_wrapper(
            lightning_charges.retrieve,
        )


class AsyncLightningChargesResourceWithRawResponse:
    def __init__(self, lightning_charges: AsyncLightningChargesResource) -> None:
        self._lightning_charges = lightning_charges

        self.create = async_to_raw_response_wrapper(
            lightning_charges.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            lightning_charges.retrieve,
        )


class LightningChargesResourceWithStreamingResponse:
    def __init__(self, lightning_charges: LightningChargesResource) -> None:
        self._lightning_charges = lightning_charges

        self.create = to_streamed_response_wrapper(
            lightning_charges.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            lightning_charges.retrieve,
        )


class AsyncLightningChargesResourceWithStreamingResponse:
    def __init__(self, lightning_charges: AsyncLightningChargesResource) -> None:
        self._lightning_charges = lightning_charges

        self.create = async_to_streamed_response_wrapper(
            lightning_charges.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            lightning_charges.retrieve,
        )
