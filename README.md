# 📁 File Organizer

> **Automatically sort your messy files into clean, categorized folders — in seconds.**

🌐 **Languages:** [English](README.md) · [فارسی](README.fa.md)

---

## ✨ What Is This?

**File Organizer** is a lightweight Python tool that sorts files into categorized subfolders automatically. Choose between:

- **CLI Mode** (`file_organizer.py`) — Terminal-based interface with simple menu
- **GUI Mode** (`file_organizer_gui.py`) — Modern graphical interface with visual controls

---

## 📂 Supported Categories

| Category | Extensions |
|---|---|
| 🖼️ Images | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.tiff` `.svg` `.webp` |
| 📄 Documents | `.pdf` `.doc` `.docx` `.txt` `.xls` `.xlsx` `.ppt` `.pptx` |
| 🎬 Videos | `.mp4` `.mkv` `.avi` `.mov` `.wmv` |
| 🎵 Audio | `.mp3` `.wav` `.aac` `.flac` `.ogg` |
| 🗜️ Archives | `.zip` `.rar` `.tar` `.gz` `.7z` |

**Custom categories can be added in GUI mode!**

---

## 🚀 Getting Started

### Prerequisites

- Python **3.6+**
- For GUI mode: `python3-tk` (usually pre-installed)

### Installation

```bash
git clone https://github.com/yourname/file-organizer.git
cd file-organizer
```

### Run CLI Version

```bash
python file_organizer.py
```

### Run GUI Version

```bash
python file_organizer_gui.py
```

---

## 🖥️ GUI Mode Features

### Modern Interface
- Dark theme with purple accents
- Responsive layout with proper spacing

### Source Selection
- **Browse Button** — Select any directory
- **Current Folder Button** — Use the folder where the program is located

### Operation Modes
- **Move** — Files moved to exported folder (originals deleted)
- **Copy** — Files copied to exported folder (originals preserved)

### Custom Categories
Add your own file type categories:
1. Enter **Folder Name** (e.g., `projects`)
2. Enter **Extensions** (e.g., `.py,.js,.html`)
3. Click **Add** to create the category
4. Files with matching extensions will be sorted into that folder

### Dry Run
Preview what files will be sorted without making any changes.

---

## 🎮 CLI Mode

Interactive terminal menu with options:
- `1` — Move files to sorted folders
- `2` — Copy files to sorted folders  
- `3` — Dry run (preview only)
- `4` — Exit

---

## 🗂️ Output Structure

Files are organized into:
```
[selected-folder]/
└── exported/
    ├── 🖼️  images/
    ├── 📄  documents/
    ├── 🎬  videos/
    ├── 🎵  audio/
    ├── 🗜️  archives/
    └── [your-custom-folders]/
```

---

## ⚙️ Customization

Edit `FILE_CATEGORIES` in the source code:

```python
FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ...],
    "code": [".py", ".js", ".ts", ".html"],  # Add your own!
    ...
}
```

---

## 📋 Notes

- Files with **unrecognized extensions** are left untouched
- The `exported/` directory is created automatically
- Running from within `exported/` folder is not recommended
- GUI requires tkinter (`sudo apt install python3-tk` on Ubuntu/Debian)

---

## 📜 License

MIT License — free to use, modify, and share.

---

<p align="center">Made with ❤️ and Python 🐍</p>