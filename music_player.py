# Import the necessary libraries
import pygame  # This is the library that allows us to play music files
import os      # This library helps us to work with files and directories on your computer

# Initialize the pygame mixer
pygame.mixer.init()  # This line initializes the mixer module, which handles audio in pygame

# Initialize pygame's mixer (the part that handles sound)
pygame.mixer.init()

# Function to load and play music
def play_music(file):
    pygame.mixer.music.load(file)  # Load the file
    pygame.mixer.music.play()  # Start playing
    print(f"Now playing: {file}")


def list_songs():
    songs = [f for f in os.listdir() if f.endswith('.mp3') or f.endswith('.wav')]
    print("Available songs:")
    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song}")
    return songs


def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

def pause_music():
    pygame.mixer.music.pause()
    print("Music paused.")

def unpause_music():
    pygame.mixer.music.unpause()
    print("Music unpaused.")


def unpause_music():
    pygame.mixer.music.unpause()  # Resume playing the paused music
    print("Music unpaused.")

def stop_music():
    pygame.mixer.music.stop()  # Stop the music playback
    print("Music stopped.")

def main():
    print("Welcome to the Python Music Player!")

    while True:
        print("\nOptions:")
        print("1. List Songs")
        print("2. Play a Song")
        print("3. Pause")
        print("4. Unpause")
        print("5. Stop")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            songs = list_songs()
        elif choice == "2":
            songs = list_songs()
            song_choice = int(input("Enter the number of the song to play: ")) - 1
            if 0 <= song_choice < len(songs):
                play_music(songs[song_choice])
            else:
                print("Invalid choice. Please try again.")
        elif choice == "3":
            pause_music()
        elif choice == "4":
            unpause_music()
        elif choice == "5":
            stop_music()
        elif choice == "6":
            print("Exiting the music player.")
            stop_music()
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()

