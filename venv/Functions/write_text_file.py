import os


class WriteTextFile:
    def __init__(self):
        self.file = None

    def open_text_file(self, path, file_name, mode):
        complete_name = os.path.join(path, file_name)
        self.file = open(complete_name, mode)

    def close_text_file(self):
        self.file.close()

    def write_text_file(self, message):
        self.file.write(str(message))
        self.file.write('\n')

    def handle_write_file(self, path, file_name, mode, message):
        self.open_text_file(path, file_name, mode)
        self.write_text_file(message)
        self.close_text_file()
