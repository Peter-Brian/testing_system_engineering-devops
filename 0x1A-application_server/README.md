# 0x1A. Application server
## Details
      By Sylvain Kalache, co-founder at Holberton School          Weight: 1                Ongoing project - started 02-21-2022, must end by 02-25-2022 (in about 20 hours)          - you're done with 0% of tasks.              Checker was released at 02-23-2022 02:24 PM              An auto review will be launched at the deadline      ## Concepts
For this project, students are expected to look at these concepts:
* [Web Server](https://intranet.hbtn.io/concepts/17) 

* [Server](https://intranet.hbtn.io/concepts/67) 

* [Web stack debugging](https://intranet.hbtn.io/concepts/68) 

 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220224%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220224T083834Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b2e9556e53e3a4cc0e1ad3b5647e2d73ff833c22f7f22e5728d00cd3f6fa288f) 

## Background Context
[](https://youtu.be/pSrKT7m4Ego) 

Your web infrastructure is already serving web pages via   ` Nginx `   that you installed in your  [first web stack project](https://intranet.hbtn.io/rltoken/RrbqMLWOJUyVaWdXsnpvXw) 
 . While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your   ` Nginx `   and make is serve your Airbnb clone project.
## Resources
Read or watch :
* [Application server vs web server](https://intranet.hbtn.io/rltoken/RerpYBxsgrpIorHjbDgulw) 

* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.hbtn.io/rltoken/uosy5QXdMbDPA1tFTR1eoA) 
 (As mentioned in the video, do not install Gunicorn using  ` virtualenv ` , just install everything globally)
* [Running Gunicorn](https://intranet.hbtn.io/rltoken/QTnnkj6vfQV9ovW_eYWWDQ) 

* [Be careful with the way Flask manages slash](https://intranet.hbtn.io/rltoken/whE8do28ZiJJoJLyb1ACwA) 
 in [route](https://intranet.hbtn.io/rltoken/JLjrXD4MLS3rUkQr5QyxtA) 
  -  ` strict_slashes ` 
* [Upstart documentation](https://intranet.hbtn.io/rltoken/rldSTo2ZFS8clyTHH3SyBg) 

## Requirements
### General
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Everything Python-related must be done using  ` python3 ` 
* All config files must have comments
### Bash Scripts
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* All your Bash script files must be executable
* Your Bash script must pass  ` Shellcheck `  (version  ` 0.3.7-5~ubuntu16.04.1 `  via  ` apt-get ` ) without any error
* The first line of all your Bash scripts should be exactly  ` #!/usr/bin/env bash ` 
* The second line of all your Bash scripts should be a comment explaining what is the script doing
## Your servers
NameUsernameIPState3014-web-01 ` ubuntu `  ` 54.90.73.219 ` running              Actions              Toggle Dropdown* [Soft reboot](https://intranet.hbtn.io/servers/7309/soft_reboot) 

* [Hard reboot](https://intranet.hbtn.io/servers/7309/hard_reboot) 

* [
                    Ask a new server
                      (Last)
](https://intranet.hbtn.io/servers/7309/ask_new) 

3014-web-02 ` ubuntu `  ` 3.84.98.183 ` running              Actions              Toggle Dropdown* [Soft reboot](https://intranet.hbtn.io/servers/7137/soft_reboot) 

* [Hard reboot](https://intranet.hbtn.io/servers/7137/hard_reboot) 

* [
                    Ask a new server
](https://intranet.hbtn.io/servers/7137/ask_new) 

3014-lb-01 ` ubuntu `  ` 34.227.103.152 ` running              Actions              Toggle Dropdown* [Soft reboot](https://intranet.hbtn.io/servers/7138/soft_reboot) 

* [Hard reboot](https://intranet.hbtn.io/servers/7138/hard_reboot) 

* [
                    Ask a new server
](https://intranet.hbtn.io/servers/7138/ask_new) 

## Tasks
### 0. Set up development with Python
          mandatory         Progress vs Score  Task Body Let’s serve what you built for  [AirBnB clone v2 - Web framework](https://intranet.hbtn.io/rltoken/EJw7FG9Zmwlu6qo9RggPfw) 
  on   ` web-01 `  . This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.
Requirements:
* Make sure that [task #3](https://intranet.hbtn.io/rltoken/eL5390Y6rOrrSCYeBBdzlw) 
 of your [SSH project](https://intranet.hbtn.io/rltoken/9r-2ODIpnVNWJp5OUl7JRA) 
 is completed for  ` web-01 ` .  The checker will connect to your servers.
* Git clone your  ` AirBnB_clone_v2 `  on your  ` web-01 `  server.
* Configure the file  ` web_flask/0-hello_route.py `  to serve its content from the route  ` /airbnb-onepage/ `  on port  ` 5000 ` .
* Be careful, another process may already listen on the same port (Datadog or something else..)
* Your Flask application object must be named  ` app `  (This will allow us to run and check your code).
Example:
##### Window 1:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -

```
##### Window 2:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x1A-application_server ` 
* File:  ` README.md ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Set up production with Gunicorn
          mandatory         Progress vs Score  Task Body Now that you have your development environment set up, let’s get your production application server set up with   ` Gunicorn `   on   ` web-01 `  , port   ` 5000 `  . You’ll need to install   ` Gunicorn `   and any libraries required by your application. Your   ` Flask `   application object will serve as a  [WSGI](https://intranet.hbtn.io/rltoken/alKO4HKARCTOB7W_fpRnTA) 
  entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.
Requirements:
* Install  ` Gunicorn `  and any other libraries required by your application.
* The Flask application object should be called  ` app ` . (This will allow us to run and check your code)
* You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a  ` Gunicorn `  instance to localhost listening on port  ` 5000 `  with your application object as the entry point.
* In order to check your code, the checker will bind a  ` Gunicorn `  instance to port  ` 6000 ` , so make sure nothing is listening on that port.
Example:
##### Terminal 1:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-03 20:47:20 +0000] [3595] [INFO] Starting gunicorn 19.9.0
[2019-05-03 20:47:20 +0000] [3595] [INFO] Listening at: http://0.0.0.0:5000 (3595)
[2019-05-03 20:47:20 +0000] [3595] [INFO] Using worker: sync
[2019-05-03 20:47:20 +0000] [3598] [INFO] Booting worker with pid: 3598

```
##### Terminal 2:
 ` ubuntu@229-web-01:~$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~$
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x1A-application_server ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Serve a page with Nginx
          mandatory         Progress vs Score  Task Body Building on your work in the previous tasks, configure   ` Nginx `   to serve your page from the route   ` /airbnb-onepage/ ` 
Requirements:
*  ` Nginx `  must serve this page both locally and on its public IP on port  ` 80 ` .
*  ` Nginx `  should proxy requests to the process listening on port  ` 5000 ` .
* Include your  ` Nginx `  config file as  ` 2-app_server-nginx_config ` .
Notes:
* In order to test this you’ll have to spin up either your production or development application server (listening on port  ` 5000 ` )
* In an actual production environment the application server will be configured to start upon startup in a system initialization script. This will be covered in the advanced tasks.
* You will probably need to  ` reboot `  your server (by using the command  ` $ sudo reboot ` ) to have Nginx publicly accessible
Example:
#### On my server:
##### Window 1:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-06 20:43:57 +0000] [14026] [INFO] Starting gunicorn 19.9.0
[2019-05-06 20:43:57 +0000] [14026] [INFO] Listening at: http://0.0.0.0:5000 (14026)
[2019-05-06 20:43:57 +0000] [14026] [INFO] Using worker: sync
[2019-05-06 20:43:57 +0000] [14029] [INFO] Booting worker with pid: 14029

```
##### Window 2:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

```
#### On my local terminal:
```bash
vagrant@ubuntu-xenial:~$ curl -sI 35.231.193.217/airbnb-onepage/
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 06 May 2019 20:44:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: keep-alive
X-Served-By: 229-web-01

vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-onepage/
Hello HBNB!vagrant@ubuntu-xenial:~$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x1A-application_server ` 
* File:  ` 2-app_server-nginx_config ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Add a route with query parameters
          mandatory         Progress vs Score  Task Body Building on what you did in the previous tasks, let’s expand our web application by adding another service for   ` Gunicorn `   to handle. In   ` AirBnB_clone_v2/web_flask/6-number_odd_or_even `  , the route   ` /number_odd_or_even/<int:n> `   should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure   ` Nginx `   to proxy HTTP requests to the route   ` /airbnb-dynamic/number_odd_or_even/(any integer) `   to a   ` Gunicorn `   instance listening on port   ` 5001 `  . The key to this exercise is getting   ` Nginx `   configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of   ` Gunicorn `   without having multiple terminals open, see tips below.
Requirements:
*  ` Nginx `  must serve this page both locally and on its public IP on port  ` 80 ` .
*  ` Nginx `  should proxy requests to the route  ` /airbnb-dynamic/number_odd_or_even/(any integer) `  the process listening on port  ` 5001 ` .
* Include your  ` Nginx `  config file as  ` 3-app_server-nginx_config ` .
Tips:
* Check out these articles/docs for clues on how to configure  ` Nginx ` : [Understanding Nginx Server and Location Block Selection Algorithms](https://intranet.hbtn.io/rltoken/e2Sg1BZRv-YLflQwLskJHg) 
, [Understanding Nginx Location Blocks Rewrite Rules](https://intranet.hbtn.io/rltoken/hptuemKYmT9Xx5vQ7G6GgQ) 
, [Nginx Reverse Proxy](https://intranet.hbtn.io/rltoken/yPcdReEOgFdaFbujCyqHZQ) 
.
* In order to spin up a  ` Gunicorn `  instance as a detached process you can use the terminal multiplexer utility  ` tmux ` . Enter the command  ` tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app' `  and if successful you should see no output to the screen. You can verify that the process has been created by running  ` pgrep gunicorn `  to see its PID. Once you’re ready to end the process you can either run  ` tmux a `  to reattach to the processes, or you can run  ` kill <PID> `  to terminate the background process by ID.
Example:
##### Terminal 1:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app'
ubuntu@229-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
1661
1665
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
ubuntu@229-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
1661
1665
1684
1688

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5001/number_odd_or_even/6
<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 6 is even</H1></BODY>
</HTML>ubuntu@229-web-01:~/AirBnB_clone_v2
ubuntu@229-web-01:~$ 
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-dynamic/number_odd_or_even/5
<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 5 is odd</H1></BODY>
</HTML>ubuntu@229-web-01:~/AirBnB_clone_v2$

```
##### Local machine:
```bash
vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-dynamic/number_odd_or_even/6<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 6 is even</H1></BODY>
</HTML>vagrant@ubuntu-xenial:~$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x1A-application_server ` 
* File:  ` 3-app_server-nginx_config ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Let's do this for your API
          mandatory         Progress vs Score  Task Body Let’s serve what you built for  [AirBnB clone v3 - RESTful API](https://intranet.hbtn.io/rltoken/o_uAVsuNqXbJIgw7-ZmiYQ) 
  on   ` web-01 `  .
Requirements:
* Git clone your  ` AirBnB_clone_v3 ` 
* Setup  ` Nginx `  so that the route  ` /api/ `  points to a  ` Gunicorn `  instance listening on port  ` 5002 ` 
*  ` Nginx `  must serve this page both locally and on its public IP on port  ` 80 ` 
* To test your setup you should bind  ` Gunicorn `  to  ` api/v1/app.py ` 
* It may be helpful to import your data (and environment variables) from [this project](https://intranet.hbtn.io/rltoken/r3mnHZ7LoLJVF8JNxstDrQ) 

* Upload your  ` Nginx `  config file as  ` 4-app_server-nginx_config ` 
Example:
##### Terminal 1:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v3$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
ubuntu@229-web-01:~/AirBnB_clone_v3$ curl 127.0.0.1:5002/api/v1/states
[{"__class__":"State","created_at":"2019-05-10T00:39:27.032802","id":"7512f664-4951-4231-8de9-b18d940cc912","name":"California","updated_at":"2019-05-10T00:39:27.032965"},{"__class__":"State","created_at":"2019-05-10T00:39:36.021219","id":"b25625c8-8a7a-4c1f-8afc-257bf9f76bc8","name":"Arizona","updated_at":"2019-05-10T00:39:36.021281"}]
ubuntu@229-web-01:~/AirBnB_clone_v3$
ubuntu@229-web-01:~/AirBnB_clone_v3$ curl 127.0.0.1/api/v1/states
[{"__class__":"State","created_at":"2019-05-10T00:39:27.032802","id":"7512f664-4951-4231-8de9-b18d940cc912","name":"California","updated_at":"2019-05-10T00:39:27.032965"},{"__class__":"State","created_at":"2019-05-10T00:39:36.021219","id":"b25625c8-8a7a-4c1f-8afc-257bf9f76bc8","name":"Arizona","updated_at":"2019-05-10T00:39:36.021281"}]
ubuntu@229-web-01:~/AirBnB_clone_v3$

```
##### Local Terminal:
```bash
vagrant@ubuntu-xenial:~$ curl 35.231.193.217/api/v1/states
[{"__class__":"State","created_at":"2019-05-10T00:39:27.032802","id":"7512f664-4951-4231-8de9-b18d940cc912","name":"California","updated_at":"2019-05-10T00:39:27.032965"},{"__class__":"State","created_at":"2019-05-10T00:39:36.021219","id":"b25625c8-8a7a-4c1f-8afc-257bf9f76bc8","name":"Arizona","updated_at":"2019-05-10T00:39:36.021281"}]
vagrant@ubuntu-xenial:~$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x1A-application_server ` 
* File:  ` 4-app_server-nginx_config ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Serve your AirBnB clone
          mandatory         Progress vs Score  Task Body Let’s serve what you built for  [AirBnB clone - Web dynamic](https://intranet.hbtn.io/rltoken/qOjECpMUaEXf4D0uoqHmQw) 
  on   ` web-01 `  .
Requirements:
* Git clone your  ` AirBnB_clone_v4 ` 
* Your  ` Gunicorn `  instance should serve content from  ` web_dynamic/2-hbnb.py `  on port  ` 5003 ` 
* Setup  ` Nginx `  so that the route  ` / `  points to your  ` Gunicorn `  instance
* Setup  ` Nginx `  so that it properly serves the static assets found in  ` web_dynamic/static/ `  (this is essential for your page to render properly)
* For your website to be fully functional, you will need to reconfigure  ` web_dynamic/static/scripts/2-hbnb.js `  to the correct IP
*  ` Nginx `  must serve this page both locally and on its public IP and port  ` 5003 ` 
* Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors
* Upload your  ` Nginx `  config  as  ` 5-app_server-nginx_config ` 
After loading, your website should look like this:
 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/7a8a7c33021b1b74f9cdc1fd8f855bdb1f8cd44e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220224%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220224T083834Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a7e862e66de80218f3dd308285910c18cb193b865bda98f29ae6e6d0f08c8a3d) 

 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x1A-application_server ` 
* File:  ` 5-app_server-nginx_config ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 2 advanced tasks now!](https://intranet.hbtn.io/projects/311/unlock_optionals) 

×#### Recommended Sandbox
[Running only]() 
### 1 image(0/5 Sandboxes spawned)
### Ubuntu 16.04 - Python 3.5 / Fabric / Puppet
Ubuntu 16.04 with Python 3.5, Fabric and Puppet installed
[Run]() 
