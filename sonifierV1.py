import time						    	## Import libraries for counting, talking via serial communications and making beeps
import serial
import winsound

data = serial.Serial('COM16',1200)				## Establish communication with Physense plugged into port COM X at data rate 1200

def playTune(tune):						## Function to make noises based from the data collected from Physense  
    tune = abs(tune)						## abs() function makes all numbers positive
    if tune >= 0.01:						## If the number collected from Physense is bigger than 0.01...
        frequency = (tune * 20000)				## ... turn the number into a playable frequency
        if frequency >=37 and frequency <= 32767:		## Make sure that the frequency is within the human hearing range (37-32767 Hertz)
            print(frequency,"Hz")				## Write the frequency down into the console
            winsound.Beep(int(frequency),50)			## Convert the frequency into a beep, which plays for 50 milliseconds
    else:
        print("I can't play that frequency (0 Hz)")		## If the above didn't work, it's because the Physense number was 0, which isn't a sound

while True:							## This command loops the program forever
    serialRead = data.readline().strip().decode()		## data.readline() reads data from the Physense; the other 2 functions "clean" the data
    data.flush()						## This clears the last number generated from the Physense memory
    try:							## try: will attempt to do the code inside the command, but won't break the program if it cant
        f_data = float(serialRead)				## Turn the number recorded from the Physense into a decimal point number
        playTune(f_data)					## Do the playTune function, giving it f_data as the variable which will become known as tune
    except ValueError:						## If the try: command didn't work, this is what the program will do instead
        print("Error: communication with Physense has become desynchronised.")
