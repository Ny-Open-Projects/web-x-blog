# 26.总结

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\26.总结_【海量资源尽在 ubkz.com】.mp4
- 时长 4分51秒（音频 291s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好最后呢我们对本章内容做一个总结今天我们主要学的啊其实就是一个插件无中软件的一个使用那么第一个我们讲的这个插件是叫Docker Maven插件那么这个插件主要的作用是什么呢主要的作用就是可以使我们的微服务工程能够啊能够实现什么呢这个自动的
[00:29] 生成一个镜像并且呢将这个镜像上传到这个私有仓库之中这是我们说Maven插件的一个使用那么接下来我们要讲这个持续集成工具Jackens的这么一个安装和使用那么这时候什么叫持续集成呢这个持续集成实际上就是我们在开发的过程中可以通过这个工具通过这个工具能够这个
[00:57] 经常性的将我们的软件产品部署到一个测试的环境之中来产生这么一个测试版本那么这样的话就使我们的集成就可以常态化那这样做的好处是什么呢第一我们能够不断的产生最新的软件版本第二我们可以在集成之后尽早的发现我们软件中存在的一些问题
[01:26] 这是我们说持续集成工具的一个使用那么在互联网开发中的持续集成是一个很常见的这么一个操作那么当然这个持续集成它要依赖于Gate这样的软件因为持续集成它需要从Gate上来获取这个源代码然后通过调用本地的JDK和一些Maven就是来去
[01:54] 生成一些容器生成一些容器和镜像这是我们说的这个持续集成工具的一个使用那么接下来我们讲的就是容器相关了容器相关的工具就是runter那么这个runter是干嘛的呢我们说这个jackens主要是用来去生成根据代码来生成镜像那么这个runter的作用就是根据镜像来生成容器和管理容器那么我们说
[02:25] Docker本身它也是管理容器的而Rancher是基于Docker的一个图形化管理界面那么通过它的可以实现对容器的管理另外还提供了负载均衡等等这些功能这是非常实用的那么我们在这里头也是需要对它进行一些初始的设置比如说我要添加环境添加主机添加应用然后我们在应用上去增加一些服务比如说我们可以配Maths Circle
[02:53] payrapidmqpayredis以及我们自己的微服务都可以通过图形化的界面的方式来进行构建了它还提供了一个非常强大的功能叫扩容与缩容这样一来我们可以去扩充我们的微服务的容器的数量这样的话就可以使我们的某一个服务能够自动搭建一个可扩充的机群这是非常常用的
[03:23] 然后接下来我们再看influke cbinfluke cb和我们的ranger以及我们后面讲的cadvancer,grafana这几个软件之间其实都是有联系的influke cb是什么是一个时间序列数据库它的作用是用来存储它的作用是用来存储我们的容器的一些运营的一些数据那么我们说cadvancer干嘛的它是作为监控数据
[03:52] 它是作为监控的一个工具它主要作用是监控Docker容器那么监控Docker容器产生的一些数据放哪呢这时候它可以把数据放到我们的influencedDB里那么放在influencedDB之后呢我们这个Graphana它又是干嘛的呢它也是负责它是负责读这个influencedDB这个C-Advanced是负责往这里写而这个Graphana作用是负责读读取这个influencedDB然后呢
[04:20] 展示一个图表的数据那么当然它还有个功能叫预警那么预警就是当我达到了某一个值的时候它会自动触发一个预警那么这个预警会去什么它会去操作我们run车里的一个web构思地址这样的话可以实现容器的扩充与缩减这是我们说的关于今天我们所讲的持续集成和容器管理咱们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了如何使用 Docker、Jenkins、Rancher、InfluxDB 和 cAdvisor 等工具构建微服务的持续集成与监控体系。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 学习目标：掌握 DockerMaven 插件的使用、Jenkins 的安装与使用、Rancher 的安装与使用、InfluxDB 的安装与使用、cAdvisor 的安装与使用、Grafana 的使用。
- 1 DockerMaven 插件：介绍两种部署方式，重点讲解自动部署。
- Maven 插件自动部署步骤：修改主机的 Docker 配置，让其可以远程访问。
- 代码片段：`vi /lib/systemd/system/Docker.Service`

画面 2:
- (3) 在工程 pom.xml 增加配置。
- 代码片段：
```xml
<build>
    <finalName>${project.artifactId}</finalName>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
        <!-- dockerMaven插件，官网：https://github.com/spotify/Docker-maven-plugin -->
        <plugin>
            <groupId>com.spotify</groupId>
            <artifactId>Docker-maven-plugin</artifactId>
            <version>0.4.15</version>
            <configuration>
                <imageName>192.168.184.141:5000/${project.artifactId}:${project.version}</imageName>
                <baseImage>JDK 8</baseImage>
                <entryPoints>
                    <entryPoint>java, -jar, ${project.build.finalName}.jar</entryPoint>
                </entryPoints>
                <resources>
                    <resource>
                        <targetPath>${targetPath}</targetPath>
                    </resource>
                </resources>
            </configuration>
        </plugin>
    </plugins>
</build>
```

画面 3:
- 2 持续集成工具-Jenkins。
- 2.1 什么是持续集成：定义、特点、必要条件。
- 代码片段：`Docker run -d --name-base -p 9001:9001 192.168.184.141:5000/tensquare_base:1.0-SNAPSHOT`

画面 4:
- 3 容器管理工具Rancher。
- 3.1 什么是Rancher：介绍其功能。
- 3.2 Rancher安装：
  - (1) 下载Rancher 镜像：`Docker pull rancher/server`
  - (2) 创建Rancher容器：`Docker run -d --name=rancher -p 9090:8080 rancher/server`

画面 5:
- 3.3.2 添加主机：在 Rancher 界面选择“主机”菜单，点击“添加主机”。
- 3.3.3 添加应用：点击“应用”→“全部（或用户）”，点击“添加应用”按钮。

画面 6:
- 3.3.3 添加应用：在“添加应用”页面填写应用信息，点击“创建”按钮。

画面 7:
- 3.4.4 微服务部署。
- (1) 启动私有仓库：`Docker run -d --name=registry -p 5000:5000 registry`
- (2) 修改 Docker 配置：`vi /etc/Docker/daemon.json`
- 代码片段：
```json
{"insecure-registries":["192.168.184.141:5000"]}
```

画面 8:
- (2) 修改 Docker 配置，允许远程访问。
- 代码片段：
```bash
vi /lib/systemd/system/Docker.Service
```
- 修改后重新加载服务：
```bash
systemctl daemon-reload
systemctl restart Docker
Docker start registry
```

画面 9:
- (4) 填写名称和要扩容的服务，点击“创建按钮”。
- 代码片段：
```json
{
  "name": "scale-base",
  "type": "扩展服务",
  "operation": "扩容",
  "targetService": "tensquare/base-Service",
  "step": 2,
  "min": 1,
  "max": 20
}
```

画面 10:
- 4 influxDB。
- 4.1 什么是 influxDB：介绍其作用。
- 4.2 influxDB 安装：
  - (1) 下载镜像：`Docker pull tutum/influxdb`
  - (2) 创建容器：`Docker run -d \ -p 8083:8083 \ -p 8086:8086`

画面 11:
- 4.2 influxDB 安装：创建容器命令。
- 代码片段：
```bash
Docker run -d \
  -p 8083:8083 \
  -p 8086:8086
```

画面 12:
- 5 cAdvisor。
- 5.1 什么是 cAdvisor：介绍其功能。
- 5.2 cAdvisor 安装：
  - (1) 下载镜像：`Docker pull google/cadvisor`
  - (2) 创建容器：`Docker run -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -p 8080:8080 --link influxdb:influxdb -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var/run/Docker.sock -v /var/lib/Docker:/var/lib/Docker -v /var/run/Docker.sock:/var

