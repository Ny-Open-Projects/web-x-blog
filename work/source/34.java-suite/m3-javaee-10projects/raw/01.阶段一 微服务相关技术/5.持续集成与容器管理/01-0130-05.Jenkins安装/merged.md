# 05.Jenkins安装

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\05.Jenkins安装_【海量资源尽在 ubkz.com】.mp4
- 时长 6分54秒（音频 414s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 咱们接下来呢要进行的就是jackets的安装因为我们说jackets本身的是java开发的所以说首先呢我们要进行jdk的安装那么jdk的这个安装炮啊我已经给大家提供了那么我们接下来就可以执行这个命令啊先把它上传然后执行这个命令就可以完成jdk的安装那么jdk安装之后呢它会安装到这个目录里就是usr java下的jdk 1.8.0
[00:32] 171t那么由于我们说给大家提供的这个镜像本身已经安装完这个JDK了所以说这个步骤我们在这个里就不给大家演示了那么在安装JDK之后接下来我们干嘛我们要安装jackensjackens同样也提供了rpm的安装包我们可以通过这个wget来进行下载或者是将我给大家提供的rpm安装包
[01:01] 上传到服务器我们现在就给大家将我提供的rpm给它拷贝一下是在这资源这里有一个jackens的安装包我给它放到我们的地盘好放在这然后接下来我进行上传地盘的setup下的jackens好上传
[01:46] 上传成功之后接下来咱们看一下我现在要安装这个jackens了就是rpm-ivh jackens好现在它已经安装成功了那么安装成功之后接下来我们来看这个要进行我们的jackens的配置jackens的配置这里需要修改这么一个文件叫etc下的sysconfig下的jackens这个文件那么打开之后
[02:18] 这里头我们要去改两行数据改哪两行数据呢改它的一个用户名和密码需要改这两行数据咱们把用户名和密码这两行找到在这儿这有一个端口先改这个端口这个端口是8080所以说我们这里头可以先给它改一下改成8888OK吧
[02:55] 改一个端口然后还有一个就是用户名了用户名这里头是我们说的jackens我们这里可以给改成root可以改成root把这个取掉把修改完成之后我们现在m2号wql退出退出之后我现在要想让服务生效我配置生效我需要重启一下服务重启服务打开systemctl
[03:33] startjackens好现在启动服务服务启动之后接下来我们就可以访问jackens192.168.184.1418888回车这时候大家看一下现在就进入了jackens的启动界面我们现在稍等好那么
[04:08] 这个在进入这样一个界面之后呢他让你干嘛让你去输入这个管理员的密码这个密码在哪呢他告诉你了说在这个文件之中的所以说我们现在呢可以把这个文件的内容给他显示一下啊或者说直接你打印出来也行啊cd好就是这个密码好我们现在把它复制一下复制之后呢我们现在把这个密码添上这样之后呢我们现在点一下下一步
[04:52] 稍等进了这么一个界面之后大家看一下这两种是一个是按照他给你选择的一些插件来进行安装一个是你自己来选择那么我们通常会选择左门按钮这时候他会给你安装一些必要的插件我们点击一下这时候就进入了一个插件的这么一个安装界面
[05:22] 那么这个对号呢就表示这个插件已经安装成功了那么这个两个箭头呢在转表示呢它现在正在安装或者正在下载啊这个过程呢有点长啊大家耐心等待啊现在已经下了已经完成六个了啊现在呢已经完成了这个插件的安装啊那么接下来呢就可以进入到了一个创建第一个管理员用户
[06:14] 那么这个就是管理员用户了我们现在输入itcast密码也是itcast全名也是itcast邮件地址admincherryitcast好现在我们就保存并且完成好现在就已经完成了Jackens的安装与配置现在我们启动Jackens这样一来我们就进入到了Jackens的主界面
[06:46] 那么到现在这一步呢我们就已经完成了Jackens的一个安装与配置

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 服务器上通过 RPM 包方式安装并配置 Jenkins 服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Windows 文件资源管理器，定位到 D 盘“软件”文件夹，其中包含多个软件压缩包，如 apache-Tomcat-7.0.52.tar.gz、jdk-8u171-linux-x64.tar.gz、Nginx-1.8.0.tar.gz、ZooKeeper-3.4.6.tar.gz，表明准备了相关软件包。
画面 2: 显示“软件”文件夹下的“testcode”文件夹，其中包含多个项目文件夹，如 MyDrivers、java_code、testcode、yml，表明准备了测试代码。
画面 3: 显示“testcode”文件夹下的“setup”文件夹，其中包含多个文件，如 setup-2、setup-3、setup-4、setup-5、setup-6、setup-7、setup-8、setup-9、setup-10、setup-11、setup-12、setup-13、setup-14、setup-15、setup-16、setup-17、setup-18、setup-19、setup-20、setup-21、setup-22、setup-23、setup-24、setup-25、setup-26、setup-27、setup-28、setup-29、setup-30、setup-31、setup-32、setup-33、setup-34、setup-35、setup-36、setup-37、setup-38、setup-39、setup-40、setup-41、setup-42、setup-43、setup-44、setup-45、setup-46、setup-47、setup-48、setup-49、setup-50、setup-51、setup-52、setup-53、setup-54、setup-55、setup-56、setup-57、setup-58、setup-59、setup-60、setup-61、setup-62、setup-63、setup-64、setup-65、setup-66、setup-67、setup-68、setup-69、setup-70、setup-71、setup-72、setup-73、setup-74、setup-75、setup-76、setup-77、setup-78、setup-79、setup-80、setup-81、setup-82、setup-83、setup-84、setup-85、setup-86、setup-87、setup-88、setup-89、setup-90、setup-91、setup-92、setup-93、setup-94、setup-95、setup-96、setup-97、setup-98、setup-99、setup-100，表明准备了多个 setup 文件。
画面 4: 显示 SecureCRT 连接终端，提示“root@localhost”，表明已连接到 Linux 服务器。
画面 5: 显示 Jenkins 配置文件内容，包括 JENKINS_HOME、JENKINS_JAVA_CMD、JENKINS_USER、JENKINS_INSTALL_SKIP_CHOWN、JENKINS_JAVA_OPTIONS、JENKINS_PORT、JENKINS_LISTEN_ADDRESS、JENKINS_HTTPS_PORT、JENKINS_HTTPS_KEYSTORE、JENKINS_HTTPS_KEYSTORE_PASSWORD、JENKINS_HTTPS_LISTEN_ADDRESS、JENKINS_DEFAULT_LOG_LEVEL、JENKINS_ENABLE_ACCESS_LOG、JENKINS_MAX_HTTP_WORKER_THREADS 等配置项。
画面 6: 显示 Jenkins 配置文件内容，包括 JENKINS_HTTPS_KEYSTORE、JENKINS_HTTPS_KEYSTORE_PASSWORD、JENKINS_HTTPS_LISTEN_ADDRESS、JENKINS_DEFAULT_LOG_LEVEL、JENKINS_ENABLE_ACCESS_LOG、JENKINS_MAX_HTTP_WORKER_THREADS 等配置项。
画面 7: 显示 Jenkins 配置文件内容，包括 JENKINS_HTTPS_KEYSTORE、JENKINS_HTTPS_KEYSTORE_PASSWORD、JENKINS_HTTPS_LISTEN_ADDRESS、JENKINS_DEFAULT_LOG_LEVEL、JENKINS_ENABLE_ACCESS_LOG、JENKINS_MAX_HTTP_WORKER_THREADS 等配置项。
画面 8: 显示 PPT 页面，标题为“2.3.2 Jenkins安装与启动”，内容包括：
(1) 下载：wget https://pkg.jenkins.io/redhat/jenkins-2.83.1.1.noarch.rpm
(2) 安装jenkins：rpm -ivh jenkins-2.83.1.1.noarch.rpm
(3) 配置jenkins：vi /etc/sysconfig/jenkins
(4) 启动服务：systemctl start jenkins
画面 9: 显示 PPT 页面，标题为“2.3.2 Jenkins安装与启动”，内容包括：
(1) 下载：wget https://pkg.jenkins.io/redhat/jenkins-2.83.1.1.noarch.rpm
(2) 安装jenkins：rpm -ivh jenkins-2.83.1.1.noarch.rpm
(3) 配置jenkins：vi /etc/sysconfig/jenkins
(4) 启动服务：systemctl start jenkins
画面 10: 显示终端命令行，输入“vi /etc/sysconfig/jenkins”，表明要编辑 Jenkins 配置文件。
画面 11: 显示浏览器页面，搜索“logo在线制作”，表明准备了相关工具。
画面 12: 显示 Jenkins 安装向导页面，提示“Unlock Jenkins”，并显示“JENKINS_ADMIN_PASSWORD”和“JENKINS_ADMIN_PASSWORD_FILE”两个字段，表明需要设置管理员密码。
画面 13: 显示 Jenkins 安装向导页面，提示“Unlock Jenkins”，并显示“JENKINS_ADMIN_PASSWORD”和“JENKINS_ADMIN_PASSWORD_FILE”两个字段，表明需要设置管理员密码。
画面 14: 显示 Jenkins 主界面，标题为“欢迎使用Jenkins!”，并显示“创建一个新任务”按钮，表明 Jenkins 已成功安装并启动。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
# descriptions: Jenkins automation server
# Type: string
# Default: "org/jib/jenkins"
# Service restart: jenkins
# Directory where Jenkins store its configuration and working
# files (checkouts, build reports, artifacts, ...).
# Type: string
# Default: "/var/lib/jenkins"
# Service restart: jenkins
# Java executable to run Jenkins.
# When empty, we'll try to find the suitable Java.
# Type: string
# Default: "jenkins"
# Service restart: jenkins
# Unix user account that runs the Jenkins daemon
# Be careful when you change this, as you need to update
# permissions of $JENKINS_HOME and /var/log/jenkins.
# Type: string
# Default: "jenkins"
# Service restart: jenkins
# Whether to skip potentially long-running chown at the
# $JENKINS_HOME location. Do not enable this, "true", unless
# you know what you're doing. See JENKINS-3375.
# Type: string
# Default: "false"
# Service restart: jenkins
# JENKINS_INSTALL_SKIP_CHOWN="false"
# Type: string
# Default: "-Djava.awt.headless=true"
# Service restart: jenkins
# Options to pass to java when running jenkins.
# Type: integer (0-65535)
# Default: 8080
# Service restart: jenkins
# Port Jenkins is listening on.
# Set to -1 to disable.
# Type: string
# Default: "8080"
# Service restart: jenkins
# IP address Jenkins listens on for HTTP requests.
# Default is all interfaces (0.0.0.0).
# Type: integer (0-65535)
# Default: 0
# Service restart: jenkins
# HTTPS port Jenkins is listening on.
# Default is disabled.
# Type: string
# Default: ""
# Service restart: jenkins
# path to the keystore in jks format (as created by the JDK "keytool").
# Default is disabled.
# Type: string
# Default: ""
# Service restart: jenkins
# password to access the keystore defined in JENKINS_HTTPS_KEYSTORE.
# Default is disabled.
# Type: string
# Default: ""
# Service restart: jenkins
# IP address Jenkins listens on for HTTPS requests.
# Default is disabled.
# Type: integer (1-9)
# Default: 5
# Service restart: jenkins
# debug level for logs -- the higher the value, the more verbose.
# 9 is INFO.
# Type

