import json
from typing import Optional


class CustomerInfo:
    def __init__(self, email: Optional[str], phone: Optional[str], name: str):
        self.email = email
        self.phone = phone
        self.name = name

    def to_dict(self):
        return {
            'email': self.email,
            'phone': self.phone,
            'name': self.name,
        }

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return CustomerInfo(
            email=data.get('email'),
            phone=data.get('phone'),
            name=data['name']
        )

    def to_json(self):
        return json.dumps(self.to_dict())
