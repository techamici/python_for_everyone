## How to install virtual environment

### Option 1: using venv (for Python 3.3+) 

[Guideline here](https://docs.python.org/3/library/venv.html#venv-def) 

#### Step 1: Create a new virtual env
```bash
python -m venv <your-virtual-env>
```

#### Step 2: Activate your selected virtual env
(reference)[]

* MacOS
```bash
#bash/zsh 
$ source <venv>/bin/activate
```

* Windows - command prompt 
```bash
# cmd.exe
C:\> <venv>\Scripts\activate.bat
```

* Window - PowerShell
```bash
# PowerShell
PS C:\> <venv>\Scripts\Activate.ps1
```

#### Step 3: Install packages in the virtual env
##### Option 1: Install each package manually
```bash
pip install numpy
pip install pandas==2.2.3
```
##### Option 2 (recommended): Install all packages together at once
- Create a new file requirements.txt and copy the following lines into the file and save it:
```bash
numpy
pandas==2.2.3
```
Install all packages
```bash
pip install -r requirements.txt
```
