from requests import get
from entities import Entities


class ConversionAPI:

    def get_conversion_rate(self, source_currency, dest_currency):

        response = get(f'{Entities.API_SERVER_BASE_URL}{source_currency}/{dest_currency}').json()
        if response[Entities.RESULT_FIELD] == Entities.ERROR_CODE:
            return -1
        return response[Entities.CONVERSION_RATE]
