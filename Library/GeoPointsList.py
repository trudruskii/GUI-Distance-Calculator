# geo_points_list.py

from tkinter import messagebox
from Library.GeoPoint import GeoPoint

class GeoPointsList:
    """Class to manage a list of GeoPoints."""

    def __init__(self):
        self.points = []

    def load_points_from_file(self, file_name):
        """Load GeoPoints from a specified file."""
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    lat, lon, description = line.strip().split(', ')
                    new_point = GeoPoint(float(lat), float(lon), description)
                    self.points.append(new_point)
        except FileNotFoundError:
            messagebox.showerror("File Error", f"Error: The file {file_name} was not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def find_closest(self, user_point):
        """Find the closest GeoPoint to the user location."""
        return min(self.points, key=lambda point: point.Distance(user_point), default=None)
