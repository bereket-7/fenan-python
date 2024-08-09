from datetime import datetime
import json
import requests
from exception import (
    fenanpay_bad_request_exception,
    fenanpay_network_exception,
    fenanpay_not_found_exception,
    fenanpay_unauthorized_exception,
    fenanpay_exception
)


class FenanpaySupport:

    @staticmethod
    def get_expire_date_from_date(date: datetime) -> str:
        # Assuming date is a datetime object
        return date.strftime('%Y-%m-%dT%H:%M:%S')

    @staticmethod
    def handle_exception(e: requests.RequestException):
        if isinstance(e, requests.HTTPError):
            response = e.response
            if response:
                if response.status_code == 401:
                    raise fenanpay_unauthorized_exception(
                        'Invalid authentication credentials') from e
                elif response.status_code == 400:
                    try:
                        response_json = response.json()
                        msg = response_json.get(
                            "msg", "Invalid Request, check your Request body.")
                    except json.JSONDecodeError:
                        msg = "Invalid Request, check your Request body."
                    raise fenanpay_bad_request_exception(msg) from e
                elif response.status_code == 404:
                    try:
                        response_json = response.json()
                        msg = response_json.get(
                            "msg", "Invalid Request, Not found.")
                    except json.JSONDecodeError:
                        msg = "Invalid Request, Not found."
                    raise fenanpay_not_found_exception(msg) from e
                else:
                    msg = response.json().get("msg", "An error occurred.")
                    raise fenanpay_exception(msg) from e
        else:
            raise fenanpay_network_exception("Network error occurred") from e
