# Monitoring Setup

Installed Netdata on Ubuntu homelab for real-time monitoring.

## What is monitored
- CPU usage
- Memory usage
- Disk activity
- Network traffic
- Docker containers
- System processes

## Access
Netdata dashboard runs on port 19999.

## Commands used
- sudo systemctl status netdata
- sudo ufw allow 19999
- docker ps
