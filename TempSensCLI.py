#!/usr/bin/env python3
# Standard librarys
import curses
from threading import Thread
import os
import time

# Librarys for sensor
import board
import digitalio
import busio
import adafruit_bme280

# Using globals is not that nice but simpel
key_pressed = False

def detect_key_press():
	global key_pressed
	stdscr = curses.initscr()
	key = stdscr.getch()
	if chr(key) == "q": # Use q to exit
		key_pressed = True

def main(screen):
	# Setup of bme280 with SPI
	spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
	bme_cs = digitalio.DigitalInOut(board.D5) # Change this according to gpio pin used (cs port on sensor)
	bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

	# Set pressure at sea level
	bme280.sea_level_pressure = 1013.25

	# Start listening for key press in other thread so ui won't get blocked
	thread = Thread(target = detect_key_press)
	thread.start()

	# Use color for nicer ui
	curses.start_color()

	# Screen setup
	num_rows, num_cols = screen.getmaxyx()

	# Colors
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)

	curses.curs_set(0) # Turn off cursor
	curses.cbreak() # Turn on cbreak mode (no enter)
	curses.noecho() # Turn echo off

	while not key_pressed:
		# Get current time
		current_time = time.localtime()
		current_clock = time.strftime("%H:%M:%S", current_time)

		# Clean screen
		screen.erase()

		# Add data to screen
		screen.addstr("******* Temp monitor (q to quit) *******\n", curses.color_pair(1))
		screen.addstr("Time: ")
		screen.addstr(current_clock + "\n", curses.color_pair(2))
		screen.addstr("Temperature: ")
		screen.addstr(" %0.1f C\n" % bme280.temperature, curses.color_pair(2))
		screen.addstr("Humidity: ")
		screen.addstr("%0.1f %%\n" % bme280.relative_humidity, curses.color_pair(2))
		screen.addstr("Pressure: ")
		screen.addstr("%0.1f hPa\n" % bme280.pressure, curses.color_pair(2))
		screen.addstr("Altitude = ")
		screen.addstr(" %0.2f meters" % bme280.altitude, curses.color_pair(2))
		
		# Refresh screen to show data
		screen.refresh()
		
		# Check for key press for faster exit
		if not key_pressed:
			# Wait for 1 second
			curses.napms(1000)


	curses.nocbreak()   # Turn off cbreak mode
	curses.echo()       # Turn echo back on
	curses.curs_set(1)  # Turn cursor back on

curses.wrapper(main)
