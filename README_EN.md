
# Python Type-1UP

[**[ZH_Tw Version]**](README.md) || [**[English Version]**](README_EN.md) || [**[Hong-Kong Version]**](README_HK.me)

This README explains how to install Python on Windows, macOS, and Linux, and how to run your `type-1up.py` script.

---

## 1. Windows

### Method 1: Traditional Installation
1. Download Python:
   - Official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Click **Download Python [latest version]**.

2. Run the installer:
   - Double-click the downloaded `.exe` file.
   - **Check “Add Python to PATH”**.
   - Click **Install Now**.

3. Verify the installation:
```cmd
python --version
```
or
```cmd
py --version
```

### Method 2: One-Click Installation (Command Line)
```cmd
winget install Python.Python.3
python --version
```

---

## 2. macOS

### Method 1: Traditional Installation
1. Open **Terminal** and check Python:
```bash
python3 --version
```
2. If not installed, go to [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the `.pkg` installer.
3. Verify the installation:
```bash
python3 --version
```

### Method 2: Quick Command-Line Installation (Homebrew)
```bash
brew install python
python3 --version
```

---

## 3. Linux (Ubuntu / Debian)

1. Update packages:
```bash
sudo apt update
sudo apt upgrade
```
2. Install Python 3 and pip:
```bash
sudo apt install python3 python3-pip
```
3. Verify the installation:
```bash
python3 --version
pip3 --version
```

---

## 4. Running the Python Script `type-1up.py`

- **Windows**:
```cmd
python type-1up.py
```
or
```cmd
py type-1up.py
```

- **macOS / Linux**:
```bash
python3 type-1up.py
```

> ⚠️ Make sure your current directory in the terminal or command prompt is where `type-1up.py` is located.

---

## 5. Optional: Installing a Development Environment (IDE)

- **VS Code:** [https://code.visualstudio.com/](https://code.visualstudio.com/)
- **PyCharm:** [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)

---

## 6. Cross-Platform One-Click Run (Optional)

You can create a simple script to run `type-1up.py` easily on Windows, macOS, or Linux.

- **Windows** (`run.bat`):
```bat
@echo off
python type-1up.py
pause
```

- **macOS / Linux** (`run.sh`):
```bash
#!/bin/bash
python3 type-1up.py
```
> Make the file executable:
```bash
chmod +x run.sh
./run.sh
```

---

After completing these steps, you can start using Python for development and run your script!
