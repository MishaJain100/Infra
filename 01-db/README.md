# 01-db

Include screenshots and textual outputs of EVERYTHING given below:
All reasonings must look non GPTish

<h3>Host mariadb locally</h3>

Installing MariaDB Server:
<p align = "center">

![](<Images/Installing MariaDB Server.png>)

</p>

Launching MariaDB:
<p align = "center">

![](<Images/Launching MariaDB.png>)

</p>
<br>

<h3>Connection string i.e. IP, port, DB name, username</h3>

Gathering Connection String Data:
<p align = "center">

![](<Images/Connection String Data.png>)

</p>

Connection String: `SERVER="127.0.0.1"; PORT=3306; DATABASE="test"; UID="root";`
<br>

<h3>Permanently change the listening port of server to 4200 and use netcat to verify</h3>

Changing port value:

<p align = "center">

![](<Images/Changing Port to 4200.png>)

</p>

`nc -vz localhost 4200`:

<p align = "center">

![](<Images/Connection Check.png>)

</p>
<br>

<h3>Run some SQL commands by connecting to server using `mysql`</h3>

<p align = "center">

![](<Images/MYSQL Commands.png>)

</p>

```
misha@debian:~$ mysql -h localhost -u root -p -P 4200
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 7
Server version: 10.11.6-MariaDB-0+deb12u1 Debian 12

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
5 rows in set (0.000 sec)

MariaDB [(none)]> USE test;
Database changed
MariaDB [test]> CREATE TABLE users (
    -> username VARCHAR(100) PRIMARY KEY,
    -> password VARCHAR(100)
    -> );
Query OK, 0 rows affected (0.009 sec)

MariaDB [test]> INSERT INTO users (username, password) VALUES ("misha", "password");
Query OK, 1 row affected (0.003 sec)

MariaDB [test]> SELECT * FROM users;
+----------+----------+
| username | password |
+----------+----------+
| misha    | password |
+----------+----------+
1 row in set (0.000 sec)
```
<br>

<h3>Give reasoning on the difference b/w mysql and mariadb</h3>

- Both MariaDB and MySQL are open-source database technologies. Many pages refer to MariaDB as a "fork" of MySQL. 

- However, in terms of performance, MariaDB stands to be better due to its existing 9 storage engines, plus 12 new storage engines to choose from, and the capacity to handle over 200,000 connections. A high thread pool capability helps optimize server resource usage, resulting in increased uptime. Unfortunately, MySQL offers only a limited number of threads on its Community version.

- MySQL supports super read-only function, dynamic columns, and data masking, whereas MariaDB supports invisible columns and temporary table space. However, MariaDB does provide some read-only replicas.

- MariaDB is fully open-source, and no proprietary code exists. MySQL has a dual-licensing model, with both open-source and premium models available.
<br>

<h3>Setup SQLAlchemy and modify "pool size" of connection to 100</h3>

- Now what is pool size? Pool size is the largest number of connections that will be kept persistently in the pool.

- Why do we need a high pool size? Typically, in CTFs, many users try to access the system at a time. A larger pool size keeps more connections ready for use, and hence reducing the wait time for participants. We limit this pool size to the maximum we predict (with a bit extra for good measure) so that the large number of available pre-existing connections don't consume a lot of resources when not in use.

```
import sqlalchemy as db

url = 'mariadb://root:1234@127.0.0.1:4200/test'
engine = db.create_engine(url, pool_size = 100)
```
<br>

<h3>Create a python script to connect to your local mariaDB server using this library</h3>

-   Create some model like User
```
class User(Base):
    __tablename__ = 'users2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __repr__(self):
        return f"id='{self.id}' \t name='{self.name}' \t email='{self.email}')"
```

-   Populate some records using model
```
user1 = User(id = 1, name = 'Misha1', email = 'misha1@gmail.com')
user2 = User(id = 2, name = 'Misha2', email = 'misha2@outlook.com')
user3 = User(id = 3, name = 'Anaya', email = 'anaya@hotmail.com')
    
session.add_all([user1, user2, user3])
session.commit()
```

-   Update those records
```
u = session.query(User).filter(User.name == "Anaya").first()
u.email = "anayanew@gmail.com"
session.commit()
```

-   Delete those records
```
session.delete(u)
session.commit()
```

- Output

<p align = "center">

![](<Images/Python Output.png>)

</p>

```
Fetching all records: 
id='1'   name='Misha1'   email='misha1@gmail.com'
id='2'   name='Misha2'   email='misha2@outlook.com'
id='3'   name='Anaya'    email='anaya@hotmail.com'

Fetching updated records: 
id='1'   name='Misha1'   email='misha1@gmail.com'
id='2'   name='Misha2'   email='misha2@outlook.com'
id='3'   name='Anaya'    email='anayanew@gmail.com'

Fetching records after deleting: 
id='1'   name='Misha1'   email='misha1@gmail.com'
id='2'   name='Misha2'   email='misha2@outlook.com'
```