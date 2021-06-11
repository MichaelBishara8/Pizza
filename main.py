import math
import tkinter as tk


def calculate_pressed(event):
    med_size = float(medium_entry.get())
    lrg_size = float(large_entry.get())
    med_cost = float(medium_price_entry.get())
    lrg_cost = float(large_price_entry.get())
    # calculate area
    medium_area = math.pi * med_size ** 2
    two_medium_area = medium_area * 2
    lrg_area = math.pi * lrg_size ** 2
    # results
    result_lrg = lrg_area / two_medium_area
    result_med = two_medium_area / lrg_area

    # Display values
    medium_result['text'] = "{:.2f} cm2".format(two_medium_area)
    large_result['text'] = "{:.2f} cm2".format(lrg_area)
    medium_cost_label['text'] = "{:.2f}".format(med_cost * 2)
    large_cost_label['text'] = "{:.2f}".format(lrg_cost)

    # display percentages (only for larger with reset)
    if two_medium_area > lrg_area:
        result_percentage_lrg['text'] = ""
        result_percentage_med['text'] = "{0:.2f}%".format((result_med - 1) * 100)
    else:
        result_percentage_med['text'] = ""
        result_percentage_lrg['text'] = "{0:.2f}%".format((result_lrg - 1) * 100)


def cm_to_inch(num):
    return num / 2.54


def inch_to_cm(num):
    return num * 2.54


# initialize window
window = tk.Tk()
window.title("Pizza Comparison")
# Window size is locked
window.resizable(width=False, height=False)

# set conversion radio buttons
radio_value = tk.IntVar()
radio_value.set(1)

# Medium label and entry
medium_label = tk.Label(window, text="Medium (cm): ")
medium_label.grid(row=1, column=0, pady=2)
medium_price = tk.Label(window, text="Price: ")
medium_price.grid(row=1, column=2, pady=2)

# Large label and entry
large_label = tk.Label(window, text="Large (cm): ")
large_label.grid(row=2, column=0, pady=2)
large_price_entry = tk.Entry()
large_price_entry.grid(row=2, column=3, pady=2)

# Medium price label and entry
medium_price_entry = tk.Entry()
medium_price_entry.grid(row=1, column=3, pady=2)
medium_entry = tk.Entry()
medium_entry.grid(row=1, column=1, pady=2)

# Large price label and entry
large_price = tk.Label(window, text="Price: ")
large_price.grid(row=2, column=2, pady=2)
large_entry = tk.Entry()
large_entry.grid(row=2, column=1, pady=2)

# Medium area label and result
medium_area_label = tk.Label(window, text="Area of 2 Medium: ")
medium_area_label.grid(row=5, column=0, pady=2)
medium_result = tk.Label(window, text="")
medium_result.grid(row=5, column=1, pady=2)

# Large area label and result
large_area_label = tk.Label(window, text="Area of Large: ")
large_area_label.grid(row=6, column=0, pady=2)
large_result = tk.Label(window, text="")
large_result.grid(row=6, column=1, pady=2)

# Medium cost label and result
medium_cost = tk.Label(window, text="Cost: ")
medium_cost.grid(row=5, column=2, pady=2)
medium_cost_label = tk.Label(window, text="$0.00")
medium_cost_label.grid(row=5, column=3, pady=2)

# Large cost label and result
large_cost = tk.Label(window, text="Cost: ")
large_cost.grid(row=6, column=2, pady=2)
large_cost_label = tk.Label(window, text="$0.00")
large_cost_label.grid(row=6, column=3, pady=2)

# Medium percent label and result
result_percentage_med = tk.Label(window, text="", fg='green')
result_percentage_med.grid(row=5, column=4, pady=2)

# Large percent label and result
result_percentage_lrg = tk.Label(window, text="", fg='green')
result_percentage_lrg.grid(row=6, column=4, pady=2)

# Calculate button
calculate_button = tk.Button(text="Calculate", width=10)
calculate_button.grid(row=7, column=4, pady=3)
calculate_button.bind("<Button-1>", calculate_pressed)

window.mainloop()

# todo: Add cm to inch and inch to cm conversion radio buttons
