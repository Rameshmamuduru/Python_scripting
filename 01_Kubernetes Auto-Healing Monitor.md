# 1. Kubernetes Auto-Healing Monitor ☸️

### Problem

Pods sometimes go into:

* `CrashLoopBackOff`
* `ImagePullBackOff`
* `Pending`

Manually checking with **kubectl** is time-consuming.

### Solution

Python script automatically:

* Checks pod status
* Restarts unhealthy pods
* Sends alerts to Slack/Email

### Architecture

```
Python Script
     │
     │ (kubectl / API)
     ▼
Kubernetes Cluster
     │
     ▼
Detect Failed Pods
     │
     ▼
Restart Pod + Send Alert
```

### Tools

* **Kubernetes**
* **kubectl**
* Python subprocess / Kubernetes API
