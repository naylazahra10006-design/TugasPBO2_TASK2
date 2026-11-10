import tkinter as tk
from tkinter import messagebox
from usecases.student_usecase import StudentUseCase
from presentation.views.student_view import StudentView

class StudentController:
    def __init__(self, usecase: StudentUseCase, view: StudentView):
        self.usecase = usecase
        self.view = view
        self.view.set_controller(self)
        
        # Bind tombol UI ke fungsi controller
        self.view.btn_add.config(command=self.add_student)
        self.view.btn_update.config(command=self.update_student)
        self.view.btn_delete.config(command=self.delete_student)
        self.view.tree.bind("<<TreeviewSelect>>", self.on_select)

    def load_students(self):
        for row in self.view.tree.get_children():
            self.view.tree.delete(row)
        students = self.usecase.list_students()
        for s in students:
            self.view.tree.insert("", tk.END, values=(s.nim, s.nama, s.prodi, s.angkatan))

    def add_student(self):
        try:
            nim = self.view.entry_nim.get()
            nama = self.view.entry_nama.get()
            prodi = self.view.entry_prodi.get()
            angkatan = int(self.view.entry_angkatan.get())
            
            self.usecase.create_student(nim, nama, prodi, angkatan)
            self.load_students()
            self.clear_form()
            messagebox.showinfo("Sukses", "Data mahasiswa berhasil ditambahkan!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_student(self):
        try:
            nim = self.view.entry_nim.get()
            nama = self.view.entry_nama.get()
            prodi = self.view.entry_prodi.get()
            angkatan = int(self.view.entry_angkatan.get())
            
            self.usecase.update_student(nim, nama, prodi, angkatan)
            self.load_students()
            self.clear_form()
            messagebox.showinfo("Sukses", "Data mahasiswa berhasil diupdate!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_student(self):
        try:
            selected = self.view.tree.selection()
            if not selected:
                messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus pada tabel!")
                return
            nim = self.view.tree.item(selected[0])['values'][0]
            self.usecase.delete_student(str(nim))
            self.load_students()
            self.clear_form()
            messagebox.showinfo("Sukses", "Data mahasiswa berhasil dihapus!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_select(self, event):
        selected = self.view.tree.selection()
        if selected:
            values = self.view.tree.item(selected[0])['values']
            self.clear_form()
            self.view.entry_nim.insert(0, values[0])
            self.view.entry_nama.insert(0, values[1])
            self.view.entry_prodi.insert(0, values[2])
            self.view.entry_angkatan.insert(0, values[3])

    def clear_form(self):
        self.view.entry_nim.delete(0, tk.END)
        self.view.entry_nama.delete(0, tk.END)
        self.view.entry_prodi.delete(0, tk.END)
        self.view.entry_angkatan.delete(0, tk.END)

    def run(self):
        self.load_students()