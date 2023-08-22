import tkinter
from tkinter import *
from tkinter import ttk


# Font variables
# bigFont = Font(
#     family = "Helvetica",
#     size = 14,
#     weight = "bold",
#     underline = 1,
#     overstrike = 0)

def toggle_mode():
    if mode_switch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")



def enter_data():
    # Equipment Info
    equipmentName = equipment_name_entry.get()
    equipmentType = equipment_type_entry.get()
    parentEquipment = parent_equipment_combobox.get() 
    quantity = quantity_spinbox.get()
    BoilerRoomLocation = Blr_RM_Location_combobox.get()
    stockStatus = stock_status_var.get()

    print("Equipment Name: ", equipmentName, "Equipment Type: ", equipmentType)
    print("Parent Equipment: ", parentEquipment, "Quantity: ", quantity, "Boiler Room Location: ", BoilerRoomLocation)
    print("Stock Status", stockStatus)

window = tkinter.Tk()
style = ttk.Style(window)
window.tk.call("source", "forest-light.tcl")
window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")
window.title("Boiler Room Inventory App")

label = ttk.Label
label.pack

frame = tkinter.Frame(window)
frame.pack()


# Saving Equipment Information
equipment_info_frame = tkinter.LabelFrame(frame, text = "EQUIPMENT INFO", font=("Poor Richard", 14, "bold") ,labelanchor="n")
equipment_info_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

bold_font = ("Helvetica", 14, "bold")

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
quantity_spinbox = tkinter.Spinbox(equipment_info_frame, from_= 0, to = 1000)
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
Other_Stuff_frame = tkinter.LabelFrame(frame, text = "STOCK STATUS", font=("Poor Richard", 14, "bold") , labelanchor="n")
Other_Stuff_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 20)

stock_status_var = tkinter.StringVar()
In_Stock_check = tkinter.Checkbutton(Other_Stuff_frame, text = "In Stock", variable = stock_status_var, onvalue = "In Stock", offvalue = "Out of Stock")
Out_of_Stock_check = tkinter.Checkbutton(Other_Stuff_frame, text = "Out of Stock", variable = stock_status_var, onvalue = "Out of Stock", offvalue = "In Stock")
Ordered_check = tkinter.Checkbutton(Other_Stuff_frame, text = "Ordered", variable = stock_status_var, onvalue = "Ordered", offvalue = "Not Ordered")


In_Stock_check.grid(row = 1, column = 0)
Out_of_Stock_check.grid(row = 1, column = 1)
Ordered_check.grid(row = 1, column = 2)

for widget in Other_Stuff_frame.winfo_children():
    widget.grid_configure(padx = 40, pady = 5)

#Enter Data Button
button = tkinter.Button(frame, text = "Enter Data", command = enter_data)
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)

#Separator

separator = ttk.Separator(frame)
separator.grid(row = 5, column = 0, padx = 20, pady = 10, sticky = "ew") 

#Dark/Light Switch

mode_switch = ttk.Checkbutton(
    frame, text = "Dark/Light Mode", style = "Switch", command = toggle_mode)
mode_switch.grid(row = 6, column = 0, padx = 5, pady = 10, sticky = "nsew")

#Right-side frame

treeFrame = ttk.Frame(frame)
treeFrame.grid(row = 0, column = 1, pady = 10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side = "right", fill = "y")

cols = ("Equipment Name", "Equipment Type", "Subscription", "Employment")
treeview = ttk.Treeview(treeFrame, show = "headings", columns = cols, height = 13)
treeview.column("Equipment Name", width = 100)
treeview.column("Equipment Type", width = 50)

treeview.pack()
treeScroll.config(command = treeview.yview)


window.mainloop()

#24:00 Tkinter Data Entry Form Tutorial for beginners - Python GUI project


