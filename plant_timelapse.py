"""
Purpose: Take timelapse images with raspberry pi camera
Author: Jeremy Pardo
"""

from picamera import PiCamera
import os
from time import sleep
import argparse
import datetime


def timelapse(int, n, dir, rotation, iso, shutter, exposure):
    """
    Uses the PI camera to take a set of images at a user defined interval
    :param int: length of interval between images in seconds
    :param n: number of images to take
    :param dir: path to output directory where images are saved
    :param rotation degrees to rotate pi image
    """
    camera = PiCamera()
    camera.rotation = rotation
    camera.iso = iso
    camera.shutter_speed = shutter
    camera.exposure_compensation = exposure
    for i in range(n):
        print("Capturing image{0:04d} at {1}".format(i, datetime.datetime.now()))
        camera.capture(os.path.join(dir, "image{0:04d}.jpg".format(i)))
        sleep(int)


def main():
    """
    main method parses command line arguments and runs the timelapse function.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", "-t", type=int,
                        help="length of time in seconds between images",
                        default=60)
    parser.add_argument("--images", "-n", type=int, help="number of images", default=1)
    parser.add_argument("--output", "-o",
                        help="path to output directory", default="./")
    parser.add_argument("--rotation", "-r",
                        help="degrees to rotate pi image", default=0)
    parser.add_argument("--iso", "-i", type=int, help="camera iso 0 is auto mode", default=0)
    parser.add_argument("--shutter", "-s", type=int,
                        help="camera shutter speed in microseconds 0 is auto mode", default=0)
    parser.add_argument("--exposure", "-e", help="exposure compensation set between -25 and +25", default=0)
    args = parser.parse_args()
    interval = int(args.interval)
    images = int(args.images)
    output = args.output
    rotation = int(args.rotation)
    iso = int(args.iso)
    shutter_speed = int(args.shutter)
    exposure_compensation = int(args.exposure)


    timelapse(int=interval,
              n=images,
              dir=output,
              rotation=rotation,
              iso=iso,
              shutter=shutter_speed,
              exposure=exposure_compensation)


if __name__ == "__main__":
    main()