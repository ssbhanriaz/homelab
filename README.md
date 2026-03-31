## DevOps Homelab

This project demonstrates a complete on-prem DevOps environment built on Ubuntu, simulating real-world infrastructure with containerization, reverse proxy, monitoring, logging, security, and automation.

---

## Architecture

User → Nginx Reverse Proxy → Docker Containers  
├── Portfolio App  
├── App2 Service  
└── Monitoring (Netdata)  

System Logs → Log Analysis (Python)  
Automation → Ansible Playbooks  

---

## Tech Stack

- Ubuntu Linux  
- Docker & Docker Compose  
- Nginx (Reverse Proxy)  
- Netdata (Monitoring)  
- Python (Log Analysis)  
- Ansible (Automation)  
- UFW & Fail2ban (Security)  

---

## Features

- Multi-container application deployment  
- Nginx reverse proxy routing (`/portfolio`, `/app2`)  
- Real-time system monitoring dashboard  
- Log analysis for detecting errors and failed logins  
- Secure server configuration (SSH, firewall, Fail2ban)  
- Infrastructure automation using Ansible  

---

## Project Structure

```

homelab/
├── ansible/
│   ├── setup.yml
│   ├── deploy.yml
│   └── inventory
├── apps/
│   ├── portfolio/
│   └── app2/
├── docker-compose.yml
├── logging/
├── monitoring/

````

---

## How to Run

### Start services

```bash
docker compose up -d
````

### Run automation

```bash
ansible-playbook ansible/setup.yml
ansible-playbook ansible/deploy.yml
```

---

## Access

* Portfolio: [http://localhost/portfolio/]
* App2: [http://localhost/app2/]
* Monitoring: [http://localhost:19999]

---

## Monitoring

Netdata provides real-time insights into:

* CPU usage
* Memory usage
* Docker container performance
* Network activity

---

## Logging & Analysis

* Nginx access & error logs
* Python scripts for:

  * detecting 404/500 errors
  * tracking failed SSH logins

---

## Security

* Disabled root SSH login
* Key-based authentication
* Firewall rules using UFW
* Fail2ban for brute-force protection

---

## Automation

Ansible playbooks automate:

* Package installation
* Service configuration
* Docker deployment

---

## Learning Outcomes

This project helped me gain hands-on experience in:

* Linux system administration
* DevOps workflows
* Infrastructure automation
* Monitoring & observability
* Security best practices

---

## Screenshots
<img width="1918" height="995" alt="app2" src="https://github.com/user-attachments/assets/bae0cbc6-1bc5-4f35-b025-038a5c93f26f" />
<img width="1918" height="918" alt="Container monitor" src="https://github.com/user-attachments/assets/fa7e8a6e-c597-448e-9a09-493f56139a7b" />
<img width="1917" height="998" alt="portfolio" src="https://github.com/user-attachments/assets/182d0d9a-c0ec-4e91-8392-2c74f592cbc2" />
<img width="1192" height="279" alt="docker ps" src="https://github.com/user-attachments/assets/1d19a5eb-1be3-44ed-b924-e12eb2dd7361" />



---

## Author

**Subhan Riaz**
GitHub: [https://github.com/ssbhanriaz]
