function set_val_null () {
    threshold = 0
    sensor_12_high = 0
    sensor_12_low = 0
    sensor_12 = 0
}
function make_null () {
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P7, 0)
    pins.digitalWritePin(DigitalPin.P5, 0)
    pins.digitalWritePin(DigitalPin.P6, 0)
}
input.onButtonPressed(Button.A, function () {
    calibrate_pin(8)
})
function calibrate_pin (Pin: number) {
    pins.digitalWritePin(DigitalPin.P8, 1)
    basic.pause(100)
    sensor_12_high = pins.analogReadPin(AnalogPin.P0)
    basic.pause(100)
    basic.showLeds(`
        . . # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(2000)
    sensor_12_low = pins.analogReadPin(AnalogPin.P0)
    pins.digitalWritePin(DigitalPin.P8, 0)
    basic.showIcon(IconNames.Yes)
}
let sensor_sum = 0
let sensor_9 = 0
let sensor_6 = 0
let sensor_3 = 0
let sensor_12 = 0
let sensor_12_low = 0
let sensor_12_high = 0
let threshold = 0
make_null()
set_val_null()
basic.forever(function () {
    make_null()
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    pins.digitalWritePin(DigitalPin.P8, 1)
    basic.pause(100)
    sensor_12 = pins.analogReadPin(AnalogPin.P0)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P7, 1)
    basic.pause(100)
    sensor_3 = pins.analogReadPin(AnalogPin.P0)
    pins.digitalWritePin(DigitalPin.P7, 0)
    pins.digitalWritePin(DigitalPin.P5, 1)
    basic.pause(100)
    sensor_6 = pins.analogReadPin(AnalogPin.P0)
    pins.digitalWritePin(DigitalPin.P5, 0)
    pins.digitalWritePin(DigitalPin.P6, 1)
    basic.pause(100)
    sensor_9 = pins.analogReadPin(AnalogPin.P0)
    pins.digitalWritePin(DigitalPin.P6, 0)
    sensor_sum = sensor_12 + (sensor_3 + (sensor_6 + sensor_9))
    threshold = 0.9 * (sensor_sum / 4)
    if (sensor_12 < threshold) {
        basic.showLeds(`
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (sensor_3 < threshold) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            `)
    } else if (sensor_6 < threshold) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            `)
    } else if (sensor_9 < threshold) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            `)
    } else {
        basic.showIcon(IconNames.No)
    }
})
