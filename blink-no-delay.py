import time

def millis():
    return int(round(time.time() * 1000))

# current_millis = millis()
previous_millis_01 = millis()
delay_time_01 = 1000

previous_millis_02 = millis()
delay_time_02 = 333

def print_first():
    print str(delay_time_01) + 'ms has elapsed.'

def print_second():
    print str(delay_time_02) + 'ms has elapsed.'



def Main():
    # global current_millis

    while True:

        global previous_millis_01
        global delay_time_01

        global previous_millis_02
        global delay_time_02

        current_millis_01 = millis()
        current_millis_02 = millis()

        if current_millis_01 > previous_millis_01 + delay_time_01:
            print_first()
            previous_millis_01 = current_millis_01

        if current_millis_02 > previous_millis_02 + delay_time_02:
            print_second()
            previous_millis_02 = current_millis_02



if __name__ == '__main__':
    Main()