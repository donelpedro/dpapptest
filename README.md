# dpapptest

assumed dockerhub is used as a container registry `docker login` required  
  note: Image is already in repository
```
docker build -t "pyapptest:v2" .
docker tag pyapptest:v2 
docker push donped/pyapptest:v2
```
image name is used in k8s manifest `donped/pyapptest:v2`
to deploy application in k8s cluster use:
```
kubeclt create -f k8s/pyapp_deployment.yaml
```

#### expected result: 
```
kubectl get pods
NAME                    READY   STATUS    RESTARTS   AGE
pyapp-995446d58-r75zt   1/1     Running   0          34m
pyapp-995446d58-sdfkh   1/1     Running   0          34m
pyapp-995446d58-z4w87   1/1     Running   0          34m
```
```
kubectl get pods -n nginx-ingress
NAME                             READY   STATUS    RESTARTS   AGE
nginx-ingress-7f68c7b965-j7nq9   1/1     Running   0          34m
nginx-ingress-7f68c7b965-lw696   1/1     Running   0          34m
nginx-ingress-7f68c7b965-nm8t7   1/1     Running   0          34m
```
```
kubectl get services
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   6h47m
pyapp        ClusterIP   10.99.169.235   <none>        80/TCP    35m
```
manifest is designed for a bbre metal env. there for external loadbalancer like haproxy is required
nodeport service should be created by :
```
kubectl create -f nodeport.yaml
```

#### expected result: 
```
kubectl get services -n nginx-ingress
NAME                    TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
ingress-service-metal   NodePort   10.101.225.196   <none>        80:30005/TCP   35m
```
port `30005` should be configured as a target in haproxy.

### How to test: ingress is set to route host: testapp
in case of bare metal setup without Loadbalancer where NODEIP is and ip address of any cluster node.
``` 
telnet <NODEIP> 30005
GET /ping HTTP/1.0
Host: testapp


```
  
```
HTTP/1.1 200 OK
Server: nginx/1.17.10
Date: Mon, 25 May 2020 18:06:56 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 2
Connection: close

OK
```
  
``` 
telnet <NODEIP> 30005
GET / HTTP/1.0
Host: testapp
```
  
```
HTTP/1.1 200 OK
Server: nginx/1.17.10
Date: Mon, 25 May 2020 18:11:54 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: close

successful!
```
