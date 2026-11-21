# 02.DockerMaven插件-1

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\02.DockerMaven插件-1_【海量资源尽在 ubkz.com】.mp4
- 时长 7分48秒（音频 469s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 首先我们来讲一下Docker的Maven插件微服务的部署呢有两种方法第一种方法呢就是手动部署就手动部署那怎么手动部署呢就是我们现在比如说要将我们的编写的一个微服务布到我们的Docker容器之中那这时候呢我们手动的方式就是将这个当前的工程导成一个jar 包先给它导成一个jar 包然后呢
[00:32] 再按照我们之前的那种方式编写一个Dockerfile文件通过这种方式来部署但是这种部署方式是不是有点太麻烦是吧有一种更简单的方法就是什么就是我们可以通过去加载一个Maven插件来实现我们微服务程序的自动部署那么加上这个插件之后呢我们就可以通过我们本地的这个工程直接
[01:03] 执行一条 maven 命令就可以实现我们这个 Docker 的容器的这个自动的部署了那么具体怎么去做呢我们来看一下实现步骤要想实现 maven 插件的自动部署我们在这里他首先应该去修改我们宿主机的 Docker 配置那么修改这个配置作用是什么呢就是让他可以远程访问因为我们说
[01:33] 现在我要在本地的操作系统上通过本地的工程执行一下命令实际上对于我们的宿主机来说它是一种远程操作而远程操作Docker默认是关闭的所以说这时候我们先把它打开这样它才能够去远程访问首先执行这一步要修改这个文件这个文件是lab下的systemd system Docker.Service这么一个文件
[02:06] 那这个文件我们迁移到编辑状态就要修改哪个部分呢注意看这时候我们要在esec start后面等号后面去添加这样的配置就行了我们来看一下在这儿空格我们添加这个-h这段配置添加之后呢我们现在保存退出那么我们保存退出之后我们接下来呢要让这个配置能够
[02:47] 刷新那这时候我们需要执行这么几条命令啊让他能够刷新配置啊重启服一次执行就行了然后呢我们重启重新启动一下这个啊这么一个这这个这个这个伺服啊重新启动一下重新启动之后呢我们这里头呢就是刚才的这个配置就生效了那么接下来呢我们现在要打开我们的工程
[03:25] 在我们需要去做这个DAO科部署的这个工程中这个泡文件中啊去增加这么一段配置咱们把这配置给它复制下来然后呢我们给它放到放到这放到我们的泡文件中啊我现在比如说要部署的就是这个tensquare-base这个文件啊这个这个工程好把它复制过来复制过来之后大家看一下这个里头实际上配着两个插件对吧
[03:57] 配两个插件第一个呢就是sloan boot maven的插件啊这个是需要的第二个就是我们说的Docker的这个插件这个Docker maven插件呢这下边里头怎么配置呢大家看上面本身是这个这个插件本身的类啊这不用说了版本类版本然后呢我们接着看这个部分就是它的配置部分那么配置部分都配置什么了呢第一我们看一下这句话这一块实际上配置的是什么
[04:26] 就是配置我们最后需要生成的镜像的名称生成的镜像的名称也就是Docker里的这个列表比如Docker就是列表中这个名称好了我们接下来看下面这个base image是什么是这个基础镜像就是我们要生成基础镜像实际上相当于什么相当于我们Docker file中的from JDK 1.8
[04:59] 这里可以点吧那么接下来我们再看往下看这个部分是什么这个部分是什么是入口点那么入口点这里有一个方块号方块里有一个加吧然后呢杠杖然后接下来是杠project build final name实际上这个部分这个部分实际上就是一个引用大家看上面部分是不是也有这个表示引用表示我要引用什么呢
[05:30] 用project的节点下的idfuckedid就是project的节点下的idfuckedid就是取它最后形成的史就是ten square 干 base然后下面后边就是版本我们要取它的版本这个部分这个版本的部分接下来我们看一下下面这个部分也是一样的这个final name就指的是这个就是build下的final name就是app所以说我们这句话的作用就相当于darkfile中的
[06:03] 这句话就相当于当中放下的这句话就是entry point然后后边加封号这句话这句话相当于什么呢相当于你在启动容器之后会自动执行加挖杠炸然后是杠app加炸相当于它自动执行的一条命令行动自动执行的命令好那么接下来我们再往下看下面resource很显然指定的是源对不对源是什么
[06:39] 就会指定我们这里头去它的路径是什么这个路径是什么这个路径就是指它的创建路径就target的路径然后这个部分就指的是什么指的是app.jar也就是说我们可以指定把哪个文件上传到上传到 Docker里那么这句话相当于什么相当于这句话add app.jar然后一杠
[07:09] 表示把当前的这个诈文件去考不到我们的这个这个这个Docker的这个根目录下啊就这样一个这样一个语句啊所以说我们说这个memory差价实际上就是代替了我们Docker file的这种写法Docker就手动编写Docker file这么一种写法让他呢就是编译和这个编译和这个上传呢就是一气呵成好这个配置我们写完了
[07:41] 那么接下来呢我们就可以去给大家演示一下它的用法

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置 Docker 和 Maven 插件以实现 Spring Boot 项目的自动打包和容器化部署。

2) 按时间顺序列出每张画面的要点：
画面1：讲解 Docker Maven 插件的使用，展示 Maven 项目中 pom.xml 的配置片段，其中包含 artifactId、groupId、version 等信息。
画面2：在终端中执行 Docker ps 查看容器状态，显示 registry、mysql、Nginx 等容器正在运行。
画面3：展示 Docker.Service 的配置文件内容，其中包含 ExecStart 和 ExecReload 的设置。
画面4：讲解修改 Docker.Service 配置，使其支持远程访问，并展示修改后的配置内容。
画面5：在终端中执行 systemctl daemon-reload 和 systemctl restart Docker 命令，重启 Docker 服务。
画面6：展示在 pom.xml 中添加 Docker Maven 插件的配置，包括 <plugin> 标签和 <configuration> 内容。
画面7：展示 pom.xml 中的 <dependencies> 部分，包含 spring-boot-starter-data-jpa 等依赖。
画面8：在 IDEA 中编辑 pom.xml，高亮显示 Docker Maven 插件的 <configuration> 部分。
画面9：在终端中执行 Docker images 命令，列出本地镜像。
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
# For containers run by Docker.
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/Docker.sock
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
        <artifactId>Docker-maven-plugin</artifactId>
        <version>0.4.13</version>
        <configuration>
            <imageName>192.168.184.141:5000/${project.artifactId}:${project.version}</imageName>
            <baseImage>JDK 8</baseImage>
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
(1) 修改主机的Docker配置，让其可以远程访问。
(2) 用编辑器配置，重启服务。
(3) 在工程pom.xml增加配置。
画面14：PPT标题为“执行后，会有如下输出，代码正在上传”，包含一个表格，列出了多个镜像的推送状态和大小。
表格数据：
| REPOSITORY | TAG | IMAGE ID | CREATED |
| --- | --- | --- | --- |
| 192.168.184.135:5000/tensquare_base | 1.0-SNAPSHOT | 83fa5b0478c | 10 minutes |
| 192.168.184.135:5000/JDK 8 | latest | 50745a8b1584 | 6 hours |
| JDK 8 | latest | 50745a8b1584 | 0 hours |

5) 不要评价画面美观，不要输出与课程无关的内容。

