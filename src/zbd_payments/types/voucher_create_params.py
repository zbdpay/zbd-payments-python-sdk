# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VoucherCreateParams"]


class VoucherCreateParams(TypedDict, total=False):
    amount: str
    """The amount for the Charge -> in millisatoshis"""

    description: str
    """Note or comment for this Charge (visible to payer)"""
