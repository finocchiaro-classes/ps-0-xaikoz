[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Tx63V4-N)
# Problem Set 0

Now that you have created a GitHub account and have accepted this invitation, you can finish the problem set. The deadline for this problem set is **August 29, at 11:59pm Boston time**. At the end of this problem set, I list all the components you are required to submit and how you must submit them.

## Part 1: Course Survey
[Take this short survey](https://docs.google.com/forms/d/e/1FAIpQLScv0UiGYhwzi2KxVmsItbr6JBi47HsW0OZsGbHsdaQpZeJ8Ow/viewform?usp=header) if you didn't already before the first day of class

## Part 2: Download and Install GitHub Desktop
In this class, most assignments will be distributed and submitted using GitHub Classroom. The easiest way to manage GitHub for new users is through the GitHub Desktop application.

1. [Download GitHub Desktop from here.](https://desktop.github.com)
2. Find the installer in your Downloads folder (or wherever things get downloaded on your computer), then double click the installer to install GitHub Desktop. In most cases, this will install the program in your Downloads folder.
3. Launch GitHub Desktop. When you do this, it might ask you if you want to move it to a more appropriate location (e.g., Applications or Programs). You should agree to this, but remember where it is getting moved to so you can find it easily later! I suggest making a shortcut or alias on your Desktop.
4. Since you have already created a GitHub account in the first part of this problem set, you should sign in to GitHub.com when prompted, and authorize GitHub Desktop to access your GitHub Files.

## Part 3: Clone your copy of the repository to your own machine
This might be the trickiest part for many people. 

You are now going to use GitHub Desktop to make a copy of `ps0-yourusername` on your own computer. It will just look like a normal folder on your computer, but it will actually be connected to your copy of this repository on the internet on GitHub. You can add files and change files in that folder, and then you will use GitHub Desktop to make those changes to your repository on GitHub. The repository on GitHub is what the TAs and I will grade, rather than a submission on Canvas.

1. Launch GitHub Desktop if you closed it before. If you have not already logged in and authorized it to access your GitHub account, follow the instructions it provides to do so now.

2. You should see a screen like this. Click on the second choice "Clone a Repository from the Internet..."

<img src="img/getstarted.png" width="500">

3. When you select that, you'll see a list of your repositories, including this one, as shown below. Select this repository, i.e., `CSCI1090-S24/ps0-yourusername`, where `yourusername` is your GitHub username.

Then in the `Local Path` box, change the path to something sensible -- like your Desktop or Documents and then a folder named for the class, as shown in the screenshot below. **Be sure to remember what this location is so you can easily find your files later on!**

<img src="img/selectrepo.png" width="500">

4. Next you'll see a screen like this. If you want to see your local copy of your repo on your computer, you can click on the `Show in Finder` option (which will be something like `Show in File Explorer` in Windows).
 
<img src="img/repoview.png" width="500">

6. On my Mac, when I click on `Show in Finder` this is what I see next: a Finder folder with the same files as I can see on GitHub in my browser! This is your local copy of the problem set. This is where you will be doing all the work for this problem set. At the end of the problem set, in step 9, you'll see how to commit your work to your repository on the internet on GitHub.

<img src="img/classroomlocation.png" width="500">

## Part 4: Download and install Python

1. Download Python for your operating system by clicking the big yellow "Download Python" button found on this webpage: https://www.python.org/downloads. It's okay if the version number is different. Python gets updated frequently!

<img src="img/download.png" width="300">

2. It will probably get downloaded to your Downloads folder. Double click on the downloaded file to install Python on your computer. Answer the questions that the installer asks you and keep clicking the "Continue" button. You might have to enter your computer's password to complete the installation.

### *Important note for Windows users: You **must** check the box in the first dialogue window that says "Add Python 3.12 to PATH"!*

### *Important note for Mac users: Allow the installer to access files in Downloads!*


3. After installation is complete, your computer will probably open a window showing you where the various Python components were installed. On a Mac, it's in `Applications` by default. In Windows, the default location is usually in `Programs`. If you are having trouble finding the Python components you just installed, you can always search for "IDLE" the way you would search for any other file or program (e.g., with the Start menu in Windows, or on a Mac with Spotlight, the magnifying glass in the upper right corner). Here's a screenshot from my Mac showing where the installer installed Python. 

<img src="img/maclocation.png" width="500">

**Pro tip: make a shortcut or alias to the IDLE application to your desktop so you always know where to find it.**


## Part 5: Write and run Python code from the IDLE interpreter

1. Launch the **IDLE** application (*not* `python.exe` or `Python launcher.app` or anything else with the word "python" in it). On a Mac it might be called ``IDLE.app``, and on a Windows machine it might be called ``IDLE.exe`` or ``IDLE.bat``. See Part 5, step 3 to recall how to find it.

2. This will open a window that looks something like this.

<img src="img/idlepicture.png" width="500">
 
3. Next to the ``>>>`` type a mathematical expression, like ``2+7`` or ``56/8``. Then hit return.

4. Now type your own personalized greeting to me and the TAs using the ``print`` command. Here's an example, below, of how the command should look, but you will replace ``Hello, world!`` with your own greeting. Don't forget to hit return after you type your command.

```print("Hello, world!")```

5. Take a screenshot of your IDLE window showing that you typed these commands, and move the screenshot into the folder on your computer for this repository (i.e., the one GitHub Desktop created called `ps0-yourusername`).

## Part 6: Write and run a Python program with IDLE

In this folder, you'll see a file called `ps0.py`.  (Your operating system might just show it as as `ps0`. That's fine -- it's the file you want.) In order to view and run this program in IDLE, you need to open it in IDLE. There are two ways of opening a Python (``.py``) file in IDLE.

**Option 1**

* Right-click on the `ps0.py` file. (On a Mac, you can right-click by tapping the icon with two fingers or by holding down the ``control`` key and then tapping the icon.)
* Select `Open with...` and then select IDLE from the submenu. On Windows, if you don't see `Open with...` select the `More options` item, which should bring up the `Open with...` option.
* If IDLE does not appear or you can't figure out how to right click, try option 2.

**Option 2**

* Launch IDLE. It might already be open from when you did Part 6.
* From the `File` menu in IDLE, select `Open`. Then navigate to the `ps0-yourusername` folder, and select `ps0.py`, which your OS might show just as `ps0`, without the `.py`.


Once you have launched IDLE and you have `ps0.py` open, click on the `ps0.py` window to make it the active window. Then go up to the `Run` dropdown menu, and select `Run Module`. In the `IDLE Shell` window, you'll see output something like this.

```
=========== RESTART: /Users/jfinocchiaro/Desktop/ps0.py ===========
Hello, World!
>>> 
```

You have successfully run your first Python program! You can now edit the program in the window where you opened it in IDLE.

1. Change the code in `ps0.py` to print out on three seperate lines: (1) "Hello, Boston College!", (2) the sum of 7 and 15, (3) any farewell message. Remember that you need to use the `print()` function for each thing you want to print out!
2. Save the program by selecting `Save` from the `File` menu or by using whatever shortcut you'd use to save a file in Word or any other app on your computer (e.g., `command-s` in Mac).
3. Run the program by selecting the `ps0.py` window and then going to `Run -> Run module`.
   

## Part 7: Make a Personal Slide

1. Using PowerPoint, Keynote, or Google Slides, create a single landscape mode PDF called `firstname_lastname.pdf` that contains the following information.

* Your name as it appears in Canvas.
* The name you prefer to be called.
* A photo of you that resembles what you currently look like.

2. Put the PDF in your folder that is the local clone of the repository (i.e., `ps0-yourusername`).


## Part 8: Commit your work to GitHub Classroom using the GitHub Desktop app
If you look at your `ps0-yourusername` folder now, it should look like this, since you have added your slide, your screenshot, and your updates to  `ps0.py`.

<img src="img/updated.png" width="500">

Now you are ready to commit your changes from your local copy of the repo to the main copy of the repo on GitHub!

1. Launch GitHub Desktop.
2. It should look something like this, showing the files that have been added or changed on the left. If you don't see something like this, you should be able to find your current ps0 repo from the drop down menu in the upper left corner.

<img src="img/githubdesktop.png" width="500">

3. Type a message saying what changes you're making in the box that says `Summary (required)`. I typed "adding a slide and screenshot, updating ps0.py".

4. Click `Commit to main`.
5. Then you'll see this screen. Click the blue button that says `Push origin`.

<img src="img/pushorigin.png" width="500">

6. Now you can double check that your changes to the repo on GitHub went through by clicking on `View on GitHub`:

<img src="img/viewongithub.png" width="500">

7. Your repo on GitHub should now look something like this (substituting in your username, of course, and different dates and times). You can see that the files I added are there, and the `ps0.py` file was updated very recently.

<img src="img/githubview.png" width="500">

If you have followed all of the steps so far, you should be done with the problem set. Congratulations!

---

**Reminder:** To receive full credit you must

* Complete the course survey (Part 1).
* Put the screenshot showing that you used the interpreter in IDLE (Part 5).
* Edit the `ps0.py` file in this directory (as described in Part 6).
* Put your personal PDF slide in this directory (Part 7).
* Commit this entire directory to GitHub Classroom (Part 8).

**All components of this problem set are due by Friday, August 29, by 11:59pm Boston time.**

---


