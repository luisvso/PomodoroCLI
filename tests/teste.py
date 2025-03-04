from pynput import keyboard

def on_press(key):
    try:
        print(f'Key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')


# Start listener in non-blocking mode
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the program running while the listener works
while listener.running:
    pass  # Wait for listener to stop or Esc key press

