def set_val_null():
    global threshold, sensor_12_high, sensor_12_low, sensor_12, button_a
    threshold = 0
    sensor_12_high = 0
    sensor_12_low = 0
    sensor_12 = 0
    button_a = 0

def make_null():
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P7, 0)
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.digital_write_pin(DigitalPin.P6, 0)

def on_button_pressed_a():
    global button_a
    button_a = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def create_variables():
    global var_namen
    var_namen = []
    for Index in range(12):
        var_namen.append("sensor_" + str(Index) + "\"_high\"")
    return var_namen

def calibrate_pins(Pin: number):
    global sensor_12_high, sensor_12_low, button_a, sensor_3_high, sensor_3_low
    pins.digital_write_pin(DigitalPin.P8, 1)
    basic.pause(100)
    sensor_12_high = pins.analog_read_pin(AnalogPin.P0)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    control.wait_for_event(button_a, 1)
    basic.pause(100)
    sensor_12_low = pins.analog_read_pin(AnalogPin.P0)
    pins.digital_write_pin(DigitalPin.P8, 0)
    basic.show_icon(IconNames.YES)
    button_a = 0
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P7, 1)
    basic.pause(100)
    sensor_3_high = pins.analog_read_pin(AnalogPin.P0)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . #
        . . . . .
        . . . . .
        """)
    control.wait_for_event(button_a, 1)
    basic.pause(100)
    sensor_3_low = pins.analog_read_pin(AnalogPin.P0)
    basic.show_icon(IconNames.YES)
    button_a = 0
    
sensor_sum = 0
sensor_9 = 0
sensor_6 = 0
sensor_3 = 0
sensor_3_low = 0
sensor_3_high = 0
var_namen: List[str] = []
button_a = 0
sensor_12 = 0
sensor_12_low = 0
sensor_12_high = 0
threshold = 0
make_null()
set_val_null()
calibrate_pins(8)

def on_forever():
    global sensor_12, sensor_3, sensor_6, sensor_9, sensor_sum, threshold
    make_null()
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    pins.digital_write_pin(DigitalPin.P8, 1)
    basic.pause(100)
    sensor_12 = Math.map(pins.analog_read_pin(AnalogPin.P0),
        sensor_12_low,
        sensor_12_high,
        0,
        10)
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P7, 1)
    basic.pause(100)
    sensor_3 = Math.map(pins.analog_read_pin(AnalogPin.P0),
        sensor_3_low,
        sensor_3_high,
        0,
        10)
    pins.digital_write_pin(DigitalPin.P7, 0)
    pins.digital_write_pin(DigitalPin.P5, 1)
    basic.pause(100)
    sensor_6 = pins.analog_read_pin(AnalogPin.P0)
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.digital_write_pin(DigitalPin.P6, 1)
    basic.pause(100)
    sensor_9 = pins.analog_read_pin(AnalogPin.P0)
    pins.digital_write_pin(DigitalPin.P6, 0)
    sensor_sum = sensor_12 + (sensor_3 + (sensor_6 + sensor_9))
    threshold = 0.9 * (sensor_sum / 4)
    if sensor_12 < threshold:
        basic.show_leds("""
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif sensor_3 < threshold:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            """)
    elif sensor_6 < threshold:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            """)
    elif sensor_9 < threshold:
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)
