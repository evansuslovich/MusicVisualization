from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt


def get_raw_data(sound):
    # get raw data
    return sound.get_array_of_samples()


def get_frame_rate(sound):
    # get frame rate
    return sound.frame_rate


def get_channels(sound):
    # get channels
    return sound.sample_width


def get_time(raw_data, frame_rate):
    time = []
    for i in range(len(raw_data)):
        time.append(i / frame_rate)
    return time


def show_plot(raw_data, time):
    # code from https://stackoverflow.com/questions/38797934/get-the-amplitude-data-from-an-mp3-audio-files-using-python

    # create title
    plt.title("Waveform of an mp3 file")
    # plot data
    plt.plot(time[:100000], raw_data[:100000], color="black")
    # y label
    plt.ylabel("Amplitude")
    # show plot
    plt.show()


def main():
    sound_url = './songs/100-bpm-drum-loop-sample-c-sharp-key.mp3'
    sound = AudioSegment.from_mp3(sound_url)

    show_plot(get_raw_data(sound), get_time(get_raw_data(sound), get_frame_rate(sound)))


main()
