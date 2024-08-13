import requests
from fenanpay import ArifPay
from helper.fenanpay_support import FenanpaySupport
from schemas.fenanpay_api_response import FenanpayAPIResponse
from schemas.fenanpay_checkout_request import FenanpayCheckoutRequest
from schemas.fenanpay_checkout_response import FenanpayCheckoutResponse
from schemas.fenanpay_checkout_session import FenanpayCheckoutSession
from schemas.fenanpay_options import FenanpayOptions
from exception.fenanpay_network_exception import FenanpayNetworkException


class FenanpayCheckout:
    def __init__(self, http_client: requests.Session):
        self.http_client = http_client

    def create(self, fenanpay_checkout_request: FenanpayCheckoutRequest, option: FenanpayOptions = None) -> FenanpayCheckoutResponse:
        if option is None:
            option = FenanpayOptions(sandbox=False)

        try:
            base_path = '/sandbox' if option.sandbox else ''
            response = self.http_client.post(
                f"{ArifPay.API_VERSION}{base_path}/payment/intent",
                json=fenanpay_checkout_request.to_dict()
            )

            arif_api_response = FenanpayAPIResponse.from_dict(response.json())
            return FenanpayCheckoutResponse.from_dict(arif_api_response.content)
        except requests.exceptions.ConnectionError:
            raise FenanpayNetworkException()
        except requests.exceptions.HTTPError as e:
            FenanpaySupport.handle_exception(e)
            raise e

    def fetch(self, session_id: str, option: FenanpayOptions = None) -> FenanpayCheckoutSession:
        if option is None:
            option = FenanpayOptions(sandbox=False)

        try:
            base_path = '/sandbox' if option.sandbox else ''
            response = self.http_client.get(
                f"{ArifPay.API_VERSION}{base_path}/payment/checkout/{session_id}"
            )

            arif_api_response = FenanpayAPIResponse.from_dict(response.json())
            return FenanpayCheckoutSession.from_dict(arif_api_response.content)
        except requests.exceptions.ConnectionError:
            raise FenanpayNetworkException()
        except requests.exceptions.HTTPError as e:
            FenanpaySupport.handle_exception(e)
            raise e

    def cancel(self, session_id: str, option: FenanpayOptions = None) -> FenanpayCheckoutSession:
        if option is None:
            option = FenanpayOptions(sandbox=False)

        try:
            base_path = '/sandbox' if option.sandbox else ''
            response = self.http_client.post(
                f"{ArifPay.API_VERSION}{
                    base_path}/payment/intent/cancel/{session_id}"
            )

            arif_api_response = FenanpayAPIResponse.from_dict(response.json())
            return FenanpayCheckoutSession.from_dict(arif_api_response.content)
        except requests.exceptions.ConnectionError:
            raise FenanpayNetworkException()
        except requests.exceptions.HTTPError as e:
            FenanpaySupport.handle_exception(e)
            raise e
