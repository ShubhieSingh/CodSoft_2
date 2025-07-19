# 🧮 Calculator GUI

<div align="center">

[![GitHub repo](https://img.shields.io/badge/GitHub-CodSoft__2-blue?style=for-the-badge&logo=github)](https://github.com/ShubhieSingh/CodSoft_2)
[![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.0+-green?style=for-the-badge&logo=tkinter)](https://github.com/TomSchimansky/CustomTkinter)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**A modern, feature-rich calculator application built with Python and CustomTkinter**

*Offering a sleek dark theme interface with comprehensive mathematical operations*

[🚀 Quick Start](#-installation) •
[📖 Usage Guide](#-usage) •
[🛠️ Technical Details](#️-technical-details) •
[🎨 Customization](#-customization)

</div>

---

## 📸 Screenshots

<div align="center">

### 🖥️ Main Interface
![Calculator Main Interface](https://github.com/ShubhieSingh/CodSoft_2/blob/eb22c6752602edf15d14f75985a0799dc3220eea/screenshots/Screenshot%202025-07-19%20232430.png)

> *The main calculator interface with modern dark theme and intuitive button layout*

### ⚡ Mathematical Operations in Action
![Calculator Operations](https://github.com/ShubhieSingh/CodSoft_2/blob/eb22c6752602edf15d14f75985a0799dc3220eea/screenshots/Screenshot%202025-07-19%20232454.png)

> *Real-time expression display and comprehensive mathematical operations*

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔢 Core Calculator Functions
- ✅ **Basic Arithmetic**: Addition (+), Subtraction (−), Multiplication (×), Division (÷)
- ✅ **Advanced Operations**: Square (x²), Square Root (²√x), Reciprocal (¹∕ₓ), Percentage (%)
- ✅ **Utility Functions**: Plus/Minus toggle (±), Decimal point support
- ✅ **Clear Operations**: Clear All (C), Clear Entry (CE), Backspace (⌫)

</td>
<td width="50%">

### 🎨 User Experience
- 🎨 **Modern Dark Theme**: Professional appearance with customizable colors
- 📱 **Responsive Layout**: Optimized button sizing and spacing
- 🔄 **Real-time Display**: Shows complete expressions during calculations
- ⚡ **Instant Feedback**: Visual button hover effects and state changes
- 🛡️ **Error Handling**: Graceful handling of division by zero and invalid operations

</td>
</tr>
</table>

### 🚀 Technical Features

> **Cross-Platform Compatibility** 🖥️ Runs seamlessly on Windows, macOS, and Linux

> **Precise Calculations** 🎯 Handles floating-point arithmetic with high accuracy

> **Extensible Architecture** 🔧 Clean, well-documented Python code structure

> **Consistent UI** 📏 Fixed window size ensures uniform experience across systems

---

## 🚀 Installation

<details>
<summary><b>📋 Prerequisites</b></summary>

- ![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square&logo=python) or higher
- ![pip](https://img.shields.io/badge/pip-package%20manager-orange?style=flat-square) package manager

</details>

### ⚡ Quick Setup

<details open>
<summary><b>🔧 Standard Installation</b></summary>

```bash
# 1️⃣ Clone the repository
git clone https://github.com/ShubhieSingh/CodSoft_2.git
cd CodSoft_2

# 2️⃣ Install dependencies
pip install customtkinter

# 3️⃣ Run the application
python Calculator_GUI.py
```

</details>

<details>
<summary><b>🐍 Virtual Environment Setup (Recommended)</b></summary>

```bash
# Create virtual environment
python -m venv calculator-env

# Activate virtual environment
# Windows:
calculator-env\Scripts\activate
# macOS/Linux:
source calculator-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python Calculator_GUI.py
```

</details>

<details>
<summary><b>📦 Alternative Installation Methods</b></summary>

**Using requirements.txt:**
```bash
pip install -r requirements.txt
```

**Direct CustomTkinter installation:**
```bash
pip install customtkinter>=5.0.0
```

</details>

---

## 🎮 Usage

<div align="center">

### 🎯 Quick Operation Guide

</div>

<table>
<tr>
<td width="50%">

#### 🔢 **Basic Operations**

| Action | Description |
|--------|-------------|
| `0-9` | Click number buttons to input values |
| `+` `-` `×` `÷` | Perform arithmetic operations |
| `=` | Calculate and display results |
| `.` | Add decimal point for floating numbers |

</td>
<td width="50%">

#### ⚡ **Advanced Functions**

| Button | Function | Description |
|--------|----------|-------------|
| `x²` | Square | Square the current number |
| `²√x` | Square Root | Find square root |
| `¹∕ₓ` | Reciprocal | Calculate 1/x |
| `%` | Percentage | Convert to percentage |

</td>
</tr>
</table>

### 🛠️ Utility Operations

<div align="center">

| Button | Action | Result |
|:------:|:-------|:-------|
| `C` | **Clear All** | Resets calculator completely |
| `CE` | **Clear Entry** | Clears current input only |
| `⌫` | **Backspace** | Removes last entered digit |
| `±` | **Plus/Minus** | Toggles positive/negative |

</div>

> ### 💡 **Pro Tip: Expression Display**
> 
> The calculator shows your complete expression as you build it!
> 
> **Example:** When calculating `25 + 7`, you'll see:
> - Enter `25` → Display: `25`
> - Click `+` → Display: `25 +`
> - Enter `7` → Display: `25 + 7`
> - Click `=` → Display: `32`

---

## 🛠️ Technical Details

<div align="center">

### 🏗️ Built With

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-FF6B6B?style=for-the-badge&logo=tkinter&logoColor=white)](https://github.com/TomSchimansky/CustomTkinter)
[![Math](https://img.shields.io/badge/Math%20Module-4CAF50?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/math.html)

</div>

### 📁 Project Structure

```
📦 CodSoft_2/
├── 📄 Calculator_GUI.py          # 🚀 Main application file
├── 📄 README.md                  # 📖 Project documentation  
├── 📄 requirements.txt           # 📋 Python dependencies
├── 📁 screenshots/               # 📸 Application screenshots
│   ├── 🖼️ calculator-main.png
│   └── 🖼️ calculator-operations.png
└── 📄 LICENSE                    # ⚖️ MIT License
```

<details>
<summary><b>🏛️ Architecture Overview</b></summary>

| Component | Description | Responsibility |
|-----------|-------------|----------------|
| **Calculator Class** | 🧠 Core application logic | UI management and state handling |
| **Widget Creation** | 🎨 Dynamic UI generation | Button styling and layout management |
| **Event Handling** | ⚡ User interaction processing | Input validation and calculation logic |
| **Display Management** | 📺 Real-time updates | Expression and result visualization |

</details>

---

## 🎨 Customization

<details>
<summary><b>🎨 Theme Modifications</b></summary>

The calculator uses CustomTkinter's powerful theming system:

```python
# Change color theme
ctk.set_default_color_theme("blue")    # Options: "blue", "green", "dark-blue"

# Switch appearance mode  
ctk.set_appearance_mode("dark")        # Options: "dark", "light", "system"
```

**Available Themes:**
- 🔵 **Blue** (Default) - Professional and modern
- 🟢 **Green** - Nature-inspired palette  
- 🔷 **Dark Blue** - Deep, sophisticated look

</details>

<details>
<summary><b>⚙️ Adding Custom Functions</b></summary>

To extend the calculator with new operations:

1. **Add button to layout:**
   ```python
   # In create_widgets() method
   ("new_op", self.custom_function)
   ```

2. **Implement the function:**
   ```python
   def custom_function(self):
       try:
           # Your custom logic here
           result = your_calculation(float(self.current))
           self.current = str(result)
           self.update_display(self.current)
       except:
           self.update_display("Error")
   ```

3. **Style the button:**
   ```python
   # Add styling logic in button creation loop
   elif text in ["new_op"]:
       fg_color = "your_color"
   ```

</details>

---

## 🐛 Troubleshooting

<details>
<summary><b>❌ Common Issues & Solutions</b></summary>

### Import Error: No module named 'customtkinter'

```bash
# Solution 1: Install CustomTkinter
pip install customtkinter

# Solution 2: Upgrade pip and retry
python -m pip install --upgrade pip
pip install customtkinter
```

### Calculator window doesn't appear

- ✅ **Check Python version**: Ensure you're running Python 3.7+
- ✅ **Verify installation**: `pip list | grep customtkinter`
- ✅ **Run from terminal**: Check for error messages
- ✅ **System compatibility**: Ensure GUI support is available

### Buttons not responding

- 🔄 **Restart application**: Close and reopen the calculator
- 🎯 **Check window focus**: Click on the calculator window
- 🐍 **Verify environment**: Ensure Python environment is correctly set up
- 💻 **System resources**: Check if system has sufficient memory

</details>

<div align="center">

### 🛡️ Built-in Error Handling

| Error Type | Handling | User Experience |
|------------|----------|-----------------|
| **Division by Zero** | ⚠️ Displays warning message | `"Cannot divide by zero"` |
| **Invalid Operations** | 🚫 Graceful error recovery | `"Error"` with reset |
| **Overflow Conditions** | 📊 Automatic formatting | Scientific notation when needed |
| **Input Validation** | ✅ Real-time checking | Prevents invalid characters |

</div>

---

## 📄 License

<div align="center">

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## 🤝 Contributing

<div align="center">

**Contributions are welcome!** 🎉

[![GitHub Issues](https://img.shields.io/github/issues/ShubhieSingh/CodSoft_2?style=for-the-badge)](https://github.com/ShubhieSingh/CodSoft_2/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/ShubhieSingh/CodSoft_2?style=for-the-badge)](https://github.com/ShubhieSingh/CodSoft_2/pulls)

</div>

### 🚀 How to Contribute

1. **🍴 Fork the repository**
   ```bash
   git clone https://github.com/ShubhieSingh/CodSoft_2.git
   ```

2. **🌿 Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **💾 Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **🚀 Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

5. **📝 Open a Pull Request**

<div align="center">

### 🎯 Contribution Guidelines

| Type | Description | Example |
|------|-------------|---------|
| 🐛 **Bug Fix** | Fix existing issues | Resolve calculation errors |
| ⚡ **Feature** | Add new functionality | Scientific calculator mode |
| 📚 **Documentation** | Improve docs | Update README, add comments |
| 🎨 **Style** | UI/UX improvements | Better themes, animations |

</div>

---

<div align="center">

### 🌟 Show Your Support

If this project helped you, please consider giving it a ⭐ on [GitHub](https://github.com/ShubhieSingh/CodSoft_2)!

**Made with ❤️ using Python and CustomTkinter**

[![GitHub stars](https://img.shields.io/github/stars/ShubhieSingh/CodSoft_2?style=social)](https://github.com/ShubhieSingh/CodSoft_2/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ShubhieSingh/CodSoft_2?style=social)](https://github.com/ShubhieSingh/CodSoft_2/network/members)

</div>
