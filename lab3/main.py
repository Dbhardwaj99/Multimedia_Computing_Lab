import matplotlib.pyplot as plt
import numpy as np

# Signal parameters
frequency = 5  # frequency of the sinusoidal signal in Hz
amplitude = 1  # amplitude of the signal
sampling_rate = 50  # sampling rate in Hz (Nyquist rate is 2 * frequency)

# Time array
t = np.arange(0, 1, 1 / sampling_rate)

# Sinusoidal signal
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Plot the signal
plt.plot(t, signal)
plt.title("Sinusoidal Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

# Perform FFT
fft_signal = np.fft.fft(signal)

# Frequency array
freqs = np.fft.fftfreq(len(fft_signal), 1 / sampling_rate)

# Plot the frequency spectrum
plt.plot(freqs, np.abs(fft_signal))
plt.title("Frequency Spectrum of Sinusoidal Signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.show()

# Parameters for synthetic audio
audio_frequency = 440  # Frequency of audio signal (A4 note)
audio_sampling_rate = 44100  # Common audio sampling rate in Hz
duration = 2  # duration of the audio in seconds

# Time array
t_audio = np.arange(0, duration, 1 / audio_sampling_rate)

# Audio signal (pure tone)
audio_signal = amplitude * np.sin(2 * np.pi * audio_frequency * t_audio)

# Plot the audio signal
plt.plot(
    t_audio[:1000], audio_signal[:1000]
)  # Plot only the first 1000 samples for clarity
plt.title("Synthetic Audio Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()


# Perform FFT
fft_audio_signal = np.fft.fft(audio_signal)

# Frequency array
freqs_audio = np.fft.fftfreq(len(fft_audio_signal), 1 / audio_sampling_rate)

# Plot the frequency spectrum
plt.plot(freqs_audio, np.abs(fft_audio_signal))
plt.title("Frequency Spectrum of Audio Signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.show()

# Parameters for synthetic ECG
ecg_sampling_rate = 500  # ECG sampling rate in Hz
duration_ecg = 2  # duration of the ECG signal in seconds

# Time array
t_ecg = np.arange(0, duration_ecg, 1 / ecg_sampling_rate)

# Simple synthetic ECG signal (combination of sinusoids)
ecg_signal = np.sin(2 * np.pi * 1.7 * t_ecg) + 0.5 * np.sin(2 * np.pi * 2.2 * t_ecg)

# Plot the ECG signal
plt.plot(t_ecg, ecg_signal)
plt.title("Synthetic ECG Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

# Perform FFT
fft_ecg_signal = np.fft.fft(ecg_signal)

# Frequency array
freqs_ecg = np.fft.fftfreq(len(fft_ecg_signal), 1 / ecg_sampling_rate)

# Plot the frequency spectrum
plt.plot(freqs_ecg, np.abs(fft_ecg_signal))
plt.title("Frequency Spectrum of ECG Signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.show()
