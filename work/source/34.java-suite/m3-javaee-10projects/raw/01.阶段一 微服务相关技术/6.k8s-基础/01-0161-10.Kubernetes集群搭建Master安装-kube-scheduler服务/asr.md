# 声音线转写：10.Kubernetes集群搭建Master安装-kube-scheduler服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.Kubernetes-基础
- 源文件：01.阶段一 微服务相关技术\6.Kubernetes-基础\10.Kubernetes集群搭建Master安装-kube-scheduler服务_【海量资源尽在 ubkz.com】.mp4
- 时长：1分47秒（音频 107s）
- 转写：faster-whisper-large-v3 / 语言 zh / 4 段
- 生成时间：2026-10-27 10:30:19

## 逐段转写（教师原声）

[00:00] 接下来我们就是Kubernetes Schedule这幅那么它也一样它也是依赖于Kubernetes API所以我们首先也去编辑一下它的Service你编辑它Service的时候其实你就会看到它里面会指定我们当前是依赖于我们刚才所说的Kubernetes API这里边不有个request吗Kubernetes API.Service所以大家要看一下这个
[00:28] 我粘贴的时候注意一下我别去把所有东西都粘过来因为这个讲义上中间会有一些东西啊所以这里边呢我这么一点点分开粘OK那粘贴完以后呢我们退出保存接下来呢我们就要去做它的一个配置文件跟刚才差不多我们过来编辑这个文件那这个文件大家也注意看哦原来我们那个叫做什么呢上面那个服务
[01:00] 我们叫KuberControllerManager看到了吗而现在这个是KuberSchedule所以这里边大家粘贴也要注意了然后同样的道理你一定要注意的就是我们要修改我当前的IP地址因为这时候会涉及到什么我们当前的Master的IP你就必须再告诉他我当前Master IP是谁所以在这里边告诉他我们当前是147
[01:29] OK吧保存退出那这样呢我们整个Kubernetes这个集群的相关服务啊我们都配置完了那么我们Kubernetes的API ServerKubernetes Controller Manager还有Kubernetes Schedule一会儿呢我们就要去启动它
