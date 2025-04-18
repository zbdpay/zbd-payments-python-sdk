# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LightningPaymentSendParams"]


class LightningPaymentSendParams(TypedDict, total=False):
    amount: str
    """
    Amount to be paid to this Charge/Invoice -> in millisatoshis _(only valid if
    Amountless Invoice)_
    """

    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """The endpoint ZBD will POST Payment updates to"""

    description: str
    """Note or comment for this Payment"""

    internal_id: Annotated[str, PropertyInfo(alias="internalId")]
    """Open metadata string property"""

    invoice: str
    """Lightning Network Payment Request / Charge"""
