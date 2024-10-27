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

for i in range(31):
    for j in range(31):
        splice_wav("Bound.wav", (i * 5), ((i + 1) * 5), "Bound1.wav")
        splice_wav("Kanye West - Bound 2.wav", (j * 5), ((j + 1) * 5), "Kanye West - Bound 22.wav")

        # Load and transform both files
        sr1, mag1 = load_and_transform('Kanye West - Bound 22.wav')
        sr2, mag2 = load_and_transform('Bound1.wav')


        # Compute cross-correlation
        corr = correlate(mag1, mag2, mode='full', method='fft')
        #lags = np.arange(-len(mag2) + 1, len(mag1))

        # Find the lag with the maximum correlation
        #best_lag = lags[np.argmax(corr)]
        curr_similarity = np.max(corr)
        if curr_similarity > best_similarity:
            best_similarity = curr_similarity
            time2 = i * 5
            time1 = j * 5

print(time1)
print(time2)
