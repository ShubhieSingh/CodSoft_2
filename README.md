# 🧮 Calculator GUI

A modern, feature-rich calculator application built with Python and CustomTkinter, offering a sleek dark theme interface with comprehensive mathematical operations.

## 📸 Screenshots

### Main Interface
![Calculator Main Interface](screenshots/calculator-main.png)
*The main calculator interface with dark theme and intuitive button layout*

### Mathematical Operations
![Calculator Operations](screenshots/calculator-operations.png)
*Demonstration of various mathematical operations and real-time expression display*

## ✨ Features

### Core Calculator Functions
- ✅ **Basic Arithmetic**: Addition (+), Subtraction (−), Multiplication (×), Division (÷)
- ✅ **Advanced Operations**: Square (x²), Square Root (²√x), Reciprocal (¹∕ₓ), Percentage (%)
- ✅ **Utility Functions**: Plus/Minus toggle (±), Decimal point support
- ✅ **Clear Operations**: Clear All (C), Clear Entry (CE), Backspace (⌫)

### User Experience
- 🎨 **Modern Dark Theme**: Professional appearance with customizable colors
- 📱 **Responsive Layout**: Optimized button sizing and spacing
- 🔄 **Real-time Display**: Shows complete expressions during calculations
- ⚡ **Instant Feedback**: Visual button hover effects and state changes
- 🛡️ **Error Handling**: Graceful handling of division by zero and invalid operations

### Technical Features
- 🖥️ **Cross-Platform**: Runs on Windows, macOS, and Linux
- 🎯 **Precise Calculations**: Handles floating-point arithmetic accurately
- 🔧 **Extensible Code**: Clean, well-documented Python code structure
- 📏 **Fixed Window Size**: Consistent UI experience across different systems

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd calculator-gui
   ```

2. **Install required dependencies**
   ```bash
   pip install customtkinter
   ```

3. **Run the application**
   ```bash
   python Calculator_GUI.py
   ```

### Alternative Installation (Virtual Environment)
```bash
# Create virtual environment
python -m venv calculator-env

# Activate virtual environment
# On Windows:
calculator-env\Scripts\activate
# On macOS/Linux:
source calculator-env/bin/activate

# Install dependencies
pip install customtkinter

# Run the application
python Calculator_GUI.py
```

## 🎮 Usage

### Basic Operations
1. **Numbers**: Click number buttons (0-9) to input values
2. **Operators**: Click operation buttons (+, −, ×, ÷) to perform calculations
3. **Equals**: Press the blue equals button (=) to get results
4. **Decimal**: Use the decimal point (.) for floating-point numbers

### Advanced Functions
- **Square**: Click `x²` to square the current number
- **Square Root**: Click `²√x` to find the square root
- **Reciprocal**: Click `¹∕ₓ` to get 1/x
- **Percentage**: Click `%` to convert to percentage

### Utility Operations
- **Clear All**: `C` button clears everything and resets calculator
- **Clear Entry**: `CE` button clears only the current input
- **Backspace**: `⌫` button removes the last entered digit
- **Plus/Minus**: `±` button toggles between positive and negative

### Expression Display
- The calculator shows the complete expression as you build it
- Example: "25 + 7" is displayed while entering the second number
- Results are shown clearly after pressing equals

## 🛠️ Technical Details

### Built With
- **Python 3.x**: Core programming language
- **CustomTkinter**: Modern UI framework for enhanced widgets
- **Math Module**: For advanced mathematical operations

### Project Structure
```
calculator-gui/
│
├── Calculator_GUI.py          # Main application file
├── README.md                  # Project documentation
├── screenshots/               # Application screenshots
│   ├── calculator-main.png
│   └── calculator-operations.png
└── requirements.txt           # Python dependencies
```

### Key Components
- **Calculator Class**: Main application logic and UI management
- **Widget Creation**: Dynamic button generation with proper styling
- **Event Handling**: Comprehensive input processing and calculation logic
- **Display Management**: Real-time expression and result display

## 🎨 Customization

### Theme Modifications
The calculator uses CustomTkinter's theming system. You can modify:
- **Color scheme**: Change `ctk.set_default_color_theme("blue")` to other themes
- **Appearance mode**: Switch between "dark" and "light" modes
- **Button colors**: Customize individual button styling in the button creation loop

### Adding New Functions
To add new mathematical operations:
1. Add the button to the `buttons` array in `create_widgets()`
2. Create a new method for the operation logic
3. Update button styling as needed

## 🐛 Troubleshooting

### Common Issues

**Import Error: No module named 'customtkinter'**
```bash
pip install customtkinter
```

**Calculator window doesn't appear**
- Ensure you're running Python 3.7+
- Check if CustomTkinter is properly installed
- Try running from command line to see error messages

**Buttons not responding**
- Restart the application
- Check if window has focus
- Verify Python environment is correctly set up

### Error Handling
The calculator includes built-in error handling for:
- Division by zero operations
- Invalid mathematical operations
- Overflow conditions
- Input validation errors

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you encounter any issues or have questions:
- Check the troubleshooting section above
- Review the code comments for implementation details
- Create an issue in the repository

## 🔄 Version History

- **v1.0.0** - Initial release with basic calculator functionality
- **v1.1.0** - Added advanced mathematical operations
- **v1.2.0** - Implemented real-time expression display
- **v1.3.0** - Enhanced UI with modern dark theme

---

**Made with ❤️ using Python and CustomTkinter**
