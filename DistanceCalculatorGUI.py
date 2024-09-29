# SpencerP11.py
# Programmer: Andrew Spencer
# Email: aspencer22@cnm.edu
# Date: 09/26/2024
# Purpose: Create a GUI application that allows the user to input a file name and coordinates to find the closest location to the user's coordinates.
# Python Version: 3.12.5

# imports
import tkinter as tk
from tkinter import messagebox
from Library.GeoPoint import GeoPoint
from Library.GeoPointsList import GeoPointsList



class location_GUI:
    """Construct the GUI window with input fields and a button to find the closest location."""

    def __init__(self, master):
        # Create a reference to the master window
        self.master = master
        # Set the title of the window
        self.master.title("Closest Location Finder")

        # Bind the close event to the on_closing method
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Create the input fields for the user to input the file name, latitude, and longitude
        # File Name Entry Label and Entry Field
        # Create a label to display the title of the file name entry field
        self.file_name_title = tk.Label(master, text="Enter the file name that contains your coordinates:")
        self.file_name_title.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        # Create an entry field for the user to input the file name
        self.file_name_entry = tk.Entry(master, width=50)
        self.file_name_entry.grid(row=1, column=0, sticky='w', padx=10, pady=5)

        # Create a separator line for better GUI appearance
        separator = tk.Frame(master, height=2, bd=1, bg="black", relief=tk.SUNKEN)
        separator.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

        # Latitude Frame
        lat_frame = tk.Frame(master)
        lat_frame.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        # Create a label for the latitude entry field
        self.lat_title = tk.Label(lat_frame, text="Enter your latitude:    ")
        self.lat_title.grid(row=0, column=0, sticky="w")
        # Create an entry field for the user to input the latitude
        self.lat_entry = tk.Entry(lat_frame, width=20)
        self.lat_entry.grid(row=0, column=1)

        # Longitude Frame
        lon_frame = tk.Frame(master)
        lon_frame.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        # Create a label for the longitude entry field
        self.lon_title = tk.Label(lon_frame, text="Enter your longitude:")
        self.lon_title.grid(row=0, column=0, sticky="w")
        # Create an entry field for the user to input the longitude
        self.lon_entry = tk.Entry(lon_frame, width=20)
        self.lon_entry.grid(row=0, column=1)

        # Create a separator line for better GUI appearance
        separator = tk.Frame(master, height=2, bd=1, bg="black", relief=tk.SUNKEN)
        separator.grid(row=5, column=0, sticky="ew", padx=10, pady=10)

        # Create a label to display the results
        self.result_label = tk.Label(master, text="Results will display here.", height=5, width=60, justify="left")
        self.result_label.grid(row=6, column=0, padx=10, pady=5)

        # Create the button to activate the find_closest_location method to calculate the closest location to the user's provided coordinates
        self.find_button = tk.Button(master, text="Find Closest Location", command=self.find_closest_location)
        self.find_button.grid(row=7, column=0, pady=5)

        # Create a new list of GeoPoints to store the locations
        self.points_list = GeoPointsList()

    # Create a method to handle the button click event to find the closest location
    def find_closest_location(self):
        """Handle the button click event to find the closest location."""
        # Load the points from whatever file the user specifies
        # Assign a variable to the file name entry field
        file_name = self.file_name_entry.get()
        # Load the points from the file into the points list
        self.points_list.load_points_from_file(file_name)

        try:
            # Get the latitude and longitude from the entry fields
            lat = float(self.lat_entry.get())
            lon = float(self.lon_entry.get())
            # Create a GeoPoint list with the user's location
            user_point = GeoPoint(lat, lon, "User's Location")
            # Find the closest point to the user's location using the find_closest method from the GeoPointsList class that uses the Distance method from the GeoPoint class
            closest_point = self.points_list.find_closest(user_point)

            # Display the results in the result label
            if closest_point:
                result_text = f'You are closest to: {closest_point.Description}\n'
                result_text += f'Which is located at: ({closest_point.Point[0]}, {closest_point.Point[1]})'
                self.result_label.config(text=result_text)  # Update label text
            else:
                self.result_label.config(text="No points available for comparison.")  # Update label text
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid coordinates.")

    def on_closing(self):
        """Handle the window closing event."""
        messagebox.showinfo("Goodbye", "Thank you for using the Closest Location Finder!\nTo follow my programming progress, visit my GitHub page at:\nwww.github.com/trudrewski")  # Show goodbye message
        self.master.destroy()  # Destroy the window

# Example main function to run the application
def main():
    root = tk.Tk()
    app = location_GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
