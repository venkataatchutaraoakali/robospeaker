import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()


# Function to customize voice (male/female)
def set_voice(gender='female'):
    voices = engine.getProperty('voices')   
    if gender == 'male':
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice


# Function to customize speech rate
def set_rate(rate=150):
    engine.setProperty('rate', rate)


# Function to customize volume (0.0 to 1.0)
def set_volume(volume=1.0):
    engine.setProperty('volume', volume)


if __name__ == '__main__':
    print("Welcome to Robospeaker 2.0")

    # Ask user for voice preference
    voice_choice = input("Choose voice (male/female): ").strip().lower()
    set_voice(voice_choice)

    # Set initial speech rate and volume
    set_rate(150)  # Set to 150 words per minute
    set_volume(1.0)  # Max volume by default

    while True:
        x = input("Enter what you want to speak (or type 'q' to quit): ")

        # Exit condition
        if x.lower() == "q":
            print("Goodbye!")
            engine.say("Bye bye, friend!")
            engine.runAndWait()
            break

        # Optionally adjust rate or volume
        elif x.lower().startswith('rate'):
            try:
                new_rate = int(x.split()[-1])
                set_rate(new_rate)
                print(f"Speech rate set to {new_rate} words per minute.")
            except ValueError:
                print("Invalid rate. Usage: rate <number>")
        elif x.lower().startswith('volume'):
            try:
                new_volume = float(x.split()[-1])
                if 0.0 <= new_volume <= 1.0:
                    set_volume(new_volume)
                    print(f"Volume set to {new_volume}.")
                else:
                    print("Volume must be between 0.0 and 1.0.")
            except ValueError:
                print("Invalid volume. Usage: volume <number between 0.0 and 1.0>")

        # Speak the text without threading
        else:
            engine.say(x)
            engine.runAndWait()
