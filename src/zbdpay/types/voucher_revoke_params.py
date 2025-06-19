# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VoucherRevokeParams"]


class VoucherRevokeParams(TypedDict, total=False):
    code: str
    """Valid 8-digit ZBD Voucher Code"""
