from pywinauto import Application
from pywinauto import keyboard as PywinautoKeyboard
from pywinauto import mouse as PywinautoMouse
import keyboard
import pyperclip
import win32api
import time

app = Application(backend="win32").connect(class_name="AfxMDIFrame100").window(class_name="AfxMDIFrame100")

#app.Montage327701.print_control_identifiers()
#app.Last32770.print_control_identifiers()

MontageLevel1 = app.Last32770
Symbol = MontageLevel1.Edit

def MainFunction():
    MousePosition = win32api.GetCursorPos()
    PywinautoMouse.double_click(button='left', coords=MousePosition)
    PywinautoKeyboard.send_keys('^c')
    CopyText = pyperclip.paste()
    print("paste: ", CopyText)
    #MontageLevel1.set_focus()
    Symbol.set_edit_text(CopyText)
    #MontageLevel1.PywinautoKeyboard.send_keys("{ENTER}")
    Symbol.send_keystrokes("{ENTER}")

keyboard.add_hotkey('F8', MainFunction)
keyboard.wait()