import random
import tkinter as tk
from tkinter import messagebox

class GCodeGame:
    def __init__(self, master):
        self.gcodes = {
            "G00": "Rapid positioning",
            "G01": "Linear interpolation",
            "G02": "Circular interpolation, clockwise",
            "G03": "Circular interpolation, counterclockwise",
            "G17": "XY plane selection",
            "G20": "Inch programming",
            "G21": "Millimeter programming",
            "G28": "Return to reference point",
            "G40": "Cutter compensation cancel",
            "G43": "Tool length compensation +",
            "G54": "Work coordinate system 1 selection",
            "M03": "Spindle on (clockwise)",
            "M05": "Spindle stop",
            "M06": "Tool change",
            "M08": "Coolant on",
            "M30": "Program end and rewind"
        }
        
        self.score = 0
        self.master = master
        master.title("G-code Learning Game")
        
        self.label = tk.Label(master, text="What does this G-code do?")
        self.label.pack(pady=10)
        
        self.gcode_display = tk.Label(master, text="", font=("Helvetica", 20))
        self.gcode_display.pack(pady=10)
        
        self.guess_entry = tk.Entry(master, width=50)
        self.guess_entry.pack(pady=10)
        
        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        
        self.score_label = tk.Label(master, text="Score: 0")
        self.score_label.pack(pady=10)
        
        self.next_question()

    def next_question(self):
        self.current_gcode, self.current_meaning = random.choice(list(self.gcodes.items()))
        self.gcode_display.config(text=self.current_gcode)
        self.guess_entry.delete(0, tk.END)

    def check_answer(self):
        guess = self.guess_entry.get().strip().lower()
        if guess == self.current_meaning.lower():
            messagebox.showinfo("Correct!", "You earned a point!")
            self.score += 1
        else:
            messagebox.showinfo("Incorrect", f"The correct answer is: {self.current_meaning}")
        
        self.score_label.config(text=f"Score: {self.score}")
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    game = GCodeGame(root)
    root.mainloop()
