<p align="center">
	<img
		width="500"
		alt="Soundcloud Username Checker"
		src="https://bit.ly/3xORzNh">
</p>

---

<h3 align="center">
	A Fast,open source Soundcloud Username Checker.
</h3>

<p align="center">
	<strong>
		<a href="https://discord.gg/U4g4bw6zNm">Discord</a>
		•
		<a href="https://cracked.to/DemsServices">Usage</a>
	</strong>
</p>

</p>

<p align="center">


### Windows installation

You will have to have a few things installed before running the sniper. This installation guide assumes that you are on a 64bit Windows system.

First, you will need to install Python. It's recommended to use either version `3.8.5` or `3.8.6`. You must use a Python version above `3.0`. 

### Installing Python

Go to the following link and download Python:

`https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe`

Once you have opened the installer, make sure that you add Python to path. Your installer should look like this:

<img align="center" src="https://i.imgur.com/iefWNyw.png">

Run through the installer as normal, then download the McSniperPY files.

### Downloading

Download the following file:

`https://codeload.github.com/irritability/SoundCoud-Checker/zip/refs/heads/main`

Extract the folder to somewhere easily accessible, such as your desktop.

You should have a folder containing the following files:

<img src="https://bit.ly/3umzJ1P">

If you have more files than this don't worry, the checker has most likely been updated since this guide was written.
If your folder doesn't have a file called `wordlist.txt`, then create one.

### Installing dependencies

You now need to open a command prompt to the checker path. An easy way to do this is by opening the folder and typing `cmd` in the path:

<img src="https://bit.ly/3ekZYQR">

Your command prompt should have a line similar to this:

`C:\Users\%USERNAME%\%PATH%\SoundCoud-Checker-main`

If there is nothing after your Windows username, you will have to type the following command:

`cd path_to_folder`

Once you have a commant prompt open to the correct path, you should type the following command:

`py -m pip install -r requirements.txt`

If you get the following message:

`'py' is not recognized as an internal or external command, operable program or batch file.`

Then you will need to reinstall Python following the guide above, make sure that you added Python to PATH.

Type `py main.py` to run the program.


> Thanks to [sneakers](https://github.com/sneakers) for letting me use his readme!
