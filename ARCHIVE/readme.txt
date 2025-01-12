1) message-send 

First I used nmap to scan all open upd connections running on port 18 in my local network. There was exactly one host running msp.

Commands:

nmap 10.128.2.6/24 -sU -p 18

Nmap scan report for 10.128.2.205
Host is up (0.00016s latency).

PORT   STATE SERVICE
18/udp open  msp
MAC Address: 02:42:0A:80:02:04 (Unknown)

After connecting to that host using netcat and sending a message, I got back the flag.

nc -u 10.128.2.205 18

2) ghost-in-the-shell

I tried listening to all TCP traffic on interface eth0. The capture messages revealed that the host at address 10.128.2.41 kept sending SYN packets from a random port to port 13236 on my shell.
When I opened port 13236 by running a netcat process in the background, the host sent a message to 13236 and then a SYN to port 14998.
After the second port also received a message, I saw that the first one was receiving a SYN again, so I wrote a bash script that tried listening on both ports in the background in a loop. Eventually, the flag was sent to port 13236.

Commands:

tcpdump -i eth0 -A tcp -w out.pcap
tcpdump -r out.pcap

3) jwt-auth

Firstly I scanned all tcp ports in the local network to find the one running the site. I used the webtunnel script to forward it to localhost:8080. The site RedactedHub had login and register pages, but you couldn't register a new user.
To understand the login API, i copied the Javascript code for the login page and ran it through a deobfuscator to make it readable.
I then used Postman to compose an HTTP POST request to the /api/login resource, containing a json object in the body. After getting a 200 status code, I logged in as the created user and got redirected to the profile page.

I made the page crash by inputing a string in the prompt instead of a number.
This resulted in a stacktrace reported by the Flask backend. The most important information here was the path to the Python code, and so I used curl to get the full source code of app.py. 
I made a python file based on app.py and called the create_token function with my username as argument and isAdmin being set to true. When ran, it generated a valid JWT token for my user.
I used dev tools to get to the cookies used for the profile page and then swapped the JWT token with the correct one in the cookie named "accessToken". After refreshing the page, a new hidden HTML element was appended, with the flag inside it.


Commands:

nmap -p- -sT 10.128.2.0/24
./webtunnel.sh 10.128.2.44 5000
curl localhost:8080/app.py
# I copied the app.py file and commented all functions except create_token.
python create_jwt_token.py



4) sqli-cart