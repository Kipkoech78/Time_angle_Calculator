import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import math

class AngleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Calculator")

        # UI1
        self.datetime_picker1_label = ttk.Label(root, text="Date(YYYY-MM-DD):")
        self.datetime_picker1_label.grid(row=0, column=0, padx=5, pady=5)
        self.datetime_picker1 = ttk.Entry(root)
        self.datetime_picker1.grid(row=0, column=1, padx=5, pady=5)

        self.datetime_picker2_label = ttk.Label(root, text="Time1:(HH:MM)")
        self.datetime_picker2_label.grid(row=0, column=2, padx=5, pady=5)
        self.datetime_picker2 = ttk.Entry(root)
        self.datetime_picker2.grid(row=0, column=3, padx=5, pady=5)

        

        self.datetime_picker3_label = ttk.Label(root, text="Date 2(YYYY-MM-DD):")
        self.datetime_picker3_label.grid(row=0, column=4, padx=5, pady=5)
        self.datetime_picker3 = ttk.Entry(root)
        self.datetime_picker3.grid(row=0, column=5, padx=5, pady=5)

        self.time_picker2_label = ttk.Label(root, text="Time 2:(HH:MM)")
        self.time_picker2_label.grid(row=1, column=4, padx=5, pady=5)
        self.time_picker2 = ttk.Entry(root)
        self.time_picker2.grid(row=1, column=5, padx=5, pady=5)


        self.long_label = ttk.Label(root, text="Longitude:In Deg")
        self.long_label.grid(row=1, column=0, padx=5, pady=5)
        self.long_entry = ttk.Entry(root)
        self.long_entry.grid(row=1, column=1, padx=5, pady=5)

        self.lat_label = ttk.Label(root, text="Latitude:In Deg")
        self.lat_label.grid(row=1, column=2, padx=5, pady=5)
        self.lat_entry = ttk.Entry(root)
        self.lat_entry.grid(row=1, column=3, padx=5, pady=5)

                 # Checkbox for selecting angles
        self.asc_var = tk.BooleanVar()
        self.mc_var = tk.BooleanVar()
        self.dsc_var = tk.BooleanVar()
        self.ic_var = tk.BooleanVar()

        self.asc_checkbox = ttk.Checkbutton(root, text="ASC", variable=self.asc_var)
        self.asc_checkbox.grid(row=2, column=1, padx=5, pady=5)

        self.mc_checkbox = ttk.Checkbutton(root, text="MC", variable=self.mc_var)
        self.mc_checkbox.grid(row=2, column=2, padx=5, pady=5)

        self.dsc_checkbox = ttk.Checkbutton(root, text="DSC", variable=self.dsc_var)
        self.dsc_checkbox.grid(row=2, column=3, padx=5, pady=5)

        self.ic_checkbox = ttk.Checkbutton(root, text="IC", variable=self.ic_var)
        self.ic_checkbox.grid(row=2, column=4, padx=5, pady=5)


        #          # Textbox for number of iterations
        # self.iterations_label = ttk.Label(root, text="Iterations:")
        # self.iterations_label.grid(row=3, column=0, padx=5, pady=5)
        # self.iterations_entry = ttk.Entry(root)
        # self.iterations_entry.grid(row=3, column=1, padx=5, pady=5)

        self.sqrt_label = ttk.Label(root, text="Select number for square root:")
        self.sqrt_label.grid(row=6, column=0, padx=5, pady=5)
        self.sqrt_entry = ttk.Entry(root)
        self.sqrt_entry.grid(row=6, column=1, padx=5, pady=5)

        self.fibonacci_label = ttk.Label(root, text="Fibonacci Number:")
        self.fibonacci_label.grid(row=11, column=0, padx=5, pady=5)
        self.fibonacci_entry = ttk.Entry(root)
        self.fibonacci_entry.grid(row=11, column=1, padx=5, pady=5)


         # New UI for selecting individual angles and performing operations
        self.operation_label = ttk.Label(root, text="Select operation:")
        self.operation_label.grid(row=7, column=0, padx=5, pady=5)

        self.operation_var = tk.StringVar(value="Multiply")  # Default operation
        self.multiply_radiobutton = ttk.Radiobutton(root, text="Multiply", variable=self.operation_var, value="Multiply")
        self.multiply_radiobutton.grid(row=7, column=1, padx=5, pady=5)

        self.add_radiobutton = ttk.Radiobutton(root, text="Add", variable=self.operation_var, value="Add")
        self.add_radiobutton.grid(row=7, column=2, padx=5, pady=5)

        self.angle_label = ttk.Label(root, text="Select individual angle:")
        self.angle_label.grid(row=8, column=0, padx=5, pady=5)

        self.asc_var = tk.BooleanVar()
        self.mc_var = tk.BooleanVar()
        self.dsc_var = tk.BooleanVar()
        self.ic_var = tk.BooleanVar()

        self.asc_checkbox = ttk.Checkbutton(root, text="ASC", variable=self.asc_var)
        self.asc_checkbox.grid(row=8, column=1, padx=5, pady=5)

        self.mc_checkbox = ttk.Checkbutton(root, text="MC", variable=self.mc_var)
        self.mc_checkbox.grid(row=8, column=2, padx=5, pady=5)

        self.dsc_checkbox = ttk.Checkbutton(root, text="DSC", variable=self.dsc_var)
        self.dsc_checkbox.grid(row=8, column=3, padx=5, pady=5)

        self.ic_checkbox = ttk.Checkbutton(root, text="IC", variable=self.ic_var)
        self.ic_checkbox.grid(row=8, column=4, padx=5, pady=5)

        self.input_label = ttk.Label(root, text="Enter value:")
        self.input_label.grid(row=9, column=0, padx=5, pady=5)
        self.input_entry = ttk.Entry(root)
        self.input_entry.grid(row=9, column=1, padx=5, pady=5)

        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate_operation)
        self.calculate_button.grid(row=9, column=2, padx=5, pady=5)

        self.iterations_label = ttk.Label(root, text="Iterations:")
        self.iterations_label.grid(row=13, column=3, padx=5, pady=5)
        self.iterations_entry = ttk.Entry(root)
        self.iterations_entry.grid(row=13, column=4, padx=5, pady=5)
        


        self.calculate_button1 = ttk.Button(root, text="ASC Range", command=self.calculate_asc_range)
        self.calculate_button1.grid(row=10, column=0, padx=5, pady=5)

        self.calculate_button2 = ttk.Button(root, text="ASC Dollar to Time", command=self.calculate_asc_dollar_to_time)
        self.calculate_button2.grid(row=10, column=1, padx=5, pady=5)

        self.calculate_button3 = ttk.Button(root, text="Starting Point", command=self.calculate_starting_point)
        self.calculate_button3.grid(row=10, column=2, padx=5, pady=5)

        self.calculate_button4 = ttk.Button(root, text="ASC to Fraction", command=self.calculate_asc_to_fraction)
        self.calculate_button4.grid(row=10, column=3, padx=5, pady=5)

        self.calculate_button6 = ttk.Button(root, text="Calculate ASC", command=self.calculate_asc)
        self.calculate_button6.grid(row=5, column=3, padx=5, pady=5)

        self.planets_label = ttk.Label(root, text="Planets:")
        self.planets_label.grid(row=5, column=0, padx=5, pady=5)
        self.planets_entry = ttk.Entry(root)
        self.planets_entry.grid(row=5, column=1, padx=5, pady=5)


        self.listview_label = ttk.Label(root, text="Output:Time  Angle  Long  Zodiac  Distance")
        self.listview_label.grid(row=13, column=2, padx=5, pady=5)
        self.listview = tk.Listbox(root, width=90, height=10)
        self.listview.grid(row=14, column=0, columnspan=5, padx=5, pady=5)



    def validate_date_time(self, date_str, time_str):

        try:
                datetime.strptime(date_str, "%Y-%m-%d")
                datetime.strptime(time_str, "%H:%M")
                
                return True
        except ValueError:
            return False



    def mark_planets(self,planets):
        planet_hits = {"Moon": "ASC", "Mer": "MC", "Sun": "MC", "Ven": "MC"}  # Define planet hits for ASC, MC, etc.
        marked_planets = []
        for planet in planets:
            if planet in planet_hits:
                marked_planets.append(f"{planet} hits {planet_hits[planet]}")
            
        return marked_planets
                


    def calculate_asc_range(self):
        date1 = datetime.strptime(self.datetime_picker1.get(), "%Y-%m-%d")
        date2 = datetime.strptime(self.datetime_picker3.get(), "%Y-%m-%d")
        deg1 = float(self.long_entry.get())
        deg2 = float(self.lat_entry.get())
        iterations = int(self.iterations_entry.get())   # Number of iterations

        ratio = deg2 / deg1
        sqrt_deg = deg1 ** 0.5


        current_ratio = 1
        marked_planets = self.mark_planets(["Moon", "Mer", "Sun", "Ven"])  # Define marked_planets here
        for i in range(iterations):
            deg = deg1 * current_ratio
            sqrt_deg = sqrt_deg * current_ratio
            marked_planets_str = ", ".join(marked_planets)
            self.listview.insert(tk.END, f"Iteration {i + 1}: {date1} ASC {deg:.4f}, Planets: {marked_planets_str}")
            current_ratio *= ratio
        # for i in range(iterations):
        #     deg = deg1 * current_ratio
        #     sqrt_deg = sqrt_deg * current_ratio
        #     marked_planets_str = ", ".join(mark_planets) if mark_planets else "None"
        #     self.listview.insert(tk.END, f"Iteration {i + 1}: {date1} ASC {deg:.4f}, Planets: {marked_planets_str}")
        #     current_ratio *= ratio
            # self.listview.insert(tk.END, f"Iteration {i + 1}: {date1.strftime('%Y-%m-%d')} ASC {deg:.2f}")
            # current_ratio *= ratio
    
    def calculate_asc_dollar_to_time(self):
        dollar_value = float(self.long_entry.get())  # Assuming the dollar value is entered in the Longitude field
        date1 = datetime.strptime(self.datetime_picker1.get(), "%Y-%m-%d")
        time1 = datetime.strptime(self.datetime_picker2.get(), "%H:%M")
        date2 = datetime.strptime(self.datetime_picker3.get(), "%Y-%m-%d")
        time2 = datetime.strptime(self.time_picker2.get(), "%H:%M")
    
        asc_deg = dollar_value / 360  # Assuming 1 dollar corresponds to 1 degree of ASC

        # Calculate ASC degree at Date1 Time1
        asc_time1 = date1.replace(hour=time1.hour, minute=time1.minute) + timedelta(seconds=asc_deg * 240)  # 240 seconds for every degree of ASC

         # Calculate ASC degree at Date2 Time2
        asc_time2 = date2.replace(hour=time2.hour, minute=time2.minute) + timedelta(seconds=asc_deg * 240)  # 240 seconds for every degree of ASC

        self.listview.insert(tk.END, f"ASC at {asc_deg:.2f} degrees on {date1.strftime('%Y-%m-%d')} {time1.strftime('%H:%M')}: {asc_time1.strftime('%Y-%m-%d %H:%M')}")
        self.listview.insert(tk.END, f"ASC at {asc_deg:.2f} degrees on {date2.strftime('%Y-%m-%d')} {time2.strftime('%H:%M')}: {asc_time2.strftime('%Y-%m-%d %H:%M')}")

    def calculate_starting_point(self):
         
         asc_deg = float(self.long_entry.get())  # Assuming the ASC degree value is entered in the Longitude field
         date1 = datetime.strptime(self.datetime_picker1.get(), "%Y-%m-%d")
         date2 = datetime.strptime(self.datetime_picker3.get(), "%Y-%m-%d")
         starting_point_date = date1 + timedelta(days=asc_deg / 360)  # Assuming 1 degree corresponds to 1 day
         starting_point_time = date2 + timedelta(days=asc_deg / 360)  # Assuming 1 degree corresponds to 1 day
         self.listview.insert(tk.END, f"Starting Point Date: {starting_point_date.strftime('%Y-%m-%d')} Time: {starting_point_time.strftime('%Y-%m-%d')}")


    

    def  calculate_asc_to_fraction(self):

        asc_deg = float(self.long_entry.get())  # Assuming the ASC degree value is entered in the Longitude field
        fraction_values = [1/3, 1/2, 1/8, 1/4, 1/5, 1/9]

        for fraction in fraction_values:
            fraction_result = asc_deg * fraction
            self.listview.insert(tk.END, f"ASC degree: {asc_deg:.2f} Fraction: {fraction:.2f} Result: {fraction_result:.2f}")
     
     
    def calculate_asc(self):
        # Retrieve values from entries
        sqrt_num = float(self.sqrt_entry.get())
        fibonacci_num = int(self.fibonacci_entry.get())

        # Apply square root and Fibonacci sequence
        sqrt_result = math.sqrt(sqrt_num)
        fib_sequence = self.generate_fibonacci_sequence(fibonacci_num)
        asc = sqrt_result * fib_sequence[-1]  # Multiply by the last Fibonacci number

        # Display the result
        self.listview.insert(tk.END, f"ASC: {asc:.2f}")

    def generate_fibonacci_sequence(self, n):
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


    def calculate_operation(self):
        angle_values = []
        if self.asc_var.get():
            angle_values.append("ASC")
        if self.mc_var.get():
            angle_values.append("MC")
        if self.dsc_var.get():
            angle_values.append("DSC")
        if self.ic_var.get():
            angle_values.append("IC")

        operation = self.operation_var.get()
        input_value = float(self.input_entry.get())
        iterations = int(self.iterations_entry.get())

        result = 0
        if operation == "Multiply":
            result = self.multiply(angle_values, input_value, iterations)
        elif operation == "Add":
            result = self.add(angle_values, input_value, iterations)

        self.listview.insert(tk.END, f"Result: {result:.2f}")

    def multiply(self, angle_values, input_value, iterations):
        total = 1
        for _ in range(iterations):
            for angle in angle_values:
                if angle == "ASC":
                    total *= input_value
                # Add similar cases for other angles if needed
        return total

    def add(self, angle_values, input_value, iterations):
        total = 0
        for _ in range(iterations):
            for angle in angle_values:
                if angle == "ASC":
                    total += input_value
                # Add similar cases for other angles if needed
        return total


if __name__ == "__main__":
    root = tk.Tk()
    app = AngleCalculator(root)
    root.mainloop()
