import time
import Neopixel
from adafruit_circuitplayground import cp

#Morse Code Dictionary
MORSE_CODE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', ' ': '/',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

#Color Dictionary
COLORS = {
    "1": (255, 0, 0),    #Red
    "2": (0, 255, 0),    #Green
    "3": (0, 0, 255),    #Blue
    "4": (255, 255, 0),  #Yellow
    "5": (255, 255, 255) #White
}

def get_unit_time():
    while True:
        try:
            unit_time = float(input("Enter the unit time (0.1 - 1 second): "))
            if unit_time < 0.1:
                raise ValueError("Unit time must be at least 0.1 seconds")
            if unit_time > 1:
                raise ValueError("Unit time must be no more than 1 second")
            return unit_time
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a value between 0.1 and 1 second")


#Function to clean and convert text to Morse code
def text_to_morse(text):
    text = text.lower()  #Convert to lowercase
    morse_list = []

    for char in text:
        try:
            if char in MORSE_CODE:
                morse_list.append(MORSE_CODE[char])
            else:
                raise ValueError(f"Invalid character '{char}' in input. Only letters and spaces are allowed.")
        except ValueError as e:
            print(e)
            continue  #Skip invalid character

    if not morse_list:  #Only Invalid inputs
        raise ValueError("No valid characters are found in the input.")

    return morse_list

#Function for the user to pick LED color by numbers
def choose_color():
    print("Choose a color:")
    for key in sorted(COLORS.keys()):
        print(f"{key}: RGB{COLORS[key]}")


    while True:
        choice = input("1.RED 2.GREEN 3.BLUE, 4.YELLOW 5.WHITE:\nEnter the number for the color:")
        if choice in COLORS:
            return COLORS[choice]
        print("Invalid input. Please try again.")

#Function to blink Morse code on LEDs
def show_morse_signal(morse_code, color, unit_time):
    for symbol in morse_code:
        for char in symbol:
            if char == ".":
                cp.pixels.fill(color)  #Dot flash
                time.sleep(unit_time)
                cp.pixels.fill((0, 0, 0))
                time.sleep(unit_time)
            elif char == "-":
                cp.pixels.fill(color)  #Dash flash
                time.sleep(unit_time * 3)
                cp.pixels.fill((0, 0, 0))
                time.sleep(unit_time)

        #Space between letters
        time.sleep(unit_time * 3)

    #Space between words
    time.sleep(unit_time * 7)

#Main program
def main():
    cp.pixels.brightness = 0.1

    try:
        unit_time = get_unit_time()  #Use the new validation function
        sentence = input("Enter a sentence to convert to Morse code: ")

        morse_code = text_to_morse(sentence)
        print(f"Morse Code: {' '.join(morse_code)}")

        selected_color = choose_color()
        show_morse_signal(morse_code, selected_color, unit_time)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cp.pixels.fill((0, 0, 0))
if __name__ == "__main__":
    main()
