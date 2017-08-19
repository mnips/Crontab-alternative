# Crontab-alternative

1) Whatever file(message_new_try.py) want to execute on a regular basis.

2) Make text file as exec_message and remove .txt extension(open with txt to check)

3) Type in terminal chmod 755 “name of text file”. This creates a new file exec which directly runs script on double clicking.

4) Now go to Automator in your Mac and choose new document.

5) Select application and then drag drop executable file and then add action to open file. 

6) Save this as an .app file.

7) Goto calendar and make a new reminder with an alert and choose custom.

8) Then choose open file and select .app file in that.

9) Finally choose timings and repetition accordingly to run script.

10) Good to go!
