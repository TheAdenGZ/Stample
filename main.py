from sample_finder import main
from youtubeConverter import download_song
from wavelengthAnalysis import 

name = "Bound 2"
artist = "Kanye West"

file = download_song(name, artist)

main()

for i in range(31):
    for j in range(31):
        splice_wav("Bound.wav", (i * 5), ((i + 1) * 5), "Sample.wav")
        splice_wav("Kanye West - Bound 2.wav", (j * 5), ((j + 1) * 5), "Original.wav")

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


best_similarity = 0
time1 = 0
time2 = 0