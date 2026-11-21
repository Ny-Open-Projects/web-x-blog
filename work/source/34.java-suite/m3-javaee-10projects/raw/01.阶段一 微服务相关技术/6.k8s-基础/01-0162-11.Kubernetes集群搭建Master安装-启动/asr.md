# 声音线转写：11.Kubernetes集群搭建Master安装-启动

- 阶段：01.阶段一 微服务相关技术
- 章节：6.Kubernetes-基础
- 源文件：01.阶段一 微服务相关技术\6.Kubernetes-基础\11.Kubernetes集群搭建Master安装-启动_【海量资源尽在 ubkz.com】.mp4
- 时长：4分31秒（音频 271s）
- 转写：faster-whisper-large-v3 / 语言 zh / 10 段
- 生成时间：2026-10-27 10:30:27

## 逐段转写（教师原声）

[00:00] 接下来我们去把所有的服务都启动一下那么我们先systemctl daem1我们先去daem1我先去把整个去reload一下重新加载一下然后我们先去启动我们当前的etcd服务什么吧ableetcd然后我再去
[00:32] Start的ETCD大家可以看一下我当前的ETCD服务它是一个Active Running然后我们再把Docker服务起来然后我们可以看一下当前的Docker服务它也是一个Running接下来我们就可以去起我们当前的
[01:02] Kubernetes相关的服务首先我们起这个Kubernetes的API Server服务systemctl enabre kuber-api-server我们先把它进它enabre kuber-sorrystart应该是start kuber-api-server然后呢你呢在起完以后啊一定要看一下它的状态它是
[01:32] Active running说明我们的没问题的然后呢systemctl cooper-cuntoler-mnh1r我们把Controller manager起一下systemctl start cooper-Controller-mnh1rsystemctl sttus cooper-cuntoler-mnh1r这也是一个running
[02:03] 接下来我们要去起的是我们当前的这个scheduleStateCouple-SCHEDULERStateCouple-SCHEDULERStateCouple-SCHEDULER大家看一下我们当前的这个schedule服务他说我报错了
[02:33] 他说我这里边有问题应该是我们整个服务失败了我们看一下说我们这个位置并一下的Kuber Schedule告诉我们什么东西呢应该是我们在这个Schedule里面呢找不到应该是他的配置文件有问题我们看一下他的配置文件我们找一下Schedule我们这个Service文件应该没问题
[03:00] 他能找到这个服务那应该是我们这个配置文件里面有问题我们可以看看啊呃vi一下我们的etc下的cubernetes下的shedu l1看一下他你看一下这个值master没问题我们47找到这儿没问题然后你看看是不是其他的呢ok吧是不是前面这块我们在
[03:29] Coffee的时候应该少钻东西了,Kuber-SCH Schedule,Shift这回我们再重新去把我们这个Kuber-SCHEDULE进一下System Start Kuber-SCHEDULE我们重新起一下这回我们再看一下它的状态OK吧,这样的话呢,我这个
[03:59] 服务就起来了那整体上我整个服务全都起来也就是说我master这个节点基本搭建完了但是大家别忘了其实前期我们说过了你应该把你的防火墙都需要去禁掉或者说把它关闭所以你在这里边你要去把我们的fire wld防火墙关了因为你现在单击没问题一会儿我们要去通过node节点去连你的master那这个时候你要是不关防火墙
[04:28] 那么影响就大了
