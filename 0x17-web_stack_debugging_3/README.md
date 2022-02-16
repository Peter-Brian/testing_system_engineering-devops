# 0x17. Web stack debugging #3
## Details
      By Sylvain Kalache, co-founder at Holberton School          Weight: 1                Ongoing project - started 02-15-2022, must end by 02-17-2022 (in about 9 hours)          - you're done with 0% of tasks.              Checker was released at 02-16-2022 07:12 AM              An auto review will be launched at the deadline      ## Concepts
For this project, students are expected to look at these concepts:
* [Web Server](https://intranet.hbtn.io/concepts/17) 

* [Web stack debugging](https://intranet.hbtn.io/concepts/68) 

## Background Context
 ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png) 

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)
Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It  [actually powers 26% of the web](https://intranet.hbtn.io/rltoken/Ah9_LmUi191dqxT-Zx7uhg) 
 , so there is a fair chance that you will end up working with it at some point in your career.
Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools. 
The web stack you are debugging today is a Wordpress website running on a LAMP stack.
## Requirements
### General
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A  ` README.md `  file at the root of the folder of the project is mandatory
* Your Puppet manifests must pass  ` puppet-lint `  version 2.1.1 without any errors
* Your Puppet manifests must run without error
* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
* Your Puppet manifests files must end with the extension  ` .pp ` 
* Files will be checked with Puppet v3.4
## More Info
### Install puppet-lint
 ` $ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
 ` ## Tasks
### 0. Strace is your friend
          mandatory         Progress vs Score  Task Body [](https://youtu.be/uHEzt1QuASo) 

Using   ` strace `  , find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
Hint:
*  ` strace `  can attach to a current running process
* You can use [tmux](https://intranet.hbtn.io/rltoken/4KkxME6-3aY9fgfok6HNFA) 
 to run [strace](https://intranet.hbtn.io/rltoken/OUc10nTtuZG65adFVbkYag) 
 in one window and  ` curl `  in another one
Requirements:
* Your  ` 0-strace_is_your_friend.pp `  file must contain Puppet code
* You can use whatever Puppet resource type you want for you fix
Example:
```bash
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
root@e514b399d69d:~#

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x17-web_stack_debugging_3 ` 
* File:  ` 0-strace_is_your_friend.pp ` 
 Self-paced manual review  Panel footer - Controls 
×#### Recommended Sandbox
[Running only]() 
### 1 image(1/5 Sandboxes spawned)
### Ubuntu 14.04 - 293
Web stack debugging #3
SSHSFTP[Webterm](https://intranet.hbtn.io/user_containers/20698/webterm) 
[Destroy]() 
#### Credentials
Host310264dfe6c1.7a64f43d.hbtn-cod.ioUsername310264dfe6c1Passwordfa696d513423255ce365#### Web access
[HTTP](http://310264dfe6c1.7a64f43d.hbtn-cod.io/) 
#### Port mapping
SSH49555HTTP49554