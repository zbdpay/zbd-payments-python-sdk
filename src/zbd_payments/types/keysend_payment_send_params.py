# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["KeysendPaymentSendParams"]


class KeysendPaymentSendParams(TypedDict, total=False):
    amount: str
    """The amount for the Payment -> in millisatoshis"""

    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """The endpoint ZBD will POST Keysend Payment updates to"""

    metadata: object
    """Open metadata object property"""

    pubkey: str
    """The Public Key for the destination Lightning node"""

    tlv_records: Annotated[List[str], PropertyInfo(alias="tlvRecords")]
    """
    List of TLV records <Expandable title="tlvRecord" defaultOpen>
    <ParamField body="type" type="number" initialValue={123456}> type of the TLV
    record
    """

    value: str
    """value of the TLV record (hex encoded string)"""
