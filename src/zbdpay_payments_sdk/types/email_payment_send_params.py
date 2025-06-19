# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmailPaymentSendParams"]


class EmailPaymentSendParams(TypedDict, total=False):
    amount: str
    """The amount for the Payment -> in millisatoshis"""

    comment: str
    """Note / description of this Payment (may be shown to recipient)"""

    email: str
    """The Email of the intended recipient (e.g. info@zebedee.io)"""
