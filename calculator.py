import CocoaGUI as gui
from size_monitor import start_monitor, stop_monitor

app = gui.Window("Calculator", width=167, height=188)
scr = gui.Label(app, "UwU", x=5, y=5)

class action: # Action values
	addition = 0
	subtraction = 1
	multiplication = 2
	division = 3

class data: # Data holder
	num_1 = 0
	num_2 = 0
	action = None
	result = None
	selected_num = 1
	num_1_decimals = 1
	num_2_decimals = 1

class btn_in: # Input handles
	@staticmethod
	def in_one():
		if data.selected_num == 1:
			if type(data.num_1) == int: data.num_1 *= 10; data.num_1 += 1
			else: data.num_1 += 1/(10*data.num_1_decimals); data.num_1_decimals += 1
		else:
			if type(data.num_2) == int: data.num_2 *= 10; data.num_2 += 1
			else: data.num_2 += 1/(10*data.num_2_decimals); data.num_2_decimals += 1
		update_label()
	@staticmethod
	def in_two():
		if data.selected_num == 1:
			if type(data.num_1) == int: data.num_1 *= 10; data.num_1 += 2
			else: data.num_1 += 2/(10*data.num_1_decimals); data.num_1_decimals += 1
		else:
			if type(data.num_2) == int: data.num_2 *= 10; data.num_2 += 2
			else: data.num_2 += 2/(10*data.num_2_decimals); data.num_2_decimals += 1
		update_label()
	@staticmethod
	def in_three():
		if data.selected_num == 1:
			if type(data.num_1) == int: data.num_1 *= 10; data.num_1 += 3
			else: data.num_1 += 3/(10*data.num_1_decimals); data.num_1_decimals += 1
		else:
			if type(data.num_2) == int: data.num_2 *= 10; data.num_2 += 3
			else: data.num_2 += 3/(10*data.num_2_decimals); data.num_2_decimals += 1
		update_label()
	@staticmethod
	def in_four():
		if data.selected_num == 1:
			if type(data.num_1) == int: data.num_1 *= 10; data.num_1 += 4
			else: data.num_1 += 4/(10*data.num_1_decimals); data.num_1_decimals += 1
		else:
			if type(data.num_2) == int: data.num_2 *= 10; data.num_2 += 4
			else: data.num_2 += 4/(10*data.num_2_decimals); data.num_2_decimals += 1
		update_label()
	@staticmethod
	def in_five():
		if data.selected_num == 1:
			if type(data.num_1) == int: data.num_1 *= 10; data.num_1 += 5
			else: data.num_1 += 5/(10*data.num_1_decimals); data.num_1_decimals += 1
		else:
			if type(data.num_2) == int: data.num_2 *= 10; data.num_2 += 5
			else: data.num_2 += 5/(10*data.num_2_decimals); data.num_2_decimals += 1
		update_label()
	@staticmethod
	def in_six():
		if data.selected_num == 1:
			if type(data.num_1) == int: data.num_1 *= 10; data.num_1 += 6
			else: data.num_1 += 6/(10*data.num_1_decimals); data.num_1_decimals += 1
		else:
			if type(data.num_2) == int: data.num_2 *= 10; data.num_2 += 6
			else: data.num_2 += 6/(10*data.num_2_decimals); data.num_2_decimals += 1
		update_label()
	@staticmethod
	def in_seven():
		if data.selected_num == 1:
			if type(data.num_1) == int: data.num_1 *= 10; data.num_1 += 7
			else: data.num_1 += 7/(10*data.num_1_decimals); data.num_1_decimals += 1
		else:
			if type(data.num_2) == int: data.num_2 *= 10; data.num_2 += 7
			else: data.num_2 += 7/(10*data.num_2_decimals); data.num_2_decimals += 1
		update_label()
	@staticmethod
	def in_eight():
		if data.selected_num == 1:
			if type(data.num_1) == int: data.num_1 *= 10; data.num_1 += 8
			else: data.num_1 += 8/(10*data.num_1_decimals); data.num_1_decimals += 1
		else:
			if type(data.num_2) == int: data.num_2 *= 10; data.num_2 += 8
			else: data.num_2 += 8/(10*data.num_2_decimals); data.num_2_decimals += 1
		update_label()
	@staticmethod
	def in_nine():
		if data.selected_num == 1:
			if type(data.num_1) == int: data.num_1 *= 10; data.num_1 += 9
			else: data.num_1 += 9/(10*data.num_1_decimals); data.num_1_decimals += 1
		else:
			if type(data.num_2) == int: data.num_2 *= 10; data.num_2 += 9
			else: data.num_2 += 9/(10*data.num_2_decimals); data.num_2_decimals += 1
		update_label()
	@staticmethod
	def in_zero():
		if data.selected_num == 1:
			if type(data.num_1) == int: data.num_1 *= 10
			else: data.num_1_decimals += 1
		else:
			if type(data.num_2) == int: data.num_2 *= 10
			else: data.num_2_decimals += 1
		update_label()
	@staticmethod
	def in_equals():
		match data.action:
			case action.addition:       data.result = data.num_1 + data.num_2
			case action.subtraction:    data.result = data.num_1 - data.num_2
			case action.multiplication: data.result = data.num_1 * data.num_2
			case action.division:       data.result = data.num_1 / data.num_2
		if data.action is not None:
			data.selected_num = 1; update_label()
	@staticmethod
	def in_decimal():
		if data.selected_num == 1: data.num_1 = float(data.num_1)
		else: data.num_2 = float(data.num_2)
		update_label()
	@staticmethod
	def in_addition():       data.action = action.addition; data.selected_num = 2; update_label()
	@staticmethod
	def in_subtraction():    data.action = action.addition; data.selected_num = 2; update_label()
	@staticmethod
	def in_multiplication(): data.action = action.addition; data.selected_num = 2; update_label()
	@staticmethod
	def in_division():       data.action = action.addition; data.selected_num = 2; update_label()

def add_buttons(): # Inputs
	gui.Button(app, "7", command=btn_in.in_seven,          x=5,   y=30 )
	gui.Button(app, "8", command=btn_in.in_eight,          x=45,  y=30 )
	gui.Button(app, "9", command=btn_in.in_nine,           x=85,  y=30 )
	gui.Button(app, "+", command=btn_in.in_addition,       x=125, y=30 )
	gui.Button(app, "4", command=btn_in.in_four,           x=5,   y=70 )
	gui.Button(app, "5", command=btn_in.in_five,           x=45,  y=70 )
	gui.Button(app, "6", command=btn_in.in_six,            x=85,  y=70 )
	gui.Button(app, "-", command=btn_in.in_subtraction,    x=125, y=70 )
	gui.Button(app, "1", command=btn_in.in_one,            x=5,   y=110)
	gui.Button(app, "2", command=btn_in.in_two,            x=45,  y=110)
	gui.Button(app, "3", command=btn_in.in_nine,           x=85,  y=110)
	gui.Button(app, "*", command=btn_in.in_multiplication, x=125, y=110)
	gui.Button(app, ".", command=btn_in.in_decimal,        x=5,   y=150)
	gui.Button(app, "0", command=btn_in.in_zero,           x=45,  y=150)
	gui.Button(app, "=", command=btn_in.in_equals,         x=85,  y=150)
	gui.Button(app, "/", command=btn_in.in_division,       x=125, y=150)
#! YES i know of https://mochacinno-dev.github.io/CocoaGUI/api/label/ which has an example for
#! button alignment better than thia but im not fucking doing that

def update_label():
	text = ""
	text += str(data.num_1)
	match data.action:
		case action.addition:       text += "+"
		case action.subtraction:    text += "-"
		case action.multiplication: text += "*"
		case action.division:       text += "/"
	if data.action is not None: text += str(data.num_2)
	if data.result is not None:
		text += "="; text += str(data.result)
	scr.set(text)

add_buttons()
start_monitor([gui, app]) # start monitoring ram usage of objects
app.run()                 # start the window
stop_monitor()            # quit monitor on close
