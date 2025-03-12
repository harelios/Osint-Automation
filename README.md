# Automation OSINT

## Overview
**Automation OSINT** is a tool designed to automate Open Source Intelligence (OSINT) tasks by collecting and analyzing publicly available information. It includes several modules for retrieving data related to IP addresses, domains, subdomains, and email addresses.

## Features
- **IP Lookup**: Retrieves detailed information about an IP address, including location and connection type.
- **Whois Lookup**: Retrieves WHOIS information for a given domain.
- **Email Finder**: Extracts email addresses associated with a domain by analyzing web pages.
- **Subdomain Scanner**: Identifies subdomains of a given domain using a wordlist-based approach.
- **Graphical User Interface**: Provides a simple UI for executing OSINT tasks.

## Installation
### Prerequisites
Ensure you have the following dependencies installed before running the project:
- Python 3.x
- Required Python libraries (can be installed using `requirements.txt`)

### Install Dependencies
Run the following command to install all required dependencies:
```bash
pip install -r requirements.txt

Usage
Running the Main Application
To launch the OSINT automation tool with the graphical interface, execute:

Main.py
Running Individual Modules
Each module can also be executed separately from the command line:

IP Lookup
You will be prompted to enter an IP address.

Whois Lookup
You will be prompted to enter a domain name.

Email Finder
You will be prompted to enter a domain, and the script will attempt to find associated email addresses.

Subdomain Scanner
You will be prompted to enter a domain and specify the wordlist range to scan.

File Structure

Automation-OSINT/
│── Ip_Lookup.py              # IP lookup tool
│── Whois_Lookup.py           # WHOIS lookup tool
│── Email_Finder.py           # Email extraction tool
│── SubDomains_Scanner.py     # Subdomain scanner
│── Subdomains_wordlist.txt   # Wordlist for subdomain enumeration
│── Main.py                   # GUI-based OSINT automation tool
│── requirements.txt          # List of dependencies
│── README.md                 # Project documentation

License
This project is released under the MIT License.

Disclaimer
This tool is intended for educational and research purposes only. The developer is not responsible for any misuse of the software.

This README follows professional documentation standards, providing a clear project overview, installation steps, usage instructions, and legal disclaimers. Let me know if you need modifications.

## Author
Developed by [harelios](https://github.com/harelios).