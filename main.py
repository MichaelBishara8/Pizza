import math
import tkinter as tk


def calculate_pressed(event):
    med_size = float(medium_entry.get())
    lrg_size = float(large_entry.get())
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

    # display percentages (only for larger with reset)
    if two_medium_area > lrg_area:
        result_perc_lrg['text'] = ""
        result_perc_med['text'] = "{0:.2f}%".format((result_med - 1) * 100)
    else:
        result_perc_med['text'] = ""
        result_perc_lrg['text'] = "{0:.2f}%".format((result_lrg - 1) * 100)


# initialize window
window = tk.Tk()
window.title("Pizza Comparison")

# set conversion radio buttons
radio_value = tk.IntVar()
radio_value.set(1)

medium_label = tk.Label(window, text="Medium (cm): ")
medium_label.grid(row=1, column=0, pady=2)

large_label = tk.Label(window, text="Large (cm): ")
large_label.grid(row=2, column=0, pady=2)

medium_entry = tk.Entry()
medium_entry.grid(row=1, column=1, pady=3)

large_entry = tk.Entry()
large_entry.grid(row=2, column=1, pady=3)

medium_area_label = tk.Label(window, text="Area of 2 Medium: ")
medium_area_label.grid(row=5, column=0, pady=2)

large_area_label = tk.Label(window, text="Area of Large: ")
large_area_label.grid(row=6, column=0, pady=2)

medium_result = tk.Label(window, text="")
medium_result.grid(row=5, column=1, pady=2)

large_result = tk.Label(window, text="")
large_result.grid(row=6, column=1, pady=2)

result_perc_med = tk.Label(window, text="", fg='green')
result_perc_med.grid(row=5, column=2, pady=2)

result_perc_lrg = tk.Label(window, text="", fg='green')
result_perc_lrg.grid(row=6, column=2, pady=2)

calculate_button = tk.Button(text="Calculate", width=10)
calculate_button.grid(row=7, column=3, pady=3)
calculate_button.bind("<Button-1>", calculate_pressed)

window.mainloop()
