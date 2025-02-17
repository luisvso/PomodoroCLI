def home():

    print("Pomodoro Tracker")
    print("[s]Start")
    print("[f]Finish")

    key = " "

    while key != "s" and key != "f" :
        key = input("")
        if key != "s" and key != "f":
            print("This key don't exist, please select")

    print(f"you press {key} congrats")
