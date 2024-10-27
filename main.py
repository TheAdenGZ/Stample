from sample_finder import main
from youtubeConverter import download_song
from wavelengthAnalysis import load_and_transform
from wavelengthAnalysis import splice_wav
import numpy as np
from scipy.io import wavfile
from scipy.signal import correlate
import math

best_similarity = 0 # store best similarity score
time1 = 0 # Time stamp for original track
time2 = 0 # Time stamp for sample track
name = "Bound 2"
artist = "Kanye West"

file = download_song(name, artist)

main()

for i in range(11):
    for j in range(11):
        splice_wav("Bound.wav", (i * 15), ((i + 1) * 15), "Sample.wav")
        splice_wav("Kanye West - Bound 2.wav", (j * 15), ((j + 1) * 15), "Original.wav")

        # Load and transform both files
        sr1, mag1 = load_and_transform('Original.wav')
        sr2, mag2 = load_and_transform('Sample.wav')


        # Compute cross-correlation
        corr = correlate(mag1, mag2, mode='full', method='fft')
        # lags = np.arange(-len(mag2) + 1, len(mag1))

        # Find the lag with the maximum correlation
        # best_lag = lags[np.argmax(corr)]
        curr_similarity = np.max(corr)
        if curr_similarity > best_similarity:
            best_similarity = curr_similarity
            time2 = i * 15
            time1 = j * 15

# Output 1 = "Bound 2 by Kanye West"
# Output 2 = "Bound by Ponderosa Twins Plus One"

# Convert times from seconds to mm:ss format
temp1 = ((time1 / 60) - (time1 // 60)) * 60
temp1 = math.trunc(temp1)
temp2 = ((time2 / 60) - (time2 // 60)) * 60
temp2 = math.trunc(temp2)

print("Bound 2 by Kanye West " + str((time1 // 60)) + ":" + str(temp1) + "\n") #Output 1
print("Bound by Ponderosa Twins Plus One " + str((time2 // 60)) + ":" + str(temp2) + "\n") # Output 2
