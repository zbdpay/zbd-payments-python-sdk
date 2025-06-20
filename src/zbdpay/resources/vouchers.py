# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import voucher_create_params, voucher_redeem_params, voucher_revoke_params
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

__all__ = ["VouchersResource", "AsyncVouchersResource"]


class VouchersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VouchersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return VouchersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VouchersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return VouchersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create Voucher

        Args:
          amount: The amount for the Charge -> in millisatoshis

          description: Note or comment for this Charge (visible to payer)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/create-voucher",
            body=maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                },
                voucher_create_params.VoucherCreateParams,
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
        Get Voucher

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
            f"/v0/vouchers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def redeem(
        self,
        *,
        code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Redeem Voucher

        Args:
          code: Valid 8-digit ZBD Voucher Code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/redeem-voucher",
            body=maybe_transform({"code": code}, voucher_redeem_params.VoucherRedeemParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def revoke(
        self,
        *,
        code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Revoke Voucher

        Args:
          code: Valid 8-digit ZBD Voucher Code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/revoke-voucher",
            body=maybe_transform({"code": code}, voucher_revoke_params.VoucherRevokeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncVouchersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVouchersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncVouchersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVouchersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncVouchersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create Voucher

        Args:
          amount: The amount for the Charge -> in millisatoshis

          description: Note or comment for this Charge (visible to payer)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/create-voucher",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                },
                voucher_create_params.VoucherCreateParams,
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
        Get Voucher

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
            f"/v0/vouchers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def redeem(
        self,
        *,
        code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Redeem Voucher

        Args:
          code: Valid 8-digit ZBD Voucher Code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/redeem-voucher",
            body=await async_maybe_transform({"code": code}, voucher_redeem_params.VoucherRedeemParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def revoke(
        self,
        *,
        code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Revoke Voucher

        Args:
          code: Valid 8-digit ZBD Voucher Code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/revoke-voucher",
            body=await async_maybe_transform({"code": code}, voucher_revoke_params.VoucherRevokeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class VouchersResourceWithRawResponse:
    def __init__(self, vouchers: VouchersResource) -> None:
        self._vouchers = vouchers

        self.create = to_raw_response_wrapper(
            vouchers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            vouchers.retrieve,
        )
        self.redeem = to_raw_response_wrapper(
            vouchers.redeem,
        )
        self.revoke = to_raw_response_wrapper(
            vouchers.revoke,
        )


class AsyncVouchersResourceWithRawResponse:
    def __init__(self, vouchers: AsyncVouchersResource) -> None:
        self._vouchers = vouchers

        self.create = async_to_raw_response_wrapper(
            vouchers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            vouchers.retrieve,
        )
        self.redeem = async_to_raw_response_wrapper(
            vouchers.redeem,
        )
        self.revoke = async_to_raw_response_wrapper(
            vouchers.revoke,
        )


class VouchersResourceWithStreamingResponse:
    def __init__(self, vouchers: VouchersResource) -> None:
        self._vouchers = vouchers

        self.create = to_streamed_response_wrapper(
            vouchers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            vouchers.retrieve,
        )
        self.redeem = to_streamed_response_wrapper(
            vouchers.redeem,
        )
        self.revoke = to_streamed_response_wrapper(
            vouchers.revoke,
        )


class AsyncVouchersResourceWithStreamingResponse:
    def __init__(self, vouchers: AsyncVouchersResource) -> None:
        self._vouchers = vouchers

        self.create = async_to_streamed_response_wrapper(
            vouchers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            vouchers.retrieve,
        )
        self.redeem = async_to_streamed_response_wrapper(
            vouchers.redeem,
        )
        self.revoke = async_to_streamed_response_wrapper(
            vouchers.revoke,
        )
