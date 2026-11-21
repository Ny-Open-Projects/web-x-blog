# 画面线理解：02.DockerMaven插件-1

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\02.DockerMaven插件-1_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 01:41, 02:22, 02:43, 02:59, 03:20, 03:37, 04:01, 04:43, 05:33, 05:52, 06:54, 07:29, 07:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:15:50

1) 这一组画面整体在讲如何配置 Docker 和 Maven 插件以实现 Spring Boot 项目的自动打包和容器化部署。

2) 按时间顺序列出每张画面的要点：
画面1：讲解 Docker Maven 插件的使用，展示 Maven 项目中 pom.xml 的配置片段，其中包含 artifactId、groupId、version 等信息。
画面2：在终端中执行 docker ps 查看容器状态，显示 registry、mysql、nginx 等容器正在运行。
画面3：展示 docker.service 的配置文件内容，其中包含 ExecStart 和 ExecReload 的设置。
画面4：讲解修改 docker.service 配置，使其支持远程访问，并展示修改后的配置内容。
画面5：在终端中执行 systemctl daemon-reload 和 systemctl restart docker 命令，重启 Docker 服务。
画面6：展示在 pom.xml 中添加 Docker Maven 插件的配置，包括 <plugin> 标签和 <configuration> 内容。
画面7：展示 pom.xml 中的 <dependencies> 部分，包含 spring-boot-starter-data-jpa 等依赖。
画面8：在 IDEA 中编辑 pom.xml，高亮显示 Docker Maven 插件的 <configuration> 部分。
画面9：在终端中执行 docker images 命令，列出本地镜像。
画面10：在 IDEA 中编辑 pom.xml，高亮显示 <plugin> 标签。
画面11：在 IDEA 中编辑 pom.xml，高亮显示 <configuration> 内容。
画面12：在 IDEA 中编辑 pom.xml，高亮显示 <resources> 部分。
画面13：在 IDEA 中编辑 pom.xml，高亮显示 <configuration> 内容。
画面14：展示 Docker 仓库的界面，显示镜像列表和推送状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<artifactId>temsqare_parent</artifactId>
<groupId>com.tensquare</groupId>
<version>4.0.0</version>
<modelVersion>4.0.0</modelVersion>
```
画面4：
```ini
[Service]
Type=notify
# The default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# For containers run by docker.
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock
ExecReload=/bin/kill -s HUP $MAINPID
```
画面6：
```xml
<build>
    <finalName>app</finalName>
    <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
    </plugin>
    <plugin>
        <groupId>com.spotify</groupId>
        <artifactId>docker-maven-plugin</artifactId>
        <version>0.4.13</version>
        <configuration>
            <imageName>192.168.184.141:5000/${project.artifactId}:${project.version}</imageName>
            <baseImage>jdk1.8</baseImage>
            <entryPoint>["java", "-jar", "/${project.build.finalName}.jar"]</entryPoint>
            <resources>
                <resource>
                    <targetPath>/</targetPath>
                    <directory>${project.build.directory}</directory>
                    <include>${project.build.finalName}.jar</include>
                </resource>
            </resources>
            <dockerHost>http://192.168.184.141:2375</dockerHost>
        </configuration>
    </plugin>
</build>
```
画面14：
```json
{
    "repositories": ["tensquare_base"]
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：PPT标题为“Maven插件自动部署步骤”，包含三个步骤：
(1) 修改主机的docker配置，让其可以远程访问。
(2) 用编辑器配置，重启服务。
(3) 在工程pom.xml增加配置。
画面14：PPT标题为“执行后，会有如下输出，代码正在上传”，包含一个表格，列出了多个镜像的推送状态和大小。
表格数据：
| REPOSITORY | TAG | IMAGE ID | CREATED |
| --- | --- | --- | --- |
| 192.168.184.135:5000/tensquare_base | 1.0-SNAPSHOT | 83fa5b0478c | 10 minutes |
| 192.168.184.135:5000/jdk1.8 | latest | 50745a8b1584 | 6 hours |
| jdk1.8 | latest | 50745a8b1584 | 0 hours |

5) 不要评价画面美观，不要输出与课程无关的内容。
