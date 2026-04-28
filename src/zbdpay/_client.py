# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
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
    from .resources.utils import UtilsResource, AsyncUtilsResource
    from .resources.oauth2 import Oauth2Resource, AsyncOauth2Resource
    from .resources.wallet import WalletResource, AsyncWalletResource
    from .resources.vouchers import VouchersResource, AsyncVouchersResource
    from .resources.gamertags import GamertagsResource, AsyncGamertagsResource
    from .resources.email_payments import EmailPaymentsResource, AsyncEmailPaymentsResource
    from .resources.keysend_payments import KeysendPaymentsResource, AsyncKeysendPaymentsResource
    from .resources.internal_transfer import InternalTransferResource, AsyncInternalTransferResource
    from .resources.lightning_address import LightningAddressResource, AsyncLightningAddressResource
    from .resources.lightning_charges import LightningChargesResource, AsyncLightningChargesResource
    from .resources.lightning_payments import LightningPaymentsResource, AsyncLightningPaymentsResource
    from .resources.withdrawal_requests import WithdrawalRequestsResource, AsyncWithdrawalRequestsResource
    from .resources.lightning_static_charges import LightningStaticChargesResource, AsyncLightningStaticChargesResource

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
    # client options
    apikey: str | None

    def __init__(
        self,
        *,
        apikey: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

        custom_headers_env = os.environ.get("ZBD_PAYMENTS_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

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

    @cached_property
    def gamertags(self) -> GamertagsResource:
        """ZBD Gamertag endpoints"""
        from .resources.gamertags import GamertagsResource

        return GamertagsResource(self)

    @cached_property
    def lightning_charges(self) -> LightningChargesResource:
        """Lightning Charges endpoints"""
        from .resources.lightning_charges import LightningChargesResource

        return LightningChargesResource(self)

    @cached_property
    def internal_transfer(self) -> InternalTransferResource:
        """Internal Transfers endpoints"""
        from .resources.internal_transfer import InternalTransferResource

        return InternalTransferResource(self)

    @cached_property
    def lightning_address(self) -> LightningAddressResource:
        """Lightning Address endpoints"""
        from .resources.lightning_address import LightningAddressResource

        return LightningAddressResource(self)

    @cached_property
    def lightning_static_charges(self) -> LightningStaticChargesResource:
        """Lightning Charges endpoints"""
        from .resources.lightning_static_charges import LightningStaticChargesResource

        return LightningStaticChargesResource(self)

    @cached_property
    def vouchers(self) -> VouchersResource:
        """Vouchers endpoints"""
        from .resources.vouchers import VouchersResource

        return VouchersResource(self)

    @cached_property
    def withdrawal_requests(self) -> WithdrawalRequestsResource:
        """Withdrawal Requests endpoints"""
        from .resources.withdrawal_requests import WithdrawalRequestsResource

        return WithdrawalRequestsResource(self)

    @cached_property
    def lightning_payments(self) -> LightningPaymentsResource:
        """Lightning Payments endpoints"""
        from .resources.lightning_payments import LightningPaymentsResource

        return LightningPaymentsResource(self)

    @cached_property
    def wallet(self) -> WalletResource:
        """Wallet endpoints"""
        from .resources.wallet import WalletResource

        return WalletResource(self)

    @cached_property
    def utils(self) -> UtilsResource:
        """Utilities endpoints"""
        from .resources.utils import UtilsResource

        return UtilsResource(self)

    @cached_property
    def oauth2(self) -> Oauth2Resource:
        """OAuth2 endpoints"""
        from .resources.oauth2 import Oauth2Resource

        return Oauth2Resource(self)

    @cached_property
    def keysend_payments(self) -> KeysendPaymentsResource:
        """Keysend Payments endpoints"""
        from .resources.keysend_payments import KeysendPaymentsResource

        return KeysendPaymentsResource(self)

    @cached_property
    def email_payments(self) -> EmailPaymentsResource:
        """Email endpoints"""
        from .resources.email_payments import EmailPaymentsResource

        return EmailPaymentsResource(self)

    @cached_property
    def with_raw_response(self) -> ZbdPaymentsWithRawResponse:
        return ZbdPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZbdPaymentsWithStreamedResponse:
        return ZbdPaymentsWithStreamedResponse(self)

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
        if headers.get("apikey") or isinstance(custom_headers.get("apikey"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the apikey to be set. Or for the `apikey` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        apikey: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
    # client options
    apikey: str | None

    def __init__(
        self,
        *,
        apikey: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

        custom_headers_env = os.environ.get("ZBD_PAYMENTS_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

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

    @cached_property
    def gamertags(self) -> AsyncGamertagsResource:
        """ZBD Gamertag endpoints"""
        from .resources.gamertags import AsyncGamertagsResource

        return AsyncGamertagsResource(self)

    @cached_property
    def lightning_charges(self) -> AsyncLightningChargesResource:
        """Lightning Charges endpoints"""
        from .resources.lightning_charges import AsyncLightningChargesResource

        return AsyncLightningChargesResource(self)

    @cached_property
    def internal_transfer(self) -> AsyncInternalTransferResource:
        """Internal Transfers endpoints"""
        from .resources.internal_transfer import AsyncInternalTransferResource

        return AsyncInternalTransferResource(self)

    @cached_property
    def lightning_address(self) -> AsyncLightningAddressResource:
        """Lightning Address endpoints"""
        from .resources.lightning_address import AsyncLightningAddressResource

        return AsyncLightningAddressResource(self)

    @cached_property
    def lightning_static_charges(self) -> AsyncLightningStaticChargesResource:
        """Lightning Charges endpoints"""
        from .resources.lightning_static_charges import AsyncLightningStaticChargesResource

        return AsyncLightningStaticChargesResource(self)

    @cached_property
    def vouchers(self) -> AsyncVouchersResource:
        """Vouchers endpoints"""
        from .resources.vouchers import AsyncVouchersResource

        return AsyncVouchersResource(self)

    @cached_property
    def withdrawal_requests(self) -> AsyncWithdrawalRequestsResource:
        """Withdrawal Requests endpoints"""
        from .resources.withdrawal_requests import AsyncWithdrawalRequestsResource

        return AsyncWithdrawalRequestsResource(self)

    @cached_property
    def lightning_payments(self) -> AsyncLightningPaymentsResource:
        """Lightning Payments endpoints"""
        from .resources.lightning_payments import AsyncLightningPaymentsResource

        return AsyncLightningPaymentsResource(self)

    @cached_property
    def wallet(self) -> AsyncWalletResource:
        """Wallet endpoints"""
        from .resources.wallet import AsyncWalletResource

        return AsyncWalletResource(self)

    @cached_property
    def utils(self) -> AsyncUtilsResource:
        """Utilities endpoints"""
        from .resources.utils import AsyncUtilsResource

        return AsyncUtilsResource(self)

    @cached_property
    def oauth2(self) -> AsyncOauth2Resource:
        """OAuth2 endpoints"""
        from .resources.oauth2 import AsyncOauth2Resource

        return AsyncOauth2Resource(self)

    @cached_property
    def keysend_payments(self) -> AsyncKeysendPaymentsResource:
        """Keysend Payments endpoints"""
        from .resources.keysend_payments import AsyncKeysendPaymentsResource

        return AsyncKeysendPaymentsResource(self)

    @cached_property
    def email_payments(self) -> AsyncEmailPaymentsResource:
        """Email endpoints"""
        from .resources.email_payments import AsyncEmailPaymentsResource

        return AsyncEmailPaymentsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncZbdPaymentsWithRawResponse:
        return AsyncZbdPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZbdPaymentsWithStreamedResponse:
        return AsyncZbdPaymentsWithStreamedResponse(self)

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
        if headers.get("apikey") or isinstance(custom_headers.get("apikey"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the apikey to be set. Or for the `apikey` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        apikey: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
    _client: ZbdPayments

    def __init__(self, client: ZbdPayments) -> None:
        self._client = client

    @cached_property
    def gamertags(self) -> gamertags.GamertagsResourceWithRawResponse:
        """ZBD Gamertag endpoints"""
        from .resources.gamertags import GamertagsResourceWithRawResponse

        return GamertagsResourceWithRawResponse(self._client.gamertags)

    @cached_property
    def lightning_charges(self) -> lightning_charges.LightningChargesResourceWithRawResponse:
        """Lightning Charges endpoints"""
        from .resources.lightning_charges import LightningChargesResourceWithRawResponse

        return LightningChargesResourceWithRawResponse(self._client.lightning_charges)

    @cached_property
    def internal_transfer(self) -> internal_transfer.InternalTransferResourceWithRawResponse:
        """Internal Transfers endpoints"""
        from .resources.internal_transfer import InternalTransferResourceWithRawResponse

        return InternalTransferResourceWithRawResponse(self._client.internal_transfer)

    @cached_property
    def lightning_address(self) -> lightning_address.LightningAddressResourceWithRawResponse:
        """Lightning Address endpoints"""
        from .resources.lightning_address import LightningAddressResourceWithRawResponse

        return LightningAddressResourceWithRawResponse(self._client.lightning_address)

    @cached_property
    def lightning_static_charges(self) -> lightning_static_charges.LightningStaticChargesResourceWithRawResponse:
        """Lightning Charges endpoints"""
        from .resources.lightning_static_charges import LightningStaticChargesResourceWithRawResponse

        return LightningStaticChargesResourceWithRawResponse(self._client.lightning_static_charges)

    @cached_property
    def vouchers(self) -> vouchers.VouchersResourceWithRawResponse:
        """Vouchers endpoints"""
        from .resources.vouchers import VouchersResourceWithRawResponse

        return VouchersResourceWithRawResponse(self._client.vouchers)

    @cached_property
    def withdrawal_requests(self) -> withdrawal_requests.WithdrawalRequestsResourceWithRawResponse:
        """Withdrawal Requests endpoints"""
        from .resources.withdrawal_requests import WithdrawalRequestsResourceWithRawResponse

        return WithdrawalRequestsResourceWithRawResponse(self._client.withdrawal_requests)

    @cached_property
    def lightning_payments(self) -> lightning_payments.LightningPaymentsResourceWithRawResponse:
        """Lightning Payments endpoints"""
        from .resources.lightning_payments import LightningPaymentsResourceWithRawResponse

        return LightningPaymentsResourceWithRawResponse(self._client.lightning_payments)

    @cached_property
    def wallet(self) -> wallet.WalletResourceWithRawResponse:
        """Wallet endpoints"""
        from .resources.wallet import WalletResourceWithRawResponse

        return WalletResourceWithRawResponse(self._client.wallet)

    @cached_property
    def utils(self) -> utils.UtilsResourceWithRawResponse:
        """Utilities endpoints"""
        from .resources.utils import UtilsResourceWithRawResponse

        return UtilsResourceWithRawResponse(self._client.utils)

    @cached_property
    def oauth2(self) -> oauth2.Oauth2ResourceWithRawResponse:
        """OAuth2 endpoints"""
        from .resources.oauth2 import Oauth2ResourceWithRawResponse

        return Oauth2ResourceWithRawResponse(self._client.oauth2)

    @cached_property
    def keysend_payments(self) -> keysend_payments.KeysendPaymentsResourceWithRawResponse:
        """Keysend Payments endpoints"""
        from .resources.keysend_payments import KeysendPaymentsResourceWithRawResponse

        return KeysendPaymentsResourceWithRawResponse(self._client.keysend_payments)

    @cached_property
    def email_payments(self) -> email_payments.EmailPaymentsResourceWithRawResponse:
        """Email endpoints"""
        from .resources.email_payments import EmailPaymentsResourceWithRawResponse

        return EmailPaymentsResourceWithRawResponse(self._client.email_payments)


class AsyncZbdPaymentsWithRawResponse:
    _client: AsyncZbdPayments

    def __init__(self, client: AsyncZbdPayments) -> None:
        self._client = client

    @cached_property
    def gamertags(self) -> gamertags.AsyncGamertagsResourceWithRawResponse:
        """ZBD Gamertag endpoints"""
        from .resources.gamertags import AsyncGamertagsResourceWithRawResponse

        return AsyncGamertagsResourceWithRawResponse(self._client.gamertags)

    @cached_property
    def lightning_charges(self) -> lightning_charges.AsyncLightningChargesResourceWithRawResponse:
        """Lightning Charges endpoints"""
        from .resources.lightning_charges import AsyncLightningChargesResourceWithRawResponse

        return AsyncLightningChargesResourceWithRawResponse(self._client.lightning_charges)

    @cached_property
    def internal_transfer(self) -> internal_transfer.AsyncInternalTransferResourceWithRawResponse:
        """Internal Transfers endpoints"""
        from .resources.internal_transfer import AsyncInternalTransferResourceWithRawResponse

        return AsyncInternalTransferResourceWithRawResponse(self._client.internal_transfer)

    @cached_property
    def lightning_address(self) -> lightning_address.AsyncLightningAddressResourceWithRawResponse:
        """Lightning Address endpoints"""
        from .resources.lightning_address import AsyncLightningAddressResourceWithRawResponse

        return AsyncLightningAddressResourceWithRawResponse(self._client.lightning_address)

    @cached_property
    def lightning_static_charges(self) -> lightning_static_charges.AsyncLightningStaticChargesResourceWithRawResponse:
        """Lightning Charges endpoints"""
        from .resources.lightning_static_charges import AsyncLightningStaticChargesResourceWithRawResponse

        return AsyncLightningStaticChargesResourceWithRawResponse(self._client.lightning_static_charges)

    @cached_property
    def vouchers(self) -> vouchers.AsyncVouchersResourceWithRawResponse:
        """Vouchers endpoints"""
        from .resources.vouchers import AsyncVouchersResourceWithRawResponse

        return AsyncVouchersResourceWithRawResponse(self._client.vouchers)

    @cached_property
    def withdrawal_requests(self) -> withdrawal_requests.AsyncWithdrawalRequestsResourceWithRawResponse:
        """Withdrawal Requests endpoints"""
        from .resources.withdrawal_requests import AsyncWithdrawalRequestsResourceWithRawResponse

        return AsyncWithdrawalRequestsResourceWithRawResponse(self._client.withdrawal_requests)

    @cached_property
    def lightning_payments(self) -> lightning_payments.AsyncLightningPaymentsResourceWithRawResponse:
        """Lightning Payments endpoints"""
        from .resources.lightning_payments import AsyncLightningPaymentsResourceWithRawResponse

        return AsyncLightningPaymentsResourceWithRawResponse(self._client.lightning_payments)

    @cached_property
    def wallet(self) -> wallet.AsyncWalletResourceWithRawResponse:
        """Wallet endpoints"""
        from .resources.wallet import AsyncWalletResourceWithRawResponse

        return AsyncWalletResourceWithRawResponse(self._client.wallet)

    @cached_property
    def utils(self) -> utils.AsyncUtilsResourceWithRawResponse:
        """Utilities endpoints"""
        from .resources.utils import AsyncUtilsResourceWithRawResponse

        return AsyncUtilsResourceWithRawResponse(self._client.utils)

    @cached_property
    def oauth2(self) -> oauth2.AsyncOauth2ResourceWithRawResponse:
        """OAuth2 endpoints"""
        from .resources.oauth2 import AsyncOauth2ResourceWithRawResponse

        return AsyncOauth2ResourceWithRawResponse(self._client.oauth2)

    @cached_property
    def keysend_payments(self) -> keysend_payments.AsyncKeysendPaymentsResourceWithRawResponse:
        """Keysend Payments endpoints"""
        from .resources.keysend_payments import AsyncKeysendPaymentsResourceWithRawResponse

        return AsyncKeysendPaymentsResourceWithRawResponse(self._client.keysend_payments)

    @cached_property
    def email_payments(self) -> email_payments.AsyncEmailPaymentsResourceWithRawResponse:
        """Email endpoints"""
        from .resources.email_payments import AsyncEmailPaymentsResourceWithRawResponse

        return AsyncEmailPaymentsResourceWithRawResponse(self._client.email_payments)


class ZbdPaymentsWithStreamedResponse:
    _client: ZbdPayments

    def __init__(self, client: ZbdPayments) -> None:
        self._client = client

    @cached_property
    def gamertags(self) -> gamertags.GamertagsResourceWithStreamingResponse:
        """ZBD Gamertag endpoints"""
        from .resources.gamertags import GamertagsResourceWithStreamingResponse

        return GamertagsResourceWithStreamingResponse(self._client.gamertags)

    @cached_property
    def lightning_charges(self) -> lightning_charges.LightningChargesResourceWithStreamingResponse:
        """Lightning Charges endpoints"""
        from .resources.lightning_charges import LightningChargesResourceWithStreamingResponse

        return LightningChargesResourceWithStreamingResponse(self._client.lightning_charges)

    @cached_property
    def internal_transfer(self) -> internal_transfer.InternalTransferResourceWithStreamingResponse:
        """Internal Transfers endpoints"""
        from .resources.internal_transfer import InternalTransferResourceWithStreamingResponse

        return InternalTransferResourceWithStreamingResponse(self._client.internal_transfer)

    @cached_property
    def lightning_address(self) -> lightning_address.LightningAddressResourceWithStreamingResponse:
        """Lightning Address endpoints"""
        from .resources.lightning_address import LightningAddressResourceWithStreamingResponse

        return LightningAddressResourceWithStreamingResponse(self._client.lightning_address)

    @cached_property
    def lightning_static_charges(self) -> lightning_static_charges.LightningStaticChargesResourceWithStreamingResponse:
        """Lightning Charges endpoints"""
        from .resources.lightning_static_charges import LightningStaticChargesResourceWithStreamingResponse

        return LightningStaticChargesResourceWithStreamingResponse(self._client.lightning_static_charges)

    @cached_property
    def vouchers(self) -> vouchers.VouchersResourceWithStreamingResponse:
        """Vouchers endpoints"""
        from .resources.vouchers import VouchersResourceWithStreamingResponse

        return VouchersResourceWithStreamingResponse(self._client.vouchers)

    @cached_property
    def withdrawal_requests(self) -> withdrawal_requests.WithdrawalRequestsResourceWithStreamingResponse:
        """Withdrawal Requests endpoints"""
        from .resources.withdrawal_requests import WithdrawalRequestsResourceWithStreamingResponse

        return WithdrawalRequestsResourceWithStreamingResponse(self._client.withdrawal_requests)

    @cached_property
    def lightning_payments(self) -> lightning_payments.LightningPaymentsResourceWithStreamingResponse:
        """Lightning Payments endpoints"""
        from .resources.lightning_payments import LightningPaymentsResourceWithStreamingResponse

        return LightningPaymentsResourceWithStreamingResponse(self._client.lightning_payments)

    @cached_property
    def wallet(self) -> wallet.WalletResourceWithStreamingResponse:
        """Wallet endpoints"""
        from .resources.wallet import WalletResourceWithStreamingResponse

        return WalletResourceWithStreamingResponse(self._client.wallet)

    @cached_property
    def utils(self) -> utils.UtilsResourceWithStreamingResponse:
        """Utilities endpoints"""
        from .resources.utils import UtilsResourceWithStreamingResponse

        return UtilsResourceWithStreamingResponse(self._client.utils)

    @cached_property
    def oauth2(self) -> oauth2.Oauth2ResourceWithStreamingResponse:
        """OAuth2 endpoints"""
        from .resources.oauth2 import Oauth2ResourceWithStreamingResponse

        return Oauth2ResourceWithStreamingResponse(self._client.oauth2)

    @cached_property
    def keysend_payments(self) -> keysend_payments.KeysendPaymentsResourceWithStreamingResponse:
        """Keysend Payments endpoints"""
        from .resources.keysend_payments import KeysendPaymentsResourceWithStreamingResponse

        return KeysendPaymentsResourceWithStreamingResponse(self._client.keysend_payments)

    @cached_property
    def email_payments(self) -> email_payments.EmailPaymentsResourceWithStreamingResponse:
        """Email endpoints"""
        from .resources.email_payments import EmailPaymentsResourceWithStreamingResponse

        return EmailPaymentsResourceWithStreamingResponse(self._client.email_payments)


class AsyncZbdPaymentsWithStreamedResponse:
    _client: AsyncZbdPayments

    def __init__(self, client: AsyncZbdPayments) -> None:
        self._client = client

    @cached_property
    def gamertags(self) -> gamertags.AsyncGamertagsResourceWithStreamingResponse:
        """ZBD Gamertag endpoints"""
        from .resources.gamertags import AsyncGamertagsResourceWithStreamingResponse

        return AsyncGamertagsResourceWithStreamingResponse(self._client.gamertags)

    @cached_property
    def lightning_charges(self) -> lightning_charges.AsyncLightningChargesResourceWithStreamingResponse:
        """Lightning Charges endpoints"""
        from .resources.lightning_charges import AsyncLightningChargesResourceWithStreamingResponse

        return AsyncLightningChargesResourceWithStreamingResponse(self._client.lightning_charges)

    @cached_property
    def internal_transfer(self) -> internal_transfer.AsyncInternalTransferResourceWithStreamingResponse:
        """Internal Transfers endpoints"""
        from .resources.internal_transfer import AsyncInternalTransferResourceWithStreamingResponse

        return AsyncInternalTransferResourceWithStreamingResponse(self._client.internal_transfer)

    @cached_property
    def lightning_address(self) -> lightning_address.AsyncLightningAddressResourceWithStreamingResponse:
        """Lightning Address endpoints"""
        from .resources.lightning_address import AsyncLightningAddressResourceWithStreamingResponse

        return AsyncLightningAddressResourceWithStreamingResponse(self._client.lightning_address)

    @cached_property
    def lightning_static_charges(
        self,
    ) -> lightning_static_charges.AsyncLightningStaticChargesResourceWithStreamingResponse:
        """Lightning Charges endpoints"""
        from .resources.lightning_static_charges import AsyncLightningStaticChargesResourceWithStreamingResponse

        return AsyncLightningStaticChargesResourceWithStreamingResponse(self._client.lightning_static_charges)

    @cached_property
    def vouchers(self) -> vouchers.AsyncVouchersResourceWithStreamingResponse:
        """Vouchers endpoints"""
        from .resources.vouchers import AsyncVouchersResourceWithStreamingResponse

        return AsyncVouchersResourceWithStreamingResponse(self._client.vouchers)

    @cached_property
    def withdrawal_requests(self) -> withdrawal_requests.AsyncWithdrawalRequestsResourceWithStreamingResponse:
        """Withdrawal Requests endpoints"""
        from .resources.withdrawal_requests import AsyncWithdrawalRequestsResourceWithStreamingResponse

        return AsyncWithdrawalRequestsResourceWithStreamingResponse(self._client.withdrawal_requests)

    @cached_property
    def lightning_payments(self) -> lightning_payments.AsyncLightningPaymentsResourceWithStreamingResponse:
        """Lightning Payments endpoints"""
        from .resources.lightning_payments import AsyncLightningPaymentsResourceWithStreamingResponse

        return AsyncLightningPaymentsResourceWithStreamingResponse(self._client.lightning_payments)

    @cached_property
    def wallet(self) -> wallet.AsyncWalletResourceWithStreamingResponse:
        """Wallet endpoints"""
        from .resources.wallet import AsyncWalletResourceWithStreamingResponse

        return AsyncWalletResourceWithStreamingResponse(self._client.wallet)

    @cached_property
    def utils(self) -> utils.AsyncUtilsResourceWithStreamingResponse:
        """Utilities endpoints"""
        from .resources.utils import AsyncUtilsResourceWithStreamingResponse

        return AsyncUtilsResourceWithStreamingResponse(self._client.utils)

    @cached_property
    def oauth2(self) -> oauth2.AsyncOauth2ResourceWithStreamingResponse:
        """OAuth2 endpoints"""
        from .resources.oauth2 import AsyncOauth2ResourceWithStreamingResponse

        return AsyncOauth2ResourceWithStreamingResponse(self._client.oauth2)

    @cached_property
    def keysend_payments(self) -> keysend_payments.AsyncKeysendPaymentsResourceWithStreamingResponse:
        """Keysend Payments endpoints"""
        from .resources.keysend_payments import AsyncKeysendPaymentsResourceWithStreamingResponse

        return AsyncKeysendPaymentsResourceWithStreamingResponse(self._client.keysend_payments)

    @cached_property
    def email_payments(self) -> email_payments.AsyncEmailPaymentsResourceWithStreamingResponse:
        """Email endpoints"""
        from .resources.email_payments import AsyncEmailPaymentsResourceWithStreamingResponse

        return AsyncEmailPaymentsResourceWithStreamingResponse(self._client.email_payments)


Client = ZbdPayments

AsyncClient = AsyncZbdPayments
