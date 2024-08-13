import json
from urllib.parse import unquote
from schemas import fenanpay_transaction


class FenanpayTransferResponse:
    def __init__(self, session_id, url, otp, transaction):
        self.session_id = session_id
        self.url = url
        self.otp = otp
        self.transaction = transaction

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "url": self.url,
            "otp": self.otp,
            "transaction": self.transaction.to_dict() if self.transaction else None,
        }

    @staticmethod
    def from_json(data: dict):
        return FenanpayTransferResponse(
            session_id=data.get("sessionId"),
            url=unquote(data.get("url", "")),
            otp=unquote(data.get("otp", "")),
            transaction=fenanpay_transaction.from_json(
                data["transaction"]) if data.get("transaction") else None
        )

    def to_json(self):
        return json.dumps(self.to_dict())
