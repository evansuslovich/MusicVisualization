from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
import numpy


def get_raw_data(sound):
    # get raw data
    return sound.get_array_of_samples()


def get_channels(sound):
    # get channels
    return sound.sample_width


def get_time(raw_data, frame_rate):
    time = []
    for i in range(len(raw_data)):
        time.append(i / frame_rate)
    return time


# with time as x-axis
def show_plot(raw_data, time):
    # code from https://stackoverflow.com/questions/38797934/get-the-amplitude-data-from-an-mp3-audio-files-using-python
    # create title
    plt.title("Waveform of an mp3 file")
    # plot data
    plt.plot(time, raw_data, color="black")
    # y label
    plt.ylabel("Amplitude")
    # show plot
    plt.show()


# indexes of array as x-axis
def show_plot(raw_data):
    # code from https://stackoverflow.com/questions/38797934/get-the-amplitude-data-from-an-mp3-audio-files-using-python
    # create title
    plt.title("Waveform of an mp3 file")
    # plot data
    plt.plot(raw_data, color="black")
    # y label
    plt.ylabel("Amplitude")
    # show plot
    plt.show()


# return an array, index 0 is max, index 1 is min.
def get_max_and_min_in_raw_data(raw_data):
    result = []

    # gets the maximum and minimum values
    max_val = raw_data[0]
    min_val = raw_data[0]
    for i in range(1, len(raw_data)):
        if raw_data[i] > max_val:
            max_val = raw_data[i]
        if raw_data[i] < min_val:
            min_val = raw_data[i]

    result.append(max_val)
    result.append(min_val)

    return result


# getting the values with high amplitudes
def getting_values_between_max_value_and_buffer(raw_data, max_val, buffer_val):
    # loop through the entire array of raw data and see if it fits through buffer <= number <= max
    horizontal_cleaning = []
    for i in range(len(raw_data)):
        if buffer_val <= raw_data[i] <= max_val:
            horizontal_cleaning.append(i)

    return horizontal_cleaning

# what if the values between the high amplitudes are close to each other? Remove them if they're close .. extra noise
def removing_extra_noise_horizontally(fit_between_buffer_and_max, length_of_data):
    # loop through the indexes_of_max array and removes indexes that are close horizontally
    vertical_cleaning = []
    for i in range(0, len(fit_between_buffer_and_max) - 1):
        # are the indexes close to each other by a factor of 0.01 * len(raw_data) is this an accurate process?
        if (fit_between_buffer_and_max[i + 1] - fit_between_buffer_and_max[i]) > (length_of_data * 0.05):
            vertical_cleaning.append(fit_between_buffer_and_max[i])

    return vertical_cleaning


# finds the difference between consecutive indices
# gets average of these differences
def average_sum_of_differences(horizontal_and_vertical_cleaning):
    sum = 0
    for i in range(0, len(horizontal_and_vertical_cleaning) - 1):
        sum += horizontal_and_vertical_cleaning[i + 1] - horizontal_and_vertical_cleaning[i]

    return (sum / len(horizontal_and_vertical_cleaning))


def main():
    sound_url = './songs/100-bpm-drum-loop-sample-c-sharp-key.mp3'
    sound = AudioSegment.from_mp3(sound_url)

    raw_data = get_raw_data(sound)
    time = get_time(raw_data, sound.frame_rate)

    max_and_min_values = get_max_and_min_in_raw_data(raw_data)
    max_val = max_and_min_values[0]

    min_val = max_and_min_values[1]

    horizontal_cleaning = getting_values_between_max_value_and_buffer(raw_data, max_val, max_val * 0.95)

    horizontal_and_vertical_cleaning = removing_extra_noise_horizontaly(horizontal_cleaning, len(raw_data))

    average_sum_of_diff = average_sum_of_differences(horizontal_and_vertical_cleaning)

    bpm = (average_sum_of_diff / sound.frame_rate) * 100

    print("BPM: " + str(bpm))
    show_plot(raw_data)


main()
