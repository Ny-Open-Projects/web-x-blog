# 04-课程分析-课程购买量-NiFi采集MySQL配置

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\04-课程分析-课程购买量-NiFi采集MySQL配置_【海量资源尽在 666java.com】.mp4
- 时长 3分13秒（音频 194s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来咱们使用NiFi采集课程购买量的数据,调度的代码在咱们的资料中第三章课程分析NiFi目录内有一个课程购买量的目录,这里边有咱们课程购买量MySQL实时采集的调度代码,上面是咱们调度的流程,感兴趣的话可以去了解一下,但是这不是咱们的重点,咱们的重点是采集数据。
[00:28] 好,咱们来切到NiFi。
[00:31] 通过本节的学习呢,咱们需要将咱们的源码给导入到NiFi上,然后呢,把调度,就是执行采集的任务调度呢,给配置好,配置好之后呢,就OK了,咱们来上传代码。
[00:45] 这里呢,在离线分析这里,新建了一个课程购买量的处理器组,咱们呢,课程购买量相关的NiFi调度就在这个处理器组里边,咱们来切过来。
[00:58] 双击就进入了咱们课程购买量的处理器组好进行模板的上传选择咱们课程购买量mycycle10采集这个调度的源码然后呢选择upload进行一个上传上传成功之后使用添加模板的方式将刚才上传的源码给添加进来这个呢就是咱们使用NiFi采集mycycle数据的一个
[01:26] 调度的一个源码这里呢咱们有这里有两个感叹号咱们来配置一下右键然后conf一个这里边呢这两项直接启用即可因为咱们在源码里边呢已经配置好直接把这两个两项给启用了就行启用完成之后呢咱们来说一些咱们来说一点注意事项就是这个缓存服务咱们之前说过缓存服务呢全局只有一个就行这里呢它
[01:55] 咱们没有配置它已经识别了因为咱们全局有一个它就自动识别了这是第一个注意事项第二个是咱们mycircle的配置咱们要读取mycircle相关的配置但是在这个里边这次是没有的咱们之前在数据读取的时候就是生产数据的时候这里的mycirclemycircle是在这里配置的但是这次情况有点不一样mycircle没有在这里配置咱们点入
[02:26] 进来咱们处理器组咱们这次MySQL的配置是在处理器上直接配置的咱们右键第一个处理器然后选择Config点击到Properties标题这里你可以看到MySQL配置的一些参数咱们还是只用设置密码就行密码是123456好设置完成之后点击OK点击Apply这里完成之后咱们就可以进行采集了
[02:57] 好,到此呢,咱们把课程购买量的一个任务调度,原码上传到咱们的NetFive中,也对它进行了一个相应配置,配置完成之后呢,咱们的视频呢,就到这里。

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 NiFi 中创建并配置一个用于实时采集 MySQL binlog 数据并写入 Hive 的数据流。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程文档中关于 NiFi MySQL binlog 处理流程的说明，包含流程图和 XML 路径。
画面2: 与画面1内容相同，为同一文档页面。
画面3: 与画面1、2内容相同，为同一文档页面。
画面4: 在 NiFi 界面中弹出“Upload Template”对话框，用于上传模板。
画面5: NiFi 界面空白画布，准备创建新流程。
画面6: 弹出“Add Template”对话框，选择“课程购买量-Mysql实时采集”模板。
画面7: 显示“1. 数据采集: 课程购买量-Mysql-To-Hive Configuration”配置页面的 GENERAL 标签页，设置 Process Group Name 和 Comments。
画面8: 在 CONTROLLER SERVICES 标签页，显示已配置的服务列表，包括 DistributedMapCacheClientService、DistributedMapCacheServer 和 HiveConnectionPool。
画面9: 在 CONTROLLER SERVICES 标签页，鼠标悬停在 DistributedMapCacheClientService 上，选中并高亮显示。
画面10: 在 NiFi 界面中，点击菜单栏的“+”按钮，弹出“1. 数据采集: 课程购买量-Mysql-To-Hive”流程组的属性面板。
画面11: 显示 NiFi 流程图，包含 CaptureChangeMySQL、RouteOnAttribute、MySQLBinLogToHiveProcessor 和 PutHiveQL 四个处理器，按顺序连接。
画面12: 与画面11内容相同，为同一流程图。
画面13: 与画面1、2、3内容相同，为同一文档页面。
画面14: 与画面13内容相同，为同一文档页面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面1、2、3、13、14 中的 XML 路径：
xml路径：
  搜索资料
    第3章-课程分析
      nifi/课程购买量/课程购买量-Mysql实时采集.xml

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1、2、3、13、14 中的 PPT 标题：
2.3.3.1.2 NiFi 调度流程
NiFi监控MySQL binlog处理通用流程如下：CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL
NiFi通用流程图，如下图所示：

流程图结构：
CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL

画面7 中的表格数据：
Process Group Name: 1.数据采集: 课程购买量-Mysql-To-Hive
Process Group Comments: MySQL实时采集数据，监控insert, update

画面8 中的表格数据：
Name | Type | Bundle | State | Scope
DistributedMapCacheClientService | DistributedMapCacheClientService 1.0 | org.apache.nifi-nifi-distributed-cache | Enabled | 1.数据采集: 课程购买量-Mysql-To-Hive
DistributedMapCacheServer | DistributedMapCacheServer 1.9.2 | org.apache.nifi-nifi-distributed-cache | Enabled | NiFi Flow
HiveConnectionPool | HiveConnectionPool 1.9.2 | org.apache.nifi-nifi-Hive-nar | Disabled | 1.数据采集: 课程购买量-Mysql-To-Hive

画面11 中的流程图结构：
CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL

5) 无

