import json
from typing import Optional, Dict, Any


class PaymentItem:
    def __init__(
        self,
        name: str,
        description: Optional[str],
        image: Optional[str],
        quantity: int,
        price: float
    ):
        self.name = name
        self.description = description
        self.image = image
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'quantity': self.quantity,
            'price': self.price
        }

    @staticmethod
    def from_json(json_str: str) -> 'PaymentItem':
        data = json.loads(json_str)
        return PaymentItem(
            name=data['name'],
            description=data.get('description'),
            image=data.get('image'),
            quantity=data['quantity'],
            price=data['price']
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
