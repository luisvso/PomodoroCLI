import time
from rich.progress import Progress

def Timer():
    sessions = int(input("Ho many sessions you are going to take?"))
    focus = int(input("What is your focus time?"))
    breaks = int(input("What is your break time?"))

    #The countdown function to run the time
    countdown(focus)


def countdown(f):
    with Progress() as progress:
        seconds = f * 60
        task = progress.add_task("Focusing....", total=seconds)
        for i in range(seconds):
            time.sleep(1)
            seconds-=1
            progress.update(task, advance=1)
        print("⏰ Time's up!")


def sessions_loop(s):
    ...
