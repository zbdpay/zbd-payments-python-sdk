# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WithdrawalRequestCreateParams"]


class WithdrawalRequestCreateParams(TypedDict, total=False):
    amount: str
    """The amount for the Withdrawal Request -> in millisatoshis"""

    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """The endpoint ZBD will POST Charge updates to"""

    description: str
    """Note or comment for this Withdrawal Request"""

    expires_in: Annotated[float, PropertyInfo(alias="expiresIn")]
    """Time until Withdrawal Request expiration -> in seconds"""

    internal_id: Annotated[str, PropertyInfo(alias="internalId")]
    """Open metadata string property"""
