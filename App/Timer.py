import time
from rich.progress import Progress

def Timer():
    try:
        sessions = int(input("Ho many sessions you are going to take?"))
        focus = int(input("What is your focus time?"))
        breaks = int(input("What is your break time?"))

        #The countdown function to run the time
        sessions_loop(focus,breaks,sessions)
    except ValueError:
        print("This value is wrong, please insert another valid one")
    


def countdown(f):
    respond = "no"
    while respond == "no":
        respond = input("You want to start the focusing timer?")

    if(respond == "yes"):
        with Progress() as progress:
            seconds = f * 60
            task = progress.add_task("Focusing....", total=seconds)
            for i in range(seconds):
                time.sleep(0.9)
                seconds-=1
                progress.update(task, advance=1)
            print("⏰ Time's up!") 


def breaker(breaker):
    respond = "no"
    while respond == "no":
        respond = input("Start Break?")


    if respond == "yes":
        seconds = breaker * 60
        if(respond == "yes"):
            with Progress() as progress:
                task = progress.add_task("Resting....", total=seconds)
                for i in range(seconds):
                    time.sleep(0.9)
                    seconds-=1
                    progress.update(task, advance=1) 
                print("The break if over")


#Trakcs the sessions of the loop
def sessions_loop(f,b,s):
    #make a loop for every session until goes to zero
    current_session = 1
    while current_session <= s:
        #call the functions responsible for the timer
        print("Current session: " , current_session ,  "/" , s)
        countdown(f)
        breaker(b)
        current_session +=1

    print("Congrats, your focus was: ", "{:.2f}".format((f*2)/60)  , " Hours")

