import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Boiler Room Inventory App")

frame = tkinter.Frame(window)
frame.pack()

# Saving Equipment Information
equipment_info_frame = tkinter.LabelFrame(frame, text = "Equipment Info")
equipment_info_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

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

quantity_label = tkinter.Label(equipment_info_frame, text = "Quantity")
quantity_spinbox = tkinter.Spinbox(equipment_info_frame, from_= 1, to = 1000)
quantity_label.grid(row = 2, column = 0)
quantity_spinbox.grid(row = 3, column = 0)

Blr_RM_Location_label = tkinter.Label(equipment_info_frame, text = "Blr RM Location") 
Blr_RM_Location_combobox = ttk.Combobox(equipment_info_frame, values = ["Blr RM Storage RM", "Cabinet #1", "Cabinet #2", "Cabinet #3", "Tool Cabinet", "Gage Cabinet", "Chemical Area"])
Blr_RM_Location_label.grid(row = 2, column = 1)
Blr_RM_Location_combobox.grid(row = 3, column = 1)

description_label = tkinter.Label(equipment_info_frame, text = "Part Description")
description_label.grid(row = 4, column = 0)

for widget in equipment_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)


#Checkboxes for something
Other_Stuff_frame = tkinter.LabelFrame(frame, text = "Stock Status")
Other_Stuff_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 20)


In_Stock_check = tkinter.Checkbutton(Other_Stuff_frame, text = "In Stock")
Out_of_Stock_check = tkinter.Checkbutton(Other_Stuff_frame, text = "Out of Stock")
Ordered_check = tkinter.Checkbutton(Other_Stuff_frame, text = "Ordered")


In_Stock_check.grid(row = 1, column = 0)
Out_of_Stock_check.grid(row = 1, column = 1)
Ordered_check.grid(row = 1, column = 2)

for widget in Other_Stuff_frame.winfo_children():
    widget.grid_configure(padx = 40, pady = 5)

window.mainloop()

#24:00 Tkinter Data Entry Form Tutorial for beginners - Python GUI project


