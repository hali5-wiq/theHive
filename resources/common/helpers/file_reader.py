class FileReader:

    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return ""
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return ""