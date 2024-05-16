import tkinter as tk
from tkinter import messagebox
import numpy as np

class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.root, text="Matrix A:").grid(row=0, column=0)
        tk.Label(self.root, text="Matrix B:").grid(row=0, column=2)
        
        self.matrixA = tk.Text(self.root, height=5, width=20)
        self.matrixA.grid(row=1, column=0, padx=10, pady=10)
        self.matrixB = tk.Text(self.root, height=5, width=20)
        self.matrixB.grid(row=1, column=2, padx=10, pady=10)
        
        operations = [
            ("Add", self.add_matrices),
            ("Subtract", self.subtract_matrices),
            ("Multiply", self.multiply_matrices),
            ("Transpose A", self.transpose_matrixA),
            ("Determinant A", self.determinant_matrixA),
            ("Inverse A", self.inverse_matrixA),
            ("Scalar Multiplication A", self.scalar_multiply_matrixA),
            ("Identity Matrix", self.create_identity_matrix)
        ]
        
        for i, (text, func) in enumerate(operations):
            tk.Button(self.root, text=text, command=func).grid(row=2+i//2, column=i%2, padx=5, pady=5)
        
        tk.Label(self.root, text="Result:").grid(row=6, column=1)
        self.result = tk.Text(self.root, height=5, width=20)
        self.result.grid(row=7, column=1, padx=10, pady=10)
        
    def get_matrix(self, text_widget):
        try:
            matrix = []
            for line in text_widget.get("1.0", tk.END).strip().split("\n"):
                matrix.append([float(x) for x in line.split()])
            return np.array(matrix)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None

    def display_result(self, result):
        self.result.delete("1.0", tk.END)
        self.result.insert(tk.END, str(result))
    
    def add_matrices(self):
        A = self.get_matrix(self.matrixA)
        B = self.get_matrix(self.matrixB)
        if A is not None and B is not None:
            try:
                result = A + B
                self.display_result(result)
            except ValueError as e:
                messagebox.showerror("Operation Error", str(e))
    
    def subtract_matrices(self):
        A = self.get_matrix(self.matrixA)
        B = self.get_matrix(self.matrixB)
        if A is not None and B is not None:
            try:
                result = A - B
                self.display_result(result)
            except ValueError as e:
                messagebox.showerror("Operation Error", str(e))
    
    def multiply_matrices(self):
        A = self.get_matrix(self.matrixA)
        B = self.get_matrix(self.matrixB)
        if A is not None and B is not None:
            try:
                result = A @ B
                self.display_result(result)
            except ValueError as e:
                messagebox.showerror("Operation Error", str(e))
    
    def transpose_matrixA(self):
        A = self.get_matrix(self.matrixA)
        if A is not None:
            result = A.T
            self.display_result(result)
    
    def determinant_matrixA(self):
        A = self.get_matrix(self.matrixA)
        if A is not None:
            if A.shape[0] != A.shape[1]:
                messagebox.showerror("Operation Error", "Matrix must be square to calculate the determinant.")
            else:
                result = np.linalg.det(A)
                self.display_result(result)
    
    def inverse_matrixA(self):
        A = self.get_matrix(self.matrixA)
        if A is not None:
            if A.shape[0] != A.shape[1]:
                messagebox.showerror("Operation Error", "Matrix must be square to calculate the inverse.")
            else:
                try:
                    result = np.linalg.inv(A)
                    self.display_result(result)
                except np.linalg.LinAlgError:
                    messagebox.showerror("Operation Error", "Matrix is not invertible.")
    
    def scalar_multiply_matrixA(self):
        A = self.get_matrix(self.matrixA)
        if A is not None:
            try:
                scalar = float(self.matrixB.get("1.0", tk.END).strip())
                result = A * scalar
                self.display_result(result)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid scalar value.")
    
    def create_identity_matrix(self):
        try:
            size = int(self.matrixA.get("1.0", tk.END).strip())
            result = np.eye(size)
            self.display_result(result)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer size.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculator(root)
    root.mainloop()
