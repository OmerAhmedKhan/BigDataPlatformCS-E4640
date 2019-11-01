# Deployment

There are three componenets of the projects namely

* mysimbdpServer

Before deployment you must have these prerequisites

* Lunix OS
* Python3
* Curl (if executing web service endpoint from terminal)
*  Terminal and web browser


#### mysimbdpServer (Main BigData Platform Server)

mysimbdpServer is responsible for all datat ingestion management to CoreDMS and apply constraints on client data and applciations

1) Open Lunix terminal
2) Run from code_assignemnt_2 to setup rabbitmq
```commandline
sh run.sh
```
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
GET /getConfig/<tenant_id>
```
Get client profile w.r.t tenant_id


```
GET /getDataFiles/<tenant_id>
```
Get client transfered data files w.r.t tenant_id

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
GET /monitor/<tenant_id>
```
Get client streaming metrics w.r.t tenant_id

