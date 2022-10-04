from guizero import App, Text, PushButton

def change_message():
    message.value = "lol you thought nerd!"

app = App(title="Heaven Program")

message = Text(app, text="Welcome to Heaven!")

button = PushButton(app, text="Push me for a reward!", command=change_message)

app.display()
