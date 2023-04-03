## This directory contains soultions to tasks on Load Balancing
# Load Balancers
Load balancing is the method of distributing network traffic equally across a
pool of resources that support an application. Modern applications must process
millions of users simultaneously and return the correct text, videos, images,
and other data to each user in a fast and reliable manner. To handle such high
volumes of traffic, most applications have many resource servers with duplicate
data between them. A load balancer is a device that sits between the user and
the server group and acts as an invisible facilitator, ensuring that all
resource servers are used equally.

## Advantages of Load Balancing
* Improves application performance 
* Application scalability
* Adds Security to internet applications
* Application availability

## Load Balancing Algorithms
These are a combination of implemented rules that a load balancer follows in order
to determine the best server for each client system request.
The best choices of algorithm for load balancers are ;
### Least Connection algorithm:
passes connection to the server to the least number of connections. Works best in
environments where all servers have similar capabilities.
### Observed Algorithm:
here, servers are ranked based on the combination of current connections and response
time of a server. The servers with better balnace of fewer connections and faster
response time receive higher proportions of the connections.
### Predictive Algorithm:
using the ranking method of the 'observed' algorithm, this method allows the system
to analyze the trend of the ranking overtime, determining whether a server's performance
is improving or declining, therefore, giving the servers in the pool of 'improving
servers' more connections. This method is said to work well in any environment.

There are also other load balancing algorithms for developers which includes;
* Random
* Round Robin
* Weighted Round Robin
* Dynamic Round Robin
* Fastest
