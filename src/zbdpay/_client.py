# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    utils,
    oauth2,
    wallet,
    vouchers,
    gamertags,
    email_payments,
    keysend_payments,
    internal_transfer,
    lightning_address,
    lightning_charges,
    lightning_payments,
    withdrawal_requests,
    lightning_static_charges,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ZbdPayments",
    "AsyncZbdPayments",
    "Client",
    "AsyncClient",
]


class ZbdPayments(SyncAPIClient):
    gamertags: gamertags.GamertagsResource
    lightning_charges: lightning_charges.LightningChargesResource
    internal_transfer: internal_transfer.InternalTransferResource
    lightning_address: lightning_address.LightningAddressResource
    lightning_static_charges: lightning_static_charges.LightningStaticChargesResource
    vouchers: vouchers.VouchersResource
    withdrawal_requests: withdrawal_requests.WithdrawalRequestsResource
    lightning_payments: lightning_payments.LightningPaymentsResource
    wallet: wallet.WalletResource
    utils: utils.UtilsResource
    oauth2: oauth2.Oauth2Resource
    keysend_payments: keysend_payments.KeysendPaymentsResource
    email_payments: email_payments.EmailPaymentsResource
    with_raw_response: ZbdPaymentsWithRawResponse
    with_streaming_response: ZbdPaymentsWithStreamedResponse

    # client options
    apikey: str | None

    def __init__(
        self,
        *,
        apikey: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous ZbdPayments client instance.

        This automatically infers the `apikey` argument from the `ZBD_PAYMENTS_API_KEY` environment variable if it is not provided.
        """
        if apikey is None:
            apikey = os.environ.get("ZBD_PAYMENTS_API_KEY")
        self.apikey = apikey

        if base_url is None:
            base_url = os.environ.get("ZBD_PAYMENTS_BASE_URL")
        if base_url is None:
            base_url = f"https://api.zebedee.io"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.gamertags = gamertags.GamertagsResource(self)
        self.lightning_charges = lightning_charges.LightningChargesResource(self)
        self.internal_transfer = internal_transfer.InternalTransferResource(self)
        self.lightning_address = lightning_address.LightningAddressResource(self)
        self.lightning_static_charges = lightning_static_charges.LightningStaticChargesResource(self)
        self.vouchers = vouchers.VouchersResource(self)
        self.withdrawal_requests = withdrawal_requests.WithdrawalRequestsResource(self)
        self.lightning_payments = lightning_payments.LightningPaymentsResource(self)
        self.wallet = wallet.WalletResource(self)
        self.utils = utils.UtilsResource(self)
        self.oauth2 = oauth2.Oauth2Resource(self)
        self.keysend_payments = keysend_payments.KeysendPaymentsResource(self)
        self.email_payments = email_payments.EmailPaymentsResource(self)
        self.with_raw_response = ZbdPaymentsWithRawResponse(self)
        self.with_streaming_response = ZbdPaymentsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        apikey = self.apikey
        if apikey is None:
            return {}
        return {"apikey": apikey}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.apikey and headers.get("apikey"):
            return
        if isinstance(custom_headers.get("apikey"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the apikey to be set. Or for the `apikey` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        apikey: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            apikey=apikey or self.apikey,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncZbdPayments(AsyncAPIClient):
    gamertags: gamertags.AsyncGamertagsResource
    lightning_charges: lightning_charges.AsyncLightningChargesResource
    internal_transfer: internal_transfer.AsyncInternalTransferResource
    lightning_address: lightning_address.AsyncLightningAddressResource
    lightning_static_charges: lightning_static_charges.AsyncLightningStaticChargesResource
    vouchers: vouchers.AsyncVouchersResource
    withdrawal_requests: withdrawal_requests.AsyncWithdrawalRequestsResource
    lightning_payments: lightning_payments.AsyncLightningPaymentsResource
    wallet: wallet.AsyncWalletResource
    utils: utils.AsyncUtilsResource
    oauth2: oauth2.AsyncOauth2Resource
    keysend_payments: keysend_payments.AsyncKeysendPaymentsResource
    email_payments: email_payments.AsyncEmailPaymentsResource
    with_raw_response: AsyncZbdPaymentsWithRawResponse
    with_streaming_response: AsyncZbdPaymentsWithStreamedResponse

    # client options
    apikey: str | None

    def __init__(
        self,
        *,
        apikey: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncZbdPayments client instance.

        This automatically infers the `apikey` argument from the `ZBD_PAYMENTS_API_KEY` environment variable if it is not provided.
        """
        if apikey is None:
            apikey = os.environ.get("ZBD_PAYMENTS_API_KEY")
        self.apikey = apikey

        if base_url is None:
            base_url = os.environ.get("ZBD_PAYMENTS_BASE_URL")
        if base_url is None:
            base_url = f"https://api.zebedee.io"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.gamertags = gamertags.AsyncGamertagsResource(self)
        self.lightning_charges = lightning_charges.AsyncLightningChargesResource(self)
        self.internal_transfer = internal_transfer.AsyncInternalTransferResource(self)
        self.lightning_address = lightning_address.AsyncLightningAddressResource(self)
        self.lightning_static_charges = lightning_static_charges.AsyncLightningStaticChargesResource(self)
        self.vouchers = vouchers.AsyncVouchersResource(self)
        self.withdrawal_requests = withdrawal_requests.AsyncWithdrawalRequestsResource(self)
        self.lightning_payments = lightning_payments.AsyncLightningPaymentsResource(self)
        self.wallet = wallet.AsyncWalletResource(self)
        self.utils = utils.AsyncUtilsResource(self)
        self.oauth2 = oauth2.AsyncOauth2Resource(self)
        self.keysend_payments = keysend_payments.AsyncKeysendPaymentsResource(self)
        self.email_payments = email_payments.AsyncEmailPaymentsResource(self)
        self.with_raw_response = AsyncZbdPaymentsWithRawResponse(self)
        self.with_streaming_response = AsyncZbdPaymentsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        apikey = self.apikey
        if apikey is None:
            return {}
        return {"apikey": apikey}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.apikey and headers.get("apikey"):
            return
        if isinstance(custom_headers.get("apikey"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the apikey to be set. Or for the `apikey` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        apikey: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            apikey=apikey or self.apikey,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ZbdPaymentsWithRawResponse:
    def __init__(self, client: ZbdPayments) -> None:
        self.gamertags = gamertags.GamertagsResourceWithRawResponse(client.gamertags)
        self.lightning_charges = lightning_charges.LightningChargesResourceWithRawResponse(client.lightning_charges)
        self.internal_transfer = internal_transfer.InternalTransferResourceWithRawResponse(client.internal_transfer)
        self.lightning_address = lightning_address.LightningAddressResourceWithRawResponse(client.lightning_address)
        self.lightning_static_charges = lightning_static_charges.LightningStaticChargesResourceWithRawResponse(
            client.lightning_static_charges
        )
        self.vouchers = vouchers.VouchersResourceWithRawResponse(client.vouchers)
        self.withdrawal_requests = withdrawal_requests.WithdrawalRequestsResourceWithRawResponse(
            client.withdrawal_requests
        )
        self.lightning_payments = lightning_payments.LightningPaymentsResourceWithRawResponse(client.lightning_payments)
        self.wallet = wallet.WalletResourceWithRawResponse(client.wallet)
        self.utils = utils.UtilsResourceWithRawResponse(client.utils)
        self.oauth2 = oauth2.Oauth2ResourceWithRawResponse(client.oauth2)
        self.keysend_payments = keysend_payments.KeysendPaymentsResourceWithRawResponse(client.keysend_payments)
        self.email_payments = email_payments.EmailPaymentsResourceWithRawResponse(client.email_payments)


class AsyncZbdPaymentsWithRawResponse:
    def __init__(self, client: AsyncZbdPayments) -> None:
        self.gamertags = gamertags.AsyncGamertagsResourceWithRawResponse(client.gamertags)
        self.lightning_charges = lightning_charges.AsyncLightningChargesResourceWithRawResponse(
            client.lightning_charges
        )
        self.internal_transfer = internal_transfer.AsyncInternalTransferResourceWithRawResponse(
            client.internal_transfer
        )
        self.lightning_address = lightning_address.AsyncLightningAddressResourceWithRawResponse(
            client.lightning_address
        )
        self.lightning_static_charges = lightning_static_charges.AsyncLightningStaticChargesResourceWithRawResponse(
            client.lightning_static_charges
        )
        self.vouchers = vouchers.AsyncVouchersResourceWithRawResponse(client.vouchers)
        self.withdrawal_requests = withdrawal_requests.AsyncWithdrawalRequestsResourceWithRawResponse(
            client.withdrawal_requests
        )
        self.lightning_payments = lightning_payments.AsyncLightningPaymentsResourceWithRawResponse(
            client.lightning_payments
        )
        self.wallet = wallet.AsyncWalletResourceWithRawResponse(client.wallet)
        self.utils = utils.AsyncUtilsResourceWithRawResponse(client.utils)
        self.oauth2 = oauth2.AsyncOauth2ResourceWithRawResponse(client.oauth2)
        self.keysend_payments = keysend_payments.AsyncKeysendPaymentsResourceWithRawResponse(client.keysend_payments)
        self.email_payments = email_payments.AsyncEmailPaymentsResourceWithRawResponse(client.email_payments)


class ZbdPaymentsWithStreamedResponse:
    def __init__(self, client: ZbdPayments) -> None:
        self.gamertags = gamertags.GamertagsResourceWithStreamingResponse(client.gamertags)
        self.lightning_charges = lightning_charges.LightningChargesResourceWithStreamingResponse(
            client.lightning_charges
        )
        self.internal_transfer = internal_transfer.InternalTransferResourceWithStreamingResponse(
            client.internal_transfer
        )
        self.lightning_address = lightning_address.LightningAddressResourceWithStreamingResponse(
            client.lightning_address
        )
        self.lightning_static_charges = lightning_static_charges.LightningStaticChargesResourceWithStreamingResponse(
            client.lightning_static_charges
        )
        self.vouchers = vouchers.VouchersResourceWithStreamingResponse(client.vouchers)
        self.withdrawal_requests = withdrawal_requests.WithdrawalRequestsResourceWithStreamingResponse(
            client.withdrawal_requests
        )
        self.lightning_payments = lightning_payments.LightningPaymentsResourceWithStreamingResponse(
            client.lightning_payments
        )
        self.wallet = wallet.WalletResourceWithStreamingResponse(client.wallet)
        self.utils = utils.UtilsResourceWithStreamingResponse(client.utils)
        self.oauth2 = oauth2.Oauth2ResourceWithStreamingResponse(client.oauth2)
        self.keysend_payments = keysend_payments.KeysendPaymentsResourceWithStreamingResponse(client.keysend_payments)
        self.email_payments = email_payments.EmailPaymentsResourceWithStreamingResponse(client.email_payments)


class AsyncZbdPaymentsWithStreamedResponse:
    def __init__(self, client: AsyncZbdPayments) -> None:
        self.gamertags = gamertags.AsyncGamertagsResourceWithStreamingResponse(client.gamertags)
        self.lightning_charges = lightning_charges.AsyncLightningChargesResourceWithStreamingResponse(
            client.lightning_charges
        )
        self.internal_transfer = internal_transfer.AsyncInternalTransferResourceWithStreamingResponse(
            client.internal_transfer
        )
        self.lightning_address = lightning_address.AsyncLightningAddressResourceWithStreamingResponse(
            client.lightning_address
        )
        self.lightning_static_charges = (
            lightning_static_charges.AsyncLightningStaticChargesResourceWithStreamingResponse(
                client.lightning_static_charges
            )
        )
        self.vouchers = vouchers.AsyncVouchersResourceWithStreamingResponse(client.vouchers)
        self.withdrawal_requests = withdrawal_requests.AsyncWithdrawalRequestsResourceWithStreamingResponse(
            client.withdrawal_requests
        )
        self.lightning_payments = lightning_payments.AsyncLightningPaymentsResourceWithStreamingResponse(
            client.lightning_payments
        )
        self.wallet = wallet.AsyncWalletResourceWithStreamingResponse(client.wallet)
        self.utils = utils.AsyncUtilsResourceWithStreamingResponse(client.utils)
        self.oauth2 = oauth2.AsyncOauth2ResourceWithStreamingResponse(client.oauth2)
        self.keysend_payments = keysend_payments.AsyncKeysendPaymentsResourceWithStreamingResponse(
            client.keysend_payments
        )
        self.email_payments = email_payments.AsyncEmailPaymentsResourceWithStreamingResponse(client.email_payments)


Client = ZbdPayments

AsyncClient = AsyncZbdPayments
