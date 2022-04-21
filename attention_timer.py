# Create a countdown timer that shows a pop-up message when it reaches zero
import time


def main():
    # Get the time from the user
    time = int(input('Enter the time in seconds: '))
    countdown(time)


def clear_screen():
    print('\033[H\033[J')

def red(text):
    return '\033[31m' + text + '\033[0m'

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        # Time format as f string
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    clear_screen()
    print(red('\nTime is up!'))
    time.sleep(1)
    clear_screen()
    # play alarm sound


if __name__ == '__main__':
    main()