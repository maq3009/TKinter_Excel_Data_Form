import tkinter

window = tkinter.Tk()
window.title("Boiler Room Inventory App")

frame = tkinter.Frame(window)
frame.pack()

# Saving Equipment Information
equipment_info_frame = tkinter.LabelFrame(frame, text = "Equipment Info")
equipment_info_frame.grid(row = 0, column = 0)

equipment_name_label = tkinter.Label(equipment_info_frame, text = "Equipment Name")
equipment_name_label.grid(row = 0, column = 0)


window.mainloop()

