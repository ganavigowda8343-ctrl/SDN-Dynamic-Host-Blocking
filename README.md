# SDN Dynamic Host Blocking

## 📌 Overview

This project demonstrates **dynamic host blocking using Software Defined Networking (SDN)**. The system monitors network traffic and automatically detects and blocks malicious hosts based on abnormal behavior such as high packet rate.

---

## 🎯 Objective

* Detect malicious hosts dynamically
* Block hosts generating excessive traffic
* Improve network security using SDN

---

## ⚙️ Technologies Used

* **Mininet** – Network simulation
* **POX Controller** – SDN controller
* **OpenFlow Protocol** – Communication between controller and switch
* **Python** – Implementation

---

## 🧠 Concept

SDN separates:

* **Control Plane** → Controller (decision making)
* **Data Plane** → Switch (packet forwarding)

The controller monitors traffic and installs **flow rules dynamically** to control the network.

---

## 🌐 Topology

* Single switch topology
* 3 hosts: **h1, h2, h3**
* 1 switch: **s1**
* Controlled by POX controller

---

## 👨‍💻 Host Roles

* **h1** → Sender / attacker (during demo)
* **h2** → Receiver / victim
* **h3** → Normal host (unaffected)

---

## 🔁 Working

1. Network is created using Mininet
2. Controller listens to packet-in events
3. Packet rate is tracked for each host
4. If packet rate exceeds threshold:

   * Host is identified as malicious
   * Flow rule is installed to **DROP packets**
5. Other hosts continue normal communication

---

## 🚫 Dynamic Blocking Logic

* Maintains packet timestamps per host
* Uses threshold-based detection
* Automatically blocks **any host** exceeding limit
* No hardcoded MAC addresses

---

## ▶️ How to Run

### Terminal 1 (Controller)

```
cd ~/pox
./pox.py log.level --DEBUG forwarding.l2_learning block
```

### Terminal 2 (Mininet)

```
sudo mn -c
sudo mn --topo single,3 --controller remote
```

### Inside Mininet

```
pingall
h1 ping -f h2
```

---

## 📊 Output

* Initially all hosts communicate normally
* When attack is generated:

  * Controller detects abnormal traffic
  * Displays: **“Dynamically blocking <MAC>”**
  * Installs flow rule to drop packets
* Malicious host is blocked
* Other hosts remain unaffected

---

## ✅ Advantages

* Real-time detection
* Automatic blocking
* Centralized control
* Improved network security

---

## ⚠️ Limitations

* Threshold-based detection
* May cause false positives
* Works in simulated environment

---

## 🚀 Future Scope

* Use Machine Learning for better detection
* Extend to large-scale networks
* Add persistent storage (database)

---

## 🎯 Conclusion

This project demonstrates how SDN enables **dynamic and automated security mechanisms** by detecting and blocking malicious hosts in real time.
