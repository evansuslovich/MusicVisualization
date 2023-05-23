from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
import time
import matplotlib as mpl
import numpy as np

mpl.rcParams['agg.path.chunksize'] = 100000


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
def show_plot_time(raw_data, time):
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
def show_plot_indices(raw_data):
    # code from https://stackoverflow.com/questions/38797934/get-the-amplitude-data-from-an-mp3-audio-files-using-python
    # create title
    plt.title("Waveform of an mp3 file")
    # plot data
    plt.plot(raw_data, color="black")
    # y label
    plt.ylabel("Amplitude")
    # show plot
    plt.show()


# getting the values with high amplitudes
# can we optimize this using np for speed boost?
def getting_indices_between_value_and_buffer(raw_data, val, buffer_val):
    # loop through the entire array of raw data and see if it fits through buffer <= number <= max
    horizontal_cleaning = []
    if val < 0:
        for i in range(len(raw_data)):
            if buffer_val >= raw_data[i] >= val:
                horizontal_cleaning.append(i)
    else:
        for i in range(len(raw_data)):
            if buffer_val <= raw_data[i] <= val:
                horizontal_cleaning.append(i)

    return horizontal_cleaning


# what if the values between the high amplitudes are close to each other? Remove them if they're close .. extra noise
def removing_extra_noise_horizontally(fit_between_buffer_and_max, length_of_data):
    # loop through the indexes_of_max array and removes indexes that are close horizontally
    vertical_cleaning = []
    for i in range(0, len(fit_between_buffer_and_max) - 1):
        # are the indexes close to each other by a factor of 0.01 * len(raw_data) is this an accurate process?
        if (fit_between_buffer_and_max[i + 1] - fit_between_buffer_and_max[i]) > (length_of_data * 0.055):
            vertical_cleaning.append(fit_between_buffer_and_max[i])

    return vertical_cleaning


# averaging noise using mean
def averaging_noise_with_mean(arr, length_of_raw_data):
    sub_arrays = []
    current_subarray = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < length_of_raw_data * 0.055:
            current_subarray.append(arr[i])
        else:
            sub_arrays.append(current_subarray)
            current_subarray = [arr[i]]

    return sorted(set([sum(subarray) / len(subarray) for subarray in sub_arrays]))


def averaging_noise_with_median(arr, length_of_raw_data):
    sub_arrays = []
    current_subarray = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < length_of_raw_data * 0.055:
            current_subarray.append(arr[i])
        else:
            mid_index = len(current_subarray) // 2
            if len(current_subarray) % 2 == 0:
                median = (current_subarray[mid_index - 1] + current_subarray[mid_index]) / 2
            else:
                median = current_subarray[mid_index]
            sub_arrays.append([median])
            current_subarray = [arr[i]]

    return sorted(set([sum(sub_arrays) / len(sub_arrays) for sub_arrays in sub_arrays]))


# finds the difference between consecutive indices
# gets average of these differences
def average_sum_of_differences(arr):
    sum = 0
    for i in range(0, len(arr) - 1):
        sum += arr[i + 1] - arr[i]

    return sum / len(arr)


def average_bpm(raw_data, sound, val):
    length_of_raw_data = len(raw_data)
    buffer = val * 0.95


    # print(len(raw_data))
    start = time.time()
    indices_between_value_and_buffer = getting_indices_between_value_and_buffer(raw_data, val, buffer)
    end = time.time()
    # print("indices between value and buffer: " + str(end - start))

    # print(indices_between_value_and_buffer)

    start = time.time()
    removing_extra_noise_horizontal = \
        removing_extra_noise_horizontally(indices_between_value_and_buffer, length_of_raw_data)

    # print("removing extra noise horizontally: " +  str(removing_extra_noise_horizontal))

    average_noise_max_mean = \
        averaging_noise_with_mean(indices_between_value_and_buffer, length_of_raw_data)

    # print("averaging noise max mean: " + str(average_noise_max_mean))

    average_noise_max_median = \
        averaging_noise_with_median(indices_between_value_and_buffer, length_of_raw_data)

    end = time.time()
    # print("averaging noise horizontal, mean, median: " + str(end-start))

    # print("averaging noise max median: " + str(average_noise_max_median))

    start = time.time()
    average_sum_of_diff_max_method_1 = average_sum_of_differences(removing_extra_noise_horizontal)
    average_sum_of_diff_max_method_2 = average_sum_of_differences(average_noise_max_mean)
    average_sum_of_diff_max_method_3 = average_sum_of_differences(average_noise_max_median)

    print("average sum of diff max method 1: " + str(average_sum_of_diff_max_method_1))
    print("average sum of diff max method 2: " + str(average_sum_of_diff_max_method_2))
    print("average sum of diff max method 3: " + str(average_sum_of_diff_max_method_3))
    end = time.time()
    # print("average of sum of diff max and min methods: " + str(end-start))

    bpm_max_method_1 = (average_sum_of_diff_max_method_1 / sound.frame_rate)
    bpm_max_method_2 = (average_sum_of_diff_max_method_2 / sound.frame_rate)
    bpm_max_method_3 = (average_sum_of_diff_max_method_3 / sound.frame_rate)

    print("bpm max method 1 " + str(bpm_max_method_1))
    print("bpm max method 2 " + str(bpm_max_method_2))
    print("bpm max method 3 " + str(bpm_max_method_3))

    averaging_bpm = (bpm_max_method_1 + bpm_max_method_2 + bpm_max_method_3) / 3

    print("average bpm: " + str(averaging_bpm))

    return averaging_bpm


def average_min_max_bpm(raw_data, sound, min_val, max_val):
    average_min_val_bpm = average_bpm(raw_data, sound, min_val)
    average_max_val_bpm = average_bpm(raw_data, sound, max_val)

    return (average_max_val_bpm + average_min_val_bpm) / 2

def moving_average(arr, window):
    return np.convolve(arr, np.ones(window), 'valid') / window


def main():
    sound_url = './songs/Dystopia.mp3'


    start = time.time()
    sound = AudioSegment.from_mp3(sound_url)
    end = time.time()
    print("audio segment: " + str(end-start))

    start = time.time()
    raw_data = get_raw_data(sound)
    end = time.time()
    print("raw data: " + str(end-start))

    start = time.time()
    max_val = np.max(raw_data)
    min_val = np.min(raw_data)
    end = time.time()
    print("min and max: " + str(end-start))

    start = time.time()
    average_of_min_and_max_vals_bpm = average_min_max_bpm(raw_data, sound, min_val, max_val)
    end = time.time()
    # print("average of min and max vals: " + str(end-start))

    print(average_of_min_and_max_vals_bpm)

    # show_plot_indices(raw_data)


main()
