import json
from typing import Optional


class FenanpayTransaction:
    def __init__(self, id, transaction_id, payment_type, transaction_status, created_at, updated_at):
        self.id = id
        self.transaction_id = transaction_id
        self.payment_type = payment_type
        self.transaction_status = transaction_status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "transactionId": self.transaction_id,
            "paymentType": self.payment_type,
            "transactionStatus": self.transaction_status,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }

    @staticmethod
    def from_json(data: dict):
        return FenanpayTransaction(
            id=data["id"],
            transaction_id=data["transactionId"],
            payment_type=data["paymentType"],
            transaction_status=data["transactionStatus"],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"]
        )

    def to_json(self):
        return json.dumps(self.to_dict())
