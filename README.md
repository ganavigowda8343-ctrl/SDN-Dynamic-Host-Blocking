# Dynamic Host Blocking using SDN

## Objective
To dynamically block a host in a network using Software Defined Networking (SDN) principles.

## Tools Used
- Mininet
- POX Controller
- Ubuntu Linux

## Network Topology
- 1 Switch (s1)
- 3 Hosts (h1, h2, h3)

## Steps to Run

### 1. Start POX Controller
cd ~/pox
python3 pox.py block

### 2. Start Mininet
sudo mn --topo single,3 --controller remote

### 3. Test Connectivity
pingall
(All hosts communicate with 0% packet loss)

### 4. Block Host
h1 ifconfig h1-eth0 down

### 5. Test Again
pingall
(Packet loss observed)

## Output

### Before Blocking
- All hosts reachable
- 0% packet loss

### After Blocking
- h1 cannot communicate
- Packet loss observed (~66%)

## Conclusion
Dynamic host blocking is successfully implemented using SDN. The controller enforces network behavior by restricting communication from a specific host.

## Author
Ganavi S
