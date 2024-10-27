import numpy as np
from scipy.io import wavfile
from scipy.signal import correlate

best_similarity = 0
time1 = 0
time2 = 0

# Function to load a .wav file and perform Fourier Transform
def load_and_transform(filename):
    sample_rate, data = wavfile.read(filename)
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo
    fft_values = np.fft.fft(data)
    magnitude = np.abs(fft_values)
    return sample_rate, magnitude

def splice_wav(filename, start_time, end_time, output_filename):
    # Load the .wav file
    sample_rate, data = wavfile.read(filename)

    # Calculate start and end samples
    start_sample = int(start_time * sample_rate)
    end_sample = int(end_time * sample_rate)

    # Splice the data
    spliced_data = data[start_sample:end_sample]

    # Save the spliced data as a new .wav file
    wavfile.write(output_filename, sample_rate, spliced_data)


