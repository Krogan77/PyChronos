# PyChronos

***
## Description
PyChronos is a small application that lets you create and run several stopwatches simultaneously. It is designed to continue tracking time even after the application has been closed.

***
## Overview

![PyChronos Interface](/images/screenshot-demo.png)
![PyChronos Interface](/images/screenshot-demo-2.png)

***
## Features
- Start and stop stopwatches at will.
- Stopwatches continue to run even after you close the application.
- Restart a stopwatch as many times as necessary.
- Rename and delete stopwatches at will.

***
## Technologies used
- Python (Tested with 3.11.2)
- PySide6
- TinyDB

***
## Installation
Clone the repository using the following command and move inside the folder :
```bash
git clone https://github.com/Krogan77/PyChronos.git && cd PyChronos
```

***
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

***
## Use
To launch the application, run the `main.py` file :
#### (from the root folder 'PyChronos')
```bash
python src/main.py
```

***
## Icon Credits

The icons used in this application are from [Icons8](https://icons8.com).

For more information on their use and licensing, please visit their website.

## Crédits des Icônes

Les icônes utilisées dans cette application proviennent de [Icons8](https://icons8.com).

Pour plus d'informations sur leur utilisation et leurs licences, veuillez visiter leur site web.

***
## License
MIT License

Copyright (c) 2024 Krogan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


