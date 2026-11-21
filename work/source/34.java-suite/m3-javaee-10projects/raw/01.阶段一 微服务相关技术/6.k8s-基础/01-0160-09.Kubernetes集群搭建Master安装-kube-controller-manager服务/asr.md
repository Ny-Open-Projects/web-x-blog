# 声音线转写：09.Kubernetes集群搭建Master安装-kube-Controller-manager服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.Kubernetes-基础
- 源文件：01.阶段一 微服务相关技术\6.Kubernetes-基础\09.Kubernetes集群搭建Master安装-kube-Controller-manager服务_【海量资源尽在 ubkz.com】.mp4
- 时长：2分12秒（音频 133s）
- 转写：faster-whisper-large-v3 / 语言 zh / 5 段
- 生成时间：2026-10-27 10:30:15

## 逐段转写（教师原声）

[00:00] 接下来我们就要安装这个叫做Kubernetes Controller Manager这里面有这句话非常重要Kubernetes Controller Manager服务它是依赖于Kubernetes API Server的所以你要注意如果你之前的Kubernetes API Server失败了安装那么我们Kubernetes Controller Manager肯定是不OK的这个时候你也需要去执行一些操作所以我们来看一下首先它告诉你还是在System D下你要去创建一个叫做Kubernetes Controller Manager Service这个文件
[00:29] 这里边我就不写了我直接copy过来Ctrl C在这里呢我们去编辑这个文件在这个文件里边呢你看一下它要写一些东西OK把这部分Ctrl C粘贴过来这样呢我们当前的Cooper Controller Manager就安装完成然后呢我们需要去配置一下这里边配置的时候你注意了一定要注意你的IP地址
[01:00] 注意那我们当前的电脑的IP是147所以你在去用的时候你不能说我只是把这个粘贴过来了你要去注意一下你自己的IP地址OK所以这里边我们看一下它呢需要去创建这么一个文件那这个文件呢我们把这些配置信息copy一下粘贴过来这个路径啊这格式位促进一下
[01:39] 然后呢我们一定要去把这一块改了我master这个机器它是147ok吧192.168.126.147那你在安装时你要根据你自己master这个主机的IP啊去设置那如果你设置有问题那我们这个服务啊就不会起来了ok吧那这样的话呢我现在把我这个Controller manager这服务啊也就安装完成
[02:09] save the jj 退出保存
