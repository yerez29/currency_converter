from entities import Entities


class InputFileHandler:

    def __init__(self):
        self.source_currency = ""
        self.dest_currency = ""
        self.amounts = []

    def parse_input_file(self, input_file_name):
        try:
            with open(input_file_name) as file:
                lines = [line.rstrip() for line in file]
                self.source_currency = lines[0]
                self.dest_currency = lines[1]
                self.amounts = lines[2:]
            file.close()
        except FileNotFoundError or FileExistsError:
            raise FileExistsError(Entities.FILE_NOT_EXISTS)

    def get_input_file_data(self):
        return self.source_currency, self.dest_currency, self.amounts
