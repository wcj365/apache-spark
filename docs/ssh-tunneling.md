# Use Jupyter Notebooks on a Remote Server through SSH Tunneling
## Problem
When a remote host starts a Jupyter Notebook server, it is only accessible via localhost:8888
and can not be accessed directly by remote clients. For example, my MITRE laptop web browser is not able to 
access the Jupyter Notebook server running on ECE Lab host (das00.mitre.org)
## Solution
User SSH Tunneling
- Setup putty
- Use Putty to log on to the remote host
- Start Jupyter Notebook `$jupyter notebook --no-browser --port 8888`
- Open the web browser on your local machine (MITRE laptop) and type `localhost:8888/lab`
- Copy the token from the remote host Jupyter Notebook server terminal 
