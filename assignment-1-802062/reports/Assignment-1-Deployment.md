# Deployment

There are three componenets of the projects namely

* CoreDms
* DataIngest
* Daas

Before deployment you must have these prerequisites

* Lunix OS
* Python3
* Curl (if executing web service endpoint from terminal)
*  Terminal and web browser


#### CoreDMS

CoreDMS is alreayd deployed over GCP at "" with 2 replica Nodes to Scale out Read/Write requests.

Steps to deploy CoreDMS from GCP

1. Create a project on GCP
2. Spin Mongo cluster from [MongoDB with Replication](https://console.cloud.google.com/marketplace/details/bitnami-launchpad/mongodb-multivm?project=bigdataplatform1 "MongoDB with Replication")
3. Note down Mongo User and password from VM Description.
4. Open Mongo port from GCP network settings to connect Mongo on remote machiens either by all or add sources and apply setting to all networks.


#### Data Ingestion

DataIngestion is a module to write data from external source in my case CSV file to a CoreDMS. For this simple task python script is implemented to write CSV file in a batch process.

To execute dataIngestion:

First install requirements form requirement.txt:
```commandline
pip install -r requirement.txt
```

* To write:
```python
python3 mydataingest.py --path "<path to csv>" --operation w
```

* To read:
```python
python3 mydataingest.py --operation r
```


#### Daas (Data As A Service)

Daas is a custom API which can allow a client to read and write to CoreDMS directly. To deploy this web service do the following:

1) Open Lunix terminal
2) Copy code directory to **/home/$USER/** (current user of the lunix) path.
3) Go to code directory
4) Execute bash script **playIt.sh**.
```commandline
sh playit.sh
```
5) And Boom your web server is deployed on localhost
6) To check the status of web services(API) execute "curl [http://127.0.0.1:5000/status](http://127.0.0.1:5000/status)"

Following are the endpoints and their arguments:

```
GET /status/
```
To check the status of a web server

```
GET /read/<recordCount>
```
Get records w.r.t count, to get all provide **0**

```
POST /write/
```
Create a record, allowed fields are as follows:

* app
* category
* rating
* reviews
* size 
* installs
* type
* price
* content_rating
* genres
* last_updated
* current_ver
* android _ver


