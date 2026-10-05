# 工具制作说明
工具可执行文件基于 linux 环境制作，go版本1.16
## protoc 和 protoc-gen-go 的安装
### 1.下载对应版本的 protoc 
```
镜像中使用如下命令下在 dockerfile 中
 apk add protoc
```
### 2.下载安装 go 的插件protoc-gen-go 
```
go install github.com/golang/protobuf/protoc-gen-go@v1.27
```
注意：要用protoc-gen-go@v1.27 版本 
### 3.安装gen-micro
这里选择的是 v3 的版本
在课程制作的过程中 go-micro v4 刚出来测试过和proto 还有兼容问题等稳定可以切换
```
go get -u github.com/asim/go-micro/cmd/protoc-gen-micro/v3    
```
### 4.安装完成后在安装的机器上运行
protoc 