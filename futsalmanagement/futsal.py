import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import os

TEAM_FILE = "teams.txt"
BOOKING_FILE = "bookings.txt"
LOG_FILE = "futsal_log.txt"

class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player_name):
        self.players.append(player_name)

    def remove_player(self, player_name):
        if player_name in self.players:
            self.players.remove(player_name)
            return True
        return False

class Booking:
    def __init__(self, team_name, date, time_slot):
        self.team_name = team_name
        self.date = date
        self.time_slot = time_slot

class FutsalManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Futsal Management System")

        self.teams = self.load_teams()
        self.bookings = self.load_bookings()

        self.setup_ui()

    def log_action(self, message):
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{datetime.now()}: {message}\n")

    def load_teams(self):
        teams = []
        if os.path.exists(TEAM_FILE):
            with open(TEAM_FILE, "r") as file:
                for line in file:
                    team_name = line.strip()
                    if team_name:
                        teams.append(Team(team_name))
            self.log_action("Loaded teams from file.")
        else:
            print("No teams file found. A new one will be created.")
        return teams

    def save_teams(self):
        with open(TEAM_FILE, "w") as file:
            for team in self.teams:
                file.write(f"{team.name}\n")
        self.log_action(f"Saved {len(self.teams)} teams to file.")
        print(f"Saved {len(self.teams)} teams to {TEAM_FILE}")

    def load_bookings(self):
        bookings = []
        if os.path.exists(BOOKING_FILE):
            with open(BOOKING_FILE, "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        team_name, date_str, time_slot = parts
                        try:
                            date = datetime.strptime(date_str, "%Y-%m-%d")
                            bookings.append(Booking(team_name, date, time_slot))
                        except ValueError:
                            continue  # Skip invalid entries
            self.log_action("Loaded bookings from file.")
        else:
            print("No bookings file found. A new one will be created.")
        return bookings

    def save_bookings(self):
        with open(BOOKING_FILE, "w") as file:
            for booking in self.bookings:
                file.write(f"{booking.team_name},{booking.date.strftime('%Y-%m-%d')},{booking.time_slot}\n")
        self.log_action(f"Saved {len(self.bookings)} bookings to file.")
        print(f"Saved {len(self.bookings)} bookings to {BOOKING_FILE}")  

    def setup_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True)

        self.calendar_frame = tk.Frame(notebook)
        self.team_frame = tk.Frame(notebook)
        self.booking_frame = tk.Frame(notebook)

        notebook.add(self.calendar_frame, text="Calendar")
        notebook.add(self.team_frame, text="Teams")
        notebook.add(self.booking_frame, text="Bookings")

        self.setup_calendar_ui()
        self.setup_team_ui()
        self.setup_booking_ui()

        # Add Exit button at the bottom
        exit_button = tk.Button(self.root, text="Exit", command=self.exit_app, bg="red", fg="white", pady=5)
        exit_button.pack(side=tk.BOTTOM, fill=tk.X)

    def exit_app(self):
        # Save all changes before exiting
        self.save_teams()
        self.save_bookings()
        self.log_action("Application exited and all changes saved.")
        self.root.destroy()

    def setup_calendar_ui(self):
        frame = tk.Frame(self.calendar_frame, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Manage Events", font=("Arial", 16, "bold"), pady=10).pack()

        btn_add_event = tk.Button(frame, text="Add Event", command=self.add_event_ui, width=20, pady=5)
        btn_add_event.pack(pady=5)

        btn_view_events = tk.Button(frame, text="View Events", command=self.view_events_ui, width=20, pady=5)
        btn_view_events.pack(pady=5)

    def setup_team_ui(self):
        frame = tk.Frame(self.team_frame, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Manage Teams", font=("Arial", 16, "bold"), pady=10).pack()

        btn_add_team = tk.Button(frame, text="Add Team", command=self.add_team_ui, width=20, pady=5)
        btn_add_team.pack(pady=5)

        btn_view_teams = tk.Button(frame, text="View Teams", command=self.view_teams_ui, width=20, pady=5)
        btn_view_teams.pack(pady=5)

    def setup_booking_ui(self):
        frame = tk.Frame(self.booking_frame, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Manage Bookings", font=("Arial", 16, "bold"), pady=10).pack()

        btn_add_booking = tk.Button(frame, text="Add Booking", command=self.add_booking_ui, width=20, pady=5)
        btn_add_booking.pack(pady=5)

        btn_view_bookings = tk.Button(frame, text="View Bookings", command=self.view_bookings_ui, width=20, pady=5)
        btn_view_bookings.pack(pady=5)

    def add_event_ui(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Event")

        tk.Label(add_window, text="Event Title:").grid(row=0, column=0, padx=10, pady=5)
        title_entry = tk.Entry(add_window)
        title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Event Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
        date_entry = tk.Entry(add_window)
        date_entry.grid(row=1, column=1, padx=10, pady=5)

        def add_event():
            title = title_entry.get()
            date_str = date_entry.get()
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                messagebox.showinfo("Event Added", f"Event '{title}' added on {date_str}.")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")

        add_btn = tk.Button(add_window, text="Add", command=add_event)
        add_btn.grid(row=2, columnspan=2, pady=10)

    def view_events_ui(self):
        messagebox.showinfo("Upcoming Events", "(Placeholder for event viewing)")

    def add_team_ui(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Team")

        tk.Label(add_window, text="Team Name:").grid(row=0, column=0, padx=10, pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        def add_team():
            team_name = name_entry.get()
            if team_name:
                self.teams.append(Team(team_name))
                messagebox.showinfo("Team Added", f"Team '{team_name}' has been added.")
                add_window.destroy()
            else:
                messagebox.showerror("Invalid Input", "Team name cannot be empty.")

        add_btn = tk.Button(add_window, text="Add", command=add_team)
        add_btn.grid(row=1, columnspan=2, pady=10)

    def view_teams_ui(self):
        if not self.teams:
            messagebox.showinfo("No Teams", "No teams have been added.")
        else:
            team_list = "\n".join(team.name for team in self.teams)
            messagebox.showinfo("Teams", f"Teams:\n{team_list}")

    def add_booking_ui(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Booking")

        tk.Label(add_window, text="Team Name:").grid(row=0, column=0, padx=10, pady=5)
        team_entry = tk.Entry(add_window)
        team_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
        date_entry = tk.Entry(add_window)
        date_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Time Slot:").grid(row=2, column=0, padx=10, pady=5)
        time_entry = tk.Entry(add_window)
        time_entry.grid(row=2, column=1, padx=10, pady=5)

        def add_booking():
            team_name = team_entry.get()
            date_str = date_entry.get()
            time_slot = time_entry.get()
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                self.bookings.append(Booking(team_name, date, time_slot))
                messagebox.showinfo("Booking Added", f"Booking for '{team_name}' on {date_str} at {time_slot} added.")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")

        add_btn = tk.Button(add_window, text="Add", command=add_booking)
        add_btn.grid(row=3, columnspan=2, pady=10)

    def view_bookings_ui(self):
        if not self.bookings:
            messagebox.showinfo("No Bookings", "No bookings have been made.")
        else:
            booking_list = "\n".join(f"{booking.team_name} - {booking.date.strftime('%Y-%m-%d')} at {booking.time_slot}" for booking in self.bookings)
            messagebox.showinfo("Bookings", f"Bookings:\n{booking_list}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FutsalManagementApp(root)
    root.mainloop()
