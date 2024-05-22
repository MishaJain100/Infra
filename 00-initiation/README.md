# 00-initiation

<h3>My approach on how to host a CTF</h3>
<br>

<b>Points discussed in the meeting:</b>

- The infrastructure of a CTF should include functionalities for monitoring flag submissions, managing challenge instances, and generating statistics.

- The server infrastructure may make the use of horizontal scaling to accomodate increasing loads.

- Utilization of MySQL for database management over SQLite is preferred.

- Challenges will be hosted in isolated containers with restricted resources.

- Hosting will include separate servers for frontend operations, challenge instances, and signup, ensuring security by isolating potential attack vectors like RCE.

- Dynamic challenge instances will be hosted using VMs and nsjail for enhanced security, with Dockerfiles for easy deployment.

- Load balancers may be deployed to manage traffic efficiently, and prevent DDoS attacks.
<br>
<br>

<b>Pertaining to these points, my approach basically consists of the following:</b>

- We can make use of CTF frameworks available, such as CTFd and Hack the Box, and can utilize their custom infrastructure. Looking at various documentations, CTFd seems to be the more common approach.

- Using cloud service providers (not entirely sure which one would be the best one):
    - <i>Google Cloud:</i> 
        - Simple
        - Competitive pricing
        - Best for beginners
    - <i>Microsoft Azure:</i>
        - Offers scalability and flexibility
        - Bit of a learning curve for beginners
    - <i>AWS:</i>
        - Extensive range of services
        - Provides tools for scalability, automation and monitoring
        - Complex and resource intensive for beginners

- Creating a VM instance with the implementation of HTTP/HTTPS (80/443) and SSH (22) ports for secure interactions and remote server management respectively. For challenges involving network forensics, packet analysis, or network services exploitation, we might need FTP (Port 21), DNS (Port 53), or SMTP (Port 25).

- Server Setup:
    - <i>Apache HTTP Server:</i> Offers flexibility and a wide range of modules.
    - <i>Nginx:</i> Offers scalability, speed, and multifunctionality as a reverse proxy server.
    - <i>lighttpd:</i> Simpler, making it easier to setup and manage.
  
- Most common server setup used is Nginx. (Don't exactly understand how its used, but oh well.) 

- Servers that may be required:
    - <i>Signup / Signin Servers:</i> Sign up has user registration, authentication, and other signup-related functionality. Sign in functionality verifies user credentials against stored records. CTFd provides built-in user registration and authentication features.
    - <i>Challenge Instances Server(s):</i> May need one or more VMs to host dynamic challenges with nsjail containers. Each challenge instance should run within its own nsjail container, ensuring isolation from other instances and the underlying host system.
    - <i>Database Server:</i> Used for storing challenge data, user information, submission logs, and other data. 
        - DBMS: PostgreSQL, MySQL, or MariaDB
    - <i>Load Balancer:</i> Distributes incoming traffic across multiple instances of the frontend server and challenge instances servers. 
        - Application Load Balancer - AWS
        - Google Cloud Load Balancer - GCP
    - <i>Frontend:</i> Used for monitoring flag submissions, providing statistics, and hosting static challenges. CTFd provides basic monitoring and statistics features, but for further customization, we can optionally use technologies such as Prometheus and Grafana.

- We could probably combine the signup / signin and frontend servers to streamline the hosting process, but I am not too sure of this strategy.

- We need to dockerize the web services, including signup, signin, and frontend components, using dockerfiles. Each service should run within its own docker container.

<h3>The normal approach</h3>

