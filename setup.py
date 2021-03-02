from setuptools import setup, find_packages
import subprocess

setup(name='PI_Phenotyping',
      version='0.1',
      description='Pi camera timelapse',
      author='Jeremy Pardo',
      author_email='mezeg39@gmail.com',
      packages=find_packages(),
      install_requires=[
                'argparse',
                'picamera',])