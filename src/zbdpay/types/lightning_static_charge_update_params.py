# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LightningStaticChargeUpdateParams"]


class LightningStaticChargeUpdateParams(TypedDict, total=False):
    allowed_slots: Annotated[float, PropertyInfo(alias="allowedSlots")]
    """Number of payments this Static Charge can accept"""

    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """The endpoint ZBD will POST Charge updates to"""

    description: str
    """Note or comment for this Static Charge (visible to payer)"""

    internal_id: Annotated[str, PropertyInfo(alias="internalId")]
    """Open metadata string property"""

    max_amount: Annotated[str, PropertyInfo(alias="maxAmount")]
    """Maximum allowed amount for the Static Charge -> in millisatoshis"""

    min_amount: Annotated[str, PropertyInfo(alias="minAmount")]
    """Minimum allowed amount for the Static Charge -> in millisatoshis"""

    success_message: Annotated[str, PropertyInfo(alias="successMessage")]
    """Message displayed to the payer AFTER payment settles"""
