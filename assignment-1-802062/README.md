# Assignment Assignment_1  802062

All the structure is same as the template, the only directory and execution need to be explain is from Code Directory.


### Code

Change the name of directory of code to code_assignment_1, because python code have reserve keyword for code and it wont run the application
Directory is as follows:

* code_assignment_1
* __init__.py
    * daas
        * api.py
        * setup.py
        * helper.py
        * playit.sh
        * testmydaas.py
        * error.log
        * __init__.py
       
    * dataIngestion
        * __init__.py
        * mydataingest.py
        * testmydataingest.py
        * requirement.txt
        * helper.py
        

###### To execute dataIngestion:

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

###### To deploy and execute daas:


1) Open Lunix terminal
2) Copy code directory to **/home/$USER/** (current user of the lunix) path.
3) Go to code directory
4) Execute bash script **playIt.sh**
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

