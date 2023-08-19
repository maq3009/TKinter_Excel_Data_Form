import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Boiler Room Inventory App")

frame = tkinter.Frame(window)
frame.pack()

# Saving Equipment Information
equipment_info_frame = tkinter.LabelFrame(frame, text = "Equipment Info")
equipment_info_frame.grid(row = 0, column = 0)

equipment_name_label = tkinter.Label(equipment_info_frame, text = "Equipment Name")
equipment_name_label.grid(row = 0, column = 0)
equipment_type_label = tkinter.Label(equipment_info_frame, text = "Equipment Type")
equipment_type_label.grid(row = 0, column = 1)

equipment_name_entry = tkinter.Entry(equipment_info_frame)
equipment_type_entry = tkinter.Entry(equipment_info_frame)
equipment_name_entry.grid(row = 1, column = 0)
equipment_type_entry.grid(row = 1, column = 1)

parent_equipment = tkinter.Label(equipment_info_frame, text = "Parent Equipment")
parent_equipment_combobox = ttk.Combobox(equipment_info_frame, values = ["Boiler #1", "Boiler #2", "Boiler #3", "DA Tank", "CRT", "Softeners", "Fuel Transfer Pumps", "Electrical Parts", "Mechanical Parts"])
parent_equipment.grid(row = 0, column = 2)
parent_equipment_combobox.grid(row = 1, column = 2)

window.mainloop()

