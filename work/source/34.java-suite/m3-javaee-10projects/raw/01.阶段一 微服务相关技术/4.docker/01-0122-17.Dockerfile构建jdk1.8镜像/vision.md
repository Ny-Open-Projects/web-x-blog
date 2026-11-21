# 画面线理解：17.Dockerfile构建jdk1.8镜像

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\17.Dockerfile构建jdk1.8镜像_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:01, 00:23, 00:56, 00:58, 00:59, 01:12, 01:15, 02:16, 08:22, 08:38, 08:41, 08:57, 08:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:09:36

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Dockerfile 构建一个包含 Java 环境的自定义镜像。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Dockerfile 文档的“6.1 什么是Dockerfile”和“6.2 常用命令”章节，其中“6.2 常用命令”部分包含一个表格，列出了 FROM、MAINTAINER、ENV、RUN、ADD、COPY、WORKDIR 等命令及其作用。
画面2：与画面1内容相同，为同一文档页面。
画面3：显示一个终端窗口，其中包含大量重复的“root@localhost”提示符，但无实际命令输入。
画面4：显示一个文件资源管理器窗口，其中包含多个视频文件，如“01.学习目录.avi”、“02.什么是Docker.avi”等，以及一个名为“16.dockerfile教程”的AVI文件。
画面5：显示一个文件资源管理器窗口，其中包含“3D”、“OneDrive”、“Windows (C:)”等文件夹。
画面6：显示一个文件资源管理器窗口，其中包含“curl-7.60.0-win64-mingw”、“elasticsearch-5.6.0”、“Hydra”、“HeimdalClient.V2.4.64”等文件。
画面7：显示一个终端窗口，其中包含“/usr/local/dockerjdk8”路径的文件夹内容。
画面8：显示一个空的终端窗口。
画面9：显示一个新建的“Dockerfile”文件。
画面10：在终端中执行命令，开始构建镜像，显示了构建过程中的各个步骤，如“Step 2/9”、“Step 3/9”等。
画面11：继续显示构建过程，显示了“Step 8/9”、“Step 9/9”等步骤，最终成功构建并标记镜像。
画面12：显示构建完成后的终端输出，包括“Successfully tagged jdk1.8:latest”。
画面13：展示 Dockerfile 文档的“6.2 常用命令”和“6.3 使用脚本创建镜像”章节，其中“6.3 使用脚本创建镜像”部分包含“步骤”和“执行命令构建镜像”的说明。
画面14：展示 Dockerfile 文档的“7.1 私有仓库搭建与配置”章节，其中包含“MAINTAINER ITCAST”、“#切换工作目录”、“RUN mkdir /usr/local/java”等命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面13中的代码：
```
MAINTAINER ITCAST
#切换工作目录
RUN mkdir /usr/local/java
#ADD 检查jdk.jar,把java添加到容器中
ADD jdk-8u171-linux-x64.tar.gz /usr/local/java/
#配置java环境变量
ENV JAVA_HOME /usr/local/java/jdk1.8.0_171
ENV JRE_HOME $JAVA_HOME/jre
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
ENV PATH $JAVA_HOME/bin:$PATH
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、2、13、14：PPT标题分别为“6 Dockerfile”、“6.1 什么是Dockerfile”、“6.2 常用命令”、“6.3 使用脚本创建镜像”、“7.1 私有仓库搭建与配置”。
画面1中的表格数据：
| 命令 | 作用 |
| --- | --- |
| FROM image_nametag | 定义了使用那个基础镜像后构建流程 |
| MAINTAINER user_name | 声明镜像的创建者 |
| ENV key value | 设置环境变量（可以写多条） |
| RUN command | 是Dockerfile的核心部分（可以写多条） |
| ADD source_dirfile dest_dirfile | 将宿主机的文件复制到容器内，如果是一个压缩文件，将会在复制后自动解压 |
| COPY source_dirfile dest_dirfile | 和ADD相似，但是如果有压缩文件并不能解压 |
| WORKDIR path_dir | 设置工作目录 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
