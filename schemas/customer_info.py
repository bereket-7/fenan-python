import json
from typing import Optional, Dict, Any


class CustomerInfo:
    def __init__(self, email: Optional[str] = None, phone: Optional[str] = None, name: str = ""):
        self.email = email
        self.phone = phone
        self.name = name

    def to_dict(self) -> Dict[str, Any]:
        return {
            'email': self.email,
            'phone': self.phone,
            'name': self.name,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'CustomerInfo':
        return CustomerInfo(
            email=data.get('email'),
            phone=data.get('phone'),
            name=data['name']
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_str: str) -> 'CustomerInfo':
        data = json.loads(json_str)
        return CustomerInfo.from_dict(data)
