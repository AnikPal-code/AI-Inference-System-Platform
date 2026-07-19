# 🚀 Running the Project Locally (Kubernetes)

## Prerequisites

- Docker Desktop
- Kubernetes enabled in Docker Desktop
- kubectl installed
- Node.js (v18+)

---

## 1. Clone the Repository

```bash
git clone https://github.com/AnikPal-code/AI-Inference-System-Platform.git
cd AI-Inference-System-Platform
```

---

## 2. Start Kubernetes

Ensure Kubernetes is enabled in Docker Desktop.

Verify the cluster:

```bash
kubectl cluster-info
```

---

## 3. Deploy the Backend

Deploy all microservices:

```bash
kubectl apply -f kubernetes/
```

Verify that all pods are running:

```bash
kubectl get pods
```

Expected output:

```text
gateway-deployment     Running
sentiment-deployment   Running
resume-deployment      Running
image-deployment       Running
```

---

## 4. Verify Services

```bash
kubectl get services
```

If the Gateway Service is a `NodePort`, access it directly.

If it is a `ClusterIP`, forward the port:

```bash
kubectl port-forward service/gateway-service 8000:8000
```

The FastAPI API documentation will then be available at:

```
http://localhost:8000/docs
```

---

## 5. Run the Frontend

Open a new terminal:

```bash
cd frontend
npm install
npm start
```

Frontend:

```
http://localhost:3000
```

---

## 6. Stop the Application

Delete all Kubernetes resources:

```bash
kubectl delete -f kubernetes/
```

Or stop the local Kubernetes cluster from Docker Desktop.

---

## Useful Commands

Check Pods:

```bash
kubectl get pods
```

Check Services:

```bash
kubectl get services
```

View Pod Logs:

```bash
kubectl logs deployment/gateway-deployment
kubectl logs deployment/sentiment-deployment
kubectl logs deployment/resume-deployment
kubectl logs deployment/image-deployment
```

Restart Deployments:

```bash
kubectl rollout restart deployment/gateway-deployment
kubectl rollout restart deployment/sentiment-deployment
kubectl rollout restart deployment/resume-deployment
kubectl rollout restart deployment/image-deployment
```