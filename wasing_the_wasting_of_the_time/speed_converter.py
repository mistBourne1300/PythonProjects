import FourLoop
import os
import numpy as np

LIGHTYEARS = {	"ALPHA_CENTAURI":4.4,
				"SUN":1.5781*(10**-5),
				"PLUTO":0.00053,
				"ANDROMEDA":2.537*(10**6),
				"SAGGITARIUS_A_STAR":25640,
				"ACROSS_MILY_WAY":100000,
				"EDGE_OF_UNIVERSE":47*(10**9),
				"UNIVERSE_ACROSS":94*(10**9)}

# all unit conversions below are converting from the lightyears to the unit specified
LENGTHS = {	"METER":9.460528405106*(10**15),
			"KILOMETER":9.460528405106*(10**12),
			"CENTIMETER":9.460528405106*(10**17),
			"MILLIMETER":9.460528405106*(10**18),
			"MICROMETER":9.460528405106*(10**21),
			"NANOMETER":9.460528405106*(10**24),
			"INCH":3.724617482325197*(10**17),
			"FOOT":3.103847901937664*(10**16),
			"YARD":1.034615967312555*(10**16),
			"MILE":5.878499814275879*(10**12),
			"ASTRO_UNIT":63239.72622,
			"PARSEC":0.306595,
			"LIGHT_YEAR":1,
			"EARTH_DIAMETER":742431382,
			"SOCCER_FIELD":1.0346159673125547*(10**14),
			"CUBIT":2.046493122156702*(10**16)}

# the following converts years to any other time intercval
TIMES = {	"YEAR":1,
			"MONTH":12,
			"WEEK":52.142857,
			"DAY":365,
			"HOUR":8760,
			"MINUTE":5256000,
			"SECOND":31536000,
			"MILISECOND":3.1536*(10**10),
			"MICROSECOND":3.1536*(10**13),
			"NANOSECOND":3.1536*(10**16),
			"PICOSECOND":3.1536*(10**19),
			"DECADE":0.1,
			"CENTURY":0.01,
			"MILLENNIUM":0.001,
			"FORTNIGHT":26.071429}


if __name__ == "__main__":


	speed = int(input("enter the numerical speed: "))

	for i,k in enumerate(list(LENGTHS.keys())):
		print(f"{i}: {k}")
	length = int(input("select the length you are using: "))
	print("\n\n")

	for i,k in enumerate(list(TIMES.keys())):
		print(f"{i}: {k}")
	time = int(input("select the time you are using: "))
	print("\n")
	
	length = list(LENGTHS.keys())[length]
	time = list(TIMES.keys())[time]
	print(f'length unit: {length}')
	print(f'time unit: {time}')

	length_convert = LENGTHS[length]
	time_convert = TIMES[time]
	print(f'length conversion factor: {length_convert}')
	print(f'time conversion factor: {time_convert}')

	tot_time = LIGHTYEARS_TO_ALPHA_CENTAURI * length_convert * (1/speed) * (1/time_convert)
	print(f'the total time to alpha centauri is {tot_time:.3f} years')
	tot_time = np.round(tot_time,3)
	print(f"that's {FourLoop.get_string_float(tot_time)}years!")
	os.system(f'say "it will take {FourLoop.get_string_float(tot_time)}years"')
