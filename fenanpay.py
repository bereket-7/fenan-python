import requests

from core import fenanpay_checkout, fenanpay_direct_pay


class Fenanpay:
    DEFAULT_HOST = 'https://api.fenanpay.com/api'
    API_VERSION = '/v1'
    PACKAGE_VERSION = '1.0.0'
    DEFAULT_TIMEOUT = 120

    def __init__(self, apikey):
        self.apikey = apikey
        self.headers = {
            'apiKey': self.apikey,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.checkout = fenanpay_checkout.FenanpayCheckout(self)
        self.direct_pay = fenanpay_direct_pay.FenanpayDirectPay(self)

    def _make_request(self, method, endpoint, data=None):
        url = f"{self.DEFAULT_HOST}{self.API_VERSION}{endpoint}"
        response = requests.request(
            method, url, headers=self.headers, json=data, timeout=self.DEFAULT_TIMEOUT
        )
        response.raise_for_status()
        return response.json()
