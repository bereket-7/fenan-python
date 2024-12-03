import json
from typing import List, Optional, Dict, Any

from schemas.currency import Currency
from schemas.customer_info import CustomerInfo
from schemas.payment_item import PaymentItem
from schemas.payment_method_type import PaymentMethodType
from schemas.split_payment import SplitPayment


class FenanpayCheckoutRequest:
    def __init__(self,
                 amount: float,
                 items: List[PaymentItem],
                 currency: Currency,
                 payment_intent_unique_id: str,
                 payment_type: PaymentMethodType,
                 payment_link_unique_id: Optional[str] = None,
                 split_payment: Optional[SplitPayment] = None,
                 return_url: str = "",
                 expire_in: int = 0,
                 callback_url: Optional[str] = None,
                 commission_paid_by_customer: bool = False,
                 customer_info: Optional[CustomerInfo] = None):
        self.amount = amount
        self.items = items
        self.currency = currency
        self.payment_intent_unique_id = payment_intent_unique_id
        self.payment_type = payment_type
        self.payment_link_unique_id = payment_link_unique_id
        self.split_payment = split_payment
        self.return_url = return_url
        self.expire_in = expire_in
        self.callback_url = callback_url
        self.commission_paid_by_customer = commission_paid_by_customer
        self.customer_info = customer_info

    def to_dict(self) -> Dict[str, Any]:
        return {
            "amount": self.amount,
            "items": [item.to_dict() for item in self.items],
            "currency": self.currency.value,
            "paymentIntentUniqueId": self.payment_intent_unique_id,
            "paymentType": self.payment_type.value,
            "paymentLinkUniqueId": self.payment_link_unique_id,
            "splitPayment": self.split_payment.to_dict() if self.split_payment else None,
            "returnUrl": self.return_url,
            "expireIn": self.expire_in,
            "callbackUrl": self.callback_url,
            "commissionPaidByCustomer": self.commission_paid_by_customer,
            "customerInfo": self.customer_info.to_dict() if self.customer_info else None,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'FenanpayCheckoutRequest':
        return FenanpayCheckoutRequest(
            amount=data.get("amount", 0.0),
            items=[PaymentItem.from_dict(item)
                   for item in data.get("items", [])],
            currency=Currency(data.get("currency", "")),
            payment_intent_unique_id=data.get("paymentIntentUniqueId", ""),
            payment_type=PaymentMethodType(data.get("paymentType", "")),
            payment_link_unique_id=data.get("paymentLinkUniqueId"),
            split_payment=SplitPayment.from_dict(
                data.get("splitPayment")) if data.get("splitPayment") else None,
            return_url=data.get("returnUrl", ""),
            expire_in=data.get("expireIn", 0),
            callback_url=data.get("callbackUrl"),
            commission_paid_by_customer=data.get(
                "commissionPaidByCustomer", False),
            customer_info=CustomerInfo.from_dict(
                data.get("customerInfo")) if data.get("customerInfo") else None,
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'FenanpayCheckoutRequest':
        data = json.loads(json_str)
        return FenanpayCheckoutRequest.from_dict(data)
