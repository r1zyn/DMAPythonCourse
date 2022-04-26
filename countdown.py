from time import sleep

t: str = input("Enter the time in seconds: ")

try:
    t: int = int(t)
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1

    print("\nTime's up!")
    exit(0)
except ValueError:
    print("An invalid time was provided.")
    exit(1)