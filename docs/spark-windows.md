# Apache Spark on Windows
This tutorial documents the steps to set up Apache Spark to practice big data analytics on a Windows machine. It is not set up on Windows directly. Instead, we use Docker container to install an Ubuntu Linux OS. 
## Benefits of this Approach
- The Windows environment and the Apache Spark environment are separated. Windows is for day to day Office Automation (OA) including  regular use of Windows Office product suite (Words, Excel, PPT, etc.). 
- Linux is a better platform for software development and data science. Especially in the Cloud Computing era, Linux is the prevalent OS. 
## Technologies Installed/Used
- Docker Container 
- Ubuntu Docker Image
- Java/JDK
- Python 3
- Apache Spark
## References 
- [Install Apache Spark on Ubuntu 19.04/18.04 & Debian 10/9/8](https://computingforgeeks.com/how-to-install-apache-spark-on-ubuntu-debian/)
## Steps
- `>` is the Windows command line prompt
- `#` is the Linux command line prompt 
- Linux root account is used
- Current directory is assumed /root
### Step 1 - Install Docker on Windows
Use Linux container instead of Window container.
### Step 2 - Pull ubuntu Image from Docker Hub
`>docker pull ubuntu`
### step 3 - Run ubuntu in Interactive Mode
`>docker run -it ubuntu` 
it = interactive \ 
The user is root. \
We are at the home folder /root \
### Update Software Package List
`#apt update`
Note: apt = Automated Package Tool
### Step 4 - Install Java JDK
`#apt install default-jdk` \
This will install the latest JDK (Java 11 as of 3/3/2020)
### Step 5 - Install Latest Apache Spark 
- download Apache Spark tarball \ 
The latest version number may be different and need to be changed according. It is 2.4.5 as of 3/3/2020 \
`#curl -O http://apache.osuosl.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz`
- Extract tarball \
`#tar xvf spark-2.4.5-bin-hadoop2.7.tgz`
- Move the Spark folder to /opt \
`#mv spark-2.4.5-bin-hadoop2.7/ /opt/spark`
- Delete the targball \
`#rm spark-2.4.5-bin-hadoop2.7.tgz`
### Step 6 - Install Vim/Vi 
`#apt install vim`
### Step 7 - Install Python 3
`#apt install python3`
### Step 8 - Set Up Spark Environment Variable
`#vi .bashrc` \
insert the following two lines:
- export SPARK_HOME=/opt/spark
- export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
`#source .bashrc`
### Step 9 - Set up Spark Python link in .profile
`#vi .profile` \ 
Enter the following line: 
- export PYSPARK_PYTHON=python3
`#source .profile`
### Step 10 - Start up a Standalone Spark Master 
`#start-master.sh`
### Step 11 - Start up Spark Worker Process (Slave)
`#start-slave.sh spark://ubuntu:7077`
### Step 12 - Run Spark Python Shell
`pyspark`
