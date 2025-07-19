import customtkinter as ctk
import math

class Calculator:
    def __init__(self):
        # Configure appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("Calculator")
        self.root.geometry("320x500")
        self.root.resizable(False, False)
        
        # Variables
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.result = ""
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title bar
        title_frame = ctk.CTkFrame(self.root, height=40, corner_radius=0)
        title_frame.pack(fill="x", padx=0, pady=0)
        title_frame.pack_propagate(False)
        
        # Display
        self.display_frame = ctk.CTkFrame(self.root, height=80, corner_radius=0)
        self.display_frame.pack(fill="x", padx=0, pady=0)
        self.display_frame.pack_propagate(False)
        
        self.display_var = ctk.StringVar(value="0")
        self.display = ctk.CTkLabel(
            self.display_frame, 
            textvariable=self.display_var,
            font=("Segoe UI", 32, "bold"),
            anchor="e",
            justify="right"
        )
        self.display.pack(fill="both", expand=True, padx=15, pady=10)
        
        # Button frame
        button_frame = ctk.CTkFrame(self.root, corner_radius=0)
        button_frame.pack(fill="both", expand=True, padx=5, pady=2)
        
        # Button layout (rows)
        buttons = [
            [("%", self.percentage), ("CE", self.clear_entry), ("C", self.clear_all), ("⌫", self.backspace)],
            [("¹∕ₓ", self.reciprocal), ("x²", self.square), ("²√x", self.square_root), ("÷", lambda: self.operator_click("/"))],
            [("7", lambda: self.number_click("7")), ("8", lambda: self.number_click("8")), ("9", lambda: self.number_click("9")), ("×", lambda: self.operator_click("*"))],
            [("4", lambda: self.number_click("4")), ("5", lambda: self.number_click("5")), ("6", lambda: self.number_click("6")), ("−", lambda: self.operator_click("-"))],
            [("1", lambda: self.number_click("1")), ("2", lambda: self.number_click("2")), ("3", lambda: self.number_click("3")), ("+", lambda: self.operator_click("+"))],
            [("±", self.plus_minus), ("0", lambda: self.number_click("0")), (".", self.decimal_point), ("=", self.equals)]
        ]
        
        for row_index, row in enumerate(buttons):
            for col_index, (text, command) in enumerate(row):
                # Button styling based on type
                if text in ["=", "+", "−", "×", "÷"]:
                    # Operator buttons
                    if text == "=":
                        fg_color = "#0078d4"  # Blue for equals
                        hover_color = "#106ebe"
                    else:
                        fg_color = "transparent"
                        hover_color = ("gray80", "gray25")
                    text_color = ("gray10", "white")
                elif text in ["%", "CE", "C", "⌫", "¹∕ₓ", "x²", "²√x", "±"]:
                    # Function buttons
                    fg_color = "transparent"
                    hover_color = ("gray80", "gray25")
                    text_color = ("gray10", "gray90")
                else:
                    # Number buttons
                    fg_color = ("gray75", "gray25")
                    hover_color = ("gray65", "gray35")
                    text_color = ("gray10", "white")
                
                btn = ctk.CTkButton(
                    button_frame,
                    text=text,
                    width=70,
                    height=55,
                    font=("Segoe UI", 16),
                    fg_color=fg_color,
                    hover_color=hover_color,
                    text_color=text_color,
                    corner_radius=5,
                    command=command
                )
                btn.grid(row=row_index, column=col_index, padx=2, pady=2, sticky="nsew")
        
        # Configure grid weights
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
    
    def update_display(self, value):
        self.display_var.set(str(value))
    
    def number_click(self, number):
        if self.current == "0" or self.current == "Error":
            self.current = number
        else:
            self.current += number
        
        # If we have an operator, show the full expression
        if self.operator and self.previous:
            operator_symbols = {
                "+": "+",
                "-": "−", 
                "*": "×",
                "/": "÷"
            }
            display_text = f"{self.previous} {operator_symbols.get(self.operator, self.operator)} {self.current}"
            self.update_display(display_text)
        else:
            self.update_display(self.current)
    
    def operator_click(self, op):
        if self.operator and self.previous and self.current:
            self.equals()
        
        self.previous = self.current
        self.current = "0"
        self.operator = op
        
        # Display the operator symbol
        operator_symbols = {
            "+": "+",
            "-": "−",
            "*": "×", 
            "/": "÷"
        }
        display_text = f"{self.previous} {operator_symbols.get(op, op)}"
        self.update_display(display_text)
    
    def equals(self):
        if self.operator and self.previous and self.current:
            try:
                prev = float(self.previous)
                curr = float(self.current)
                
                if self.operator == "+":
                    result = prev + curr
                elif self.operator == "-":
                    result = prev - curr
                elif self.operator == "*":
                    result = prev * curr
                elif self.operator == "/":
                    if curr == 0:
                        self.update_display("Cannot divide by zero")
                        self.clear_all()
                        return
                    result = prev / curr
                
                # Format result
                if result == int(result):
                    result = int(result)
                
                self.current = str(result)
                self.update_display(self.current)
                self.operator = ""
                self.previous = ""
                
            except:
                self.update_display("Error")
                self.clear_all()
    
    def clear_all(self):
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.update_display("0")
    
    def clear_entry(self):
        self.current = "0"
        
        # If we have an operator, show the expression with the cleared current number
        if self.operator and self.previous:
            operator_symbols = {
                "+": "+",
                "-": "−",
                "*": "×",
                "/": "÷"
            }
            display_text = f"{self.previous} {operator_symbols.get(self.operator, self.operator)} {self.current}"
            self.update_display(display_text)
        else:
            self.update_display("0")
    
    def backspace(self):
        if len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"
            
        # If we have an operator, show the full expression
        if self.operator and self.previous:
            operator_symbols = {
                "+": "+",
                "-": "−",
                "*": "×",
                "/": "÷"
            }
            display_text = f"{self.previous} {operator_symbols.get(self.operator, self.operator)} {self.current}"
            self.update_display(display_text)
        else:
            self.update_display(self.current)
    
    def decimal_point(self):
        if "." not in self.current:
            self.current += "."
            
            # If we have an operator, show the full expression
            if self.operator and self.previous:
                operator_symbols = {
                    "+": "+",
                    "-": "−",
                    "*": "×", 
                    "/": "÷"
                }
                display_text = f"{self.previous} {operator_symbols.get(self.operator, self.operator)} {self.current}"
                self.update_display(display_text)
            else:
                self.update_display(self.current)
    
    def plus_minus(self):
        if self.current != "0":
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
            self.update_display(self.current)
    
    def percentage(self):
        try:
            result = float(self.current) / 100
            self.current = str(result)
            self.update_display(self.current)
        except:
            self.update_display("Error")
    
    def reciprocal(self):
        try:
            if float(self.current) == 0:
                self.update_display("Cannot divide by zero")
                return
            result = 1 / float(self.current)
            self.current = str(result)
            self.update_display(self.current)
        except:
            self.update_display("Error")
    
    def square(self):
        try:
            result = float(self.current) ** 2
            self.current = str(result)
            self.update_display(self.current)
        except:
            self.update_display("Error")
    
    def square_root(self):
        try:
            if float(self.current) < 0:
                self.update_display("Invalid input")
                return
            result = math.sqrt(float(self.current))
            self.current = str(result)
            self.update_display(self.current)
        except:
            self.update_display("Error")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
