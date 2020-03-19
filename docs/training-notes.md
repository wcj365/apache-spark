# Notes from Apache Spark Training
### To convert Jupyter notebook to presentaion in PDF (PPT, may be)
`jupyter nbconvert --to slides <notebook>.ipynb --post serve`
### Start an interactive terminal (it) to a docker container
- first find out the container ID by issuing `docker ps` command
- then issue `docker exec -it <ontainer-id> /bin/bash` command
### Secure Copy  (scp) a file from another machine/host
- `scp <user>@<host>:<file> .`
- Example: `scp ipython@ipython01.mitre.org:spark-course-data.tar.bz2 .`
### To find out if Docker engine is up and running
`sudo service docker status`
### To start up the Docker engine
`sudo service docker start`
### To check out the code from repository into a local new branch
`git checkout -b <new_branch>`
### To check out the code from a branch of a repository
`git checkout <branch>`
### Apache Spark Deployment Models 
- Non-distributed (local)
- Distributed 
    - Standlone 
    - Apache Mesos 
    - YARN (Yet Another Resource Manager)
    - AWS EMR
### Apache Spark Actors
- Edge Node/Client Machine (where the driver application runs)
- Cluster Manager/Resource Manager 
- Worker/Slave Nodes
### Pipelined RDD vs RDD
- PipelinedRDD: PipelinedRDD operations are pipelined and sent to worker; the code is executed from top to bottom. It is a subclass of RDD.
- RDD: Represents a constant, partitioned collection of elements that can be worked on in parallel.


