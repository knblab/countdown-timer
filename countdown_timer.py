"""
Countdown Timer Application
A modern, portable Windows desktop timer with theme switching and fullscreen support.
"""

import tkinter as tk
from tkinter import messagebox
import winsound


class CountdownTimer:
    """Main Countdown Timer Application Class"""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("800x600")
        
        # Timer state variables
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.is_running = False
        self.is_paused = False
        
        # Theme state (True = Dark mode, False = Light mode)
        self.dark_mode = True
        
        # Fullscreen state
        self.is_fullscreen = False
        self.normal_geometry = "800x600"
        
        # Always on top state
        self.always_on_top = False
        
        # Initialize UI
        self.setup_ui()
        self.apply_theme()
        
        # Bind escape key to exit fullscreen
        self.root.bind("<Escape>", lambda e: self.toggle_fullscreen() if self.is_fullscreen else None)
        
    def setup_ui(self):
        """Setup the user interface"""
        
        # Main container
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Top control panel
        self.control_frame = tk.Frame(self.main_frame)
        self.control_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=20)
        
        # Input section
        input_frame = tk.Frame(self.control_frame)
        input_frame.pack(side=tk.TOP, pady=10)
        
        tk.Label(input_frame, text="Minutes:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        self.minutes_var = tk.StringVar(value="0")
        self.minutes_entry = tk.Entry(input_frame, textvariable=self.minutes_var, 
                                      font=("Arial", 12), width=8, justify="center")
        self.minutes_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(input_frame, text="Seconds:", font=("Arial", 12)).grid(row=0, column=2, padx=5)
        self.seconds_var = tk.StringVar(value="0")
        self.seconds_entry = tk.Entry(input_frame, textvariable=self.seconds_var, 
                                      font=("Arial", 12), width=8, justify="center")
        self.seconds_entry.grid(row=0, column=3, padx=5)
        
        # Button section
        button_frame = tk.Frame(self.control_frame)
        button_frame.pack(side=tk.TOP, pady=10)
        
        self.start_btn = tk.Button(button_frame, text="Start", font=("Arial", 11, "bold"),
                                   command=self.start_timer, width=10, height=1)
        self.start_btn.grid(row=0, column=0, padx=5)
        
        self.pause_btn = tk.Button(button_frame, text="Pause", font=("Arial", 11, "bold"),
                                   command=self.pause_resume_timer, width=10, height=1,
                                   state=tk.DISABLED)
        self.pause_btn.grid(row=0, column=1, padx=5)
        
        self.reset_btn = tk.Button(button_frame, text="Reset", font=("Arial", 11, "bold"),
                                   command=self.reset_timer, width=10, height=1)
        self.reset_btn.grid(row=0, column=2, padx=5)
        
        # Display section (centered countdown)
        self.display_frame = tk.Frame(self.main_frame)
        self.display_frame.pack(fill=tk.BOTH, expand=True)
        
        self.countdown_label = tk.Label(self.display_frame, text="00:00", 
                                       font=("Arial", 120, "bold"))
        self.countdown_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Bottom control panel
        self.bottom_frame = tk.Frame(self.main_frame)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)
        
        self.theme_btn = tk.Button(self.bottom_frame, text="🌓 Toggle Theme", 
                                   font=("Arial", 10), command=self.toggle_theme,
                                   width=15, height=1)
        self.theme_btn.pack(side=tk.LEFT, padx=5)
        
        self.fullscreen_btn = tk.Button(self.bottom_frame, text="⛶ Fullscreen", 
                                       font=("Arial", 10), command=self.toggle_fullscreen,
                                       width=15, height=1)
        self.fullscreen_btn.pack(side=tk.LEFT, padx=5)
        
        self.always_on_top_btn = tk.Button(self.bottom_frame, text="📌 Always on Top", 
                                           font=("Arial", 10), command=self.toggle_always_on_top,
                                           width=15, height=1)
        self.always_on_top_btn.pack(side=tk.LEFT, padx=5)
        
    def apply_theme(self):
        """Apply the current theme to all widgets"""
        if self.dark_mode:
            bg_color = "#000000"
            fg_color = "#FFFFFF"
            entry_bg = "#1a1a1a"
            button_bg = "#333333"
            button_fg = "#FFFFFF"
        else:
            bg_color = "#FFFFFF"
            fg_color = "#000000"
            entry_bg = "#F0F0F0"
            button_bg = "#E0E0E0"
            button_fg = "#000000"
        
        # Apply to root and frames
        self.root.configure(bg=bg_color)
        self.main_frame.configure(bg=bg_color)
        self.control_frame.configure(bg=bg_color)
        self.display_frame.configure(bg=bg_color)
        self.bottom_frame.configure(bg=bg_color)
        
        # Apply to countdown label
        self.countdown_label.configure(bg=bg_color, fg=fg_color)
        
        # Apply to input labels and entries
        for widget in self.control_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(bg=bg_color)
                for child in widget.winfo_children():
                    if isinstance(child, tk.Label):
                        child.configure(bg=bg_color, fg=fg_color)
                    elif isinstance(child, tk.Entry):
                        child.configure(bg=entry_bg, fg=fg_color, 
                                      insertbackground=fg_color,
                                      disabledbackground=entry_bg,
                                      disabledforeground=fg_color)
                    elif isinstance(child, tk.Button):
                        child.configure(bg=button_bg, fg=button_fg, 
                                      activebackground=button_bg,
                                      activeforeground=button_fg)
        
        # Apply to buttons in bottom frame
        for widget in self.bottom_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=button_bg, fg=button_fg,
                               activebackground=button_bg,
                               activeforeground=button_fg)
    
    def toggle_theme(self):
        """Toggle between dark and light theme"""
        self.dark_mode = not self.dark_mode
        self.apply_theme()
    
    def toggle_fullscreen(self):
        """Toggle between fullscreen and normal mode"""
        self.is_fullscreen = not self.is_fullscreen
        
        if self.is_fullscreen:
            # Save current geometry before going fullscreen
            self.normal_geometry = self.root.geometry()
            self.root.attributes("-fullscreen", True)
            self.fullscreen_btn.config(text="⛶ Exit Fullscreen")
        else:
            self.root.attributes("-fullscreen", False)
            self.root.geometry(self.normal_geometry)
            self.fullscreen_btn.config(text="⛶ Fullscreen")
    
    def toggle_always_on_top(self):
        """Toggle always on top mode"""
        self.always_on_top = not self.always_on_top
        self.root.attributes("-topmost", self.always_on_top)
        
        if self.always_on_top:
            self.always_on_top_btn.config(text="📌 Unpin Window")
        else:
            self.always_on_top_btn.config(text="📌 Always on Top")
    
    def validate_input(self) -> bool:
        """Validate timer input"""
        try:
            minutes = int(self.minutes_var.get())
            seconds = int(self.seconds_var.get())
            
            if minutes < 0 or seconds < 0:
                messagebox.showerror("Invalid Input", "Please enter positive numbers.")
                return False
            
            if minutes == 0 and seconds == 0:
                messagebox.showerror("Invalid Input", "Please set a time greater than 0.")
                return False
            
            return True
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")
            return False
    
    def start_timer(self):
        """Start the countdown timer"""
        if self.is_running:
            return
        
        if not self.validate_input():
            return
        
        # Calculate total seconds
        minutes = int(self.minutes_var.get())
        seconds = int(self.seconds_var.get())
        self.total_seconds = minutes * 60 + seconds
        self.remaining_seconds = self.total_seconds
        
        # Update UI state
        self.is_running = True
        self.is_paused = False
        self.start_btn.config(state=tk.DISABLED)
        self.pause_btn.config(state=tk.NORMAL, text="Pause")
        self.minutes_entry.config(state=tk.DISABLED)
        self.seconds_entry.config(state=tk.DISABLED)
        
        # Start countdown using after() method (non-blocking)
        self.countdown()
    
    def countdown(self):
        """Countdown logic using Tkinter's after() method"""
        if not self.is_running or self.is_paused:
            return
        
        if self.remaining_seconds > 0:
            # Update display
            minutes = self.remaining_seconds // 60
            seconds = self.remaining_seconds % 60
            self.countdown_label.config(text=f"{minutes:02d}:{seconds:02d}")
            
            # Decrement and schedule next update
            self.remaining_seconds -= 1
            self.root.after(1000, self.countdown)
        else:
            # Timer finished
            self.countdown_label.config(text="00:00")
            self.timer_finished()
    
    def pause_resume_timer(self):
        """Pause or resume the timer"""
        if not self.is_running:
            return
        
        self.is_paused = not self.is_paused
        
        if self.is_paused:
            self.pause_btn.config(text="Resume")
        else:
            self.pause_btn.config(text="Pause")
            self.countdown()  # Resume countdown
    
    def reset_timer(self):
        """Reset the timer to initial state"""
        self.is_running = False
        self.is_paused = False
        self.remaining_seconds = 0
        
        # Update UI
        self.countdown_label.config(text="00:00")
        self.start_btn.config(state=tk.NORMAL)
        self.pause_btn.config(state=tk.DISABLED, text="Pause")
        self.minutes_entry.config(state=tk.NORMAL)
        self.seconds_entry.config(state=tk.NORMAL)
    
    def timer_finished(self):
        """Handle timer completion"""
        self.is_running = False
        self.is_paused = False
        
        # Play sound
        self.play_sound()
        
        # Update UI
        self.start_btn.config(state=tk.NORMAL)
        self.pause_btn.config(state=tk.DISABLED, text="Pause")
        self.minutes_entry.config(state=tk.NORMAL)
        self.seconds_entry.config(state=tk.NORMAL)
        
        # Show completion message
        messagebox.showinfo("Timer Complete", "Countdown finished!")
    
    def play_sound(self):
        """Play a beep sound when timer finishes"""
        try:
            # Play system beep sound (works without external files)
            winsound.Beep(1000, 500)  # 1000 Hz for 500ms
        except Exception as e:
            print(f"Could not play sound: {e}")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
