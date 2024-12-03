from typing import Optional
from schemas.split_type import SplitType


class CheckoutSplitPaymentDto:
    def __init__(self, split_id: int, account_number: str, amount: float, split_type: Optional[SplitType] = None):
        self.split_id = split_id
        self.account_number = account_number
        self.amount = amount
        self.split_type = split_type
