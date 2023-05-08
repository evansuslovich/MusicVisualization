import pygame

def playSong(song):
    # initialize pygame mixer
    pygame.mixer.init()

    # load the MP3 file
    pygame.mixer.music.load("./songs/100-bpm-drum-loop-sample-c-sharp-key.mp3")

    # play the MP3 file
    pygame.mixer.music.play()

    # wait for the song to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1)

    # clean up the pygame mixer
    pygame.mixer.quit()

