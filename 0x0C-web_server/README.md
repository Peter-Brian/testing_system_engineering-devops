# 0x0C. Web server
## Details
      By Sylvain Kalache          Weight: 1                Ongoing project - started 01-05-2022, must end by 01-06-2022 (in about 16 hours)          - you're done with 0% of tasks.              Checker will be released at 01-05-2022 12:00 PM      Manual QA review must be done          (request it when you are done with the project)              QA review fully automated.       ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png) 

## Background Context
[](https://www.youtube.com/watch?v=AZg4uJkEa-4&feature=youtu.be&hd=1) 

In this project, some of the tasks will be graded on 2 aspects:
Is your  ` web-01 `  server configured according to requirementsDoes your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)For example, if I need to create a file   ` /tmp/test `   containing the string   ` hello world `   and modify the configuration of Nginx to listen on port   ` 8080 `   instead of   ` 80 `  , I can use   ` emacs `   on my server to create the file and to modify the Nginx configuration file   ` /etc/nginx/sites-enabled/default `  .
But my answer file would contain:
```bash
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu

```
As you can tell, I am not using   ` emacs `   to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an  [SRE](https://intranet.hbtn.io/rltoken/Hjv9yJQtW6X7VRa2ByMeEg) 
 , that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the   ` root `   user, you do not need to use the   ` sudo `   command.
A good Software Engineer is a  [lazy Software Engineer](https://intranet.hbtn.io/rltoken/y1MX-uAX-0a4bgXfH3uweQ) 
 .  ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg) 

Tips: to test your answer Bash script, feel free to reproduce the checker environment: 
* start an  ` ubuntu:16.04 `  Docker container
* run your script on it
* see how it behaves
Check out the Docker concept page for more info about how to manipulate containers.
## Resources
Read or watch :
* [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works) 
* [Nginx](https://en.wikipedia.org/wiki/Nginx) 
* [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04) 
* Child process concept page
* [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/) 
* [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm) 
* [HTTP redirection](https://moz.com/learn/seo/redirection) 
* [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404) 
* [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/) 

For reference:
* [RFC 7231 (HTTP/1.1)](https://datatracker.ietf.org/doc/html/rfc7231) 
* [RFC 7540 (HTTP/2)](https://datatracker.ietf.org/doc/html/rfc7540) 

man or help : 
*  ` scp ` 
*  ` curl ` 
## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/HLB_f8cKD3VOdBgXcaHTdA) 
 ,  without the help of Google :
### General
* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests
### DNS
* What DNS stands for
* What is DNS main role
### DNS Record Types
*  ` A ` 
*  ` CNAME ` 
*  ` TXT ` 
*  ` MX ` 
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass  ` Shellcheck `  (version  ` 0.3.7 ` ) without any error
* The first line of all your Bash scripts should be exactly  ` #!/usr/bin/env bash ` 
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* You can’t use  ` systemctl `  for restarting a process
## Quiz questions
#### Question #0
 Quiz question Body The main role of a web server is to
 Quiz question Answers * serve dynamic content

* serve static content

* host files

 Quiz question Tips #### Question #1
 Quiz question Body A web server is
 Quiz question Answers * a physical machine

* a software

 Quiz question Tips #### Question #2
 Quiz question Body The main role of DNS is to
 Quiz question Answers * translate domain name into IP address

* translate domain name into port

* name websites

 Quiz question Tips #### Question #3
 Quiz question Body What was one of the most important reason for which DNS was created
 Quiz question Answers * because humans are not good at remembering long sequences of numbers (IP address)

* to connect the Internet

* to index the web

 Quiz question Tips #### Question #4
 Quiz question Body A HTTP GET request is to
 Quiz question Answers * request data

* submit data

* delete data

 Quiz question Tips #### Question #5
 Quiz question Body A HTTP POST request is to
 Quiz question Answers * request data

* submit data

* delete data

 Quiz question Tips #### Question #6
 Quiz question Body A DNS A record translates to
 Quiz question Answers * an IP

* a domain

 Quiz question Tips #### Question #7
 Quiz question Body A DNS CNAME record translates to
 Quiz question Answers * an IP

* a domain

 Quiz question Tips #### Question #8
 Quiz question Body What is TTL within the context of DNS
 Quiz question Answers * a time period when DNS query results are cached

* a time period when DNS is not answering requests

* a time period for DNS maintenance

 Quiz question Tips #### Question #9
 Quiz question Body Why web servers usually use child processes?
 Quiz question Answers * That’s just a subjective technical choice from the developers who created the software

* So that the web server can dynamically change the number of child process to accommodate the volume of requests to be processed

* To prevent memory leak

 Quiz question Tips Submit answers## Please make sure to validate all quiz questions before moving on to project tasks
