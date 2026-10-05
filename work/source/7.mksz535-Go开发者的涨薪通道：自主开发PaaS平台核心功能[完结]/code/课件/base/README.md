# Base  
慕课网 Cap 老师已上课程购买地址：http://www.imooc.com/t/6512963

当前代码名称 Base  

##1.快速创建代码仓库请使用下方命令
```
sudo docker run --rm -v $(pwd): $(pwd) -w  $(pwd) -e ICODE=xxxxxx cap1573/cap-tool new git.imooc.com/cap1573/base

注意：
1.sudo 如果是 Mac 系统提示输入的密码是你本机的密码。
2.以上命令ICODE=xxxxxx 中 "xxxxxx" 为个人购买的 icode 码。
3.icode 码在购买完课程后，请使用电脑点击进入学习课程页面。
4.请勿多人使用统一个 icode 码（会被慕课网检测封号）。
5.这里git.imooc.com/cap1573/base仓库 名字需要和 go mod 名称一致
```
 

##2.根据 proto 自动生成 go 基础代码
```
make proto
```

##3.根据代码编译现有 Go 代码  
```
make build
```
代码执行后会产生 base 二进制文件

##4.编译执行二进制文件
```
make docker
```
编译成功后会自动生成 base:latest 镜像
可使用 docker images | grep base 查看是否生成

##5.本课程使用 go-micro v3 版本作为微服务开发框架
框架地址：https://github.com/asim/go-micro


