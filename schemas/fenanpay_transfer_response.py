import json
from typing import Optional

from fenanpay_transaction import FenanpayTransaction


class FenanpayTransferResponse:
    def __init__(self,
                 session_id: str,
                 url: Optional[str] = None,
                 otp: Optional[str] = None,
                 transaction: Optional[FenanpayTransaction] = None):
        self.session_id = session_id
        self.url = url
        self.otp = otp
        self.transaction = transaction

    def to_dict(self) -> dict:
        return {
            "sessionId": self.session_id,
            "url": self.url,
            "otp": self.otp,
            "transaction": self.transaction.to_dict() if self.transaction else None,
        }

    @staticmethod
    def from_dict(data: dict) -> 'FenanpayTransferResponse':
        transaction = FenanpayTransaction.from_dict(
            data["transaction"]) if "transaction" in data else None
        return FenanpayTransferResponse(
            session_id=data.get("sessionId", ""),
            url=data.get("url", ""),
            otp=data.get("otp", ""),
            transaction=transaction
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'FenanpayTransferResponse':
        data = json.loads(json_str)
        return FenanpayTransferResponse.from_dict(data)
