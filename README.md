# Phishing Website Detection using Machine Learning

## Project Overview

Phishing attacks are one of the most common cybersecurity threats where attackers create fake websites that imitate legitimate platforms to steal sensitive information such as passwords, credit card details, and personal data.

This project focuses on building a **machine learning model that can automatically detect phishing websites** based on various characteristics of URLs, domain information, and webpage behavior.

The model analyzes multiple features extracted from websites, such as URL structure, domain properties, security indicators, and webpage behavior, to determine whether a website is **legitimate or phishing**.

---

## Dataset Description

The dataset used in this project contains multiple features that describe different aspects of a website. These features include:

* URL-based features (URL length, presence of IP address, use of URL shortening services)
* Domain-based features (domain age, DNS records, domain registration length)
* Security features (SSL certificate status, HTTPS usage)
* Website behavior features (popups, iframes, redirection behavior)
* Website popularity indicators (web traffic, page rank, Google indexing)

Each record in the dataset represents a website and contains a **label indicating whether the website is legitimate or phishing**.
