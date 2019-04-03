DEFAULT_DAYTIME = "morning"

def say_good_daytime(daytime = DEFAULT_DAYTIME):
    print("Good " + daytime + "!")

if __name__ == '__main__':
    print("Gooddatetime module run as command.")
    say_good_daytime()
#else:
#    print("Gooddatetime module loaded.")
