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
### Docker Swarm (managing multiple containers)
- `docker swarm init`
- `docker stack deploy -c stack-with-kafka.yml pyspark` 
- pyspark is the name of the swarm.
- stack-with-kafka.yml is the Docker Swarm configuration file

### List docker containers in a docker swarm
- `docker service ls`
- 0 = service not up
- 1 = service is up

### To find the Jupyter Notebook sever token when it is running in the background
`docker logs $(docker ps | grep pyspark_pyspark | awk '{print $NF}')`

### List Docker networks
`docker network ls`
### Check docker network status
`docker network inspect <network id>`
### Some concepts
- Docker Swarm vs Kubernetes for container ochestration
- !pip vs !run
- arrow-based columnar data
- zipWithIndex RDD header row
- RDD vs Spark DataFrame
- builder pattern and pipe (python, unix, map/filter/reduce)
- parquest columnar database on top of hadoop?
- java, jdbc, sql
- docker log
- mount point is important for docker. /home/data/postgres
- unix command: less, more, tail and head
- pickler
- copy env to .env
- low latency and high throughput
- fastjump TDP Transportation Data Platform
- Cookiecutter Data Science
- GraphFrame 
- computational social science
- mitrepedia tls-ca-bundle.pem
### To check a container status
`docker service ps --no-trunc pyspark_postgres` 
### To check logs
`docker logs $(docker ps | grep pyspark_zookeeper | awk '{print $NF}')` 
### To force override local changes
- `git fetch --all`
- `git reset --hard origin/<branch>` followed by `git pull origin <branch>` 
- <branch> can be master or other branch
    
### Check postgres container
- `docker ps | grep postgres`
### Remove services
`docker service rm pyspark_adminer pyspark_kafka pyspark_postgres pyspark_pyspark pyspark_zookeeper` 
### Code snippet
from dotenv import find_dotenv
from pathlib import Path
project_dir = Path(find_dotenv()).parent
work_dir = project_dir / 'notebooks' / 'python-spark-streaming' / '2_basics' / 'data'

### Streaming repository
`git clone https://github.com/jleetutorial/python-spark-streaming.git`

### To convert the deply to integer

flights_geo = spark.sql(""" \
    select
    f.timestamp as tripid, INT(f.departure_delay) as delay, f.distance,  f.origin_airport as src, \
    f.destination_airport as dst, o.city as city_src, d.city as city_dst, o.state as state_src, d.state as state_dst \
    from flights f, airports o, airports d \
    where \
    f.departure_delay > 0 and \
    (o.iata_code=f.origin_airport) and (d.iata_code=f.destination_airport) \
""")     \
flights_geo.cache() \

### to get the sort to work I had to import the desc function: “from pyspark.sql.functions import desc” 
tripGraph.edges\
.filter("src = 'SFO' and delay > 0")\
.groupBy("src", "dst")\
.avg("delay")\
.orderBy(("avg(delay)"), ascending=False) \
.take(10) 
 
### To change folder permission
`chmod -R go+w <folder name>` 


