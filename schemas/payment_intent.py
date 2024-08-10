import json
from typing import List, Dict, Any, Optional


class PaymentIntent:
    def __init__(
        self,
        amount: float,
        items: List[Dict[str, Any]],
        currency: str,
        payment_intent_unique_id: str,
        payment_link_unique_id: str,
        method_type: List[str],
        split_payment: List[Dict[str, Any]],
        return_url: str,
        expire_in: int,
        callback_url: str,
        commission_paid_by_customer: bool,
        customer_info: Optional[dict]
    ):
        self.amount = amount
        self.items = items
        self.currency = currency
        self.payment_intent_unique_id = payment_intent_unique_id
        self.payment_link_unique_id = payment_link_unique_id
        self.method_type = method_type
        self.split_payment = split_payment
        self.return_url = return_url
        self.expire_in = expire_in
        self.callback_url = callback_url
        self.commission_paid_by_customer = commission_paid_by_customer
        self.customer_info = customer_info

    def to_dict(self):
        return {
            'amount': self.amount,
            'items': self.items,
            'currency': self.currency,
            'paymentIntentUniqueId': self.payment_intent_unique_id,
            'paymentLinkUniqueId': self.payment_link_unique_id,
            'methodType': self.method_type,
            'splitPayment': self.split_payment,
            'returnUrl': self.return_url,
            'expireIn': self.expire_in,
            'callbackUrl': self.callback_url,
            'commissionPaidByCustomer': self.commission_paid_by_customer,
            'customerInfo': self.customer_info,
        }

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return PaymentIntent(
            amount=data['amount'],
            items=data['items'],
            currency=data['currency'],
            payment_intent_unique_id=data['paymentIntentUniqueId'],
            payment_link_unique_id=data['paymentLinkUniqueId'],
            method_type=data['methodType'],
            split_payment=data['splitPayment'],
            return_url=data['returnUrl'],
            expire_in=data['expireIn'],
            callback_url=data['callbackUrl'],
            commission_paid_by_customer=data['commissionPaidByCustomer'],
            customer_info=data.get('customerInfo')
        )

    def to_json(self):
        return json.dumps(self.to_dict())
