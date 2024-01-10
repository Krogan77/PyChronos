# PyChronos

## Description
PyChronos is an application that lets you create and run several stopwatches simultaneously. It is designed to continue tracking time even after the application has been closed.

## Demo
![PyChronos Interface](/images/screenshot-demo.png)

## Features
- Start and stop stopwatches at will
- Stopwatches continue to run even after you close the application 
- Restart a stopwatch as many times as necessary 
- Rename and delete stopwatches at will.

## Technologies used
- Python (Tested with 3.11.2)
- PySide6
- TinyDB

## Installation
Clone the repository using the following command :
```bash
git clone https://github.com/Krogan77/PyChronos.git
```

## Configuration (Git Bash)
Create a virtual environment and install the required dependencies specified in the file `requirements.txt` :
### Linux
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
### Windows bash
```bash
python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
```
### Windows cmd
```bash
python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
```

## Use
To launch the application, run the file main.py :
#### (from the root folder 'PyChronos')
```bash
python src/main.py
```