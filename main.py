from files_handler import InputFileHandler
from entities import Entities
from convertion_API import ConversionAPI
import sys


class ParseFileAndShowResults:

    def preprocess_input_data(self, file_handler):

        try:
            file_handler.parse_input_file(Entities.INPUT_FILE_NAME)
        except FileExistsError:
            print(Entities.FILE_NOT_EXISTS)
            sys.exit(-1)
        return file_handler.get_input_file_data()

    def calculate_and_print_results(self, conversion_api, source_curr, dest_curr, amnts):

        conversion_rate = conversion_api.get_conversion_rate(source_curr, dest_curr)
        if conversion_rate == -1:
            print(Entities.API_ERROR_MESSAGE)
            sys.exit(-1)
        try:
            results = [float(amount) * conversion_rate for amount in amnts]
            print(*results, sep='\n')
        except ValueError:
            print(Entities.CONVERSION_ERROR_MESSAGE)
            sys.exit(-1)


if __name__ == '__main__':

    input_file_handler = InputFileHandler()
    results_manager = ParseFileAndShowResults()
    source_currency, dest_currency, amounts = results_manager.preprocess_input_data(input_file_handler)
    api = ConversionAPI()
    results_manager.calculate_and_print_results(api, source_currency, dest_currency, amounts)


