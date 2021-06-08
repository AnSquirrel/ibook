
# -*- coding: utf-8 -*-
#

"""iBook updata

Please click on the link：www.ibook.Support.com
check iBook the latest version

Copyright (C)2019.ibook.support.com
"""


import tkinter


def updata():
    WIDTH_HEIGHT = '450x400'
    WINDOW_POSITION = '+520+220'

    updata = tkinter.Toplevel()
    updata.title('updata')
    updata.geometry(WIDTH_HEIGHT)
    updata.geometry(WINDOW_POSITION)
    updata.resizable(False, False)
    updata.transient()
    updata.iconbitmap('./icons/apple.ico')

    background = tkinter.Label(updata, width=450, height=400, bg='dim gray')
    background.pack()

    information = tkinter.Text(updata, width=50, height=40, 
        selectbackground="dark cyan", wrap='word', font=("arial", 12))
    information.place(x=0, y=0)
    information.insert('end', __doc__)
