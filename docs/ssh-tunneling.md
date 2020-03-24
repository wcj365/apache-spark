# Use Jupyter Notebooks on a Remote Server through SSH Tunneling
## Problem - Remote Access to Jupyter Notebook Server
When a remote host starts a Jupyter Notebook server, it is only accessible via localhost:8888
and cannot be accessed directly from remote clients. For example, my MITRE laptop web browser is not able to 
access the Jupyter Notebook server running on ECE Lab host (das00.mitre.org)
## Solution - Use SSH Tunneling
- Setup putty on the laptop (Windows machine)
![](https://github.com/wcj365/apache-spark/blob/master/docs/images/ssh-tunneling-01.png)
![](https://github.com/wcj365/apache-spark/blob/master/docs/images/ssh-tunneling-02.png)
- Use Putty to log on to the remote host
- Start Jupyter Notebook on remote host `$jupyter notebook --no-browser --port 8888`
![](https://github.com/wcj365/apache-spark/blob/master/docs/images/ssh-tunneling-03.png)
- Open the web browser on the local machine (MITRE laptop) and type `localhost:8888/lab`
- Copy the token from the remote host Jupyter Notebook server terminal (see previous screen)
![](https://github.com/wcj365/apache-spark/blob/master/docs/images/ssh-tunneling-04.png)
