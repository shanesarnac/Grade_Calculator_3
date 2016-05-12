from tkinter import *
import Subject

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
	option_list.insert(1, "Create New Class")
	option_list.insert(2, "Load Old Class")
	option_list.insert(3, "Exit")
	option_list.pack()
	return option_list
	
def build_Button(root, message, cmd):
	selection_button = Button(root, text = message, command = cmd)
	selection_button.pack()
	
def build_Entry(root, message, r, col):
	label = Label(root, text = message)
	label.grid(row = r, column = col, sticky = 'e')
	#label.pack(side = LEFT)
	
	entry = Entry(root)
	entry.grid(row = r, column = col + 1)
	#entry.pack(side = RIGHT)
	return entry
	
def initial_option_screen():
	(selected_option, ) = option_list.curselection()
	if selected_option == 0:
		create_Subject()
	elif selected_option == 1:
		load_Subject()
	else:
		quit()
		
def add_Category(root):
	category_entry = build_Entry(root, "Category Type (i.e. Exam 1, Homework):", 3, 0)
	category_weight_entry = build_Entry(root, "Category Weight (i.e. 25 for 25%):", 4, 0)
	add_category_button = Button(root, text = "Add Category", command = add_Category)
	add_category_button.grid(row = 3, column = 2, rowspan = 2)
	
def create_Subject():
	print("Create Subjected Initiated")
	initial_frame.destroy()
	create_subject_frame = Frame(root)
	create_subject_frame.pack()
	
	name_entry = build_Entry(create_subject_frame, "Class Name:", 0, 0)
	category_entry = build_Entry(create_subject_frame, "Category Type (i.e. Exam 1, Homework):", 1, 0)
	category_weight_entry = build_Entry(create_subject_frame, "Category Weight (i.e. 25 for 25%):", 2, 0)
	add_category_button = Button(create_subject_frame, text = "Add Category", command = add_Category(create_subject_frame))
	add_category_button.grid(row = 1, column = 2, rowspan = 2)
	
	
	
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








