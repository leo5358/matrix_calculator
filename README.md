# 矩陣計算機 (Matrix Calculator)

這是一個使用 Python 開發的圖形化介面 (GUI) 矩陣計算機，旨在提供直觀且簡單的矩陣運算功能。

本專案經過重構，將運算邏輯與使用者介面分離，以提高程式碼的可讀性與維護性。

## 功能特色

本程式支援以下矩陣運算：
* **基本運算**：矩陣加法、減法與乘法。
* **單一矩陣運算 (矩陣 A)**：
    * 轉置矩陣 (Transpose)
    * 計算行列式值 (Determinant)
    * 計算反矩陣 (Inverse)
* **數值運算**：
    * 純量相乘：將矩陣 A 乘以矩陣 B 欄位中輸入的數值。
    * 生成單位矩陣：根據矩陣 A 欄位中輸入的大小生成單位矩陣。

## 專案結構

重構後的程式碼分為三個主要檔案：
* **`main.py`**: 程式進入點，負責啟動應用程式。
* **`ui.py`**: 負責圖形介面 (GUI) 的繪製與使用者互動。
* **`core.py`**: 負責所有矩陣運算邏輯與資料解析 (基於 NumPy)。

## 安裝步驟

1.  **複製專案**：
    將專案程式碼下載至您的本地電腦。

2.  **建立虛擬環境 (建議)**：
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    # .venv\Scripts\activate   # Windows
    ```

3.  **安裝必要套件**：
    本專案依賴於 `numpy` 庫進行數學運算。
    ```bash
    pip install -r requirements.txt
    ```

    > **macOS 使用者注意事項**：
    > 如果執行時出現 `ModuleNotFoundError: No module named '_tkinter'` 錯誤，請確保已安裝 `python-tk`。
    > 使用 Homebrew 的使用者可執行：`brew install python-tk` (或重新安裝 python)。

## 使用說明

1.  **啟動程式**：
    請執行 `main.py` (而非舊版的 `mat.py`)：
    ```bash
    python main.py
    ```

2.  **操作方式**：
    * 在 **Matrix A** 與 **Matrix B** 的文字方塊中輸入矩陣數值。
    * 每一行代表矩陣的一列 (Row)，數字之間請以空格分隔。
    * 點擊對應的按鈕進行運算。
    * 運算結果將顯示於下方的 **Result** 方塊中。

### 注意事項
* 進行行列式或反矩陣運算時，矩陣 A 必須為方陣 (Square Matrix)。
* 進行純量相乘時，請將純量值輸入在 Matrix B 的位置。
* 生成單位矩陣時，請在 Matrix A 的位置輸入整數大小。

## 使用技術
* **Python 3**
* **Tkinter**: 用於建構圖形化介面。
* **NumPy**: 用於高效處理矩陣運算。