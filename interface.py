import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from SemGus_bit_vector import synthesize_program
from SemGus_bit_vector import test_cases



def run_synthesis():
    specification = spec_input.get("1.0", tk.END).strip()
    if not specification:
        messagebox.showerror("Error", "Please enter a specification")
        return
    
    try:
        # Assuming test_cases is predefined or gathered from another input
        program, code = synthesize_program(specification, test_cases)
        output_display.config(state=tk.NORMAL)
        output_display.delete("1.0", tk.END)
        output_display.insert(tk.END, f"Result Program Code: {code}\n")
        output_display.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Setting up the main window
root = tk.Tk()
root.title("SemGus Solver UI")

# Specification input
tk.Label(root, text="Enter Specification:").pack()
spec_input = scrolledtext.ScrolledText(root, height=5)
spec_input.pack()

# Run button
run_button = tk.Button(root, text="Run Synthesis", command=run_synthesis)
run_button.pack()

# Output display
output_display = scrolledtext.ScrolledText(root, height=10)
output_display.pack()
output_display.config(state=tk.DISABLED)

# Start the GUI event loop
root.mainloop()
