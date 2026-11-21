# 声音线转写：14.Kubernetes集群搭建Node安装-kube-proxy服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.Kubernetes-基础
- 源文件：01.阶段一 微服务相关技术\6.Kubernetes-基础\14.Kubernetes集群搭建Node安装-kube-proxy服务_【海量资源尽在 ubkz.com】.mp4
- 时长：2分4秒（音频 125s）
- 转写：faster-whisper-large-v3 / 语言 zh / 5 段
- 生成时间：2026-10-27 10:30:43

## 逐段转写（教师原声）

[00:00] 下面呢我们说一下当前我们这个Coopers Proxy那么对于Coopers Proxy来说啊它是依赖于Network的那么Network服务呢大家如果这个遇到了问题呢可以参考上我讲义上给大家提供的这四种解决方案基本上就能解决你的Network这个服务的问题那我们来看一下对于这个Coopers Proxy我们要想操作它呢首先第一件事啊
[00:25] 你需要去编辑一下kuberproxy.Service这个服务的配置文件所以我们在这里编vi-usr下的lab下的我们systemd下的system下的一个叫做kuber-proxy.pyxyvse在这个文件里面我们要去指定一下
[00:53] 大家来看一下这里边我们是不是需要了network serviceOK吧那我们把它呢配置一下然后呢我们的save.jj退出退出以后呢我们接下来要配置的是Kubernetes自己的配置文件一个叫etc下的Kubernetes下的proxy也就是说我们在这里边需要vi我们etc下的Kubernetes下的一个叫做proxyproxy这名配置文件在这个配置文件里边
[01:22] 你要注意了我们还涉及到IP地址的问题我们在这编辑它那我呢需要把这个位置控制一下我们要连接的master一定要注意它是1478080没问题而我们自己的IP是148这个一定要注意啊这是我们自己的IP这个是master IPOK我们save的JJ保存
[01:57] 这样的话呢我们就已经把我们当前的Cooper Proxy配置完成
