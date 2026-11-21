# day09-15-标的快速检索-logstash环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-12 使用ES&logstash实现标的快速检索
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-12 使用ES&logstash实现标的快速检索\day09-15-标的快速检索-logstash环境搭建_【海量资源尽在 666java.com】.mp4
- 时长 3分55秒（音频 235s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们把也是的环境给搭建了一下接下来呢我们就搭建一下logsdash的这个环境这个logsdash啊我们前面在讲技术方案的时候提到过它对不对我们说了logsdash呢是用来干嘛的对它是一个数据采集引擎是吧而且是实时的啊实时数据采集引擎那么在咱们这个标的快速检索这个业务当中呢它的作用就是从mycircle数据库里边采集数据
[00:30] 然后同步到哪一S索引库里这是logsdash它的作用那咱接下来呢把它的环境搭建一下那首先就是下载和安装了对不对我们下载的版本是731这个版本因为我们Elasticsearch用的版本是731它俩要保持一致版本不一致这个会出问题的这个大家不用下载了我们课件里面提供的有这个下载好的东西大家直接拿用就行你下载到手的是一个
[01:02] zip 是一个压缩软件然后呢你可以把它解压到任意路径都可以用那你解压完之后呢接下来主要是呢我们要在logsdash里边呢去安装一个插件叫logsdash-input-gdbc哎你看看这个插件的名字我觉得你就能猜出来他是干嘛input gdbc你觉得他是干嘛你再看看这个图
[01:32] 我们说了logstash是不是要从mycircle数据库去采集数据采集数据不就是读取吗是不是不就是从这里边读取数据然后他再把数据给写到什么呀yes索引库里边所以说这个插件哪个插件呢logstash-input-gdb插件就是用来从数据库干什么呀采集数据但是呢我们的这个logstash呢它本身不带这个插件所以说我们需要安装一下
[02:00] 怎么安装呢这里边你要注意这个插件呢它是由Ruby这个脚本员开发Ruby那所以说呢你要想安装这个插件你得先安装RubyRuby怎么安装呢你去官网上下载一下然后下载2.6这个版本下载完之后双击一直下一步下一步下一步就完事很简单我们课店里边提供的有安装程序你找到它直接双击下一步就OK了然后这个Ruby安装完之后呢你就执行这个命令
[02:33] 开始安装谁你看这in store安装谁对安装logs-input-gdbc这个插件注意了这个插件安装的时候要求电脑是联网必须是联网的因为它这个是联网下载然后安装的就执行这个命这个命在哪执行看好了是在logs-的bin目录下就这你看这是我logs-解压后的然后在bin注意了bin目录下为什么要在bin目录下
[03:03] 因为你看他是要用这个程序进行安装的logs-polygon.bat是不是你看这里边b目录下边你看是他吧对通过这个程序去干什么呀去安装这个插件input-gdbc这个插件而且要保证你的电脑此时是联网那这样呢我就不再给大家运行了那这样你可能会稍等一下这边你看到这个什么呀successful证明这个插件就安装完毕
[03:32] 那当然了对于大家来说呢你不用这么麻烦啊我们在课店里边给你提供了一份logstash那这个logstash里边已经安装好这个插件啊你只需要在你的电脑上安装一下ruby就行了啊然后直接拿着我提供的这个logstash使用就行了具体怎么用一会儿再说这是我们先把logstash先给它安装一下这个环境先搭建好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何下载、安装并配置 Logstash 插件，以实现 MySQL 数据库与 Elasticsearch 索引库之间的数据同步。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“4.4 Logstash数据采集和同步”，并指出本节将讲解如何使用 Logstash 保证 MySQL 数据库和 Elasticsearch 索引库的标的数据同步。
画面 2: 展示一个架构图，说明数据同步流程：前端发起请求 → 交易中心微服务 → 增删改 MySQL 数据库 → 采集 → Logstash → 同步 → ES索引库 → 内容检索微服务。
画面 3: 展示 PPT 页面，标题为“4.4.1 下载和安装Logstash”，并说明需从官网下载 Logstash 7.3.1 版本（ZIP）。
画面 4: 展示 Logstash 下载页面，显示版本 7.3.1，发布日期为 2019 年 8 月 23 日，提供 TAR.GZ、ZIP、DEB 三种下载格式。
画面 5: 展示 PPT 页面，说明安装 Logstash-input-jdbc 插件需先安装 Ruby 2.6 版本，并给出命令行提示符，显示已安装 Ruby 2.6.3p62。
画面 6: 展示 PPT 页面，内容与画面 3 相同，强调下载 Logstash 7.3.1 版本。
画面 7: 展示 PPT 页面，标题为“4.3.1 安装和配置”，并说明 Elasticsearch 和 IK 分词器的安装配置由用户自行完成，同时展示 `Elasticsearch.yml` 配置文件内容：
cluster.name: wanxin2p
node.name: wanxin2p_node
network.host: 0.0.0.0
画面 8: 展示 PPT 页面，说明安装 Logstash-input-jdbc 插件需先安装 Ruby 2.6 版本，并给出命令行提示符，显示已安装 Ruby 2.6.3p62。
画面 9: 展示命令行窗口，执行命令 `.\logstash-plugin.bat install logstash-input-jdbc`，并显示“Installation successful!”。
画面 10: 展示命令行窗口，执行命令 `.\logstash-plugin.bat install logstash-input-jdbc`，并显示“Installation successful!”。
画面 11: 展示 Windows 资源管理器，路径为 `logstash-7.3.1\bin`，列出 `logstash.bat`、`logstash-plugin.bat` 等文件。
画面 12: 展示 PPT 页面，标题为“4.4.2 创建模板文件”，并说明创建模板文件。
画面 13: 展示 PPT 页面，说明安装 Logstash-input-jdbc 插件需先安装 Ruby 2.6 版本，并给出命令行提示符，显示已安装 Ruby 2.6.3p62。
画面 14: 展示 PPT 页面，内容与画面 4 相同，显示 Logstash 下载页面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 7 中的 YAML 配置：
cluster.name: wanxin2p
node.name: wanxin2p_node
network.host: 0.0.0.0

画面 5、8、10、13 中的命令行提示符：
C:\Users\apple\ruby -v
ruby 2.6.3p62 (2019-04-16 revision 67580) [x64-mingw32]

画面 9、10、13 中的命令：
.\logstash-plugin.bat install logstash-input-jdbc

画面 11 中的目录结构：
logstash-7.3.1\bin
├── logstash.bat
├── logstash-plugin.bat
├── logstash-input-jdbc
├── logstash-output-Elasticsearch
├── logstash-filter-geoip
├── logstash-filter-mutate
├── logstash-filter-ruby
├── logstash-filter-sql
├── logstash-filter-xml
├── logstash-filter-yaml
├── logstash-filter-json
├── logstash-filter-geoip
├── logstash-filter-mutate
├── logstash-filter-ruby
├── logstash-filter-sql
├── logstash-filter-xml
├── logstash-filter-yaml
├── logstash-filter-json
├── logstash-filter-geoip
├── logstash-filter-mutate
├── logstash-filter-ruby
├── logstash-filter-sql
├── logstash-filter-xml
├── logstash-filter-yaml
├── logstash-filter-json

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2 中的架构图：
前端 → 交易中心微服务 → MySQL 数据库（增删改）
交易中心微服务 → Logstash（采集）
Logstash → ES索引库（同步）
内容检索微服务 ← ES索引库
内容检索微服务 → 前端（查询）

画面 7 中的 PPT 标题：
4.3.1 安装和配置

画面 3、6 中的 PPT 标题：
4.4.1 下载和安装Logstash

画面 12 中的 PPT 标题：
4.4.2 创建模板文件

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

