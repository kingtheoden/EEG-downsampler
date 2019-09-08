from csv import reader
from sys import argv
from typing import List, Tuple
from fractions import Fraction
from math import floor


def main():
    if len(argv) != 2:
        raise Exception("Incorrect number of command line aruguemnts. 1 arguement, the name of the csv file is expected. {} were detected.".format(len(argv) - 1))

    file_name = argv[1]
    data_points = []

    with open(file_name) as file:
        data = reader(file, delimiter = ",")
        datalist = list(data)

        delta_t = int(datalist[-1][0]) - int(datalist[0][0]) # Total time in miliseconds
        sample_rate = int(1000 * len(datalist) // delta_t) # Sample rate in Hertz

        print("Sample rate:", str(sample_rate) + "Hz")
        downsample_rate = int(floor(float(input("Please enter a new sample rate (in Hertz): "))))
        downsample_factor = Fraction(sample_rate, downsample_rate)

        for point in datalist:
            data_points.append((int(point[0]), float(point[1])))

        # To Downsample a data set by a rational number M/l:
        # 1. Upsample the data by a factor of L.
        # 2. Downsample the data by a factor of M.

        upsampled_data = upsample(data_points, downsample_factor.denominator)
        downsampled_data = downsample(upsampled_data, downsample_factor.numerator)

        print_data(downsampled_data)
        return

# Helper Functions

# Upscales Data by an integer factor.
def upsample(original_data: List[Tuple[int, int]], upsample_factor: int) -> List[Tuple[int, int]]:
    expanded_data = expand_data(original_data, upsample_factor)
    upsampled_data = interpolate(expanded_data)
    return upsampled_data

# Expands the data_set adding zeroes in between the original points.
def expand_data(original_data: List[Tuple[int, int]], upscale_factor: int) -> List[Tuple[int, int]]:
    expanded_data = []
    for point in original_data:
        for x in range(upscale_factor):
            if x == 0:
                expanded_data.append(point)
            else:
                expanded_data.append((point[0], 0))
    return expanded_data

# Interpolates a data set by an integer factor as described in https://en.wikipedia.org/wiki/Upsampling
# This is essentially a low-pass filter.
def interpolate(original_data: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    interpolated_data = []
    smoothing_factor = 0.5

    interpolated_data.append((original_data[0][0],  smoothing_factor * original_data[0][1]))

    for i in range(1, len(original_data)):
        interpolated_data.append((original_data[i][0], interpolated_data[i-1][1] + smoothing_factor * (original_data[i][1] - interpolated_data[i-1][1])))
    return interpolated_data

# Downscales Data by an integer factor.
def downsample(original_data: List[Tuple[int, int]], downsample_factor: int) -> List[Tuple[int, int]]:
    return original_data[::downsample_factor]

def print_data(data: List[Tuple[int, int]]):
    for point in data:
        print(point[0], point[1], sep=",")

# Run it!
if __name__ == "__main__":
    main()
