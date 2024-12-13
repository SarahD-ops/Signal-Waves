import numpy as np
import matplotlib.pyplot as plt

# Define parameters
T = 1  # Period of the signal (seconds)
f0 = 1  # Frequency of the signal (Hz)
omega_0 = 2 * np.pi * f0  # Fundamental angular frequency
t = np.linspace(0, T, 1000)  # Time points for one period
num_terms = 10  # Number of terms in Fourier series

# Define a sample signal (e.g., a square wave or sawtooth wave)
def signal(t):
    return np.sign(np.sin(2 * np.pi * f0 * t))  # Example: square wave

# Fourier series reconstruction
def fourier_series(t, num_terms):
    a_0 = np.mean(signal(t))  # Average or DC component
    result = a_0  # Start with the DC component
    
    # Calculate Fourier coefficients (up to num_terms)
    for n in range(1, num_terms + 1):
        a_n = (2 / T) * np.trapz(signal(t) * np.cos(n * omega_0 * t), t)
        b_n = (2 / T) * np.trapz(signal(t) * np.sin(n * omega_0 * t), t)
        result += a_n * np.cos(n * omega_0 * t) + b_n * np.sin(n * omega_0 * t)
    
    return result

# Generate the original and reconstructed signals
original_signal = signal(t)
reconstructed_signal = fourier_series(t, num_terms)

# Plot the results
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, original_signal, label="Original Signal", color='blue')
plt.title("Original Signal")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, reconstructed_signal, label="Reconstructed Signal (Fourier Series)", color='red')
plt.title("Reconstructed Signal Using Fourier Series")
plt.grid()

plt.tight_layout()
plt.show()
