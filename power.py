<<<<<<< HEAD

# -*- coding: utf-8 -*-
#

import tkinter
import message


def power():
	WIDTH_HEIGHT = '400x299'
	WINDOW_POSITION = '+550+280'
	
	power = tkinter.Toplevel(message.about)
	power.title('Power')
	power.geometry(WIDTH_HEIGHT)
	power.geometry(WINDOW_POSITION)
	power.resizable(False, False)
	power.transient(message.about)
	power.iconbitmap('./icons/apple.ico')

	background = tkinter.Label(power, width = 400, 
							   height=299, bg = 'dim gray')
	background.pack()

	title = tkinter.Label(power, text = 'ibook Support',  
						  fg = 'white', bg = 'dim gray',
						  font = ('Arial', 20, 'bold'))
	title.place(x = 100, y = 40)

	information = tkinter.Label(power, text = 
								'Designed by ibook Support'
								+"\n" + 
								'in China Power by Python'
								+ "\n" + 
								'Copyright ©2019.Python.org', 
								fg = 'light gray', bg = 'dim gray',
								font = ('Arial', 15))

	information.place(x = 65, y = 150)
 
=======

# -*- coding: utf-8 -*-
#

import tkinter
import message


def power():
	WIDTH_HEIGHT = '400x299'
	WINDOW_POSITION = '+550+280'
	
	power = tkinter.Toplevel(message.about)
	power.title('Power')
	power.geometry(WIDTH_HEIGHT)
	power.geometry(WINDOW_POSITION)
	power.resizable(False, False)
	power.transient(message.about)
	power.iconbitmap('./icons/apple.ico')

	background = tkinter.Label(power, width = 400, 
							   height=299, bg = 'dim gray')
	background.pack()

	title = tkinter.Label(power, text = 'ibook Support',  
						  fg = 'white', bg = 'dim gray',
						  font = ('Arial', 20, 'bold'))
	title.place(x = 100, y = 40)

	information = tkinter.Label(power, text = 
								'Designed by ibook Support'
								+"\n" + 
								'in China Power by Python'
								+ "\n" + 
								'Copyright ©2019.Python.org', 
								fg = 'light gray', bg = 'dim gray',
								font = ('Arial', 15))

	information.place(x = 65, y = 150)
 
>>>>>>> 5fe0f235b55c0d09829eeb8cfacbf120b7550fad
 