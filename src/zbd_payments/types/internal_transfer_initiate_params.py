# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InternalTransferInitiateParams"]


class InternalTransferInitiateParams(TypedDict, total=False):
    amount: str
    """The amount to be transferred -> in millisatoshis"""

    receiver_wallet_id: Annotated[str, PropertyInfo(alias="receiverWalletId")]
    """The Wallet ID of the recipient Project"""
