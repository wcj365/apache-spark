# Install Apache Spark on Ubuntu
This tutorial documents the steps to set up Apache Spark to practice big data analytics on a Windows machine. It is not set up on Windows directly. Instead, we use Docker container to install an Ubuntu Linux OS and then install Apache Spark and the related software including Python and Java. 

Note: Learn about Python's anonymous functions (lambda functions) and its build-in funcitons like map and filter and reduce functions from functools package. THese functions are related to Hadoop MapReduce and pyspark library which aim tro distribute data processing across multiple notes within a cluster. Understanding the concept of functional programming and the benefits it brings to big data analytics. 
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
- [First Steps With PySpark and Big Data Processing](https://realpython.com/pyspark-intro/)
## Notes
- `>` is Windows command line prompt
- `#` is Linux command line prompt 
- Linux root account is used
- Current directory in Linux is /root
### Step 1 - Install Docker on Windows
Use Linux container instead of Window container. Make sure enable Hyper-v and Container in Windows.
### Step 2 - Pull ubuntu Image from Docker Hub
`>docker pull ubuntu`
### step 3 - Run ubuntu in Interactive Mode
`>docker run -it ubuntu` 
Notes:
- it = interactive  
- The user is root. 
- We are at the home folder /root 
### Step 4 - Update Software Package List
`#apt update`

Note: apt = Advanced Package Tool. Ubuntu's package manager. Red Hat Enterprise Linux (RHEL)/Centos package manager is called yum.
### Step 5 - Install Java JDK 8
`#apt install openjdk-8-jdk-headless`

Tip: To find out all versions of Java installed and switch which one to use, run this command `#update-alternatives --config java`. I installed JDK 11 first and found out Spark 2 did not work. So I had to install JDK 8 and switch the default Java from 11 to 8.
### Step 5 (Future) - Install Java JDK 11
`#apt install default-jdk` \
This will install the latest JDK (Java 11 as of 3/3/2020). Spark 2.x only runs on Java 8. Spark 3 will run on Java 11.
### Step 6 - Install Latest Apache Spark 
- download Apache Spark tarball \ 
The latest version number may be different and need to be changed according. It is 2.4.5 as of 3/3/2020 \
`#curl -O http://apache.osuosl.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz`
- Extract tarball \
`#tar xvf spark-2.4.5-bin-hadoop2.7.tgz`
- Move the Spark folder to /opt \
`#mv spark-2.4.5-bin-hadoop2.7/ /opt/spark`
- Delete the targball \
`#rm spark-2.4.5-bin-hadoop2.7.tgz`
### Step 7 - Install Vim/Vi 
`#apt install vim`
### Step 8 - Install Python 3
`#apt install python3`
### Step 9 - Set Up Spark Environment Variable
`#vi .bashrc` 

Insert the following two lines:
- `export SPARK_HOME=/opt/spark`
- `export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin`

and run this command `#source .bashrc`
### Step 10 - Set up Spark Python link in .profile
`#vi .profile` 

Insert this line: `export PYSPARK_PYTHON=python3` and run this command `#source .profile`
### Step 11 - Start up a Standalone Spark Master 
`#start-master.sh`

The Master web UI is http://localhost:8080. However we need to install GUI desktop and a web browser.
### Step 12 - Start up Spark Worker Process (Slave)
`#start-slave.sh spark://ubuntu:7077`

The Applications/Jobs web UI is http://localhost:4040. However we need to install GUI desktop and a web browser.

### Step 14 - Run Spark Python Shell
`#pyspark`

While in the pyspark shell as prompted by >>>, perform the following test:
- `>>>a = sc.parallelize(range4))`
- `>>>a.collect()    # this should return [0,1,2,3]`
- `>>>a.count()      # this should return 4`
- `>>>quit()         # exit the shell`

These statements server as a test for the success/failure of the installation. I have encountered problems due to issues with Java version compaibility. Also Python version compatibility too. Note:
- Apache Spark 2.x runs on JDK 8, not JDK 11. 
- Apache Spark requires JDK. JRE is not enough.
- There may be multiple versions of Python installed on a system, be aware. For example:
    - System comes with a default Python
    - There are Python 2 and Python 3 along with pip 2 and pip 3
    - If installed, Anaconda comes with its own Python
### Step 15 - Stop Spark Slave and Master
`#stop-slave.sh`

`#stop-master.sh`

### Step 16 - Install pip
`#apt install python3-pip`

### Step 17 - Install pyspark package using pip3
`#pip3 install pyspark`

This allows for running Python program using pyspark package (a Apache Spark cluster is optional). 
### Step 18 - Install pyspark package using conda
`#conda install pyspark`

This allows for running Jupyter notebooks using pyspark package (a Apache Spark cluster is optional). 

## Additional Notes:

You didn’t have to create a SparkContext variable in the Pyspark shell. The PySpark shell automatically creates a variable, sc (stands for Spark Context), to connect you to the Spark engine in single-node mode.

You must create your own SparkContext when submitting real PySpark programs with spark-submit or a Jupyter notebook.

To run pyspark shell with a cluster:
`#pyspark --master spark://das00.mitre.org:7077`

To find out which cluster the pyspark shell is connected to:
`>>>sc`
This will display `>>><SparkContext master=local[*] appName=PySparkShell>` if it is connected to a default local single-node/single-machine cluster. master=local[*] * means using all processors/cores. This is the result of starting the shell without specifying a cluster using --master option.

This will display `>>><SparkContext master=spark://das00.mitre.org:7077 appName=PySparkShell>` if it is connected to the cluster spark://das00.mitre.org:7077.

## Various Startup Shell Scripts
- sbin/start-master.sh - Starts a master instance on the machine the script is executed on.
- sbin/start-slaves.sh - Starts a slave instance on each machine specified in the conf/slaves file.
- sbin/start-slave.sh - Starts a slave instance on the machine the script is executed on.
- sbin/start-all.sh - Starts both a master and a number of slaves as described above.
- sbin/stop-master.sh - Stops the master that was started via the sbin/start-master.sh script.
- sbin/stop-slaves.sh - Stops all slave instances on the machines specified in the conf/slaves file.
- sbin/stop-all.sh - Stops both the master and the slaves as described above.

## Typical Spark Related Entries in .bashrc
- export JAVA_HOME=/usr/local/java/jdk1.8.0_121
- export JRE_HOME=$JAVA_HOME/jre
- export SCALA_HOME=/usr/local/src/scala/scala-2.12.1
- export SPARK_HOME=/usr/local/spark/2.1.0
- export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin:$SCALA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin
