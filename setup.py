from setuptools import setup, find_packages

setup(
    name='real-time-streaming-data',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'apache-airflow',
    ],
    entry_points={
        'console_scripts': [
            # No command line in mind for the moment ( command-line = funct to execute)
        ],
    },
)
