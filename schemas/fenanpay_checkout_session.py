import json

from schemas import fenanpay_transaction


class FenanpayCheckoutSession:
    def __init__(self, id, transaction, total_amount, test, uuid, created_at, updated_at):
        self.id = id
        self.transaction = transaction
        self.total_amount = total_amount
        self.test = test
        self.uuid = uuid
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "transaction": self.transaction.to_dict() if self.transaction else None,
            "total_amount": self.total_amount,
            "test": self.test,
            "uuid": self.uuid,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @staticmethod
    def from_json(json_data: dict):
        transaction = fenanpay_transaction.from_json(
            json_data["transaction"]) if json_data.get("transaction") else None
        return FenanpayCheckoutSession(
            id=json_data["id"],
            transaction=transaction,
            total_amount=json_data["totalAmount"],
            test=json_data["test"],
            uuid=json_data["uuid"],
            created_at=json_data["createdAt"],
            updated_at=json_data["updatedAt"]
        )

    def to_json(self):
        return json.dumps(self.to_dict())
