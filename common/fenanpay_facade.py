from common.fenanpay import Fenanpay


class FenanpayFacade:
    _service = None

    @classmethod
    def _get_service(cls):
        if cls._service is None:
            cls._service = Fenanpay()
        return cls._service

    @classmethod
    def perform_action(cls):
        return cls._get_service().perform_action()
