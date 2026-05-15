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
    """create folders_
    """

    for category, _ in FILE_CATEGORIES.items():

        (target_path / category).mkdir(parents=True, exist_ok=True)


def copy_to_directories():
    """copy to folders
    """
    create_category_directories()
    for files in base_path.glob("*"):
        for cat, extension in FILE_CATEGORIES.items():
            if files.suffix in extension:
                Path.copy_into(files, target_path / cat)
                print(f"🔵 {files.name} 🔵 copy to {cat} ")


def move_to_directories():
    """move to folders
    """
    create_category_directories()
    for files in base_path.glob("*"):
        for cat, extension in FILE_CATEGORIES.items():
            if files.suffix in extension:
                Path.move_into(files, target_path / cat)
                print(f"🟡 {files.name} 🟡 Moved to {cat} ")


def dry_mode():
    """dry mode 
    """
    for files in base_path.glob("*"):
        for cat, extension in FILE_CATEGORIES.items():
            if files.suffix in extension:
                print(f"🟢 {files.name} 🟢 will be copy / move to {cat} ")


print("*" * 20, "\n")
print("📁 File Organizer \n")
print("*" * 20, "\n")

print("1.🟡 Move File To Folders \n ")
print("2.🔵 Copy Files To Folders \n")
print("3.🟢 Dry Mode \n")
print("4.🔴 Exit \n")

user_choice = input("❓: ")

if user_choice == "1":
    move_to_directories()

elif user_choice == "2":
    copy_to_directories()

elif user_choice == "3":
    dry_mode()

elif user_choice == "4":
    exit()
