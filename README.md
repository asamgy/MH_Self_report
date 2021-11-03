# MH_Self_report


#### 1) Clone the REPO branch neural-intent

- > git clone -b neural-intent https://github.com/asamgy/MH_Self_report.git
- > cd MH_Self_report

#### 2) Install requirments.txt

- > pip3 install requirments.txt

#### 3) Update Config.py file

Update the config.py file for mysql database connection
```
#SQL Configuration
HOST = "localhost"
USER = "yourusername"
PASSWORD = "yourpassword"
DATABASE = "databasetablename"
```

#### 4) RUN database.py

```
python3 database.py
```

This will create a database connection to create a table inside mysql database to store conversation, time and scenarios. 
## NOTE - RUN this only one time

### 5) Finally run the app
```
python3 app.py
```
After a short training it will be ready to listen. 

Something like this screen will be presented : 

[image](https://user-images.githubusercontent.com/530190/140071847-87c58a5f-9ffb-4e1f-9ec1-ede7dbce9e69.png)

Start speaking and see whatsoever you speak will be logged like this :

[image](https://user-images.githubusercontent.com/530190/140073008-6e8fb877-bb86-4deb-9fcd-6e718ac68f80.png)


IMPORTANT NOTE : TABLE Name in the database created using database.py and used in app.py is ```paul_table```. In case you need to change it, please update it in both the places and run do Step 4) and Step 5) again. 

