## Virtual environment 
- Virtual environment is a self-contained directory that contains
    - a Python installation
    - additional packages (e.g: numpy, pandas, Pillow ...)
for **particular versions** so that you can maintain seperate enviroment for your project

- Why do we need a virtual environment?
    - Installing everything globally can cause version conflicts.
    - Different projects may require different versions of libraries. 
    - Each project should have its own dependencies as best practice.

## How to install virtual environment

### Option 1: using venv (for Python 3.3+) 

[Guideline here](https://docs.python.org/3/library/venv.html#venv-def) 

#### Step 1: Create a new virtual env 
```bash
cd <your-project-folder> # go to the project folder
python3 -m venv <your-virtual-env>
```

#### Step 2: Activate your selected virtual env
(reference)[]

* MacOS/Linux
```bash
#bash/zsh 
$ source <your-virtual-env>/bin/activate
```

* Windows - command prompt 
```bash
# cmd.exe
<your-virtual-env>\Scripts\activate.bat
```

* Window - PowerShell
```bash
# PowerShell
<your-virtual-env>\Scripts\Activate.ps1
```

#### Step 3: Install packages in the virtual env
The Python Package Index (PyPI)[https://pypi.org/] is a repository of software for the Python programming language.

##### Option 1: Install individual packages  
```bash
pip install pillow
pip install pandas==2.2.3
```

Export your installed packages into a file and share it to your friend

> pip freeze > requirements.txt

##### Option 2 (recommended): Install all packages from a file
- Create a new file requirements.txt and copy the following lines into the file and save it:
```bash
pillow
pandas==2.2.3
```
Install all packages
```bash
pip install -r requirements.txt
pip list # show the list of installed packages
```

#### Step 4: After finishing your project, deactivate env
```bash
deactivate
```

### Link 
(TechAmici Github)[https://github.com/techamici/python_for_everyone]
