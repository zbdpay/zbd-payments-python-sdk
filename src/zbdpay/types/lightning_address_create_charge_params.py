# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LightningAddressCreateChargeParams"]


class LightningAddressCreateChargeParams(TypedDict, total=False):
    amount: str
    """The amount for the Charge -> in millisatoshis"""

    description: str
    """Note or comment of this Charge"""

    lnaddress: str
    """The Lightning Address of the intended recipient"""
