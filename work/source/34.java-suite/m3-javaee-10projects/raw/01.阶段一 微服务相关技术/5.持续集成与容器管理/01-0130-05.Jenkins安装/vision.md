# 画面线理解：05.Jenkins安装

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\05.Jenkins安装_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:05, 01:16, 01:28, 01:46, 02:16, 02:27, 02:40, 03:03, 03:17, 03:30, 03:46, 04:22, 05:15, 06:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:18:12

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 服务器上通过 RPM 包方式安装并配置 Jenkins 服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Windows 文件资源管理器，定位到 D 盘“软件”文件夹，其中包含多个软件压缩包，如 apache-tomcat-7.0.52.tar.gz、jdk-8u171-linux-x64.tar.gz、nginx-1.8.0.tar.gz、zookeeper-3.4.6.tar.gz，表明准备了相关软件包。
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
# service restart: jenkins
# Directory where Jenkins store its configuration and working
# files (checkouts, build reports, artifacts, ...).
# Type: string
# Default: "/var/lib/jenkins"
# service restart: jenkins
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
