import tkinter as tk
from tkinter import messagebox
import numpy as np
from core import MatrixLogic  # 引入剛剛寫好的邏輯模組

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        self.logic = MatrixLogic()
        self.create_widgets()

    def create_widgets(self):
        # 標籤與輸入框
        tk.Label(self.root, text="Matrix A / Size:").grid(row=0, column=0)
        tk.Label(self.root, text="Matrix B / Scalar:").grid(row=0, column=2)

        self.matrixA_input = tk.Text(self.root, height=5, width=20)
        self.matrixA_input.grid(row=1, column=0, padx=10, pady=10)

        self.matrixB_input = tk.Text(self.root, height=5, width=20)
        self.matrixB_input.grid(row=1, column=2, padx=10, pady=10)

        # 定義按鈕與對應的函式
        operations = [
            ("Add", self.run_add),
            ("Subtract", self.run_subtract),
            ("Multiply", self.run_multiply),
            ("Transpose A", self.run_transpose),
            ("Determinant A", self.run_determinant),
            ("Inverse A", self.run_inverse),
            ("Scalar Mul A", self.run_scalar),
            ("Identity Matrix", self.run_identity)
        ]

        # 產生按鈕
        for i, (text, func) in enumerate(operations):
            tk.Button(self.root, text=text, command=func).grid(row=2 + i // 2, column=i % 2, padx=5, pady=5)

        # 結果顯示區
        tk.Label(self.root, text="Result:").grid(row=6, column=1)
        self.result_display = tk.Text(self.root, height=5, width=20)
        self.result_display.grid(row=7, column=1, padx=10, pady=10)

    def _get_inputs(self, needs_b=True):
        """內部輔助函式：取得並解析輸入"""
        try:
            txt_a = self.matrixA_input.get("1.0", tk.END)
            a = self.logic.parse_matrix_text(txt_a)
            
            b = None
            if needs_b:
                txt_b = self.matrixB_input.get("1.0", tk.END)
                b = self.logic.parse_matrix_text(txt_b)
                if b is None: raise ValueError("Matrix B is empty")
            
            if a is None: raise ValueError("Matrix A is empty")
            return a, b
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return None, None

    def _show_result(self, res):
        """內部輔助函式：顯示結果"""
        self.result_display.delete("1.0", tk.END)
        self.result_display.insert(tk.END, str(res))

    # --- 按鈕事件處理 ---

    def run_add(self):
        a, b = self._get_inputs(needs_b=True)
        if a is not None and b is not None:
            try:
                self._show_result(self.logic.add(a, b))
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def run_subtract(self):
        a, b = self._get_inputs(needs_b=True)
        if a is not None and b is not None:
            try:
                self._show_result(self.logic.subtract(a, b))
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def run_multiply(self):
        a, b = self._get_inputs(needs_b=True)
        if a is not None and b is not None:
            try:
                self._show_result(self.logic.multiply(a, b))
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def run_transpose(self):
        a, _ = self._get_inputs(needs_b=False)
        if a is not None:
            self._show_result(self.logic.transpose(a))

    def run_determinant(self):
        a, _ = self._get_inputs(needs_b=False)
        if a is not None:
            try:
                self._show_result(self.logic.determinant(a))
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def run_inverse(self):
        a, _ = self._get_inputs(needs_b=False)
        if a is not None:
            try:
                self._show_result(self.logic.inverse(a))
            except np.linalg.LinAlgError:
                messagebox.showerror("Error", "Matrix is not invertible")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def run_scalar(self):
        a, _ = self._get_inputs(needs_b=False)
        if a is not None:
            try:
                scalar_txt = self.matrixB_input.get("1.0", tk.END).strip()
                val = float(scalar_txt)
                self._show_result(self.logic.scalar_multiply(a, val))
            except ValueError:
                messagebox.showerror("Error", "Invalid scalar value")

    def run_identity(self):
        try:
            size_txt = self.matrixA_input.get("1.0", tk.END).strip()
            size = int(size_txt)
            self._show_result(self.logic.identity(size))
        except ValueError:
            messagebox.showerror("Error", "Invalid integer for size")