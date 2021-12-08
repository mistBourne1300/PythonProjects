""" 
A simple program (in development) that will interactively perform an audiogram with the user. 
It (will) generate sounds of various frequencies and Db levels, and ask the user to to 
"""


from matplotlib import pyplot as plt
import numpy as np
from scipy.io import wavfile
import IPython
from scipy.fftpack import fft, ifft

import os
import sounddevice as sd
import time


class SoundWave(object):
    """A class for working with digital audio signals."""

    # Problem 1.1
    def __init__(self, rate, samples):
        """Set the SoundWave class attributes.

        Parameters:
            rate (int): The sample rate of the sound.
            samples ((n,) ndarray): NumPy array of samples.
        """
        self.rate = rate
        self.samples = samples

    # Problems 1.1 and 1.7
    def plot(self, dft = False, audible = False, bottom_end = None, top_end = None):
        """Plot the graph of the sound wave (time versus amplitude)."""
        if(dft):
            plt.subplot(211)
        plt.title("Time vs Amplitude")
        seconds = len(self.samples)/self.rate
        print(f'seconds: {seconds}')
        domain = np.linspace(0, seconds, len(self.samples))
        plt.plot(domain, self.samples)
        if(dft):
            plt.subplot(212)
            plt.title("Frequency vs Amplitude")
            freqs = fft(self.samples)
            top = len(freqs) / seconds
            print(f'top: {top}')
            dom = np.linspace(0,top, len(freqs))
            if audible:
                if not bottom_end: 
                    bottom_end = 0
                else:
                    bottom_end = np.abs(dom-bottom_end).argmin()
                
                if not top_end:
                    top_end = np.abs(dom-20000).argmin()
                else:
                    top_end = np.abs(dom-top_end).argmin()
                print(f'top end: {top_end}')
                if(top_end > len(freqs)//2):
                    print("sample fully within audible range printing full sample")
                    plt.plot(dom[:len(freqs)//2], np.abs(freqs[:len(freqs)//2]))
                else:
                    plt.plot(dom[bottom_end:top_end], np.abs(freqs[bottom_end:top_end]))
            else:
                plt.plot(dom[:len(freqs)//2], np.abs(freqs[:len(freqs)//2]))
        
        plt.tight_layout()
        plt.show()


    # Problem 1.2
    def export(self, filename, force=False):
        """Generate a wav file from the sample rate and samples. 
        If the array of samples is not of type np.int16, scale it before exporting.

        Parameters:
            filename (str): The name of the wav file to export the sound to.
        """
        if force:
            samples = np.int16(self.samples/np.max(np.abs(self.samples)) * 32767)
        elif self.samples.dtype != np.int16:
            samples = np.int16(self.samples/np.max(np.abs(self.samples)) * 32767)
        else: samples = self.samples
        
        wavfile.write(filename, self.rate, samples)
    
    # Problem 1.4
    def __add__(self, other):
        """Combine the samples from two SoundWave objects.

        Parameters:
            other (SoundWave): An object containing the samples to add
                to the samples contained in this object.
        
        Returns:
            (SoundWave): A new SoundWave instance with the combined samples.

        Raises:
            ValueError: if the two sample arrays are not the same length.
        """
        if(len(self.samples) != len(other.samples)):
            raise ValueError("Sample arrays are not of same length")
        return SoundWave(self.rate, self.samples + other.samples)


    # Problem 1.4
    def __rshift__(self, other):
        """Concatentate the samples from two SoundWave objects.

        Parameters:
            other (SoundWave): An object containing the samples to concatenate
                to the samples contained in this object.

        Raises:
            ValueError: if the two sample rates are not equal.
        """
        if(self.rate != other.rate):
            raise ValueError("Sample rates are not the same")
        return SoundWave(self.rate, np.append(self.samples, other.samples))

    
    # Problem 2.1
    def __mul__(self, other):
        """Convolve the samples from two SoundWave objects using circular convolution.
        
        Parameters:
            other (SoundWave): An object containing the samples to convolve
                with the samples contained in this object.
        
        Returns:
            (SoundWave): A new SoundWave instance with the convolved samples.

        Raises:
            ValueError: if the two sample rates are not equal.
        """
        raise NotImplementedError("Problem 2.1 Incomplete")

    # Problem 2.2
    def __pow__(self, other):
        """Convolve the samples from two SoundWave objects using linear convolution.
        
        Parameters:
            other (SoundWave): An object containing the samples to convolve
                with the samples contained in this object.
        
        Returns:
            (SoundWave): A new SoundWave instance with the convolved samples.

        Raises:
            ValueError: if the two sample rates are not equal.
        """
        raise NotImplementedError("Problem 2.2 Incomplete")

    # Problem 2.4
    def clean(self, low_freq = None, high_freq = None):
        """Remove a range of frequencies from the samples using the DFT. 

        Parameters:
            low_freq (float): Lower bound of the frequency range to zero out.
            high_freq (float): Higher boound of the frequency range to zero out.
        """
        seconds = len(self.samples)/self.rate
        freqs = fft(self.samples)/seconds
        if not high_freq:
            high_freq = len(freqs)//2 / seconds
        if not low_freq:
            low_freq = 0
        freqs[int(low_freq*seconds):int(high_freq*seconds)] = 0
        freqs[int(-high_freq*seconds):int(-low_freq*seconds)] = 0
        self.samples = ifft(freqs)
        
def generate_note(frequency, duration):
    """Generate an instance of the SoundWave class corresponding to 
    the desired soundwave. Uses sample rate of 44100 Hz.
    
    Parameters:
        frequency (float): The frequency of the desired sound.
        duration (float): The length of the desired sound in seconds.
    
    Returns:
        sound (SoundWave): An instance of the SoundWave class.
    """
    RATE = 44100
    num_samples = int(duration * RATE)
    domain = np.linspace(0,duration, num_samples)
    rng = np.sin(2*np.pi * frequency * domain)
    return SoundWave(RATE, rng)

if __name__ == "__main__":
	os.chdir("/Users/chase/Desktop/Python/audiogram_samples")
	a440 = generate_note(440, 1)
	a440.export("a440.wav")
	samples = [250,500,1000,1500,1000,500,250]
	
	#samples per second
	sps = 44100
	
	# Frequency / pitch
	freq_hz = 440.0

	# Duration
	duration_s = .1

	# Attenuation so the sound is reasonable
	atten = 0.1

	for i in samples:
		freq_hz = i

		# NumpPy magic to calculate the waveform
		each_sample_number = np.arange(duration_s * sps)
		waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
		waveform_quiet = waveform * atten

		# Play the waveform out the speakers
		sd.play(waveform_quiet, sps)
		time.sleep(duration_s)