import tkinter as tk
from tkinter import ttk

class StudentView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Data Mahasiswa - Clean Architecture")
        self.geometry("600x450")
        
        self.controller = None
        self._build_ui()

    def set_controller(self, controller):
        self.controller = controller

    def _build_ui(self):
        title_label = tk.Label(self, text="Manajemen Data Mahasiswa", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Form Input Frame
        form_frame = tk.Frame(self)
        form_frame.pack(pady=5)
        
        tk.Label(form_frame, text="NIM:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.entry_nim = tk.Entry(form_frame, width=30)
        self.entry_nim.grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(form_frame, text="Nama:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.entry_nama = tk.Entry(form_frame, width=30)
        self.entry_nama.grid(row=1, column=1, padx=5, pady=2)
        
        tk.Label(form_frame, text="Prodi:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.entry_prodi = tk.Entry(form_frame, width=30)
        self.entry_prodi.grid(row=2, column=1, padx=5, pady=2)
        
        tk.Label(form_frame, text="Angkatan:").grid(row=3, column=0, sticky="w", padx=5, pady=2)
        self.entry_angkatan = tk.Entry(form_frame, width=30)
        self.entry_angkatan.grid(row=3, column=1, padx=5, pady=2)
        
        # Button Frame
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        
        self.btn_add = tk.Button(btn_frame, text="Tambah", bg="green", fg="white", width=10)
        self.btn_add.grid(row=0, column=0, padx=5)
        
        self.btn_update = tk.Button(btn_frame, text="Update", bg="orange", fg="white", width=10)
        self.btn_update.grid(row=0, column=1, padx=5)
        
        self.btn_delete = tk.Button(btn_frame, text="Hapus", bg="red", fg="white", width=10)
        self.btn_delete.grid(row=0, column=2, padx=5)
        
        # Table / Treeview
        columns = ("NIM", "Nama", "Prodi", "Angkatan")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)