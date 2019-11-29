# Assignment Assignment_1  802062

All the structure is same as the template, the only directory and execution need to be explain is from Code Directory.


### Code

Change the name of directory of code to code_assignment_2, because python code have reserve keyword for code and it wont run the application
Directory is as follows:

````
* code_assignment_3
* __init__.py
    * clientSideApp
        * data_publisher.py
       
    * mysimbdp-batchanalyticsmanager
        * client
            * clientbatchanalytics.py.py
    
    * mysimbdp-streamanalyticsmanager
        * client
            * clientstreamingestapp.py
            * clientStreamAnalyticsApp.py
    
    * mysimbdp_server
        * __init__.py
        * api.py
        * configuration.json
        * helper.py
        * setup.py
        * playit.sh
    * run.sh
````

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

```
GET /executeStream/
Parameters:
 - tenant_id
 - operation (To start or stop Consumer)
```

Execute Stream Analytics script of client namely clientStreamApp w.r.t to tenant

```
GET /executeStreamAnalytics/
Parameters:
 - tenant_id
 - windowSize (WindowSize for Analytics)
```
