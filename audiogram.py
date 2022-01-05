""" 
A simple program (in development) that will interactively perform an audiogram with the user. 
It (will) generate sounds of various frequencies and Db levels, and ask the user to to 
"""


from matplotlib import pyplot as plt
import numpy as np




import os
import sounddevice as sd
import time
import curses
from datetime import date

os.system("clear")
print("IMPORTANT: this amateur audiogram will play sounds, some of them very high pitched.")
print("The volume of these sounds may be uncomfortable for some people.")
print("Discretion is advised.\nThis will take several minutes. If you need to terminate the test, press CTRL-C.")
print("\n\nWith that out of the way, note that the sound generation is not perfect, and some artifacts are present.")
print("Please ignore static - they are not part of the test. Listen only for pure tones.")
print("After entring your name, if you hear a sound, press any key.")
print("Closing your eyes may help mitigate any placbo effect from what is printed on the screen")
username = input("please enter your name: ")
 


def main(stdscr):
    os.chdir("/Users/chase/Desktop/Python/audiogram_samples")
    freqs = [25, 50,100,200,400,500,750,1000,1250,1500,1750,2000,2500,3000,3500,4000,4750,5500,6250,7000,8000,9000,10000,11000,12500,14000,15500,17000,18500,20000,25000]
	# samples per second
    sps = 44100
	 
	# Frequency / pitch
    freq_hz = 440.0

	# Duration
    duration_s = 1

    time_delay = 3

	# Attenuation so the sound is reasonable
    atten = -2 # i will define this as zero decibels

    freq_v_dB = []
    
    for i in freqs:
        freq_hz = i
        atten = 0 # i will define this as 1 decibel
        they_heard_it = True

        # move down one decibel at a time until the user can no longer hear the frequency
        count = 0
        while they_heard_it:
            atten -= 1

            # NumpPy magic to calculate the waveform

            stdscr.clear()
            curses.noecho()
            curses.cbreak()
            stdscr.nodelay(True)

            each_sample_number = np.arange(duration_s * sps)
            waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
            waveform_quiet = waveform * (10**atten)


            start = time.time()
            sd.play(waveform_quiet, sps)
            key_pressed = False
            while time.time() - start < time_delay:
                stdscr.addstr(f'freq:{freq_hz}\ndB:{atten}\n{time.time()-start}')
                
                key = stdscr.getch()
                if key >= 0:
                    key_pressed = True
                    break
                    
                stdscr.clear()
            if not key_pressed:
                  they_heard_it = False


            sd.stop()
            time.sleep(.5)
            count += 1
        
        # the user didn't hear the first frequency, doubtful they will hear the frequency at all
        if count == 1:
            freq_v_dB.append(None)
            continue
        
        # count up three tenths of a decibel at a time until the user can hear the frequency again
        while not they_heard_it:
            atten += .3
            stdscr.clear()
            curses.noecho()
            curses.cbreak()
            stdscr.nodelay(True)

            each_sample_number = np.arange(duration_s * sps)
            waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
            waveform_quiet = waveform * (10**atten)


            start = time.time()
            sd.play(waveform_quiet, sps)
            key_pressed = False
            while time.time() - start < time_delay:
                stdscr.addstr(f'freq:{freq_hz}\ndB:{atten}\n{time.time()-start}')
                
                key = stdscr.getch()
                if key >= 0:
                    key_pressed = True
                    break
                    
                stdscr.clear()
            if key_pressed:
                  they_heard_it = True


            sd.stop()
            time.sleep(.5)

        # count down a tenth of a decibel at a time until the user can no longer hear the frequency again
        while they_heard_it:
            atten -= .1
            stdscr.clear()
            curses.noecho()
            curses.cbreak()
            stdscr.nodelay(True)

            each_sample_number = np.arange(duration_s * sps)
            waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
            waveform_quiet = waveform * (10**atten)


            start = time.time()
            sd.play(waveform_quiet, sps)
            key_pressed = False
            while time.time() - start < time_delay:
                stdscr.addstr(f'freq:{freq_hz}\ndB:{atten}\n{time.time()-start}')
                
                key = stdscr.getch()
                if key >= 0:
                    key_pressed = True
                    break
                    
                stdscr.clear()
            if not key_pressed:
                  they_heard_it = False


            sd.stop()
            time.sleep(.5)
        
        # now to plot the data
        freq_v_dB.append(atten)
    
    today = date.today()

    plt.plot(freqs, freq_v_dB)
    plt.title(f'{username}\'s audiogram {today}')
    plt.xlabel("frequency")
    plt.ylabel("decibel level")
    plt.savefig(f'{username}_{today}.png')



if __name__ == "__main__":
	curses.wrapper(main)