from pathlib import Path
from typing import Dict

class Process:
    """
    Handles folder creation and file movement operations.
    """

    def __init__(self, base_folder: Path):
        """
        Initializes the processing engine.

        Args:
            base_folder (Path):
                Root folder being organized.
        """
        self.base_folder = base_folder

    def create_folder(self, destination: Path) -> None:
        """
        Creates a folder if it does not exist.

        Args:
            destination (Path): Folder path to create.

        Returns:
            None
        """
        destination.mkdir(parents=True, exist_ok=True)

    def move_file(self, file_path: Path, destination: Path) -> None:
        """
        Moves a file into a destination folder.

        Args:
            file_path (Path): File to move.
            destination (Path): Destination folder.

        Returns:
            True: success
            False: Permission eror
        """
        try:
            target_path = destination / file_path.name
            file_path.rename(target_path)
        except PermissionError:
            return False

    def process_file(
        self,
        file_path: Path,
        category: str,
        destination: Path
    ) -> None:
        """
        Processes a file by ensuring the destination folder exists
        and moving the file into it.

        DFS-OA Execution:
        - Validates destination folder
        - Creates folder if missing
        - Performs safe move operation

        Args:
            file_path (Path): Full path of file.
            category (str): File category.
            destination (Path): Destination folder path.

        Returns:
            None
        """
        
        # Create folder if it does not exist
        if not destination.exists():
            self.create_folder(destination)

        # Move file
        self.move_file(file_path, destination)