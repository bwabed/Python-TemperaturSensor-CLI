# Python-TemperaturSensor-CLI

## Dependencies

[Python adafruit](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test)

## Installation

### Hardware
#### Assembly
For assembly use adafruit's instructions linked below.

[Assembly for adafruit BME280 sensor.](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/assembly)

#### Wiring
Wiring can be done using a breadboard as seen in the image below. It can also be wired directly to the gpio pins as I did for this example. 

![Wiring for raspi](https://cdn-learn.adafruit.com/assets/assets/000/097/132/original/adafruit_products_BME280_RasPi_SPI_original.png?1605727339)
*Imagesource: [learn.adafruit.com](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test)*

In this example the GPIO5 ```(board.D5)``` pin is used. The numbering is ```GPIOx = board.Dx```.

*Note that it worked best for me if one of the GPIO pins is used without something in brackets at the end.*

![GPIO pins](images/GPIO-Pinout-Diagram-2.png)
*Imagesource: [raspberrypi.org](https://www.raspberrypi.org/documentation/usage/gpio/)*

## Usage
