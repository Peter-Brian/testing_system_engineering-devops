# PID, env and signals in shell

## Resources
Read or watch:

* [Linux PID](https://intranet.hbtn.io/rltoken/FcpEdqz8hau7eEB0Pi8Ong)
* [Linux process](https://intranet.hbtn.io/rltoken/hX_t2YK0erLPbdTq0-uKwQ)
* [Linux signal](https://intranet.hbtn.io/rltoken/SojW4zvL8j1yaoa7_NM6rA)

## man or help:
```
ps
pgrep
pkill
kill
exit
trap
```

## General
* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

0. What is my PID
mandatory
Score: 100.00% (Checks completed: 100.00%)
Write a Bash script that displays its own PID

1. List your processes
mandatory
Score: 100.00% (Checks completed: 100.00%)
Write a Bash script that displays a list of currently running processes.

Requirements:

Must show all processes, for all users, including those which might not have a TTY
Display in a user-oriented format
Show process hierarchy

2. Show your Bash PID
mandatory
Score: 100.00% (Checks completed: 100.00%)
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

You cannot use pgrep
The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error [here](https://intranet.hbtn.io/rltoken/BYXAGPH5zbPpsqIR84ndFQ))

3. Show your Bash PID made easy
mandatory
Score: 100.00% (Checks completed: 100.00%)
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

You cannot use ps

4. To infinity and beyond
mandatory
Score: 100.00% (Checks completed: 100.00%)
Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:

In between each iteration of the loop, add a sleep 2

5. Don't stop me now!
mandatory
Score: 100.00% (Checks completed: 100.00%)
We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:

You must use kill
Terminal #0

6. Stop me if you can
mandatory
Score: 100.00% (Checks completed: 100.00%)
Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:

You cannot use kill or killall

7. Highlander
mandatory
Score: 100.00% (Checks completed: 100.00%)
Write a Bash script that displays:

To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal
Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

Terminal #0

8. Beheaded process
mandatory
Score: 100.00% (Checks completed: 100.00%)
Write a Bash script that kills the process 7-highlander.

Terminal #0

9. Process and PID file
#advanced
Score: 100.00% (Checks completed: 100.00%)
Write a Bash script that:

Creates the file /var/run/holbertonscript.pid containing its PID
Displays To infinity and beyond indefinitely
Displays I hate the kill command when receiving a SIGTERM signal
Displays Y U no love me?! when receiving a SIGINT signal
Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

10. Manage my process

Read:

* [&](https://intranet.hbtn.io/rltoken/ISCvYLlssHBRk3117QINuw)
* [init.d](https://intranet.hbtn.io/rltoken/YhzaWR9jdFi2W0d0qrNJ3w)
* [Daemon](https://intranet.hbtn.io/rltoken/mNOdP_7ieM7KQaNHh504NA)
* [Positional parameters](https://intranet.hbtn.io/rltoken/YPgjXhBUEDN1yh1rkQOe1w)
man: sudo

Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: start, restart and stop. The most popular way of doing so on Unix system is to use the init scripts.

Write a manage_my_process Bash script that:

Indefinitely writes I am alive! to the file /tmp/my_process
In between every I am alive! message, the program should pause for 2 seconds
Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)

Requirements:

* When passing the argument start:
Starts manage_my_process
Creates a file containing its PID in /var/run/my_process.pid
Displays manage_my_process started
* When passing the argument stop:
Stops manage_my_process
Deletes the file /var/run/my_process.pid
Displays manage_my_process stopped
* When passing the argument restart
Stops manage_my_process
Deletes the file /var/run/my_process.pid
Starts manage_my_process
Creates a file containing its PID in /var/run/my_process.pid
Displays manage_my_process restarted
* Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed
Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing ./101-manage_my_process start, in our case it will simply create a new process instead of saying that it is already started.

11. Zombie

Read [what a zombie process is](https://intranet.hbtn.io/rltoken/lD64_7WBTGbjxM9IJ5ncdg)

Write a C program that creates 5 zombie processes.

Requirements:

For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
When your code is done creating the parent process and the zombies, use the function bellow

12. Screencast

Now that you have mastered signals, how about sharing your knowledge?

Create a screencast where you live-code/demo something related to Unix signals.

Requirements:

Step by step video
Two minutes of above
Done in English
Published to Youtube
While you are free to choose the recording system to record the screencast, I highly recommend [screencast-o-matic](https://intranet.hbtn.io/rltoken/izYNM_2BzVVoGOJTTK7f_g)
Once you are done, please share the Youtube URL in your answer file and below.
We’ll be watching you!
