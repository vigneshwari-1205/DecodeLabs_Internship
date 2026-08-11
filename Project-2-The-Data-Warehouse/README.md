# Project 3: The Data Warehouse

## Scenario
An e-commerce company is struggling with Excel sheets to manage customer data. As their user base grows, they need a robust, scalable, and secure cloud database to store user records reliably.

## Mission
Provision a managed cloud database using Amazon RDS inside a private, secure network — accessible only through a bastion host — and verify data persistence.

## Architecture
- **VPC**: Custom VPC (10.0.0.0/16) with public and private subnets across 2 Availability Zones
- **Public Subnet**: Hosts the EC2 bastion host with a public IP
- **Private Subnet**: Hosts the RDS MySQL instance — no public IP, no direct internet access
- **Bastion Host**: EC2 instance used as an SSH gateway into the private subnet
- **Security Groups**:
  - RDS SG allows inbound MySQL (port 3306) only from the bastion's SG
  - Bastion SG allows inbound SSH (port 22) only from my IP
- **Connection Path**: Local Machine → SSH Tunnel → Bastion (EC2) → RDS (Private Subnet)

## Steps Performed
1. Created a custom VPC with public and private subnets across 2 AZs
2. Attached an Internet Gateway and configured route tables
3. Launched an EC2 bastion host in the public subnet
4. Created a DB Subnet Group using the private subnets
5. Provisioned an Amazon RDS MySQL instance with Public access disabled
6. Restricted the RDS security group to allow port 3306 only from the bastion's security group
7. Connected to RDS via MySQL Workbench using Standard TCP/IP over SSH
8. Created the `Interns` table with schema constraints
9. Inserted dummy records and verified persistence with a SELECT query
10. Verified connectivity independently using a Python script (pymysql) over an SSH tunnel

## Database Schema
```sql
CREATE TABLE Interns01 (
  InternID INT PRIMARY KEY,
  Name VARCHAR(50) NOT NULL,
  Role VARCHAR(50) NOT NULL,
  Email VARCHAR(100) UNIQUE NOT NULL
);
```

## Sample Data
```sql
INSERT INTO Interns01 (InternID, Name, Role, Email) VALUES
(1, 'Vigneshwari', 'Cloud Intern', 'vignesh@decodelabs.com'),
(2, 'Arjun', 'DevOps Intern', 'arjun@decodelabs.com'),
(3, 'Priya', 'Data Intern', 'priya@decodelabs.com');
```

## Verification

**MySQL Workbench**
![Workbench Select Query](workbench-select-query.png)

**Python Script (Bonus)**
![Python Output](python-output.png)

**RDS Instance (Private, Available)**
![RDS Instance Details](rds-instance-details.png)

**Security Group Rules**
![Security Group Rules](security-group-rules.png)

## Core Skills Demonstrated
- **Amazon RDS** — Managed relational database provisioning, engine/instance configuration
- **VPC Networking** — Public/private subnet design, route tables, isolation
- **Bastion Host Pattern** — Secure SSH-tunneled access to private resources
- **Security Groups** — Least-privilege, source-restricted firewall rules
- **SQL** — DDL (CREATE TABLE with constraints) and DML (INSERT, SELECT)
- **Python (pymysql)** — Programmatic database connectivity over SSH

## Tools Used
AWS VPC · Amazon EC2 · Amazon RDS (MySQL) · MySQL Workbench · Python (pymysql) · SSH Tunneling

## Key Learning
A publicly accessible database is a security risk. Placing RDS in a private subnet and requiring an SSH tunnel through a bastion host keeps the database completely unreachable from the public internet while remaining fully usable by authorized engineers.
