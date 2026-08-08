# Project 2: The Server Commander

## 📌 Objective
Provision a virtual server on AWS EC2, secure it with proper access 
controls, connect remotely via SSH, and deploy a live web server 
hosting a custom webpage — simulating a real-world SysAdmin task.

## 🛠️ Tools & Technologies
- **AWS EC2** (Amazon Linux 2023, t3.micro)
- **SSH** (Windows PowerShell)
- **Nginx** (Web Server)
- **AWS Security Groups** (Firewall)

## 🚀 Steps Performed

### 1. Launched EC2 Instance
- AMI: Amazon Linux 2023
- Instance type: t3.micro (Free Tier eligible)
- Created a new key pair (`.pem`) for secure authentication

### 2. Configured Security Groups
| Type  | Port | Source           |
|-------|------|------------------|
| SSH   | 22   | My IP only       |
| HTTP  | 80   | Anywhere (0.0.0.0/0) |

### 3. Connected via SSH
```bash
ssh -i "servercommander.pem" ec2-user@<Public-IP>
```
Resolved a Windows file-permission issue using:
```powershell
icacls.exe .\servercommander.pem /reset
icacls.exe .\servercommander.pem /grant:r "$($env:username):(R)"
icacls.exe .\servercommander.pem /inheritance:r
```

### 4. Installed & Started Nginx
```bash
sudo dnf update -y
sudo dnf install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

### 5. Deployed Custom Webpage
Edited `/usr/share/nginx/html/index.html` to display a custom 
welcome message.

### 6. Verified Deployment
Accessed `http://<Public-IP>` in the browser — confirmed the 
custom page loads successfully.

## 📷 Screenshots
| Step | Screenshot |
|------|-----------|
| EC2 Instance Running | `screenshots/ec2-instance-running.png` |
| SSH Connection Established | `screenshots/ssh-connection.png` |
| Nginx Active Status | `screenshots/nginx-status.png` |
| Live Webpage | `screenshots/webpage-live.png` |

## 💡 Key Learnings
- Security Groups follow an **allow-only** model — all traffic is 
  denied by default unless explicitly permitted.
- Restricting SSH access to a specific IP significantly reduces 
  attack surface compared to leaving it open to "Anywhere."
- Stopping and restarting an EC2 instance assigns a **new public IP** 
  unless an Elastic IP is attached — an important operational detail 
  for production environments.
- File permission handling differs between Windows and Linux; 
  `.pem` key files require restricted read-only access before SSH 
  will accept them.

## ✅ Result
Successfully provisioned, secured, and deployed a live web server 
on AWS EC2, demonstrating end-to-end Infrastructure-as-a-Service 
(IaaS) skills.

---
**Internship:** Cloud Computing (AWS/Azure) — DecodeLabs  
**Project:** 2 of 4 — The Server Commander

