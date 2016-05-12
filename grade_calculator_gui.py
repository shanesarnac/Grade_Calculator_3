from tkinter import *

root = Tk()
root.grid()
root.title("Grade Calculator 3.0")

def build_Frame(root):
	frame = Frame(root)
	frame.pack()
	return frame
	
def build_Message(root, message_str):
	message_var = StringVar()
	message_box = Message(root, textvariable = message_var, relief = FLAT)
	message_var.set(message_str)
	message_box.pack()

def build_List(root):
	option_list = Listbox(root, selectmode = SINGLE)
	option_list.insert(1, "Add New Class")
	option_list.insert(2, "Load Old Class")
	option_list.insert(3, "Exit")
	option_list.pack()
	return option_list
	
def build_Button(root, message, cmd):
	selection_button = Button(root, text = message, command = cmd)
	selection_button.pack()
	
def initial_option_screen():
	(selected_option, ) = option_list.curselection()
	if selected_option == 0:
		create_Subject()
	elif selected_option == 1:
		load_Subject()
	else:
		quit()
	
def create_Subject():
	print("Create Subjected Initiated")
	initial_frame.destroy()
	create_subject_frame = Frame(root)
	create_subject_frame.pack()
	


def load_Subject():
	print("Load Subjected Initiated")
	initial_frame.destroy()
	

initial_frame = build_Frame(root)
opening_message = "What would you like to do?"
build_Message(initial_frame, opening_message)
option_list = build_List(initial_frame)
button_message = "Ok"
build_Button(initial_frame, button_message, initial_option_screen)



root.mainloop()






