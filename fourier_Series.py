import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the Fourier series representation
def fourier_series(signal_type, T, N, f0, t):
    """ Returns the Fourier series approximation of a given signal.
    
    Parameters:
        signal_type (str): The type of the signal ('sine', 'square', 'triangle').
        T (float): The period of the signal.
        N (int): The number of Fourier series terms to approximate.
        f0 (float): The fundamental frequency of the signal.
        t (array): Time values at which to evaluate the Fourier series.

    Returns:
        approx_signal (array): Fourier series approximation of the signal.
    """
    approx_signal = np.zeros_like(t)
    for n in range(1, N+1):
        if signal_type == 'sine':
            # Fourier series for a sine wave
            approx_signal += (2 / np.pi) * np.sin(2 * np.pi * n * f0 * t) / n
        elif signal_type == 'square':
            # Fourier series for a square wave
            if n % 2 == 1:
                approx_signal += (4 / (np.pi * n)) * np.sin(2 * np.pi * n * f0 * t)
        elif signal_type == 'triangle':
            # Fourier series for a triangle wave
            if n % 2 == 1:
                approx_signal += ((8 / (np.pi*2 * n2)) * (-1)*((n-1)//2)) * np.sin(2 * np.pi * n * f0 * t)
    
    return approx_signal

# User input
signal_type = input("Enter the signal type (sine, square, triangle): ").lower()
T = float(input("Enter the period (T) of the signal: "))
N = int(input("Enter the number of Fourier series terms (N): "))
f0 = 1 / T
t = np.linspace(0, 2*T, 1000)  # Time values for 2 periods of the signal

# Generate the signal based on the input type
if signal_type == 'sine':
    signal = np.sin(2 * np.pi * f0 * t)
elif signal_type == 'square':
    signal = np.sign(np.sin(2 * np.pi * f0 * t))  # Square wave
elif signal_type == 'triangle':
    signal = 2 * np.abs(2 * (t / T - np.floor(t / T + 0.5))) - 1  # Triangle wave
else:
    print("Invalid signal type.")
    exit()

# Fourier series approximation
approx_signal = fourier_series(signal_type, T, N, f0, t)

# Plotting the signal and its Fourier series representation
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal, label="Original Signal")
plt.title(f"Original {signal_type.capitalize()} Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, approx_signal, label="Fourier Series Approximation", color='r')
plt.title(f"Fourier Series Approximation of {signal_type.capitalize()} Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
