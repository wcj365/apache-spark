# Install Apache Spark on Red Hat Enterprise Linux (RHEL) 8 on AWS EC2
Establish a Apache Spark environment on the Cloud to practice Big Data Analytics. 
- Launch a AWS EC2 instance using RHEL 8 image
- Install Python 3 
- Install Java 8 JDK
- Install Apache Spark 2.4.5

## References
- [How to install Java 8 on RHEL 8](https://www.tecmint.com/install-java-on-rhel-8/)
- [How to install spark on RHEL 8](https://linuxconfig.org/how-to-install-spark-on-redhat-8)


### Step 1 - Launch AWS EC2 instance 
Use RHEL 8 AWS Machine Image (AMI). Use ESB for storage. 
### Step 2 - Log on to the instance using SSH
From windows, open Git bash shell (assuming Git is installed).
`$ssh -i "wangumbc.pem" ec2-user@<the public IP of the EC2 instance>`
Assuming the private key file "wangumbc.pem" is in the current folder.
### Step 3 - Update Software Package List
`$sudo dnf update`

Note: Different Linux distributions use different package managers. 
- Ubuntu uses apt (Advanced Package Tool)
- RHEL/Centos uses dnf or yum
### Step 4 - Install Python 3
`$sudo dnf install python3`
### Step 5 - Install Java JDK 8
`sudo dnf install java-1.8.0-openjdk-devel`

Tip: To find out all versions of Java installed, run this command `$update-alternatives --config java`. 
- Apache Spark 2.x runs on JDK 8 
- Apache Spark 3.x runs on JDK 11
### Step 6 - Install Apache Spark 
- `$cd /opt`
- download Apache Spark tarball \ 
The latest version number may be different and need to be changed according. It is 2.4.5 as of 3/3/2020. \
`$sudo curl -O "https://downloads.apache.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz"
- Extract tarball \
`$tar xvf spark-2.4.5-bin-hadoop2.7.tgz`
- Delete the targball \
`$rm spark-2.4.5-bin-hadoop2.7.tgz`
- Create a symbolic link as a shortcut \
`ln -s /opt/spark-2.4.0-bin-hadoop2.7 /opt/spark`
### Step 9 - Set Up Spark Environment Variable
`$vi .bashrc` 

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


