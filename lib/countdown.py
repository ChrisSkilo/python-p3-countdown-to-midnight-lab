# your code goes here!
import time

def countdown(number=5):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number=5):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")

# # Example usage:
# countdown(5)  # Countdown from 5 to 1
# countdown_with_sleep(5)  # Countdown from 5 to 1 with pauses