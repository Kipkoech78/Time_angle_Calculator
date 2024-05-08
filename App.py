import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class AngleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Angle Calculator")

        # UI1
        self.datetime_picker1_label = ttk.Label(root, text="Date:")
        self.datetime_picker1_label.grid(row=0, column=0, padx=5, pady=5)
        self.datetime_picker1 = ttk.Entry(root)
        self.datetime_picker1.grid(row=0, column=1, padx=5, pady=5)

        self.datetime_picker2_label = ttk.Label(root, text="Time:")
        self.datetime_picker2_label.grid(row=0, column=2, padx=5, pady=5)
        self.datetime_picker2 = ttk.Entry(root)
        self.datetime_picker2.grid(row=0, column=3, padx=5, pady=5)

        self.time_zone_label = ttk.Label(root, text="Time Zone:")
        self.time_zone_label.grid(row=1, column=0, padx=5, pady=5)
        self.time_zone_combobox = ttk.Combobox(root)
        self.time_zone_combobox['values'] = ('GMT', 'EST', 'CST', 'PST')
        self.time_zone_combobox.grid(row=1, column=1, padx=5, pady=5)

        self.long_label = ttk.Label(root, text="Longitude:")
        self.long_label.grid(row=2, column=0, padx=5, pady=5)
        self.long_entry = ttk.Entry(root)
        self.long_entry.grid(row=2, column=1, padx=5, pady=5)

        self.lat_label = ttk.Label(root, text="Latitude:")
        self.lat_label.grid(row=2, column=2, padx=5, pady=5)
        self.lat_entry = ttk.Entry(root)
        self.lat_entry.grid(row=2, column=3, padx=5, pady=5)

        self.asc_checkbox = ttk.Checkbutton(root, text="ASC")
        self.asc_checkbox.grid(row=3, column=0, padx=5, pady=5)
        self.mc_checkbox = ttk.Checkbutton(root, text="MC")
        self.mc_checkbox.grid(row=3, column=1, padx=5, pady=5)
        self.dsc_checkbox = ttk.Checkbutton(root, text="DSC")
        self.dsc_checkbox.grid(row=3, column=2, padx=5, pady=5)
        self.ic_checkbox = ttk.Checkbutton(root, text="IC")
        self.ic_checkbox.grid(row=3, column=3, padx=5, pady=5)

        self.time_interval_label = ttk.Label(root, text="Time Interval:")
        self.time_interval_label.grid(row=4, column=0, padx=5, pady=5)
        self.time_interval_entry = ttk.Entry(root)
        self.time_interval_entry.grid(row=4, column=1, padx=5, pady=5)

        self.iteration_label = ttk.Label(root, text="Iterations:")
        self.iteration_label.grid(row=4, column=2, padx=5, pady=5)
        self.iteration_entry = ttk.Entry(root)
        self.iteration_entry.grid(row=4, column=3, padx=5, pady=5)

        self.search_deg_label = ttk.Label(root, text="Search degrees:")
        self.search_deg_label.grid(row=5, column=0, padx=5, pady=5)
        self.search_deg_entry = ttk.Entry(root)
        self.search_deg_entry.grid(row=5, column=1, padx=5, pady=5)

        self.search_time_label = ttk.Label(root, text="Search time:")
        self.search_time_label.grid(row=5, column=2, padx=5, pady=5)
        self.search_time_entry = ttk.Entry(root)
        self.search_time_entry.grid(row=5, column=3, padx=5, pady=5)

        self.listview_label = ttk.Label(root, text="Output:")
        self.listview_label.grid(row=6, column=0, padx=5, pady=5)
        self.listview = tk.Listbox(root, width=50, height=10)
        self.listview.grid(row=7, column=0, columnspan=5, padx=5, pady=5)

        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate_angles)
        self.calculate_button.grid(row=8, column=0, padx=5, pady=5)

        self.search_button = ttk.Button(root, text="Search", command=self.search_output)
        self.search_button.grid(row=8, column=1, padx=5, pady=5)

        # UI2
        self.planets_hits_label = ttk.Label(root, text="Planets hits ASC MC DSC IC")
        self.planets_hits_label.grid(row=9, column=0, padx=5, pady=5)
        self.planets_hits_button = ttk.Button(root, text="Calculate Planets Hits", command=self.calculate_planets_hits)
        self.planets_hits_button.grid(row=9, column=1, padx=5, pady=5)

        self.sqrtroot_label = ttk.Label(root, text="Sqrtroot and Time GMT for US")
        self.sqrtroot_label.grid(row=10, column=0, padx=5, pady=5)
        self.sqrtroot_button = ttk.Button(root, text="Calculate Sqrtroot and Time GMT", command=self.calculate_sqrtroot)
        self.sqrtroot_button.grid(row=10, column=1, padx=5, pady=5)

        # UI3
        self.rise_middle_set_label = ttk.Label(root, text="Rise Middle Set all planets")
        self.rise_middle_set_label.grid(row=11, column=0, padx=5, pady=5)
        self.rise_middle_set_button = ttk.Button(root, text="Calculate Rise Middle Set", command=self.calculate_rise_middle_set)
        self.rise_middle_set_button.grid(row=11, column=1, padx=5, pady=5)

        self.starting_point_label = ttk.Label(root, text="Starting Point Date and Time")
        self.starting_point_label.grid(row=12, column=0, padx=5, pady=5)
        self.starting_point_button = ttk.Button(root, text="Calculate Starting Point", command=self.calculate_starting_point)
        self.starting_point_button.grid(row=12, column=1, padx=5, pady=5)

    def calculate_asc_range(self):
        date1 = datetime.strptime(self.datetime_picker1.get(), "%Y-%m-%d")
        date2 = datetime.strptime(self.datetime_picker2.get(), "%Y-%m-%d")
        deg1 = float(self.long_entry.get())
        deg2 = float(self.lat_entry.get())
        iterations = 5  # Number of iterations

        ratio = deg2 / deg1

        current_ratio = 1
        for i in range(iterations):
            deg = deg1 * current_ratio
            self.listview.insert(tk.END, f"Iteration {i + 1}: {date1.strftime('%Y-%m-%d')} ASC {deg:.2f}")
            current_ratio *= ratio

    def calculate_asc_dollar_to_time(self):
        dollar_value = float(self.long_entry.get())  # Assuming the dollar value is entered in the Longitude field
        date1 = datetime.strptime(self.datetime_picker1.get(), "%Y-%m-%d")
        time1 = datetime.strptime(self.datetime_picker2.get(), "%H:%M")
        asc_deg = dollar_value / 360  # Assuming 1 dollar corresponds to 1 degree of ASC
        asc_time = date1.replace(hour=time1.hour, minute=time1.minute) + timedelta(seconds=asc_deg * 240)  # 240 seconds for every degree of ASC
        self.listview.insert(tk.END, f"ASC at {asc_deg:.2f} degrees: {asc_time.strftime('%Y-%m-%d %H:%M')}")
        

    def calculate_starting_point(self):
         
         asc_deg = float(self.long_entry.get())  # Assuming the ASC degree value is entered in the Longitude field
         date1 = datetime.strptime(self.datetime_picker1.get(), "%Y-%m-%d")
         date2 = datetime.strptime(self.datetime_picker2.get(), "%Y-%m-%d")
         starting_point_date = date1 + timedelta(days=asc_deg / 360)  # Assuming 1 degree corresponds to 1 day
         starting_point_time = date2 + timedelta(days=asc_deg / 360)  # Assuming 1 degree corresponds to 1 day
         self.listview.insert(tk.END, f"Starting Point Date: {starting_point_date.strftime('%Y-%m-%d')} Time: {starting_point_time.strftime('%Y-%m-%d')}")


    

    def  calculate_asc_to_fraction(self):

        asc_deg = float(self.long_entry.get())  # Assuming the ASC degree value is entered in the Longitude field
        fraction_values = [1/3, 1/2, 1/8, 1/4, 1/5, 1/9]

        for fraction in fraction_values:
            fraction_result = asc_deg * fraction
            self.listview.insert(tk.END, f"ASC degree: {asc_deg:.2f} Fraction: {fraction:.2f} Result: {fraction_result:.2f}")





    # def calculate_angles(self):
    #     date1= self.datetime_picker1.get()
    #     print("date1", date1)
    #     date2= self.datetime_picker2.get()
    #     print("date2", date2)
    #     long_entry_value = self.long_entry.get()
    #     lat_entry_value = self.lat_entry.get()
    #     deg1=float(self.long_entry.get())
    #     deg2=float(self.lat_entry.get())
    #     iterations = int(self.iteration_entry.get())

    #     if not long_entry_value or not lat_entry_value:
    #         self.listview.insert(tk.END, "Please enter a value for longitude and latitude.")
    #         return
    #     try:
    #         deg1 = float(long_entry_value)
    #         deg2 = float(lat_entry_value)
    #     except ValueError:
    #         print("Invalid numerical values for Longitude and Latitude.")
    #     return
    
    #     ratio = deg2/deg1
    #     current_ratio = 1

    #     for i in range(iterations):
    #         deg= deg1*current_ratio
    #         self.listview.insert(tk.END, f"Iteration {i + 1}: {date1} ASC {deg:.2f}")
    #         print("Inserted into Listbox.")
    #         current_ratio *= ratio

    # def search_output(self):
    #     # Placeholder function for searching output
    #     pass

    # def calculate_planets_hits(self):
    #     # Placeholder function for calculating planets hits
    #     pass

    # def calculate_sqrtroot(self):
    #     # Placeholder function for calculating sqrtroot and Time GMT
    #     pass

    # def calculate_rise_middle_set(self):
    #     # Placeholder function for calculating Rise Middle Set
    #     pass

    # def calculate_starting_point(self):
    #     # Placeholder function for calculating starting point
    #     pass

if __name__ == "__main__":
    root = tk.Tk()
    app = AngleCalculator(root)
    root.mainloop()
