from picamera import PiCamera
import os
from time import sleep
import argparse


def timelapse(int, n, dir):
    camera = PiCamera()
    for i in range(n):
        camera.capture(dir+os.pathsep()+"image{0:04d.jpg".format(i))
        sleep(int)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", "-i",
                        help="length of time in seconds between images",
                        default=60)
    parser.add_argument("--images", "-n", help="number of images", default=1)
    parser.add_argument("--output", "-o",
                        help="path to output directory", default="./")
    args = parser.parse_args()
    interval = args.interval
    images = args.images
    output = args.output
    timelapse(int=interval, n=images, dir=output)


if __name__ == "__main__":
    main()