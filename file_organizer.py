from pathlib import Path
import os

base_path = Path(os.path.dirname(__file__))
target_path = base_path / "sorted"


FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
}


def create_category_directories():

    for category, _ in FILE_CATEGORIES.items():

        (target_path / category).mkdir(parents=True, exist_ok=True)


def search_directories():
    for files in base_path.glob("*"):
        for cat, extension in FILE_CATEGORIES.items():
            if files.suffix in extension:
                Path.copy_into(files, target_path / cat)


create_category_directories()
search_directories()
