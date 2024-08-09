from sshkeyboard import listen_keyboard

def press(key):
    return {key}


listen_keyboard(
    on_press=press,
)

print(press(key))



