
# -*- coding: utf-8 -*-
#

file     = [" File ", 
            " New... ", 
            " Open File...", 
            " Save ",
            " Save As...", 
            " Set File Encoding to...", 
            " Close File", 
            " Page Setting...", 
            " Print...", 
            " Exit "
           ]

edit     = [" Edit ", 
            " Undo ", 
            " Redo ", 
            " Cut ", 
            " Copy ",
            " Paste ", 
            " Delete ", 
            " Find...", 
            " Find Next ", 
            " Replace ", 
            " Select All ", 
            " Date And Time"
           ]

formats  = [" Format ", 
            " Text wrap ", 
            " Fonts..."
           ]

view     = [" View ", 
            " Show Status Bar "
           ]

helpping = [" Help ", 
            " Panel background color ", 
            " About ibook ", 
            " Check for updates... "
           ]

back     = [" Light background ",
            " Dark background ",
            " Custom background... "
           ] 

code     = ["UTF-8", 
            "UTF-8 Contain BOM", 
            "UTF-16 LE", 
            "UTF-16 LE 包含BOM",
            "UTF-16 BE", 
            "UTF-16 BE 包含BOM", 
            "Western Language(windows 1252)", 
            "Western Language(ISO 8859-1)", 
            "Western Language(ISO 8859-3)", 
            "Western Language(ISO 8859-15)",
            "Western Language(Mac-roman)", 
            "DOS(CP 437)", 
            "Arabic(windows 1256)", 
            "Arabic(ISO 8859-6)", 
            "Greek(windows 1253)", 
            "Greek(ISO 8859-7)", 
            "Hexadecimal"
           ]


import tkinter
import os
import time
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox

import updata
import message
from tkinter import ttk


window = tkinter.Tk()

filename = ""


def mainWindow():
    global text

    DEFAULT_FONT = "Arial"
    DEFAULT_SIZE = 12 

    WIDTH_HEIGHT = '680x500'
    WINDOW_POSITION = '+400+150'

    FORE_GROUND = 'white'
    BACK_GROUND = "#4a4a4a"

    window.title('ibook')
    window.geometry(WIDTH_HEIGHT)
    window.geometry(WINDOW_POSITION)
    # window.attributes('-alpha', 0.9)
    window.iconbitmap('./icons/apple.ico')
    # window.geometry('800x600+400+150')

    ybar = tkinter.Scrollbar(window, orient = 'vertical')
    ybar.pack(fill = 'y', side = 'right')
    xbar = tkinter.Scrollbar(window, orient = 'horizontal')
    xbar.pack(fill = 'x', side = 'bottom')

    text = tkinter.Text(window, wrap = 'none', insertbackground = "white", 
                        selectbackground = "royal blue",
                        yscrollcommand = ybar.set, xscrollcommand = xbar.set, 
                        fg = FORE_GROUND, bg = BACK_GROUND, 
                        font = (DEFAULT_FONT, DEFAULT_SIZE), undo = True) 
    text.pack(fill = 'both', expand = 'yes')

    ybar.config(command = text.yview)
    xbar.config(command = text.xview)


class BackGround(object):
    def lightGround(self):
        text.config(foreground = "black",
                    background = "#dfdfdf",
                    insertbackground = "black",
                    selectbackground = "dark cyan")

    def darkGround(self):
        text.config(foreground = "white",
                    background = "#4a4a4a",
                    insertbackground = "white",
                    selectbackground = "royal blue")


def line():
    text.config(wrap = 'char')

    
def localTime():
    localtime = time.strftime("%Y-%m-%d %H:%M:%S \n", 
                         time.localtime())
    text.insert('end', localtime)


def font():
    WIDTH_HEIGHT = '400x290'
    WINDOW_POSITION = '+550+280'

    font = tkinter.Toplevel(window)
    font.title('Font')
    font.geometry(WIDTH_HEIGHT)
    font.geometry(WINDOW_POSITION)
    font.resizable(False, False)
    font.transient(window)
    font.iconbitmap('./icons/apple.ico')

    background = tkinter.Label(font, width = 290, height=140,
                               fg = 'white', bg = "dim gray")
    background.pack()

    face = ("Arial", "Arial Black", "Arial Narrow", 
            "Berlin Sans FB", 
            "Berlin Sans FB Demi","Consolas", 
            "Calibri", "Candara", "Century Gothic", 
            "Comic Sans MS", "Corbel", "Dotum", 
            "icomoon", "ISOCP", "Meiryo UI", 
            "Microsoft Sans Serif", "Stylus BT", 
            "Swis721 LtCn BT", "Tahoma", "Technic")

    size = (4, 5, 6, 8, 10, 12, 14, 16, 18, 20,  
            22, 24, 26, 28, 30, 32, 35, 40, 42, 
            44, 46, 48, 50, 52, 54, 56, 58, 60, 
            62)

    typeface = tkinter.StringVar(value = face)
    fontsize = tkinter.StringVar(value = size)

    fontlabel = tkinter.Label(font, text = "Selec Typeface", 
                              fg = 'white', bg = 'dim gray', 
                              font = ('Arial', 15))
    fontlabel.place(x = 38, y = 25)

    sizelabel = tkinter.Label(font, text = "Selec Font Size", 
                              fg = 'white', bg = 'dim gray', 
                              font = ('Arial', 15))
    sizelabel.place(x = 220, y = 25)

    fontbox = tkinter.Listbox(font, width = 20, height = 9, 
                              listvariable = typeface, selectmode = "browse")  
    fontbox.place(x = 45, y = 72)

    sizebox = tkinter.Listbox(font, width = 20, height = 9, 
                              listvariable = fontsize, selectmode = "browse")
    sizebox.place(x = 230, y = 72)

    ok = tkinter.Button(font, text = "Ok", width = 8, height = 1 , 
                        fg = 'white', bg = 'dim gray', command = None,
                        font = ('Arial', 8, 'bold'))
    ok.place(x = 120, y = 250)

    cancel = tkinter.Button(font, text = "Canael", width = 8, height = 1 , 
                            fg = 'white', bg = 'dim gray',
                            font = ('Arial', 8, 'bold'))
    cancel.place(x = 220, y = 250)

    def selectedFont(event):
        font = fontbox.get(fontbox.curselection())
        text.config(font = (font,))
                            
    def selectedSize(event):
        size = sizebox.get(sizebox.curselection())
        text.config(font = ("", size))      
     
    fontbox.bind('<ButtonRelease-1>', selectedFont)
    sizebox.bind('<ButtonRelease-1>', selectedSize)


class Font(object):
    def __init__(self, initface = "Arial", 
                 initsize = 10, initthick = 'bold'):
        self.initface = initface
        self.initsize = initsize
        self.initthick = initthick

    def fontFace(self, face = 'none', 
                 size = 'none', thick = 'bold'):
        face = self.initface
        size = self.initsize
        thcick = self.initthick
        return face, size, thick
    

def copyRight():
    cpoyright = tkinter.Label(window, 
        text = "Copyright ©2001-2019." +
        "Python Software Foundation" + 
        " Legal Statements  Privacy Policy" + 
        "  " +
        "Powered by Heroku",
        fg = 'gray', width = 105, 
        font = ("Arial", 9))

    cpoyright.pack(side = 'bottom')


def findDialog():
    WIDTH_HEIGHT = '450x55'
    WINDOW_POSITION = '+500+550'

    findwindow = tkinter.Toplevel(window)
    findwindow.title('ibook Find')
    findwindow.geometry(WIDTH_HEIGHT)
    findwindow.geometry(WINDOW_POSITION)
    findwindow.resizable(False, False)
    findwindow.transient(window)
    findwindow.iconbitmap('./icons/find.ico')

    character = tkinter.StringVar()
    integer = tkinter.IntVar()

    background = tkinter.Label(findwindow, width = 10, 
                               height= 5, bg = 'dim gray')
    background.place(x = 0, y = 0,)

    findlabel = tkinter.Label(findwindow, text = "Find", 
                              fg = 'light gray', bg = 'dim gray',
                              font = ('Arial', 12))
    findlabel.place(x = 0, y = 0)

    findbox = tkinter.Entry(findwindow, width = 25, 
                            textvariable = character,
                            fg = 'white', bg = 'dim gray', 
                            font = ("Arial", 16))
    findbox.grid(row = 0, column = 1)

    findbox.focus_set()

    replacelabel = tkinter.Label(findwindow, text = "Replace", 
                                 fg = 'light gray', bg = 'dim gray',
                                 font = ('Arial', 12))
    replacelabel.grid(row = 1, column = 0, stick = "e")

    replacebox = tkinter.Entry(findwindow, width = 25, 
                               fg = 'white', bg = 'dim gray', 
                               font = ("Arial", 16))
    replacebox.grid(row = 1, column = 1)

    caeswrite = tkinter.Checkbutton(findwindow, text = "", 
                                    bg = 'dim gray', variable = integer)
    caeswrite.place(x = 36, y = 2)

    findbutton = tkinter.Button(findwindow, text = "Find Now",
                                width = 9, height = 1,
                                fg = 'light gray', bg = 'dim gray',
                                command = lambda:find(character.get(), 
                                integer.get(), text, findwindow, findbox), 
                                font = ("Arial", 10))
    findbutton.grid(row = 0, column = 2)

    replacebutton = tkinter.Button(findwindow, text = " RePlace",
                                   width = 9, height = 1, 
                                   fg = 'light gray', bg = 'dim gray', 
                                   font = ("Arial", 10))
    replacebutton.grid(row = 1, column = 2)

    def finishFind():
        text.tag_remove("match", "1.0", "end")
        findwindow.destroy()

    findwindow.protocol("WM_DELETE_WINDOW", finishFind)


def find(stringvar, intvar, text, findwindow, findbox):
    text.tag_remove("match", "1.0", "end")
    count = 0
    if stringvar:
        position = "1.0"
        while True:
            position = text.search(stringvar, position, 
                                   nocase = intvar, stopindex = 'end')
            if not position: 
                break
            endposition = position + str(len(stringvar))
            text.tag_add("match", position, endposition)
            count = count + 1
            position = endposition
        text.tag_config("match", foreground = "white", background = "#ff5f57")
        findwindow.focus_set()
        findwindow.title("Search" + str(count) + "Result")


class MainMenuBar(object):
    def __init__(self, menubar = tkinter.Menu(window), 
                 configmenubar = window):
        self.menubar = menubar
        self.configmenubar = configmenubar.config(menu = self.menubar)

    def fileMenu(self):
        fileoption = tkinter.Menu(self.menubar, tearoff = 0)
        fileoption.add_command(label = file[1], accelerator = "Ctrl+N",
                               command = FileOperation.newFile,
                               font = (Font.fontFace()))

        fileoption.add_command(label = file[2], accelerator = "Ctrl+Z", 
                               command = AskDialog.openDialog, 
                               font = (Font.fontFace()))

        fileoption.add_command(label = file[3], accelerator = "Ctrl+S",
                               command = FileOperation.saveFile, 
                               font = (Font.fontFace()))

        fileoption.add_command(label = file[4], 
                                command = FileOperation.saveAsFile, 
                                font = (Font.fontFace())) 

        saveencode = tkinter.Menu(fileoption, tearoff = 0)
        saveencode.add_checkbutton(label = code[0], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[1], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[2], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[3], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[4], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[5], 
                                   font = (Font.fontFace()))
        saveencode.add_separator()
        saveencode.add_checkbutton(label = code[6], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[7], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[8], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[9], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[10], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[11], 
                                   font = (Font.fontFace()))
        saveencode.add_separator()
        saveencode.add_checkbutton(label = code[12], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[13], 
                                   font = (Font.fontFace()))
        saveencode.add_separator()
        saveencode.add_checkbutton(label = code[14], 
                                   font = (Font.fontFace()))

        saveencode.add_checkbutton(label = code[15], 
                                   font = (Font.fontFace()))
        saveencode.add_separator()
        saveencode.add_checkbutton(label = code[16], 
                                   font = (Font.fontFace()))
        
        fileoption.add_cascade(label = file[5], 
                               font = (Font.fontFace()), 
                               menu = saveencode)

        fileoption.add_command(label = file[6], 
                               command = FileOperation.closeFile, 
                               font = (Font.fontFace()))
        fileoption.add_separator()
        fileoption.add_command(label = file[7], 
                               command = message.MessageBox.printMessage, 
                               font = (Font.fontFace()))

        fileoption.add_command(label = file[8], accelerator = "Ctrl+P", 
                               command = message.MessageBox.printMessage, 
                               font = (Font.fontFace()))

        fileoption.add_separator()
        fileoption.add_command(label = file[9], 
                               command = message.MessageBox.exitMessage, 
                               font = (Font.fontFace()))

        self.menubar.add_cascade(label = file[0], menu = fileoption,  
                                 font = (Font.fontFace()))

    def editMenu(self):
        editoption = tkinter.Menu(self.menubar, tearoff = 0)
        editoption.add_command(label = edit[1], accelerator = "Ctrl+Z", 
                               command = Edit.undo, font = (Font.fontFace()))

        editoption.add_command(label = edit[2], accelerator = "Ctrl+Y", 
                               command = Edit.redo, font = (Font.fontFace()))

        editoption.add_separator()
        editoption.add_command(label = edit[3], accelerator = "Ctrl+X", 
                               command = Edit.cut, font = (Font.fontFace()))

        editoption.add_command(label = edit[4], accelerator = "Ctrl+C", 
                               command = Edit.copy, 
                               font = (Font.fontFace()))

        editoption.add_command(label = edit[5], accelerator = "Ctrl+V", 
                               command = Edit.paste, 
                               font = (Font.fontFace()))
        editoption.add_command(label = edit[6], accelerator = "Del", 
                               font = (Font.fontFace()))
        editoption.add_separator()
        editoption.add_command(label = edit[7], accelerator = "Ctrl+F",
                               command = findDialog, 
                               font = (Font.fontFace()))

        editoption.add_command(label = edit[8], accelerator = "F3", 
                               font = (Font.fontFace()))

        editoption.add_command(label = edit[9], accelerator = "Ctrl+H", 
                               command = findDialog,
                               font = (Font.fontFace()))

        editoption.add_separator()
        editoption.add_command(label = edit[10], accelerator = "Ctrl+A", 
                               command = Edit.selectAll, 
                               font = (Font.fontFace()))

        editoption.add_command(label = edit[11], accelerator = "F5", 
                               command = localTime,
                               font = (Font.fontFace()))

        self.menubar.add_cascade(label = edit[0], menu = editoption)
    
    def formatMenu(self):
        formatoption = tkinter.Menu(self.menubar, tearoff = 0)
        formatoption.add_checkbutton(label = formats[1], 
                                     command = line,
                                     font = (Font.fontFace()))
        formatoption.add_separator()
        formatoption.add_command(label = formats[2], command = font, 
                                 font = (Font.fontFace()))
        self.menubar.add_cascade(label = formats[0], menu = formatoption)

    def viewMenu(self):
        viewoption = tkinter.Menu(self.menubar, tearoff = 0)
        viewoption.add_checkbutton(label = view[1], command = copyRight, 
                                   font = (Font.fontFace()))

        self.menubar.add_cascade(label = view[0], menu = viewoption)

    def helpMenu(self):
        helpoption = tkinter.Menu(self.menubar, tearoff = 0)

        background = tkinter.Menu(helpoption, tearoff = 0)
        background.add_radiobutton(label = back[0], 
                                   command = BackGround.lightGround, 
                                   font = (Font.fontFace()))
        background.add_radiobutton(label = back[1], 
                                   command = BackGround.darkGround,
                                   font = (Font.fontFace()))
        background.add_separator()
        background.add_radiobutton(label = back[2], 
                                   command = AskDialog.colorDialog,
                                   font = (Font.fontFace()))
        helpoption.add_cascade(label = helpping[1], menu = background, 
                               font = (Font.fontFace()))

        helpoption.add_separator()
        helpoption.add_command(label = helpping[2], 
                               command = message.MessageBox.aboutIbook, 
                               font = (Font.fontFace()))
        
        helpoption.add_separator()
        helpoption.add_command(label = helpping[3], command = updata.updata, font = (Font.fontFace()))
        self.menubar.add_cascade(label = helpping[0], menu = helpoption)


class MouseRightClick(object):
    def __init__(self, rclick_menu = tkinter.Menu(window)):
        self.rclick_menu = rclick_menu
    
    def rightClick(self, event):
        rclick_options = tkinter.Menu(self.rclick_menu, tearoff = 0)
        rclick_options.add_command(label = edit[1], command = Edit.undo, 
                                   font = (Font.fontFace()))

        rclick_options.add_command(label = edit[2], command = Edit.redo, 
                                   font = (Font.fontFace()))
        rclick_options.add_separator()
        rclick_options.add_command(label = edit[3], command = Edit.cut, 
                                   font = (Font.fontFace()))

        rclick_options.add_command(label = edit[4], command = Edit.copy, 
                                   font = (Font.fontFace()))

        rclick_options.add_command(label = edit[5], command = Edit.paste, 
                                   font = (Font.fontFace()))

        rclick_options.add_command(label = edit[6], command = Edit.undo, 
                                   font = (Font.fontFace()))

        rclick_options.add_separator()
        rclick_options.add_command(label = edit[10], command = Edit.selectAll, 
                                   font = (Font.fontFace()))
        rclick_options.add_separator()

        linked_menu = tkinter.Menu(rclick_options, tearoff = 0)
        linked_menu.add_radiobutton(label = "chinese simplified", 
                                    font = (Font.fontFace()))

        linked_menu.add_radiobutton(label = "chinese Traditional", 
                                    font = (Font.fontFace()))
        linked_menu.add_separator()
        linked_menu.add_radiobutton(label = "Korean(EUC-KR)", 
                                    font = (Font.fontFace()))
        linked_menu.add_separator()
        linked_menu.add_radiobutton(label = "Japanese(CP932)", 
                                    font = (Font.fontFace()))

        linked_menu.add_radiobutton(label = "Japanese(Shift_JIS)", 
                                    font = (Font.fontFace()))

        linked_menu.add_radiobutton(label = "Japanese(EUC-JP)", 
                                    font = (Font.fontFace()))
        linked_menu.add_separator()
        linked_menu.add_radiobutton(label = "UTF-8", 
                                    font = (Font.fontFace()))

        rclick_options.add_cascade(label = "Set Encoding...   ", 
                                   font = (Font.fontFace()), 
                                   menu = linked_menu)       
        rclick_options.post(event.x_root, event.y_root)

    def responseMouse(self):
        window.bind("<Button-3>", self.rightClick)


class AskDialog(object):
    def __init__(self, askobject = tkinter.filedialog, 
                 chooseobject = tkinter.colorchooser):
        self.askobject = askobject
        self.chooseobject = chooseobject

    def openDialog(self):
        global filename
        filename = self.askobject.askopenfilename(title = 'ibook Open File',
            filetypes = [('All Files', '*'), ('Text', '*.txt'), 
                        ('Python', '*.py *.pyw'), ('Java', '*.java'),
                        ('C', '*.c *.h')])
        FileOperation.openFile(filename)

    # def saveDialog(self):
    #     savename = self.askobject.asksaveasfilename(title = 'ibook Save As', 
    #       initialdir = r'C:\ ibook',                                                       
    #        filetypes = [('All Files', '*'), ('Text', '*.txt'), 
    #                     ('Python', '*.py *.pyw'),('Java', '*.java'), 
    #                     ('C', '*.c *.h')], 
    #                     initialfile = '', 
    #                     defaultextension = '.txt') 
    #     return savename

    def saveAsDialog(self):
        global filename
        saveasname = self.askobject.asksaveasfilename(title = 'ibook Save As', 
            initialdir = r'C:\ ibook',                                                       
            filetypes = [('All Files', '*'), ('Text', '*.txt'), 
                         ('Python', '*.py *.pyw'),('Java', '*.java'), 
                         ('C', '*.c *.h')], 
                         initialfile = '', 
                         defaultextension = '.txt')
        filename = saveasname
        
    def colorDialog(self):
        color = self.chooseobject.askcolor(title = 'ibook Background Color')
        _color = color[0]
        _color = _color[0] + _color[1] + _color[2]

        if _color >= 280:
            text.config(foreground = "black", background = color[1])
        else:
            text.config(foreground = "white", background = color[1])
        

class FileOperation(object):
    def newFile(self):
        new = tkinter.messagebox.askokcancel("ibook Save File", "Save File")
        if new == True:
            filename = None
            FileOperation.saveFile()        
            text.delete('1.0', 'end')
            window.title('New File')
        else:
            text.delete('1.0', 'end')
            window.title('New File')

    def closeFile(self):
        FileOperation.saveFile()
        text.delete('1.0', 'end')
        window.title('ibook')

    def openFile(self, filename):
        _text = None
        if filename == "":
            filename = None
        else:
            with open(filename, 'r') as files:
                _text = files.read()
                files.close()
            text.insert('end', _text)
            window.title('' + os.path.basename(filename))

    def saveFile(self):
        try:
            file = open(filename, 'w')
            save = text.get(1.0, 'end')
            file.write(save)
            file.close()
        except:
            self.saveAsFile()

    def saveAsFile(self):
        AskDialog.saveAsDialog()
        file = open(filename, 'w')
        saveas = text.get(1.0, 'end')
        file.write(saveas)
        file.close()
        window.title('ibook ' + os.path.basename(filename))


class Edit(object):
    def undo(self):
        text.event_generate("<<Undo>>")

    def redo(self):
        text.event_generate("<<Redo>>")

    def copy(self):
        text.event_generate("<<Copy>>")

    def cut(self):
        text.event_generate("<<Cut>>")

    def paste(self):
        text.event_generate("<<Paste>>")

    def selectAll(self):
        text.tag_add("sel", "1.0", "end")

              
if __name__ == '__main__':
    mainWindow()
    Font = Font()
    Edit = Edit()
    BackGround = BackGround()
    MainMenuBar = MainMenuBar()
    MouseRightClick = MouseRightClick()
    AskDialog = AskDialog()
    FileOperation = FileOperation()

    MainMenuBar.fileMenu()
    MainMenuBar.editMenu()
    MainMenuBar.formatMenu()
    MainMenuBar.viewMenu()
    MainMenuBar.helpMenu()
    MouseRightClick.responseMouse()

    window.mainloop()
