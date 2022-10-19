from guizero import *

app = App(title="Automated Greenhouse Thingy")
on_screen_title = Text(app, text="Automated Greenhouse GUI", size=18, align="top")

water_window = Window(app, title="Water Control Setting")
water_title = Text(water_window, text="Welcome to Water Controls!", size=18, align="top")
water_window.hide()

def goto_waterControl():
    app.hide()
    water_window.show()

light_window = Window(app, title="Light Control Setting")
light_title = Text(light_window, text="Welcome to Light Controls!", size=18, align="top")
light_window.hide()

def goto_lightControl():
    app.hide()
    light_window.show()

checkTemp = PushButton(light_window, text="Check Temperature", align="left")
checkTemp.text_size = 14

data_window = Window(app, title="Data Control Setting")
data_title = Text(data_window, text="Welcome to Data Controls!", size=18, align="top")
data_window.hide()

def goto_dataControl():
    app.hide()
    data_window.show()

data_button_box = Box(data_window, align="left")

currentData = PushButton(data_button_box, text="Current Plant Database", align="top")
currentData.text_size = 14

addData = PushButton(data_button_box, text="Add new plants", align="bottom")
addData.text_size = 14

setRegion = PushButton(data_button_box, text="Set Plant Region", align="bottom")
setRegion.text_size = 14

def back_to_main():
    water_window.hide()
    light_window.hide()
    data_window.hide()
    app.show()

def exit_thing():
    app._close_window()

button_box = Box(app, align="bottom")

water_button = PushButton(button_box, text="Water Options", command=goto_waterControl, width=12, height=3, align="left")
water_button.text_size = 16

light_button = PushButton(button_box, text="Light Options", command=goto_lightControl, width=12, height=3, align="left")
light_button.text_size = 16

data_button = PushButton(button_box, text="Data Options", command=goto_dataControl, width=12, height=3, align="left")
data_button.text_size = 16

main_button = PushButton(water_window, text="Back to Main", command=back_to_main, width=20, height=3, align="bottom")
main_button = PushButton(light_window, text="Back to Main", command=back_to_main, width=20, height=3, align="bottom")
main_button = PushButton(data_window, text="Back to Main", command=back_to_main, width=20, height=3, align="bottom")

picture = Picture(app, image="cactus_copy.png", width=350, height=350, align="top")
app.display()

"""
Just some miscellaneous things

app.tk.attributes("-fullscreen", True)

exit_message = Text(app)
exit_button = PushButton(app, text="Exit Program", command=exit_thing, width=12, height=1, align="top")
exit_button.text_size = 12
"""