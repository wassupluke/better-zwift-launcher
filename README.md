# Better Zwift Launcher

### ABOUT
<p>The Better Zwift Launcher (BEZL) is a simple, 13-line Python script to launch Zwift automagically as a maximized window.

BEZL depends on the <a href="https://zwifthacks.com/zwift-login/">ZwiftHacks zwift-login script</a> to get you logged in and past the LET'S RIDE button garbage. We already know you want to ride, that's why you told the computer to start Zwift, eh?

I run my Zwift in windowed mode and the ZwiftHacks login scripting isn't able to maximize the Zwift game window once it has been started.

That's where my script comes in. You get the login simplicity of ZwiftHacks, and the maximum windowed goodness of Zwift all in one package.</p>

### REQUIREMENTS
<ol>
    <li>A Windows machine capable of running Zwift (if you're running Zwift on Linux, good for you, I still have yet to get that wizardy to work for me)</li>
    <li><a href="https://zwifthacks.com/zwift-login/">zwift-login by ZwiftHacks</a></li>
    <li>Python</li>
</ol>
<i>I have this running on Windows 11 Pro version 23H2 with Python version 3.12.7, zwift-login version 47, Zwift Launcher version 1.1.13.0, and Zwift Game version 1.77.0</i>

### INSTALLATION
<p>Easiest method (for most folks):</p>
<ol>
    <li>Go to <a href="https://github.com/wassupluke/better-zwift-launcher/blob/master/BEZL.exe">https://github.com/wassupluke/better-zwift-launcher/blob/master/BEZL.exe</a></li>
    <li>Click the "Download raw file" button to save the program to your computer</li>
</ol>
<i>I recommend saving the program somewhere memorable, like on the Desktop, to make it easier to find.</i>

<p>The other way for the more techincally inclined:</p>
<ol>
    <li>gh repo clone wassupluke/better-zwift-launcher</li><i>note where you install this</i>
    <li>cd better-zwift-launcher</li>
    <li>pip install -r requirements.txt</li>
</ol>

### USING THE SCRIPT
<p>You've got options:
You can run the script from any terminal/command line with `python PATH_TO_BEZL.py_HERE`
or
run the BEZL.exe file.
</p>
