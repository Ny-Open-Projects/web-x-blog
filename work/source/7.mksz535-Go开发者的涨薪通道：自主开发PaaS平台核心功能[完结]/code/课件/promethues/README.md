### Prometheus 安装说明

#### 1.解压 zip 包
```cassandraql
unzip v0.9.0.zip
```

#### 2.进入目录 
```cassandraql
cd kube-prometheus-0.9.0
```

#### 3.执行安装命令
```cassandraql
//创建命名空间和CRD
kubectl create -f manifests/setup

//等待创建结束
until kubectl get servicemonitors --all-namespaces ; do date; sleep 1; echo ""; done

//创建监控组件
kubectl create -f manifests/

//查看 monitoring 内的 pod
kubectl get pods -n monitoring
```

#### 4.添加路由外网访问
通过前一章开发的 route 功能添加 monitoring 命名空间下
grafana.caplost.com 域名
第一次登录默认账号：admin 密码：admin
