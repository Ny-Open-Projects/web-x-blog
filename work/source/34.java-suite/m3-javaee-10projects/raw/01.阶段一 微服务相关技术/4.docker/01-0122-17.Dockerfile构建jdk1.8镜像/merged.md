# 17.Dockerfile构建jdk1.8镜像

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\17.Dockerfile构建jdk1.8镜像_【海量资源尽在 ubkz.com】.mp4
- 时长 9分3秒（音频 543s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才给大家讲解了Dockerfile它的一些常用的命令那么接下来咱们就给大家演示一下如何使用Dockerfile来构建一个镜像我们在这里以构建JDK 8镜像为例给大家作为演示我们所使用的基础镜像是CentOS7好咱们首先看第一步第一步我们先构建一个目录USR local下载
[00:32] DockerJDK8比如我们先创建一个这么一个目录我创建的目录的目的是在这个目录下我构建一个Dockerfile文件并且把Dockerfile文件所需要的JDK8的压缩包也放在这个目录下好了我们现在创建完目录之后我们接下来要做的事就是干嘛呢需要做上传上传的文件在这
[01:03] 有一个JDK-8u171这个就是JDK8的压缩包咱把这个上传上去所以说outp然后我们这里头来上传put地盘的setup下的JDK8上传上传成功之后上传成功之后我们接下来看一下现在已经有这个文件了那么这个文件我们要怎么办我们要把它
[01:40] 移动到刚才我们所创建的这个这个DockerJDK8这个目录好移动了移动之后呢我们现在呢就来进到这个目录下进到这个目录下进到这个目录下之后这个有这么一个文件除了这个文件之外我们还要去构建一个文件用vi Docker fail注意d是大写的
[02:11] 这个名称必须叫dockerfile必须叫dockerfile是固定的一个名称我们现在呢进到这个编辑页面然后呢一次的去输入我们的一些命令那么首先我们来看第一个啊第一个我们学的就是它要指定一个基础镜像什么技术镜像是什么呢我们这里以centos7作为技术镜像这个镜像呢你本地是必须存在的如果不存在它会首先去下载这个镜像首先下载
[02:42] 好那第二步呢我们可以这样啊去指定我们镜像的创建者的信息啊指定镜像的创建者叫mentormentor是吧m a i n m a i n t t a i n e rt n mentor然后呢接下来我们就可以写edcast这一句话呢就是用来指定什么呢
[03:17] 指定我们的创建镜像的创建者创建镜像的创建者那么接下来咱们再看一下下面这一句我们可以有一个叫设置当前目录对吧设置当前目录叫workdr就是设置当前目录比如说我们现在设置当前目录为usr行不行也可以对吧那么设置完当前目录之后我们现在要创建一个目录创建一个目录比如叫mkdr
[03:52] usrlocal下的java那这句话呢就是用来创建一个目录对吧就是在local下我创建一个叫java的目录那么创建完目录之后我现在需要做的就是什么呢添加这个压缩包对吧并且自动解压所以说我们用addadd什么add你刚才上传的这个压缩文件上传到哪里呢
[04:23] 给他传到哪呢就是usr local下的java就是给他存在这里传这里之后他会自动解压那么接下来我们要设置就是一些环境变量了叫envenv首先我们创建第一个环境变量叫java home等于什么等于usr local下的java下的他解压之后他叫这个名叫ekdk1.8.0
[04:53] JDK 8.0-171这是他自动解压之后的名字如果你不知道这个名字你可以先在速入机圈先进行解压加之后你就可以看到这个名字了那么接下来我们再看下一句就是我们要设置一个jre的home叫envjjre home等于什么呢$java home
[05:24] 加home下的jre这是我们设置的第二个环境面量那么接下来我们再设置环境面量env设置环境面量什么有个class passclass pass这里没有档号没有档号是空格class pass然后这什么是dollar forjava home下的什么live下的dt.jar对吧注意
[05:57] 中间分隔用帽号分隔用帽号分隔然后到了服什么java homelab下的什么to点这然后接下来我们再设置jre home下的到了服jjre home下的laba这是laba然后再接着我们再往下看
[06:34] 再有一个就是什么呢就是我们的道德服class passclass pass这是我们说来设置这么一个环境变量就class pass然后最后我们再设置环境变量就是pass这个pass等于道德服java home下的bin然后那么二号接下来我们再道德服pass好这是我们说
[07:10] 设置了环境面量这个环境面量就是用来配置JDK的这样一来我们在任何的目录下都可以执行JDK中的一些命令好我们把它写完之后我们现在WQ保存一下保存之后我们会发现有一个Dockerfile文件还有一个就是我们的需要打包到镜像中的这么一个JDK那么接下来我们就
[07:40] 执行最关键的一步就是一个命令,build,就是构建,-t就是用来指定,指定什么呢?
[07:48] 指定你的镜像的名称,比如说我们这个镜像名称就叫JDK 8,空格点,这个点就代表我们要指定Dogfile的文件夹,那么我们当前文件夹是不是就有一个Dogfile,所以说这个点就代表指定当前目录,它就会在当前目录中找这个Dogfile文件,
[08:13] 这个dollars file文件这个名称是固定的我们现在回车现在它就开始去构建了就是一共9步它现在是分别去执行前5步已经即时进行第5步了前4步已经执行完了那么接下来我们看现在已经成功了现在已经成功了那么构建成功之后接下来我们再看Docker images我们就会发现这地方是不是多了一个JDK 8
[08:48] 这个JDK 8就是我们新构建的一个镜像新构建的镜像这是关于这个镜像的一个构建咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Dockerfile 构建一个包含 Java 环境的自定义镜像。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Dockerfile 文档的“6.1 什么是Dockerfile”和“6.2 常用命令”章节，其中“6.2 常用命令”部分包含一个表格，列出了 FROM、MAINTAINER、ENV、RUN、ADD、COPY、WORKDIR 等命令及其作用。
画面2：与画面1内容相同，为同一文档页面。
画面3：显示一个终端窗口，其中包含大量重复的“root@localhost”提示符，但无实际命令输入。
画面4：显示一个文件资源管理器窗口，其中包含多个视频文件，如“01.学习目录.avi”、“02.什么是Docker.avi”等，以及一个名为“16.dockerfile教程”的AVI文件。
画面5：显示一个文件资源管理器窗口，其中包含“3D”、“OneDrive”、“Windows (C:)”等文件夹。
画面6：显示一个文件资源管理器窗口，其中包含“curl-7.60.0-win64-mingw”、“Elasticsearch-5.6.0”、“Hydra”、“HeimdalClient.V2.4.64”等文件。
画面7：显示一个终端窗口，其中包含“/usr/local/dockerjdk8”路径的文件夹内容。
画面8：显示一个空的终端窗口。
画面9：显示一个新建的“Dockerfile”文件。
画面10：在终端中执行命令，开始构建镜像，显示了构建过程中的各个步骤，如“Step 2/9”、“Step 3/9”等。
画面11：继续显示构建过程，显示了“Step 8/9”、“Step 9/9”等步骤，最终成功构建并标记镜像。
画面12：显示构建完成后的终端输出，包括“Successfully tagged JDK 8:latest”。
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
ENV JAVA_HOME /usr/local/java/JDK 8.0_171
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

