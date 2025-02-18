from App import Timer
from rich import print


def home():

    key = " "

    while key != "f":
        print("[bold magenta]Pomodoro Tracker")
        print("( s ) [green]Start")
        print("( f ) [red]Finish")
        print("Current Streak [bold magenta]13")
        print("Longest Streak [blue]14")

        key = input("")

        if key != "s" and key != "f":
            print("This key don't exist, please select")
        elif key == "s":
            Timer.Timer()


    print(f"you press {key} congrats")

