# Secure CI/CD Pipeline (DevSecOps Demo)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.9-blue)
![Security](https://img.shields.io/badge/security-automated-red)

# Welcome!
This project is a Proof of Concept (POC) to demonstrate **"Shifting Security Left"**.
Instead of waiting for a security audit *after* deployment, this pipeline uses **GitHub Actions** to automatically scan code for vulnerabilities, secrets, and bad patterns every time a developer commits code.

---

# How It Works (The Workflow)

Here is the automated logic that runs on every `git push`:

Code Commit ➔  Linting (Flake8) ➔  SAST Scan (Bandit) ➔ Dependency Check (Safety) ➔ Build/Deploy
