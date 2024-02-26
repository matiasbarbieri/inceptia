# LOG FOLDER CREATE EXCEPTIONS

class LogFolderCreateError(Exception):
    def __init__(self, folder_path, error):
        self.message = f'ERROR -> Failed to create {folder_path} folder: {str(error)}'
        super().__init__(self.message)
