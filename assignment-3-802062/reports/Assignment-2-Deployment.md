# Deployment

There are three components of the projects namely

* spark
* rabbitMQ
* mysimbdpServer

Before deployment you must have these prerequisites

* java
* Lunix OS
* Python3
* Curl (if executing web service endpoint from terminal)
*  Terminal and web browser


#### mysimbdpServer (Main BigData Platform Server)

mysimbdpServer is responsible for all datat ingestion management to CoreDMS and to execute stream analytics

How to install spark
1) change directory to /opt
2) run
```commandline
sudo curl -O https://www-us.apache.org/dist/spark/spark-2.4.2/spark-2.4.2-bin-hadoop2.7.tgz
sudo tar xvf spark-2.4.2-bin-hadoop2.7.tgz
sudo mkdir spark
sudo mv spark-2.4.2-bin-hadoop2.7/ /opt/spark 
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```
3) Then run
```commandline
start-master.sh 
```

And go to http://localhost:8080/, to find the URL of spark

4) Run
```commandline
start-slave.sh <spark_url>
```

and your spark is setup now

5) Open Lunix terminal
6) Run from code_assignemnt_3 to setup rabbitmq
```commandline
sh run.sh
```
7) Copy code directory to **/home/$USER/** (current user of the lunix) path.
8) Go to code directory
9) Execute bash script **playIt.sh**.
```commandline
sh playit.sh
```
10) And Boom your web server is deployed on localhost
11) To check the status of web services(API) execute "curl [http://127.0.0.1:5000/status](http://127.0.0.1:5000/status)"

Following are the endpoints and their arguments:

```
GET /status/
```
To check the status of a web server

```
POST /executeBatch/
Parameters:
 - tenant_id
 - file name (Staged file name)
```
Execute Batch script of client namely clientBatchApp w.r.t to tenant


```
GET /executeBatch/
Parameters:
 - tenant_id
 - operation (To start or stop Consumer)
```
Execute Stream script of client namely clientStreamApp w.r.t to tenant and operation

