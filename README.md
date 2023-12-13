# Windows Drawing Script

This script provides simple functions to draw pixels, lines, and boxes on the screen using the `win32gui` and `win32api` libraries. It includes features for drawing with drop shadows and outlines.

## Prerequisites

- Python
- `pywin32` package

## Installation

Before running the script, you need to have Python installed on your Windows machine. You can download Python from the official website: https://www.python.org/downloads/windows/.

Once Python is installed, you need to install the `pywin32` package, which provides access to many of the Windows APIs from Python. You can install it using pip:

```bash
pip install pywin32

## Usage

Run the script directly from the command line:

python main.py

## Features

- Drawing pixels, lines, and boxes directly on the screen.
- Functions for drawing boxes with drop shadows and outlined borders.

## Classes and Methods

color: A class containing color constants.
draw:
- pixel(x, y, color): Draws a pixel at the specified coordinates.
- line(x1, y1, x2, y2, color): Draws a line between two points.
- box(x1, y1, x2, y2, color): Draws a rectangle.
dropshadow:
- box(x1, y1, x2, y2, color, color_shadow): Draws a box with a drop shadow effect.
- outlined:
- box(x1, y1, x2, y2, color, color_outline): Draws a box with an outlined border.

## Notes

The script includes a main function that demonstrates how to use the drawing functions. It repeatedly draws boxes with different styles on the screen.
The script runs in an infinite loop, so you will need to terminate it manually (e.g., with Ctrl+C in the command line).

## Disclaimer

This script directly interacts with the Windows graphical interface, which could interfere with the user's activities. Use it responsibly and with caution.
