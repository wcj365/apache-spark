# Notes from Apache Spark Training
## To convert Jupyter notebook to presentaion in PDF (PPT, may be)
`jupyter nbconvert --to slides data_analysis_with_apache_spark-day1.ipynb --post serve`
## Start an interactive terminal (it) to a docker container
`docker exec -it <ontainer-id> /bin/bash`
## Secure Copy  (scp) a file from another machine
` scp  ipython@ipython01.mitre.org:spark-course-data.tar.bz2 .`
## To find out if Docker enginer is up and running
`sudo service docker status`
## To start up the Docker engine
`sudo service docker start `
## To check out the code from repository into a local new branch
`git checkout -b <new_branch>`
## Apache Concepts 
- Distributed vs Non-distributed (local)
- Edge Node and Client Machine (the driver, entry point)
- Cluster Manager/Resource Manager (Standalone, Apache Mesos, YARN, aws EMR)
- Worker Nodes
    


