# PyChronos

## Description
My first public project. PyChronos is a small application that lets you create and run several stopwatches simultaneously. It is designed to continue tracking time even after the application has been closed.

## Overview
![PyChronos Interface](/images/screenshot-demo.png)

## Features
- Start and stop stopwatches at will.
- Stopwatches continue to run even after you close the application.
- Restart a stopwatch as many times as necessary.
- Rename and delete stopwatches at will.

## Technologies used
- Python (Tested with 3.11.2)
- PySide6
- TinyDB

## Installation
Clone the repository using the following command and move inside the folder :
```bash
git clone https://github.com/Krogan77/PyChronos.git && cd PyChronos
```

## Configuration
Create a virtual environment and install the required dependencies specified in the `requirements.txt` file :
### Linux
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
### Windows bash (Git Bash)
```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```
### Windows cmd
```bash
python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
```

## Use
To launch the application, run the `main.py` file :
#### (from the root folder 'PyChronos')
```bash
python src/main.py
```