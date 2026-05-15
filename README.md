# 📁 File Organizer

> **Automatically sort your messy files into clean, categorized folders — in seconds.**

🌐 **Languages:** [English](README.md) · [فارسی](README.fa.md)

---

## ✨ What Is This?

**File Organizer** is a lightweight Python script that scans a directory and sorts files into categorized subfolders automatically. No more hunting through cluttered downloads folders!

---

## 📂 Supported Categories

| Category | Extensions |
|---|---|
| 🖼️ Images | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.tiff` `.svg` `.webp` |
| 📄 Documents | `.pdf` `.doc` `.docx` `.txt` `.xls` `.xlsx` `.ppt` `.pptx` |
| 🎬 Videos | `.mp4` `.mkv` `.avi` `.mov` `.wmv` |
| 🎵 Audio | `.mp3` `.wav` `.aac` `.flac` `.ogg` |
| 🗜️ Archives | `.zip` `.rar` `.tar` `.gz` `.7z` |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.6+**
- No external dependencies — uses only the standard library!

### Installation

```bash
# Clone or download the script
git clone https://github.com/yourname/file-organizer.git
cd file-organizer

# Place the script in the folder you want to organize
# (or point base_path to your target directory)
```

### Run

```bash
python file_organizer.py
```

---

## 🎮 How It Works

When you run the script, you'll see an interactive menu:

```
********************

📁 File Organizer

********************

1.🟡 Move File To Folders
2.🔵 Copy Files To Folders
3.🟢 Dry Mode
4.🔴 Exit
```

### Menu Options

#### 🟡 `1` — Move Files
Moves every recognized file from the source directory into the appropriate subfolder inside `sorted/`. The original files are **removed** from their current location.

```
🟡 photo.jpg 🟡 Moved to images
🟡 report.pdf 🟡 Moved to documents
```

#### 🔵 `2` — Copy Files
Copies every recognized file into the appropriate subfolder inside `sorted/`. The original files **remain in place** — great for a non-destructive organization.

```
🔵 song.mp3 🔵 copy to audio
🔵 archive.zip 🔵 copy to archives
```

#### 🟢 `3` — Dry Mode
Simulates the organization **without touching any files**. Perfect for previewing what will happen before committing.

```
🟢 video.mp4 🟢 will be copy / move to videos
🟢 notes.txt 🟢 will be copy / move to documents
```

#### 🔴 `4` — Exit
Exits the program. Simple as that.

---

## 🗂️ Output Structure

After running, your `sorted/` folder will look like this:

```
sorted/
├── 🖼️  images/
├── 📄  documents/
├── 🎬  videos/
├── 🎵  audio/
└── 🗜️  archives/
```

---

## ⚙️ Customization

Want to add more file types? Open `file_organizer.py` and edit the `FILE_CATEGORIES` dictionary:

```python
FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ...],
    "code": [".py", ".js", ".ts", ".html"],   # ← add your own!
    ...
}
```

Want to change the output folder? Update `target_path`:

```python
target_path = base_path / "sorted"   # ← change "sorted" to anything
```

---

## 📋 Notes

- Files with **unrecognized extensions** are left untouched.
- The `sorted/` directory and all category subfolders are created **automatically** if they don't exist.
- Running the script from within the `sorted/` folder is not recommended.

---

## 📜 License

MIT License — free to use, modify, and share.

---

<p align="center">Made with ❤️ and Python 🐍</p>
