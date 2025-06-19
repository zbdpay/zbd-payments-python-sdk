# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["Oauth2Resource", "AsyncOauth2Resource"]


class Oauth2Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> Oauth2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return Oauth2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Oauth2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return Oauth2ResourceWithStreamingResponse(self)

    def create_authorization_url(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Create an authorization URL for ZBD Login."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v1/oauth2/authorize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def refresh_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Generate a new accessToken for a ZBD Login user."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/oauth2/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_user_data(
        self,
        *,
        usertoken: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Fetch user-related information about a logged-in ZBD User.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"usertoken": usertoken}), **(extra_headers or {})}
        return self._get(
            "/v1/oauth2/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_wallet_data(
        self,
        *,
        usertoken: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Fetch wallet-related information about a logged-in ZBD User.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"usertoken": usertoken}), **(extra_headers or {})}
        return self._get(
            "/v1/oauth2/wallet",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOauth2Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOauth2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOauth2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOauth2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zbdpay/zbd-payments-python-sdk#with_streaming_response
        """
        return AsyncOauth2ResourceWithStreamingResponse(self)

    async def create_authorization_url(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Create an authorization URL for ZBD Login."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v1/oauth2/authorize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def refresh_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Generate a new accessToken for a ZBD Login user."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/oauth2/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_user_data(
        self,
        *,
        usertoken: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Fetch user-related information about a logged-in ZBD User.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"usertoken": usertoken}), **(extra_headers or {})}
        return await self._get(
            "/v1/oauth2/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_wallet_data(
        self,
        *,
        usertoken: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Fetch wallet-related information about a logged-in ZBD User.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"usertoken": usertoken}), **(extra_headers or {})}
        return await self._get(
            "/v1/oauth2/wallet",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class Oauth2ResourceWithRawResponse:
    def __init__(self, oauth2: Oauth2Resource) -> None:
        self._oauth2 = oauth2

        self.create_authorization_url = to_raw_response_wrapper(
            oauth2.create_authorization_url,
        )
        self.refresh_token = to_raw_response_wrapper(
            oauth2.refresh_token,
        )
        self.retrieve_user_data = to_raw_response_wrapper(
            oauth2.retrieve_user_data,
        )
        self.retrieve_wallet_data = to_raw_response_wrapper(
            oauth2.retrieve_wallet_data,
        )


class AsyncOauth2ResourceWithRawResponse:
    def __init__(self, oauth2: AsyncOauth2Resource) -> None:
        self._oauth2 = oauth2

        self.create_authorization_url = async_to_raw_response_wrapper(
            oauth2.create_authorization_url,
        )
        self.refresh_token = async_to_raw_response_wrapper(
            oauth2.refresh_token,
        )
        self.retrieve_user_data = async_to_raw_response_wrapper(
            oauth2.retrieve_user_data,
        )
        self.retrieve_wallet_data = async_to_raw_response_wrapper(
            oauth2.retrieve_wallet_data,
        )


class Oauth2ResourceWithStreamingResponse:
    def __init__(self, oauth2: Oauth2Resource) -> None:
        self._oauth2 = oauth2

        self.create_authorization_url = to_streamed_response_wrapper(
            oauth2.create_authorization_url,
        )
        self.refresh_token = to_streamed_response_wrapper(
            oauth2.refresh_token,
        )
        self.retrieve_user_data = to_streamed_response_wrapper(
            oauth2.retrieve_user_data,
        )
        self.retrieve_wallet_data = to_streamed_response_wrapper(
            oauth2.retrieve_wallet_data,
        )


class AsyncOauth2ResourceWithStreamingResponse:
    def __init__(self, oauth2: AsyncOauth2Resource) -> None:
        self._oauth2 = oauth2

        self.create_authorization_url = async_to_streamed_response_wrapper(
            oauth2.create_authorization_url,
        )
        self.refresh_token = async_to_streamed_response_wrapper(
            oauth2.refresh_token,
        )
        self.retrieve_user_data = async_to_streamed_response_wrapper(
            oauth2.retrieve_user_data,
        )
        self.retrieve_wallet_data = async_to_streamed_response_wrapper(
            oauth2.retrieve_wallet_data,
        )
