# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LightningAddressSendPaymentParams"]


class LightningAddressSendPaymentParams(TypedDict, total=False):
    amount: str
    """The amount for the Payment -> in millisatoshis"""

    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """The endpoint ZBD will POST Charge updates to"""

    comment: str
    """Note or description of this Payment"""

    internal_id: Annotated[str, PropertyInfo(alias="internalId")]
    """Open metadata string property"""

    ln_address: Annotated[str, PropertyInfo(alias="lnAddress")]
    """The Lightning Address of the intended recipient (e.g. andre@zbd.gg)"""
