# day01-6-微服务基础工程环境配置

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-6-微服务基础工程环境配置_【海量资源尽在 666java.com】.mp4
- 时长 4分19秒（音频 260s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把数据空缓性搞定了非常简单执行一下搜索脚本就OK了那接下来该干嘛接下来我们要创建我们福奇端的这个微服务基础工程是不是然后呢在此就让进行开发嘛但一般在企业当中呢这个基础工程是不需要大家创建一般会直接发给你你直接在ADIR当中打开然后进行开发就行了一般都是通过Git那咱这也是如此这个微服务的基础工程是我们直接提供给大家
[00:30] 在客栖里面这个代码文件夹里面这个地方这个one-sync p2p就是我们微服的基础工程你用idea呢直接打开就行你看我这是不是就已经打开了是不是我们的开发工具是用大家最熟悉的idea那你找到那个工程直接打开就行了这一块就不再说了那我们接下来要给大家强调的就是你新导入或者新打开一个基础工程之后你是不是要做一些基本的环境配置是不是这个大家需要知道
[01:02] 那首先我们要配的就是Maven这个都不用说但Maven这块配置的话它是这样你要看你的企业的一个情况不同的企业它的情况是不一样比如说第一种配置方法有的企业它是不是搭的有伺服对不对那你在你的setting.xml当中就要配什么你企业当中搭建的这个伺服的比如说账号伺服的密码等等这个我就不再过多说了包括伺服的地址是不是那么还有这种情况就是最懒的一种行为就是从中央仓库直接下载
[01:32] 那这个其实你都不用做任何配置没问他本身就是默认就是从中央仓库但是我们不建议啊因为中央仓库他是在国外啊我们国内下载的时候这个大家也也尝试过网感觉也感受过网速非常慢有时候甚至都下不下来对不对和电容方式呢不建议那么还有种方式呢就是使用本地仓库啊他是不是用起来最方便的一种就是仓库本身就在本地啊就在美丽那我们这个在学习期间我们建议用这个本地仓库
[02:02] 那我们在客栖里面呢会把咱们P2P项目它的本地仓库直接发给你你直接拿用就行这个你也不涉及到什么下载或者说由于这个下载仓库导致出现了一些各种奇迹怪怪的一些问题就不存在了你就直接使用我们客栖里面提供的本地仓库就行那这个本地仓库你在用的时候是不是得配一下在setting.xml当中对不对你要配什么呀配你本地仓库的这个路径是不是这个路径我要给大家抢的你可不敢照抄啊
[02:32] 你可不敢照着我这个照着我的仓库是在C盘这个位置你那可不一定在C盘你可不敢抄抄啊你可不能这个考试抄人家答案连人家名字都抄上去了对不对你这个有点太嚣张了是不是你要看你的路径啊你的路径是啥你就写啥就行了还有就是配一下阿里云这个中央仓库吧这个主要是这个保险起见万一我给你发的本地仓库万一缺个什么价包对不对那你那你缺啥你就从阿里云上进去下载吧这个咱国内的仓库
[03:03] 下载起来更方便那具体怎么配置这这个我不用再给大家过头说了啊这个大家都非常熟悉啊讲一里边也都给你标记出来你参考进行配置就行好就是配这个编码我们统一全部采用 utf 杠8的这个编码这个你给你讲一自己配啊一定要配啊要不然你可能这个打开这个机库基础工程当中某些文件某些代码时候可能会乱了说这个你一定要配一下
[03:32] 剩下这些配置你看个人习惯了比如说这个咱带这个什么代码提示我们可以让他忽略带好险这样提示更方便了就这个地方不要选这个勾就行你选中的话他是区分带好险不选就是不区分带好险好就是我们基地下的版本我们用的是1.8就不低于1.8这个地方你要检查一下还有就是这个自动导包的一个优化自动导包
[04:04] 这个你参考讲也自己配一下这个一般吧我们在前段中新打开一块新导入一些呃工程项目之后呢这是基本上你要中年检查了啊要做的一些配置我们在这上再给大家强调一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解微服务基础工程的开发工具配置，包括IDEA环境搭建、Maven仓库配置、编码格式设置和项目SDK配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：显示Windows文件资源管理器，路径为“wanxinp2p > day01”，选中“代码”文件夹，准备打开项目。
画面2：PPT页面标题为“1.2 微服务基础工程”，子标题“1.2.1 开发工具配置”，内容说明服务端工程使用IntelliJ IDEA开发（需2018以上版本），并提到配置Maven环境。
画面3：PPT页面显示在setting.xml中配置私服地址的代码片段，包含<server>标签，用于配置<maven-releases>和<maven-snapshots>的用户名和密码。
画面4：PPT页面显示在setting.xml中配置私服地址的代码片段，包含<server>标签，用于配置<maven-releases>和<maven-snapshots>的用户名和密码，并显示了<mirrors>标签的配置。
画面5：PPT页面显示在setting.xml文件中配置本地仓库路径的代码片段，<localRepository>标签指向C:\apache-maven-3.1.1\rep\localRepository。
画面6：PPT页面显示在setting.xml文件中配置本地仓库路径的代码片段，<localRepository>标签指向C:\apache-maven-3.1.1\rep\localRepository，并有红色箭头标注“本地仓库路径”。
画面7：PPT页面显示在setting.xml文件中配置<mirrors>标签的代码片段，包含<mirror>标签，用于指定镜像仓库。
画面8：PPT页面显示在IDEA中配置Maven的界面，Maven Home Path设置为C:\apache-maven-3.1.1，settings.xml文件路径为C:\apache-maven-3.1.1\conf\settings.xml。
画面9：PPT页面显示在IDEA中配置文件编码的界面，Project Encoding设置为UTF-8，File Encoding设置为UTF-8。
画面10：PPT页面显示在IDEA中配置代码提示的界面，Code Completion设置为“不匹配大小写”。
画面11：PPT页面显示在IDEA中配置项目SDK的界面，Project SDK设置为1.8（java version “1.8.0_202”），Project language level设置为8 - Lambdas, type annotations etc。
画面12：PPT页面显示在IDEA中配置自动导入的界面，Insert imports on paste设置为Ask。
画面13：PPT页面显示在IDEA中配置文件编码的界面，Project Encoding设置为UTF-8，File Encoding设置为UTF-8。
画面14：PPT页面显示在setting.xml文件中配置<mirrors>标签的代码片段，包含<mirror>标签，用于指定镜像仓库，并显示在IDEA中配置Maven的界面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
在setting.xml中的<servers>段增加：
<server>
<id>maven-releases</id>
<username>私服账号</username>
<password>私服密码</password>
</server>
<server>
<id>maven-snapshots</id>
<username>私服账号</username>
<password>私服密码</password>
</server>

画面4：
在<mirrors>添加：
<mirror>
<id>aliyun</id>
<mirrorOf>central</mirrorOf>
<name>阿里云公共仓库</name>
<url>http://maven.aliyun.com/repository/public</url>
</mirror>

画面5：
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">
<localRepository>C:\apache-maven-3.1.1\rep\localRepository</localRepository>
</settings>

画面7：
<mirror>
<id>aliyun</id>
<name>阿里云公共仓库</name>
<url>http://maven.aliyun.com/repository/public</url>
<mirrorOf>central</mirrorOf>
</mirror>

画面8：
Maven Home Path: C:\apache-maven-3.1.1
settings.xml: C:\apache-maven-3.1.1\conf\settings.xml

画面11：
Project SDK: 1.8 (java version "1.8.0_202")
Project language level: 8 - Lambdas, type annotations etc.

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题“1.2 微服务基础工程”，子标题“1.2.1 开发工具配置”，内容说明服务端工程使用IntelliJ IDEA开发（需2018以上版本），并提到配置Maven环境。
画面3：PPT内容说明在setting.xml中配置私服地址的代码片段，包含<server>标签，用于配置<maven-releases>和<maven-snapshots>的用户名和密码。
画面4：PPT内容说明在setting.xml中配置私服地址的代码片段，包含<server>标签，用于配置<maven-releases>和<maven-snapshots>的用户名和密码，并显示了<mirrors>标签的配置。
画面5：PPT内容说明在setting.xml文件中配置本地仓库路径的代码片段，<localRepository>标签指向C:\apache-maven-3.1.1\rep\localRepository。
画面6：PPT内容说明在setting.xml文件中配置本地仓库路径的代码片段，<localRepository>标签指向C:\apache-maven-3.1.1\rep\localRepository，并有红色箭头标注“本地仓库路径”。
画面7：PPT内容说明在setting.xml文件中配置<mirrors>标签的代码片段，包含<mirror>标签，用于指定镜像仓库。
画面8：PPT内容说明在IDEA中配置Maven的界面，Maven Home Path设置为C:\apache-maven-3.1.1，settings.xml文件路径为C:\apache-maven-3.1.1\conf\settings.xml。
画面9：PPT内容说明在IDEA中配置文件编码的界面，Project Encoding设置为UTF-8，File Encoding设置为UTF-8。
画面10：PPT内容说明在IDEA中配置代码提示的界面，Code Completion设置为“不匹配大小写”。
画面11：PPT内容说明在IDEA中配置项目SDK的界面，Project SDK设置为1.8（java version “1.8.0_202”），Project language level设置为8 - Lambdas, type annotations etc。
画面12：PPT内容说明在IDEA中配置自动导入的界面，Insert imports on paste设置为Ask。
画面13：PPT内容说明在IDEA中配置文件编码的界面，Project Encoding设置为UTF-8，File Encoding设置为UTF-8。
画面14：PPT内容说明在setting.xml文件中配置<mirrors>标签的代码片段，包含<mirror>标签，用于指定镜像仓库，并显示在IDEA中配置Maven的界面。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

