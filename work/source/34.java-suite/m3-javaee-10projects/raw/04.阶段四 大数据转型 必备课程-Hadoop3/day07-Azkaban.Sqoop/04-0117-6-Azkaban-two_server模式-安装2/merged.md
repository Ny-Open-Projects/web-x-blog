# 6-Azkaban-two_server模式-安装2

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\6-Azkaban-two_server模式-安装2【海量资源尽在 ubkz.com】.mp4
- 时长 8分22秒（音频 503s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来进行第四步的安装我们要装一个AzKaban Web ServerOK 刚才呢我们在这个Surface这个目录里边解压了一个文件文件夹是这个AzKaban Web Server 3.51.0在这个conf下面呢有一个文件需要配置就是azkaban.properties配置什么呢我们向下看这里边有很多参数呢我们要去做一些设置首先呢我们来打开这个文件好 在这里我们
[00:30] 这个地方是web server我们进到他这个conf目录下面在这个目录下面呢有一个azkaban properties把它打开在这个里边呢我们第一个呢我们要配个azkaban的一个名字这个名字你可以随便写但是我们呢尽量统一一下打开我们的讲义我们给他名字起了azkaban在这里azkaban
[01:02] 接下来还有一个这个label也就是这个阿斯卡标签我们可以写个my.askaban都行接下来还有一个地方需要更改这里有一个时区这个地方timezone我们这个地方改成Asia上海这个地方别写错了ASIA上海再来想想看这个地方还有一个SSL这个Jet use
[01:33] SL那这个地方我们使用SL协议我改成trueOK这个地方改一下接下来呢在这里我们还需要配置其他参数我们来看一下讲义吧在这里呢有这么一个配置比如说这个SL一个端口是8443还有呢我们产生的那个密钥文件Kistall它的位置是这个位置我把这个呢直接复制过来来粘在我们这个8081的下面好放在这个位置
[02:05] 粘贴一下粘贴的时候一定要确定你这些路径是正确的我来检测一下我的KSTO在哪里呢我们刚才运行了这个命令之后呢稍等啊我们刚才运行了这个命令之后数据库退出吧这个命令在export softwareas kaban在哪里呢在应该是应该是在哪个目录啊我们来看一下这个KSTO
[02:38] 应该是在上一季应该是在上一季我们回到上一季应该是在web server应该是在这里咱们进去azkabanweb serversend为0进来之后呢在这里你看这里边有个kistall这个地方呢我们把这个路径复制一下保证它不会出问题回到我们的这个配置在这里的话我们web server是在web server下面的web stall把前面呢
[03:10] 干掉应该路径是一样的为了保证它没问题我再粘贴一下是这个目录那下面这个是阿兹卡班这个地方那这个地方应该是粘错了应该是粘在这个位置粘错了再粘一下好粘一下之后呢还有一个叫还有一个叫ESCC Server我们也把它粘一下好回到上一集在这个地方有阿兹卡班ESCC Server进去进去之后呢
[03:53] 还进去之后我们来看一下这里边没有没有的话呢我们来继续看这个两个路径应该是一样的OK一样的话呢这个密码adkban这个地方呢密码adkban这个trace什么password也是adkbanOK这个就配好了配好之后呢我们向下看还有个数据库的配置向下走这个地方你看mycircle数据库的配置这个端口不变而这个host呢我们的数据库呢在node03所以说改成node03
[04:23] 好了那后面这个呢也不变这个就默认就可以了再向下看这个地方有一个叫阿兹卡班执行选择过滤器我们要把这个注释掉我们不用把它注释掉加个警号好那么再向下走来看一下讲义再向下走的话呢最后还有一个地方需要配置就是这些地方最后呢还有这几句话呢我们把它直接复制过来复制到我们的这个配置文件好进来粘到最后就可以了
[04:54] 比如说什么刷新的频率还有什么一个刷新的一些最大线程等等我把它放在这里好放在这里之后呢我们这个web server呢就配好了OK这个AzureKaban properties配好了配好之后接下来我们来继续我们来配置这个ESC server那在ESC server里边呢也有一个AzureKaban properties我们来进来好回到我们的上一集好回到上一集
[05:25] 在这里边有ESC ServerCD,AzKaban,ESC Server进来进来之后进到conf目录下面也有一个AzKaban Properties好,进来我们对这里的内容进行修改修改的时候首先这个AzKaban的名字我们还是修改一下这个不改也可以叫MyAzKabanMyAzKaban好,那这个地方AzKaban的label我们就不改了接下来还有一个时区
[06:00] 还是这个时区的问题我们要改一个Asia然后上海好这个时区修改完了修改完成之后我们向下走这个地方还有一个SSL这个地方呢我们UZSL我们给它改成初我们使用这个SSL安全验证OK改成初好那么再向下走在这个地方呢8081后面我们也需要去设置我们的KSTOXX它的一个路径来向下看
[06:34] 我要把这四句话呢给它加进来好那这些路径呢你再次确认一下保证它没有问题就这个Kistall所在的位置在web server下面我们来再确定一下吧在这个二次卡版web serverOK在这里这里的Kistall把这个路径给我复制一份然后粘在这个后面去好粘一下
[07:13] 那下面这个也是一样也把它粘一下我的意思你做这个事情保证它肯定没问题不然的话你配置完之后有的同学会出现它运行不了的情况那这个地方我们配完了接下来继续向下走在这个位置在这一行叫阿兹卡班web server url就是访问阿兹卡班的一个地址这个地方我们不用http我们用https
[07:42] 因为我们装了一个SLSL安全验证好这个地方呢我们也不用localhost我们用node03而这个端口呢我们也不用8081我们用8443好这个配置完毕之后呢接下来我们再配置我们的数据库在这个位置向下走还是这个mycircle好这个host呢我们选择node03node03别的应该不需要再配置了
[08:14] 那么我们就把这个文件配置好了配置好之后我们WQ保存退出OK那么我们先把这个视频先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

