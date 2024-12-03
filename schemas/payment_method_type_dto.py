from typing import Optional
from schemas.payment_method_type import PaymentMethodType
from schemas.currency import Currency


class PaymentMethodTypeDto:
    def __init__(self,
                 payment_type_id: Optional[int] = None,
                 name: str = "",
                 description: str = "",
                 type: str = "",
                 options: Optional[str] = None,
                 enabled: bool = False,
                 currency: Optional[Currency] = None,
                 code: Optional[PaymentMethodType] = None):
        self.payment_type_id = payment_type_id
        self.name = name
        self.description = description
        self.type = type
        self.options = options
        self.enabled = enabled
        self.currency = currency
        self.code = code
