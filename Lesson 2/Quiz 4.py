# Write Python code that stores the distance in meters that light travels in one nanosecond in the variable, nanodistance.

# These variables are defined for you:
speed_of_light = 299800000 # meters per second
nano_per_sec = 1000000000 # 1 billion

# should output: 0.2998

nanodistance = speed_of_light / nano_per_sec
print ('Light travels ' + str(nanodistance) + 'm in one nanosecond')