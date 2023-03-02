import tkinter as tk
from schedule_generator import schedule_remote_days
from xlsx_writer import write_schedule_to_xlsx
import os

def update_people_selection():
    global people_selection
    try:
        num_people = int(number_entry.get())
        if num_people > 0:
            people_selection = num_people
            generate_button.config(state='normal')
            generate_button.grid(row=num_people+6, column=0, columnspan=2, pady=20)  # adjust the row for the generate button
            people_label.grid(row=5, column=0, pady=10, padx=10, sticky="w")  # adjust the row for the people label
            
            number_label.grid_forget()
            people_ok_button.grid_forget()

            # create text fields
            global people_textfields
            people_textfields = create_textfields(names[:num_people],num_people)
            
            # show mandatory day label and menu
            mandatory_day_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")
            mandatory_day_menu.grid(row=2, column=1, pady=10, padx=10, sticky="w")
        else:
            generate_button.grid_forget()
            people_label.grid_forget()
            
            # hide mandatory day label and menu
            mandatory_day_label.grid_forget()
            mandatory_day_menu.grid_forget()
    except ValueError:
        generate_button.grid_forget()
        people_label.grid_forget()
        
        # hide mandatory day label and menu
        mandatory_day_label.grid_forget()
        mandatory_day_menu.grid_forget()
        
    number_entry.delete(0, tk.END)
    number_entry.insert(0, str(people_selection))


def get_people_from_textfields(people_textfields):
    people = []
    for textfield in people_textfields:
        value = textfield.get().strip()
        if value:
            people.append(value)
    return ", ".join(people)





def generate_schedule():

    people_str = get_people_from_textfields(people_textfields)
    people = [p.strip() for p in people_str.split(",") if p.strip()]
    mandatory_day = mandatory_day_var.get()
    schedule = schedule_remote_days(people, mandatory_day)
    schedule_label.configure(text=schedule)

    # Save schedule to xlsx file
    write_schedule_to_xlsx(people, schedule)

    # Open generated Excel file
    file_path = os.path.join(os.getcwd(), "schedule.xlsx")
    os.startfile(file_path)

    # Exit application
    window.destroy()

names = ['Yosra', 'Amine', 'Zeineb', 'Fares', 'Ahmed', 'Baha', 'Kais']

def create_textfields(names, num_fields):
    textfields = []
    for i in range(num_fields):
        if i < len(names):
            tf = tk.Entry(window, font=("Arial", 16))
            tf.insert(0,names[i])
        else:
            tf = tk.Entry(window, font=("Arial", 16))
        tf.grid(row=i+5, column=1, pady=10, padx=10)
        textfields.append(tf)
    return textfields




# Create the tkinter window and widgets
window = tk.Tk()
window.attributes("-fullscreen", False)
window.title("Remote Work Schedule Generator")
window.geometry("800x600")

# Center the window on the screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

people_label = tk.Label(window, text="Enter people (separated by commas):", font=("Arial", 16))
mandatory_day_label = tk.Label(window, text="Choose mandatory day:", font=("Arial", 16))
mandatory_day_label.grid_forget()
generate_button = tk.Button(window, text="Generate Schedule", command=generate_schedule, bg="#4CAF50", fg="white", font=("Arial", 14), state="disabled")  # initially disabled
schedule_label = tk.Label(window, text="", font=("Arial", 14))


people_entry = tk.Entry(window, font=("Arial", 16))
people_ok_button = tk.Button(window, text="OK", command=update_people_selection, font=("Arial", 14))

mandatory_day_var = tk.StringVar()
mandatory_day_var.set("Thursday")
mandatory_day_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

number_label = tk.Label(window, text="Enter the number of people:", font=("Arial", 16))
number_entry = tk.Entry(window, font=("Arial", 16))

mandatory_day_menu = tk.OptionMenu(window, mandatory_day_var, *mandatory_day_options)
mandatory_day_menu.grid_forget()

# Initialize people selection
people_selection = 1


people_ok_button.grid(row=3, column=0, columnspan=2, pady=20)
people_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

people_entry.grid(row=1, column=1, pady=10, padx=10)

number_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")
number_entry.grid(row=1, column=1, pady=10, padx=10)
number_entry.insert(0,str("7"))

mandatory_day_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")
mandatory_day_menu.grid(row=2, column=1, pady=10, padx=10, sticky="w")
generate_button.grid(row=3, column=0, columnspan=2, pady=20)
schedule_label.grid(row=4, column=0, columnspan=2, pady=10)

generate_button.grid_forget()  # enable generate button
people_entry.grid_forget()
people_label.grid_forget()


window.mainloop()
