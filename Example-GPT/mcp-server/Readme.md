> docker build -t mcp-server:latest .
> docker tag mcp-server:latest dexteromen/mcp-server:latest
> docker push dexteromen/mcp-server:latest 
> kubectl apply -f k8s
> kubectl get pods && kubectl get svc
> kubectl port-forward pod/mcp-server-8bfcff556-sdln4 5000:5000
> open http://localhost:5000/health