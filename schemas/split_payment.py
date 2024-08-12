import json
from typing import Any, Dict


class SplitPayment:
    def __init__(self, amount: float, bank: str, split_type: str, credit_account: str):
        self.amount = amount
        self.bank = bank
        self.split_type = split_type
        self.credit_account = credit_account

    def to_dict(self) -> Dict[str, Any]:
        return {
            "amount": self.amount,
            "bank": self.bank,
            "splitType": self.split_type,
            "creditAccount": self.credit_account
        }

    @staticmethod
    def from_json(json_data: str) -> 'SplitPayment':
        data = json.loads(json_data)
        return SplitPayment(
            amount=data["amount"],
            bank=data["bank"],
            split_type=data["splitType"],
            credit_account=data["creditAccount"]
        )
