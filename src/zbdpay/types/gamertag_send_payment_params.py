# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GamertagSendPaymentParams"]


class GamertagSendPaymentParams(TypedDict, total=False):
    amount: str
    """The amount for the Payment -> in millisatoshis"""

    description: str
    """Note or comment for this Payment (visible to recipient)"""

    gamertag: str
    """Destination ZBD Gamertag"""
