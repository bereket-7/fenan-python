from fenanpay import ArifPay
from helper.fenanpay_support import FenanpaySupport
from schemas.fenanpay_api_response import FenanpayAPIResponse
from schemas.fenanpay_transfer_response import FenanpayTransferResponse
from exception.fenanpay_network_exception import FenanpayNetworkException
from schemas.payment_intent import PaymentIntent
from requests.exceptions import HTTPError
import requests


class DirectPay:
    def __init__(self, http_client, payment_method):
        self.http_client = http_client
        self.payment_method = payment_method

    def pay(self, payment_intent: PaymentIntent) -> FenanpayTransferResponse:
        try:
            response = self.http_client.post(
                f"{ArifPay.API_VERSION}/payment/{self.payment_method}/direct",
                json=payment_intent.json()
            )

            arif_api_response = FenanpayAPIResponse.from_json(response.json())
            return FenanpayTransferResponse.from_json(arif_api_response.data)
        except requests.ConnectionError:
            raise FenanpayNetworkException()
        except HTTPError as e:
            FenanpaySupport.handle_exception(e)
            raise
