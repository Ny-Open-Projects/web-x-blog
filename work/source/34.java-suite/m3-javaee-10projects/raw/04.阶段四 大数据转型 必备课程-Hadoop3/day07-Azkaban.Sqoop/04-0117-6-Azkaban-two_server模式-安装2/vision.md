# 画面线理解：6-Azkaban-two_server模式-安装2

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\6-Azkaban-two_server模式-安装2【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:33, 01:38, 01:59, 02:18, 03:02, 04:11, 04:40, 04:53, 05:21, 06:25, 06:50, 08:00, 08:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 09:20:48

1) 这一组画面整体在讲什么（一句话）：
演示如何配置并安装 Azkaban Web Server，包括设置 SSL 证书、修改配置文件以启用 HTTPS 和配置数据库连接。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Azkaban 安装文档的第 3 步“安装 SSL 安全认证”和第 4 步“azkaban web server 安装”，并显示了修改配置文件的命令：cd /export/servers/azkaban-web-server-3.51.0/conf 和 vim azkaban.properties。
画面 2: 在终端中执行 keytool 命令生成 keystore，提示输入组织名、城市、国家等信息，最后确认并输入密码。
画面 3: 显示了 azkaban.properties 配置文件内容，其中包含 jetty.port=8081 等设置。
画面 4: 在 Notepad++ 中编辑 azkaban-web-server-3.51.0/keystore 文件，右键菜单显示“复制”、“粘贴”等选项。
画面 5: 在 MySQL 命令行中执行 show tables;，列出 Azkaban 数据库中的表。
画面 6: 在终端中切换到 azkaban-web-server-3.51.0 目录，执行 pwd 命令查看当前路径。
画面 7: 显示 azkaban.properties 配置文件内容，其中包含 jetty.ssl.port=8443 和 jetty.port=8081 等设置。
画面 8: 在 Notepad++ 中编辑 azkaban.properties 文件，光标位于 mail.host= 行。
画面 9: 显示 azkaban.properties 配置文件内容，其中包含数据库连接配置：mysql.host=node03、mysql.database=azkaban 等。
画面 10: 在终端中执行 ls 命令查看当前目录下的文件，然后执行 cd .. 命令返回上级目录。
画面 11: 显示 azkaban.properties 配置文件内容，其中包含 jetty.port=8081 设置。
画面 12: 在终端中切换到 azkaban-exec-server-3.51.0 目录，执行 cd .. 命令返回上级目录。
画面 13: 显示 azkaban.properties 配置文件内容，其中包含 jetty.port=8081 设置。
画面 14: 显示 azkaban.properties 配置文件内容，其中包含 executor.flow.threads=30 设置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
cd /export/servers/azkaban-web-server-3.51.0
keytool -keystore keystore -alias jetty -keyalg RSA

画面 2:
What is the name of your organization?
[Unknown]:
What is the name of your City or Locality?
[Unknown]:
What is the name of your State or Province?
[Unknown]:
What is the two-letter country code for this unit?
[Unknown]:
Is CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown correct?
[no]: yes
Enter key password for <jetty>
(RETURN if same as keystore password):
Re-enter new password:
[root@node03 azkaban-web-server-3.51.0]# ls
bin conf keystore lib web
[root@node03 azkaban-web-server-3.51.0]# ls
bin conf keystore lib web

画面 3:
# Azkaban Personalization Settings
azkaban.name=Azkaban
azkaban.label=My Local Azkaban
azkaban.color=#FF3601
azkaban.default.servlet.path=/index
web.resource.dir=web
default.timezone.id=Asia/Shanghai
# Azkaban UserManager class
user.manager.class=azkaban.user.XmlUserManager
user.manager.xml.file=conf/azkaban-users.xml
# Loader for projects
executor.global.properties=conf/global.properties
azkaban.project.dir=projects
# Velocity dev mode
velocity.dev.mode=false
# Azkaban Jetty server properties.
jetty.use.ssl=true
jetty.maxThreads=25
jetty.port=8081

画面 4:
# Azkaban Personalization Settings
azkaban.name=Azkaban
azkaban.label=My Local Azkaban
azkaban.color=#FF3601
azkaban.default.servlet.path=/index
web.resource.dir=web
default.timezone.id=Asia/Shanghai
# Azkaban UserManager class
user.manager.class=azkaban.user.XmlUserManager
user.manager.xml.file=conf/azkaban-users.xml
# Loader for projects
executor.global.properties=conf/global.properties
azkaban.project.dir=projects
# Velocity dev mode
velocity.dev.mode=false
# Azkaban Jetty server properties.
jetty.use.ssl=true
jetty.maxThreads=25
jetty.port=8081

画面 5:
mysql> show tables;
+-------------------------------------+
| Tables_in_azkaban                   |
+-------------------------------------+
| QRTZ_BLOB_TRIGGERS                  |
| QRTZ_CALENDARS                      |
| QRTZ_CRON_TRIGGERS                  |
| QRTZ_FIRED_TRIGGERS                 |
| QRTZ_JOB_DETAILS                    |
| QRTZ_LOCKS                          |
| QRTZ_PAUSED_TRIGGER_GRPS            |
| QRTZ_SCHEDULER_STATE                |
| QRTZ_SIMPLE_TRIGGERS                |
| QRTZ_TRIGGERS                       |
| active_executing_flows              |
| active sla                          |
| execution_dependencies              |
| execution_flows                     |
+-------------------------------------+

画面 6:
[root@node03 azkaban-web-server-3.51.0]# cd ..
[root@node03 servers]# cd azkaban-web-server-3.51.0/
[root@node03 azkaban-web-server-3.51.0]# pwd
/export/servers/azkaban-web-server-3.51.0

画面 7:
# Velocity dev mode
velocity.dev.mode=false
# Azkaban Jetty server properties.
jetty.use.ssl=true
jetty.maxThreads=25
jetty.port=8081
jetty.ssl.port=8443
jetty.keystore=/export/servers/azkaban-web-server-3.51.0/keystore
jetty.password=azkaban
jetty.keypassword=azkaban
jetty.truststore=/export/servers/azkaban-web-server-3.51.0/keystore
jetty.trustpassword=azkaban
# Azkaban Executor settings
# mail settings
mail.sender=
# User facing web server configurations used to construct the user facing server URLs. They are useful when there is a reverse proxy between Azkaban web servers and users.
# enduser -> myazkabanhost:443 -> proxy -> localhost:8081

画面 8:
# Azkaban Personalization Settings
azkaban.name=Azkaban
azkaban.label=My Local Azkaban
azkaban.color=#FF3601
azkaban.default.servlet.path=/index
web.resource.dir=web
default.timezone.id=Asia/Shanghai
# Azkaban UserManager class
user.manager.class=azkaban.user.XmlUserManager
user.manager.xml.file=conf/azkaban-users.xml
# Loader for projects
executor.global.properties=conf/global.properties
azkaban.project.dir=projects
# Velocity dev mode
velocity.dev.mode=false
# Azkaban Jetty server properties.
jetty.use.ssl=true
jetty.maxThreads=25
jetty.port=8081
# Azkaban Executor settings
# mail settings
mail.sender=
mail.host=

画面 9:
# Velocity dev mode
velocity.dev.mode=false
# Azkaban Jetty server properties.
jetty.use.ssl=true
jetty.maxThreads=25
jetty.port=8081
# Azkaban Executor settings
# mail settings
mail.sender=
mail.host=
# User facing web server configurations used to construct the user facing server URLs. They are useful when there is a reverse proxy between Azkaban web servers and users.
# enduser -> myazkabanhost:443 -> proxy -> localhost:8081
# Azkaban mysql settings by default. Users should configure their own username and password.
database.type=mysql
mysql.port=3306
mysql.host=node03
mysql.database=azkaban
mysql.user=azkaban
mysql.password=azkaban
mysql.numconnections=100
# Multiple Executor
azkaban.use.multiple.executors=true
# azkaban.executor.selector.filters=StaticRemainingFlowSize,MinimumFreeMemory,CpuStatus
azkaban.executor.selector.comparator.NumberOfAssignedFlowComparator=1
azkaban.executor.selector.comparator.Memory=1
azkaban.executor.selector.comparator.LastDispatched=1
azkaban.executor.selector.comparator.CpuUsage=1

画面 10:
[root@node03 conf]# ls
azkaban
