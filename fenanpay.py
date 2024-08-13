import requests
from .core.fenanpay_checkout import FenanpayCheckout
from .core.fenanpay_direct_pay import FenanpayDirectPay


class ArifPay:
    DEFAULT_HOST = 'https://api.fenanpay.com/api'
    API_VERSION = '/v1'
    PACKAGE_VERSION = '1.0.0'
    DEFAULT_TIMEOUT = 1000 * 60 * 2

    def __init__(self, apikey: str):
        self.apikey = apikey
        self.http_client = requests.Session()
        self.http_client.headers.update({
            'apiKey': apikey,
            "Content-Type": "application/json",
            "Accepts": "application/json",
        })
        self.http_client.base_url = self.DEFAULT_HOST

        self.checkout = FenanpayCheckout(self.http_client)
        self.direct_pay = FenanpayDirectPay(self.http_client)
