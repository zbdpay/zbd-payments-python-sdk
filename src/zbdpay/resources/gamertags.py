# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import gamertag_send_payment_params, gamertag_create_charge_params
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

__all__ = ["GamertagsResource", "AsyncGamertagsResource"]


class GamertagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GamertagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return GamertagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GamertagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return GamertagsResourceWithStreamingResponse(self)

    def create_charge(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expires_in: float | NotGiven = NOT_GIVEN,
        gamertag: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Generate a payment request for a ZBD User.

        Args:
          amount: The amount for the Payment -> in millisatoshis

          callback_url: The endpoint ZBD will POST Charge updates to

          description: Note or comment for this Payment (visible to recipient)

          expires_in: Time until Charge expiration -> in seconds

          gamertag: Destination ZBD Gamertag

          internal_id: Open metadata string property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/gamertag/charges",
            body=maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "description": description,
                    "expires_in": expires_in,
                    "gamertag": gamertag,
                    "internal_id": internal_id,
                },
                gamertag_create_charge_params.GamertagCreateChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_by_gamertag(
        self,
        gamertag: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Retrieve Gamertag from a ZBD user ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gamertag:
            raise ValueError(f"Expected a non-empty value for `gamertag` but received {gamertag!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v0/user-id/gamertag/{gamertag}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_by_zbd_id(
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
        Retrieve ZBD user ID from a Gamertag.

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
            f"/v0/gamertag/user-id/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_payment(
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
        Retrieve all data about a Payment sent to ZBD User.

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
            f"/v0/gamertag/transaction/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_payment(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        gamertag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send instant Bitcoin payments to ZBD Users.

        Args:
          amount: The amount for the Payment -> in millisatoshis

          description: Note or comment for this Payment (visible to recipient)

          gamertag: Destination ZBD Gamertag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v0/gamertag/send-payment",
            body=maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                    "gamertag": gamertag,
                },
                gamertag_send_payment_params.GamertagSendPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGamertagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGamertagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGamertagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGamertagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncGamertagsResourceWithStreamingResponse(self)

    async def create_charge(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expires_in: float | NotGiven = NOT_GIVEN,
        gamertag: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Generate a payment request for a ZBD User.

        Args:
          amount: The amount for the Payment -> in millisatoshis

          callback_url: The endpoint ZBD will POST Charge updates to

          description: Note or comment for this Payment (visible to recipient)

          expires_in: Time until Charge expiration -> in seconds

          gamertag: Destination ZBD Gamertag

          internal_id: Open metadata string property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/gamertag/charges",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "callback_url": callback_url,
                    "description": description,
                    "expires_in": expires_in,
                    "gamertag": gamertag,
                    "internal_id": internal_id,
                },
                gamertag_create_charge_params.GamertagCreateChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_by_gamertag(
        self,
        gamertag: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Retrieve Gamertag from a ZBD user ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gamertag:
            raise ValueError(f"Expected a non-empty value for `gamertag` but received {gamertag!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v0/user-id/gamertag/{gamertag}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_by_zbd_id(
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
        Retrieve ZBD user ID from a Gamertag.

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
            f"/v0/gamertag/user-id/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_payment(
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
        Retrieve all data about a Payment sent to ZBD User.

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
            f"/v0/gamertag/transaction/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_payment(
        self,
        *,
        amount: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        gamertag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send instant Bitcoin payments to ZBD Users.

        Args:
          amount: The amount for the Payment -> in millisatoshis

          description: Note or comment for this Payment (visible to recipient)

          gamertag: Destination ZBD Gamertag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v0/gamertag/send-payment",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                    "gamertag": gamertag,
                },
                gamertag_send_payment_params.GamertagSendPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GamertagsResourceWithRawResponse:
    def __init__(self, gamertags: GamertagsResource) -> None:
        self._gamertags = gamertags

        self.create_charge = to_raw_response_wrapper(
            gamertags.create_charge,
        )
        self.retrieve_by_gamertag = to_raw_response_wrapper(
            gamertags.retrieve_by_gamertag,
        )
        self.retrieve_by_zbd_id = to_raw_response_wrapper(
            gamertags.retrieve_by_zbd_id,
        )
        self.retrieve_payment = to_raw_response_wrapper(
            gamertags.retrieve_payment,
        )
        self.send_payment = to_raw_response_wrapper(
            gamertags.send_payment,
        )


class AsyncGamertagsResourceWithRawResponse:
    def __init__(self, gamertags: AsyncGamertagsResource) -> None:
        self._gamertags = gamertags

        self.create_charge = async_to_raw_response_wrapper(
            gamertags.create_charge,
        )
        self.retrieve_by_gamertag = async_to_raw_response_wrapper(
            gamertags.retrieve_by_gamertag,
        )
        self.retrieve_by_zbd_id = async_to_raw_response_wrapper(
            gamertags.retrieve_by_zbd_id,
        )
        self.retrieve_payment = async_to_raw_response_wrapper(
            gamertags.retrieve_payment,
        )
        self.send_payment = async_to_raw_response_wrapper(
            gamertags.send_payment,
        )


class GamertagsResourceWithStreamingResponse:
    def __init__(self, gamertags: GamertagsResource) -> None:
        self._gamertags = gamertags

        self.create_charge = to_streamed_response_wrapper(
            gamertags.create_charge,
        )
        self.retrieve_by_gamertag = to_streamed_response_wrapper(
            gamertags.retrieve_by_gamertag,
        )
        self.retrieve_by_zbd_id = to_streamed_response_wrapper(
            gamertags.retrieve_by_zbd_id,
        )
        self.retrieve_payment = to_streamed_response_wrapper(
            gamertags.retrieve_payment,
        )
        self.send_payment = to_streamed_response_wrapper(
            gamertags.send_payment,
        )


class AsyncGamertagsResourceWithStreamingResponse:
    def __init__(self, gamertags: AsyncGamertagsResource) -> None:
        self._gamertags = gamertags

        self.create_charge = async_to_streamed_response_wrapper(
            gamertags.create_charge,
        )
        self.retrieve_by_gamertag = async_to_streamed_response_wrapper(
            gamertags.retrieve_by_gamertag,
        )
        self.retrieve_by_zbd_id = async_to_streamed_response_wrapper(
            gamertags.retrieve_by_zbd_id,
        )
        self.retrieve_payment = async_to_streamed_response_wrapper(
            gamertags.retrieve_payment,
        )
        self.send_payment = async_to_streamed_response_wrapper(
            gamertags.send_payment,
        )
