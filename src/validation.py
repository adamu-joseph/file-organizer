from pathlib import Path
from typing import Tuple, List, Union

class FileManager:
    """
    A utility class for handling file system operations such as validation,
    path normalization, directory checks, file retrieval, and file utilities.
    """

    def __init__(self, folder: str):
        self.folder = folder
        self.path = None
        self.base_folder = None

    # 1. Validation Layer
    def validate_target_folder(self) -> Tuple[bool, Union[str, None]]:
        """
        Validates that the target folder is a non-empty string.

        Returns:
            Tuple[bool, Optional[str]]:
                (True, None) if valid
                (False, error message) if invalid
        """
        if not isinstance(self.folder, str) or not self.folder.strip():
            return False, "TARGET_FOLDER must be a non-empty string."

        return True, None

    # 2-3. Path Normalization Layer
    def normalize_path(self) -> Union[Path, None]:
        """
        Converts folder path into an absolute Path object and validates it.
    
        Returns:
            Path: If valid directory
            None: If path is invalid or not a directory
        """
        path = Path(self.folder).expanduser().resolve()
    
        if not path.exists() or not path.is_dir():
            return None
    
        self.path = path
        self.base_folder = path.parent
        return self.path

    # 4. File Retrieval Layer
    def get_all_files(self) -> List[str]:
        """
        Retrieves all files in the directory (excluding folders).

        Returns:
            List[str]: List of file names
            None: if folder does not contain files
        """
        if self.path is None:
            self.normalize_path()

        files = [item.name for item in self.path.iterdir() if item.is_file()]
        if not files:
            return None
        
        return files

    # 5. File Extension Utility
    @staticmethod
    def get_extension(file_name: str) -> str:
        """
        Extracts file extension in lowercase format.

        Args:
            file_name (str): File name

        Returns:
            str: File extension (e.g. '.pdf')
        """
        return Path(file_name).suffix.lower()