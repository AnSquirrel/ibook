<<<<<<< HEAD

# -*- coding: utf-8 -*-
#

import power
import tkinter.messagebox


class MessageBox(object):
	def __init__(self, message = tkinter.messagebox):
		self.message = message

	def aboutIbook(self):       
		self.message.showinfo('About ibook', 
			'            ibook' 
			+ "\n" + "\n" + "\n" +
			'Copyright (C)2001-2019.Python.org' 
			+ "\n" + 
			'       ibook Version 1.0.0')

	def aboutIbook(self):
		global about

		WIDTH_HEIGHT = '290x140'
		WINDOW_POSITION = '+600+400'

		about = tkinter.Toplevel()
		about.title('about')
		about.geometry(WIDTH_HEIGHT)
		about.geometry(WINDOW_POSITION)
		about.resizable(False, False)
		about.transient()
		about.iconbitmap('./icons/apple.ico')

		background = tkinter.Label(about, width = 290, 
								   height=140, bg = 'dim gray')
		background.pack()

		title = tkinter.Label(about, text = 'ibook',  
							  fg = 'white', bg = 'dim gray',
							  font = ('Arial', 18, 'bold'))
		title.place(x = 115, y = 15)

		information = tkinter.Label(about, text = 'Copyright ©2019.Python.org'
									+ "\n" + 
									'ibook Version 1.0.0',  
									fg = 'light gray', bg = 'dim gray',
									font = ('Arial', 10, 'bold'))
		information.place(x = 40, y = 80)

		powerbutton = tkinter.Button(about,text = 'Power', 
									 width = 8, height = 1 ,
									 fg = 'white', bg = 'dim gray',
									 command = power.power, 
									 font = ('Arial', 8, 'bold'))

		powerbutton.place(x = 40, y = 21)

	def printMessage(self):
		self.message\
		.showerror('ibook Print', 
				   '  ' + 'Please connect a printing device' + '        ')

	def exitMessage(self):
		_exit = self.message.askokcancel('ibook Exit', 'Exit ibook')
		if _exit == True:
			quit()

MessageBox = MessageBox()
=======

# -*- coding: utf-8 -*-
#

import power
import tkinter.messagebox


class MessageBox(object):
	def __init__(self, message = tkinter.messagebox):
		self.message = message

	def aboutIbook(self):       
		self.message.showinfo('关于 ibook', 
			'            ibook' 
			+ "\n" + "\n" + "\n" +
			'Copyright (C)2001-2019.Python.org' 
			+ "\n" + 
			'       ibook Version 1.0.0')

	def aboutIbook(self):
		global about

		WIDTH_HEIGHT = '290x140'
		WINDOW_POSITION = '+600+400'

		about = tkinter.Toplevel()
		about.title('about')
		about.geometry(WIDTH_HEIGHT)
		about.geometry(WINDOW_POSITION)
		about.resizable(False, False)
		about.transient()
		about.iconbitmap('./icons/apple.ico')

		background = tkinter.Label(about, width = 290, 
								   height=140, bg = 'dim gray')
		background.pack()

		title = tkinter.Label(about, text = 'ibook',  
							  fg = 'white', bg = 'dim gray',
							  font = ('Arial', 18, 'bold'))
		title.place(x = 115, y = 15)

		information = tkinter.Label(about, text = 'Copyright ©2019.Python.org'
									+ "\n" + 
									'ibook Version 1.0.0',  
									fg = 'light gray', bg = 'dim gray',
									font = ('Arial', 10, 'bold'))
		information.place(x = 40, y = 80)

		powerbutton = tkinter.Button(about,text = 'Power', 
									 width = 8, height = 1 ,
									 fg = 'white', bg = 'dim gray',
									 command = power.power, 
									 font = ('Arial', 8, 'bold'))

		powerbutton.place(x = 40, y = 21)

	def printMessage(self):
		self.message\
		.showerror('ibook 打印', 
				   '  ' + '请连接打印设备' + '        ')

	def exitMessage(self):
		_exit = self.message.askokcancel('ibook 退出', '退出 ibook')
		if _exit == True:
			quit()

MessageBox = MessageBox()
>>>>>>> 5fe0f235b55c0d09829eeb8cfacbf120b7550fad
