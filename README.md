
# Python Type-1UP

[**[ZH_Tw Version]**](README.md) || [**[English Version]**](README_EN.md) || [**[Hong-Kong Version]**](README_HK.md)

這份 README 教你如何在 Windows、macOS 和 Linux 上安裝 Python，並啟動你的  `type-1up.py`。

---

## 1. Windows

### 方法 1：傳統安裝
1. 下載 Python：
   - 官方網站: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - 點擊 **Download Python [最新版]**。

2. 執行安裝程式：
   - 雙擊下載的 `.exe` 檔案。
   - **勾選 “Add Python to PATH”**。
   - 點擊 **Install Now**。

3. 驗證安裝：
```cmd
python --version
```
或
```cmd
py --version
```

### 方法 2：一鍵安裝（命令行）
```cmd
winget install Python.Python.3
python --version
```

---

## 2. macOS

### 方法 1：傳統安裝
1. 打開 **終端機**，檢查 Python：
```bash
python3 --version
```
2. 若未安裝，前往 [https://www.python.org/downloads/](https://www.python.org/downloads/) 下載 `.pkg` 安裝包並安裝。
3. 驗證：
```bash
python3 --version
```

### 方法 2：命令行快速安裝（Homebrew）
```bash
brew install python
python3 --version
```

---

## 3. Linux (Ubuntu / Debian)

1. 更新套件：
```bash
sudo apt update
sudo apt upgrade
```
2. 安裝 Python 3 與 pip：
```bash
sudo apt install python3 python3-pip
```
3. 驗證：
```bash
python3 --version
pip3 --version
```

---

## 4. 啟動 Python 腳本 `type-1up.py`

- **Windows**：
```cmd
python type-1up.py
```
或
```cmd
py type-1up.py
```

- **macOS / Linux**：
```bash
python3 type-1up.py
```

> ⚠️ 確保你在終端機或命令提示字元中，當前路徑是 `type-1up.py` 所在資料夾。

---

## 5. 選擇性：安裝開發環境（IDE）

- **VS Code:** [https://code.visualstudio.com/](https://code.visualstudio.com/)
- **PyCharm:** [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)

---

## 6. 跨平台一鍵啟動（可選）

你可以建立一個簡單的啟動腳本，方便 Windows / macOS / Linux 一鍵執行 `type-1up.py`。

- **Windows** (`run.bat`)：
```bat
@echo off
python type-1up.py
pause
```

- **macOS / Linux** (`run.sh`)：
```bash
#!/bin/bash
python3 type-1up.py
```
> 給檔案執行權限：
```bash
chmod +x run.sh
./run.sh
```

---

完成以上步驟後，你就可以開始使用 Python 進行開發並運行腳本了！
