# 画面线理解：26.总结

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\26.总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:26, 02:03, 02:17, 02:48, 02:51, 02:55, 03:00, 03:24, 03:28, 03:44, 03:59, 04:30, 04:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:28:38

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了如何使用 Docker、Jenkins、Rancher、InfluxDB 和 cAdvisor 等工具构建微服务的持续集成与监控体系。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 学习目标：掌握 DockerMaven 插件的使用、Jenkins 的安装与使用、Rancher 的安装与使用、InfluxDB 的安装与使用、cAdvisor 的安装与使用、Grafana 的使用。
- 1 DockerMaven 插件：介绍两种部署方式，重点讲解自动部署。
- Maven 插件自动部署步骤：修改主机的 docker 配置，让其可以远程访问。
- 代码片段：`vi /lib/systemd/system/docker.service`

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
        <!-- dockerMaven插件，官网：https://github.com/spotify/docker-maven-plugin -->
        <plugin>
            <groupId>com.spotify</groupId>
            <artifactId>docker-maven-plugin</artifactId>
            <version>0.4.15</version>
            <configuration>
                <imageName>192.168.184.141:5000/${project.artifactId}:${project.version}</imageName>
                <baseImage>jdk1.8</baseImage>
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
- 代码片段：`docker run -d --name-base -p 9001:9001 192.168.184.141:5000/tensquare_base:1.0-SNAPSHOT`

画面 4:
- 3 容器管理工具Rancher。
- 3.1 什么是Rancher：介绍其功能。
- 3.2 Rancher安装：
  - (1) 下载Rancher 镜像：`docker pull rancher/server`
  - (2) 创建Rancher容器：`docker run -d --name=rancher -p 9090:8080 rancher/server`

画面 5:
- 3.3.2 添加主机：在 Rancher 界面选择“主机”菜单，点击“添加主机”。
- 3.3.3 添加应用：点击“应用”→“全部（或用户）”，点击“添加应用”按钮。

画面 6:
- 3.3.3 添加应用：在“添加应用”页面填写应用信息，点击“创建”按钮。

画面 7:
- 3.4.4 微服务部署。
- (1) 启动私有仓库：`docker run -d --name=registry -p 5000:5000 registry`
- (2) 修改 docker 配置：`vi /etc/docker/daemon.json`
- 代码片段：
```json
{"insecure-registries":["192.168.184.141:5000"]}
```

画面 8:
- (2) 修改 docker 配置，允许远程访问。
- 代码片段：
```bash
vi /lib/systemd/system/docker.service
```
- 修改后重新加载服务：
```bash
systemctl daemon-reload
systemctl restart docker
docker start registry
```

画面 9:
- (4) 填写名称和要扩容的服务，点击“创建按钮”。
- 代码片段：
```json
{
  "name": "scale-base",
  "type": "扩展服务",
  "operation": "扩容",
  "targetService": "tensquare/base-service",
  "step": 2,
  "min": 1,
  "max": 20
}
```

画面 10:
- 4 influxDB。
- 4.1 什么是 influxDB：介绍其作用。
- 4.2 influxDB 安装：
  - (1) 下载镜像：`docker pull tutum/influxdb`
  - (2) 创建容器：`docker run -d \ -p 8083:8083 \ -p 8086:8086`

画面 11:
- 4.2 influxDB 安装：创建容器命令。
- 代码片段：
```bash
docker run -d \
  -p 8083:8083 \
  -p 8086:8086
```

画面 12:
- 5 cAdvisor。
- 5.1 什么是 cAdvisor：介绍其功能。
- 5.2 cAdvisor 安装：
  - (1) 下载镜像：`docker pull google/cadvisor`
  - (2) 创建容器：`docker run -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -p 8080:8080 --link influxdb:influxdb -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var
