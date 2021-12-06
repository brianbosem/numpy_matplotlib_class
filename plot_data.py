import numpy as np
import matplotlib.pyplot as plt


def input_data(filename):
    with open(filename, 'r') as in_file:
        in_lines = in_file.readlines()
    return in_lines

def parse_data(in_line):
    list_no_return = in_line.strip("\n")
    list_split = list_no_return.split(",")
    list_int = [int(x) for x in list_split]
    return list_int

def parse_data_sin_cos(in_line):
    list_no_return = in_line.strip("\n")
    list_split = list_no_return.split(",")
    list_float = [float(x) for x in list_split]
    return list_float

def plot_single_trace(in_data):
    time = np.arange(0, len(in_data), 1)
    plt.plot(time, in_data)
    plt.show()

def plot_multiple_windows(data_0, data_1, data_2):
    time = np.arange(0, len(data_0), 1)
    plt.figure(1)
    plt.plot(time, data_0)
    plt.ylabel("Pulse Oximetry")
    plt.figure(2)
    plt.plot(time, data_1)
    plt.ylabel("Blood Pressure")
    plt.figure(3)
    plt.plot(time, data_2)
    plt.ylabel("ECG")
    plt.show()

def plot_three_in_same_window(data_0, data_1, data_2):
    time = np.arange(0, len(data_0), 1)
    plt.subplot(3,1,1)
    plt.plot(time, data_0)
    plt.ylabel("Pulse Oximetry")
    plt.subplot(3,1,2)
    plt.plot(time, data_1)
    plt.ylabel("Blood Pressure")
    plt.subplot(3,1,3)
    plt.plot(time, data_2)
    plt.ylabel("ECG")
    plt.show()

def plot_together(data_0, data_1, data_2):
    time = np.arange(0, len(data_0), 1)
    plt.plot(time, data_0)
    plt.plot(time, data_1)
    plt.plot(time, data_2)
    plt.legend(["O2", "BP", "ECG"])
    plt.show()

def plot_sin_cos(data_0, data_1):
    time = np.arange(0, 10, 0.1)
    amp_cos = 2
    freq_cos = 3
    amp_sin = 1
    freq_sin = 2
    y = amp_cos * np.cos(freq_cos * time)
    x = amp_sin * np.sin(freq_sin * time)
    my_wave = x + y
    plt.plot(data_0, data_1)
    plt.plot(time, my_wave)
    plt.legend(["Your Wave", "My Wave"])
    plt.show()

def class_main():
    in_data = input_data("curve_to_match.dat")
    data_0 = parse_data_sin_cos(in_data[0])
    data_1 = parse_data_sin_cos(in_data[1])
    plot_sin_cos(data_0, data_1) 

def main():
    in_data = input_data("overall_data.dat")
    data_0 = parse_data(in_data[0])
    data_1 = parse_data(in_data[1])
    data_2 = parse_data(in_data[2])
    # plot_single_trace(data_0)
    # plot_single_trace(data_1)
    # plot_single_trace(data_2)
    # plot_multiple_windows(data_0, data_1, data_2)
    # plot_three_in_same_window(data_0, data_1, data_2)
    plot_together(data_0, data_1, data_2)

if __name__ == "__main__":
    # main()
    class_main()