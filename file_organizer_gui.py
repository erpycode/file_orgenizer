import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import os
import threading
import shutil

FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
}

custom_categories = {}


class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📁 File Organizer")
        self.root.geometry("650x700")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)
        
        self.source_path = tk.StringVar()
        self.operation_mode = tk.StringVar(value="move")
        self.target_type = tk.StringVar(value="auto")
        
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg="#1e1e2e")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        header = tk.Frame(main_frame, bg="#1e1e2e")
        header.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(header, text="📁 File Organizer", font=("Segoe UI", 22, "bold"), 
                 bg="#1e1e2e", fg="#ffffff").pack(side=tk.LEFT)
        tk.Label(header, text="Smart File Sorting", font=("Segoe UI", 10), 
                 bg="#1e1e2e", fg="#888888").pack(side=tk.LEFT, padx=(10, 0))
        
        source_frame = tk.Frame(main_frame, bg="#2d2d44", padx=15, pady=15, relief=tk.RIDGE, bd=1)
        source_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(source_frame, text="📂 Source Directory", font=("Segoe UI", 11, "bold"), 
                 bg="#2d2d44", fg="#ffffff").pack(anchor=tk.W)
        
        source_entry_frame = tk.Frame(source_frame, bg="#2d2d44")
        source_entry_frame.pack(fill=tk.X, pady=(10, 0))
        
        entry = tk.Entry(source_entry_frame, textvariable=self.source_path, font=("Segoe UI", 10),
                         bg="#1e1e2e", fg="#ffffff", relief=tk.FLAT, insertbackground="#ffffff")
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
        
        browse_btn = tk.Button(source_entry_frame, text="📁 Browse", font=("Segoe UI", 10),
                               bg="#007acc", fg="#ffffff", relief=tk.FLAT, padx=15, cursor="hand2",
                               command=self.browse_source)
        browse_btn.pack(side=tk.RIGHT)
        
        auto_btn = tk.Button(source_entry_frame, text="🏠 Current Folder", font=("Segoe UI", 9),
                             bg="#3a3a5c", fg="#ffffff", relief=tk.FLAT, padx=10, cursor="hand2",
                             command=self.use_current_folder)
        auto_btn.pack(side=tk.RIGHT, padx=(0, 10))
        
        mode_frame = tk.Frame(main_frame, bg="#2d2d44", padx=15, pady=15, relief=tk.RIDGE, bd=1)
        mode_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(mode_frame, text="⚙️ Operation Mode", font=("Segoe UI", 11, "bold"), 
                 bg="#2d2d44", fg="#ffffff").pack(anchor=tk.W)
        
        radio_frame = tk.Frame(mode_frame, bg="#2d2d44")
        radio_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Radiobutton(radio_frame, text="📦 Move files", variable=self.operation_mode, value="move",
                       font=("Segoe UI", 10), bg="#2d2d44", fg="#ffffff", selectcolor="#1e1e2e",
                       activebackground="#2d2d44", activeforeground="#ffffff").pack(side=tk.LEFT, padx=(0, 20))
        tk.Radiobutton(radio_frame, text="📋 Copy files", variable=self.operation_mode, value="copy",
                       font=("Segoe UI", 10), bg="#2d2d44", fg="#ffffff", selectcolor="#1e1e2e",
                       activebackground="#2d2d44", activeforeground="#ffffff").pack(side=tk.LEFT)
        
        target_info = tk.Frame(mode_frame, bg="#1e1e2e", padx=10, pady=8, relief=tk.FLAT, bd=1)
        target_info.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(target_info, text="🎯 Target: [source]/exported/ (auto-sorted by file type)",
                 font=("Segoe UI", 9), bg="#1e1e2e", fg="#888888").pack(anchor=tk.W)
        
        custom_frame = tk.Frame(main_frame, bg="#2d2d44", padx=15, pady=15, relief=tk.RIDGE, bd=1)
        custom_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(custom_frame, text="➕ Custom Categories", font=("Segoe UI", 11, "bold"), 
                 bg="#2d2d44", fg="#ffffff").pack(anchor=tk.W)
        
        custom_input_frame = tk.Frame(custom_frame, bg="#2d2d44")
        custom_input_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(custom_input_frame, text="Folder:", font=("Segoe UI", 9), 
                 bg="#2d2d44", fg="#cccccc").pack(side=tk.LEFT)
        self.custom_folder = tk.Entry(custom_input_frame, font=("Segoe UI", 9), width=12,
                                      bg="#1e1e2e", fg="#ffffff", relief=tk.FLAT, insertbackground="#ffffff")
        self.custom_folder.pack(side=tk.LEFT, padx=(5, 10))
        self.custom_folder.insert(0, "myfiles")
        
        tk.Label(custom_input_frame, text="Extensions:", font=("Segoe UI", 9), 
                 bg="#2d2d44", fg="#cccccc").pack(side=tk.LEFT)
        self.custom_ext = tk.Entry(custom_input_frame, font=("Segoe UI", 9), width=20,
                                   bg="#1e1e2e", fg="#ffffff", relief=tk.FLAT, insertbackground="#ffffff")
        self.custom_ext.pack(side=tk.LEFT, padx=5)
        self.custom_ext.insert(0, ".xyz,.abc")
        
        add_btn = tk.Button(custom_input_frame, text="Add", font=("Segoe UI", 9),
                            bg="#00aa66", fg="#ffffff", relief=tk.FLAT, padx=10, cursor="hand2",
                            command=self.add_custom_category)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        self.custom_list = tk.Listbox(custom_frame, height=3, font=("Segoe UI", 9),
                                        bg="#1e1e2e", fg="#ffffff", relief=tk.FLAT,
                                        selectbackground="#007acc")
        self.custom_list.pack(fill=tk.X, pady=(5, 0))
        
        del_btn = tk.Button(custom_frame, text="🗑️ Delete Selected", font=("Segoe UI", 8),
                            bg="#aa3333", fg="#ffffff", relief=tk.FLAT, padx=8, cursor="hand2",
                            command=self.delete_custom_category)
        del_btn.pack(anchor=tk.E, pady=(5, 0))
        
        button_frame = tk.Frame(main_frame, bg="#1e1e2e")
        button_frame.pack(pady=(10, 15))
        
        self.run_btn = tk.Button(button_frame, text="▶ Run", font=("Segoe UI", 11, "bold"),
                                   bg="#00aa66", fg="#ffffff", relief=tk.FLAT, padx=30, pady=8,
                                   cursor="hand2", command=self.run_operation)
        self.run_btn.pack(side=tk.LEFT, padx=5)
        
        self.dry_btn = tk.Button(button_frame, text="👁️ Dry Run", font=("Segoe UI", 11),
                                   bg="#3a3a5c", fg="#ffffff", relief=tk.FLAT, padx=20, pady=8,
                                   cursor="hand2", command=self.dry_run)
        self.dry_btn.pack(side=tk.LEFT, padx=5)
        
        result_frame = tk.Frame(main_frame, bg="#2d2d44", padx=15, pady=15, relief=tk.RIDGE, bd=1)
        result_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(result_frame, text="📋 Results", font=("Segoe UI", 11, "bold"), 
                 bg="#2d2d44", fg="#ffffff").pack(anchor=tk.W)
        
        text_frame = tk.Frame(result_frame, bg="#1e1e2e", relief=tk.FLAT, bd=1)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.result_text = tk.Text(text_frame, font=("Consolas", 9), bg="#1e1e2e", fg="#88ff88",
                                      relief=tk.FLAT, wrap=tk.NONE, state=tk.DISABLED)
        v_scroll = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        h_scroll = ttk.Scrollbar(text_frame, orient=tk.HORIZONTAL, command=self.result_text.xview)
        self.result_text.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", background="#3a3a5c")
    
    def use_current_folder(self):
        current = os.path.dirname(os.path.abspath(__file__))
        self.source_path.set(current)
    
    def browse_source(self):
        path = filedialog.askdirectory(title="Select Source Directory")
        if path:
            self.source_path.set(path)
    
    def add_custom_category(self):
        folder = self.custom_folder.get().strip()
        extensions = self.custom_ext.get().strip()
        
        if not folder or not extensions:
            messagebox.showwarning("Warning", "Please enter folder name and extensions")
            return
        
        if folder in FILE_CATEGORIES or folder in custom_categories:
            messagebox.showwarning("Warning", "Category already exists")
            return
        
        ext_list = [e.strip() if e.strip().startswith(".") else f".{e.strip()}" for e in extensions.split(",")]
        custom_categories[folder] = ext_list
        self.custom_list.insert(tk.END, f"{folder}: {', '.join(ext_list)}")
        self.custom_folder.delete(0, tk.END)
        self.custom_ext.delete(0, tk.END)
    
    def delete_custom_category(self):
        selection = self.custom_list.curselection()
        if not selection:
            return
        
        index = selection[0]
        item = self.custom_list.get(index)
        folder_name = item.split(":")[0].strip()
        if folder_name in custom_categories:
            del custom_categories[folder_name]
        self.custom_list.delete(index)
    
    def log(self, message, color="#88ff88"):
        self.result_text.configure(state=tk.NORMAL)
        self.result_text.insert(tk.END, message + "\n")
        self.result_text.see(tk.END)
        self.result_text.configure(state=tk.DISABLED)
    
    def get_category(self, file_path):
        suffix = file_path.suffix.lower()
        for category, extensions in FILE_CATEGORIES.items():
            if suffix in extensions:
                return category
        for category, extensions in custom_categories.items():
            if suffix in extensions:
                return category
        return None
    
    def process_files(self, mode, dry_run=False):
        source = Path(self.source_path.get())
        target = source / "exported"
        
        self.run_btn.config(state=tk.DISABLED)
        self.dry_btn.config(state=tk.DISABLED)
        
        if not source.exists():
            self.log("❌ Source directory does not exist")
            self.run_btn.config(state=tk.NORMAL)
            self.dry_btn.config(state=tk.NORMAL)
            return
        
        target.mkdir(parents=True, exist_ok=True)
        
        for category in FILE_CATEGORIES.keys():
            (target / category).mkdir(parents=True, exist_ok=True)
        
        for category in custom_categories.keys():
            (target / category).mkdir(parents=True, exist_ok=True)
        
        files_processed = 0
        for file_path in source.glob("*"):
            if file_path.is_file() and file_path.parent != target:
                category = self.get_category(file_path)
                if category:
                    dest = target / category / file_path.name
                    if dry_run:
                        self.log(f"🟢 {file_path.name} → exported/{category}/")
                    else:
                        try:
                            if mode == "copy":
                                shutil.copy2(file_path, dest)
                                self.log(f"🔵 {file_path.name} → exported/{category}/")
                            else:
                                shutil.move(str(file_path), dest)
                                self.log(f"🟡 {file_path.name} → exported/{category}/")
                            files_processed += 1
                        except Exception as e:
                            self.log(f"❌ Error processing {file_path.name}: {e}")
        
        self.log(f"\n✅ Done! {files_processed} files processed.")
        self.run_btn.config(state=tk.NORMAL)
        self.dry_btn.config(state=tk.NORMAL)
    
    def run_operation(self):
        if not self.source_path.get():
            messagebox.showwarning("Warning", "Please select a source directory")
            return
        
        self.result_text.configure(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.configure(state=tk.DISABLED)
        
        threading.Thread(target=self.process_files, args=(self.operation_mode.get(), False), daemon=True).start()
    
    def dry_run(self):
        if not self.source_path.get():
            messagebox.showwarning("Warning", "Please select a source directory")
            return
        
        self.result_text.configure(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.configure(state=tk.DISABLED)
        
        threading.Thread(target=self.process_files, args=(self.operation_mode.get(), True), daemon=True).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()