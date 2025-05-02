# Visit
> https://github.com/bitnami/charts/tree/main/bitnami/redis

> helm pull oci://registry-1.docker.io/bitnamicharts/redis

> helm install my-redis ./redis-20.13.4.tgz
```
NAME: my-redis
LAST DEPLOYED: Thu May  1 14:02:38 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: redis
CHART VERSION: 20.13.4
APP VERSION: 7.4.3

Did you know there are enterprise versions of the Bitnami catalog? For enhanced secure software supply chain features, unlimited pulls from Docker, LTS support, or application customization, see Bitnami Premium or Tanzu Application Catalog. See https://www.arrow.com/globalecs/na/vendors/bitnami for more information.

** Please be patient while the chart is being deployed **

Redis&reg; can be accessed on the following DNS names from within your cluster:

    my-redis-master.default.svc.cluster.local for read/write operations (port 6379)
    my-redis-replicas.default.svc.cluster.local for read-only operations (port 6379)



To get your password run:

    export REDIS_PASSWORD=$(kubectl get secret --namespace default my-redis -o jsonpath="{.data.redis-password}" | base64 -d)

To connect to your Redis&reg; server:

1. Run a Redis&reg; pod that you can use as a client:

   kubectl run --namespace default redis-client --restart='Never'  --env REDIS_PASSWORD=$REDIS_PASSWORD  --image docker.io/bitnami/redis:7.4.3-debian-12-r0 --command -- sleep infinity

   Use the following command to attach to the pod:

   kubectl exec --tty -i redis-client \
   --namespace default -- bash

2. Connect using the Redis&reg; CLI:
   REDISCLI_AUTH="$REDIS_PASSWORD" redis-cli -h my-redis-master
   REDISCLI_AUTH="$REDIS_PASSWORD" redis-cli -h my-redis-replicas

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace default svc/my-redis-master 6379:6379 &
    REDISCLI_AUTH="$REDIS_PASSWORD" redis-cli -h 127.0.0.1 -p 6379

WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
  - replica.resources
  - master.resources
+info https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
```


# If you want to see the chart contents before installing (to edit values or templates):
> helm show values ./redis-20.13.4.tgz

OR extract it:

> tar -zxvf redis-20.13.4.tgz 

# Install with custom values:
If you have a custom values.yaml (e.g., changing password, persistence, etc.):

> helm install my-redis ./redis-20.13.4.tgz -f my-values.yaml

# Bonus Tip: Test it's working

Once installed, check the release:

> helm list && kubectl get pods && kubectl get svc