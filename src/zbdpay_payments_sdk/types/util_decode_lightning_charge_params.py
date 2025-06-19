# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UtilDecodeLightningChargeParams"]


class UtilDecodeLightningChargeParams(TypedDict, total=False):
    invoice: str
    """The Charge or Invoice QR code contents"""
