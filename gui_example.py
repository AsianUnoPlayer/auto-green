from guizero import *

app = App(title="Automated Greenhouse Thingy")
on_screen_title = Text(app, text="Automated Greenhouse GUI", size=18, align="top")

water_window = Window(app, title="Water Control Setting")
water_title = Text(water_window, text="Welcome to Water Controls!", size=18, align="top")
#water_window.tk.attributes("-fullscreen", True)
water_window.hide()

light_window = Window(app, title="Light Control Setting")
light_title = Text(light_window, text="Welcome to Light Controls!", size=18, align="top")
#light_window.tk.attributes("-fullscreen", True)
light_window.hide()

data_window = Window(app, title="Data Control Setting")
data_title = Text(data_window, text="Welcome to Data Controls!", size=18, align="top")
#data_window.tk.attributes("-fullscreen", True)
data_window.hide()

#app.tk.attributes("-fullscreen", True)

def back_to_main():
    water_window.hide()
    light_window.hide()
    data_window.hide()
    app.show()

def water_thing():
    app.hide()
    water_window.show()

def light_thing():
    app.hide()
    light_window.show()

def data_thing():
    app.hide()
    data_window.show()

def exit_thing():
    app._close_window()

button_box = Box(app, align="bottom")

water_message = Text(app)
water_button = PushButton(button_box, text="Water Options", command=water_thing, width=12, height=3, align="left")
water_button.text_size = 16

light_message = Text(app)
light_button = PushButton(button_box, text="Light Options", command=light_thing, width=12, height=3, align="left")
light_button.text_size = 16

data_message = Text(app)
data_button = PushButton(button_box, text="Data Options", command=data_thing, width=12, height=3, align="left")
data_button.text_size = 16

main_button = PushButton(water_window, text="Back to Main", command=back_to_main, width=20, height=3, align="bottom")
main_button = PushButton(light_window, text="Back to Main", command=back_to_main, width=20, height=3, align="bottom")
main_button = PushButton(data_window, text="Back to Main", command=back_to_main, width=20, height=3, align="bottom")

#exit_message = Text(app)
#exit_button = PushButton(app, text="Exit Program", command=exit_thing, width=12, height=1, align="top")
#exit_button.text_size = 12

picture = Picture(app, image="cactus_copy.png", width=350, height=350, align="top")
app.display()