from pathlib import Path
from typing import Dict, Tuple

class FileCategorizer:
    """
    Handles file classification and destination path generation
    based on file extensions and category mappings.
    """

    def __init__(self, categories: Dict[str, Tuple[str, ...]]):
        """
        Initializes the FileCategorizer.

        Args:
            categories (Dict[str, Tuple[str, ...]]):
                Mapping of category names to tuples of file extensions.
                Example:
                {
                    "Images": (".jpg", ".png"),
                    "Documents": (".pdf", ".docx")
                }
        """
        self.categories = categories

    def classify_file(self, extension: str) -> str:
        """
        Determines the category of a file based on its extension.

        Args:
            extension (str): File extension (e.g., ".jpg").

        Returns:
            str: Category name or 'Others' if no match is found.
        """
        for category, extensions in self.categories.items():
            if extension in extensions:
                return category
        return "Others"

    def build_destination_folder(self, base: Path, category: str) -> Path:
        """
        Builds a destination folder path for a given category.

        Args:
            base (Path): Base directory path.
            category (str): File category name.

        Returns:
            str: Full path to the destination folder.
        """
        return base / category 