# 12.MongoDB入门之客户端工具Robo的介绍

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\12.MongoDB入门之客户端工具Robo的介绍【海量资源尽在 ubkz.com】.mp4
- 时长 2分45秒（音频 165s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来简单的介绍一下UI工具啊就是前面的我们对芒果DB的操作呢都是基于命令行那么其实有些时候啊那我们会发现敲这个命令呢不是很方便那么所以我们就希望呢有一个这个UI工具帮我们去做一些基本的一些CUD的操作但是比较遗憾的是呢芒果DB官方呢并没有提供这样的客户端工具那么其实第三我们就需要采用第三方的了
[00:28] 第三方的一些这个客户端工具呢会有很多我们今天呢就给大家来介绍其中一款呢就叫什么的Robo3T这样的一个客户端工具那我们来打开来看一下当然它的安装包呢大家在我们的这个所提供的资料中呢能够找到然后呢打开之后呢我们去可以看到在这个有个Create创建一个连接那么我在这个位置已经创建好了然后点击这个连接就可以了那么我们可以看到在左侧这个位置是不是有拿着一些这个数据库
[00:57] 对吧那么我们其中一个是要testdb就是我们自己所创建的一个自己的数据库那么点击这个testdb那么在这个里面就可以看到connections显然在这个下面是不是就会有我们的一些表那么打开来看一下这个里面就是有个优质表那么可以双击打开所以可以打开这张表来查看这个表里面的数据那么这个查看我们可以点击前面这个箭头这个符号对吧点一下把它展开就可以查看具体一些字段的值ok
[01:26] 那么其实在这个UI工具中呢它还可以不同的一种这个展现形式去展现这个数据那么可以点击这个位置它以表格的形式去做一个展现那么也可以呢去以这个我们的文本的这种形式去做一些这个展现都是可以的那么这个看你的个人习惯啊那么有些同学可能喜欢这种表格的形式就选择它就可以了哎呀OK那么
[01:48] 我们有些时候还是需要我们去写一些命令的那么可以看到在上面这个位置也是可以写命令的比如说我们去根据ID或者说我们根据age吧age去查选什么查选年龄等于22的这个用户OK那么这个要注意要加这个引号加引号然后点击执行走那么是不是我们就查到有三条数据三条数据年龄都等于22
[02:15] OK好那么基本的一些使用呢我们就讲了就讲那么多啊它的这个功能呢也是相对比较简单的这样的功能其中我们使用这个UI工具呢就是辅助我们来做一些数据的一种查看啊OK好那么更多的功能吧大家可以自行去做一些这个探索其实UI工具呢就是做一些辅助性的一些工作了OK好那么关于这个robot的一个工具呢我们就简单的去给大家做一个介绍啊OK好那么就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Robo 3T 客户端工具连接并操作 MongoDB 数据库，包括连接设置、查看数据和执行查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于 Robo 3T 是 MongoDB 客户端工具的介绍，同时显示了 Robo 3T 的连接设置窗口，其中“Type”为“Direct Connection”，“Address”为“127.0.0.1:27017”。
画面 2: PDF 文档页面保持不变，Robo 3T 的连接设置窗口中“Address”字段被选中，准备输入。
画面 3: PDF 文档页面保持不变，Robo 3T 的连接设置窗口中“Address”字段被选中，准备输入。
画面 4: Robo 3T 主界面，显示“MongoDB Connections”窗口，其中已添加名为“test!”的连接，地址为“127.16.55.195:27017”。
画面 5: Robo 3T 主界面，连接成功后显示数据库“test!”下的集合“user”，并列出多个文档。
画面 6: Robo 3T 主界面，显示“user”集合中的数据，包含“_id”、“id”、“username”、“age”字段，数据行数为16。
画面 7: Robo 3T 主界面，切换到“Documents”视图，显示“user”集合中前4个文档的详细内容，包括“_id”、“id”、“username”、“age”字段。
画面 8: Robo 3T 主界面，切换到“Documents”视图，显示“user”集合中前4个文档的详细内容，包括“_id”、“id”、“username”、“age”字段。
画面 9: Robo 3T 主界面，切换到“Documents”视图，显示“user”集合中前4个文档的详细内容，包括“_id”、“id”、“username”、“age”字段。
画面 10: Robo 3T 主界面，执行了查询语句“db.getCollection('user').find({'age':22})”，结果只显示了3个文档，age为22的用户。
画面 11: PDF 文档页面，显示 Robo 3T 的“Connection Settings”窗口，其中“Type”为“Direct Connection”，“Address”为“127.0.0.1:27017”。
画面 12: PDF 文档页面，显示 Robo 3T 的“Connection Settings”窗口，其中“Type”为“Direct Connection”，“Address”为“127.0.0.1:27017”。
画面 13: PDF 文档页面，显示 Robo 3T 的“Connection Settings”窗口，其中“Type”为“Direct Connection”，“Address”为“127.0.0.1:27017”。
画面 14: PDF 文档页面，显示 Robo 3T 主界面，数据库“test!”下的集合“user”被选中，显示了多个文档。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1 中的代码：
{
  "host": "c493d5ff730a",
  "port": 27017,
  "version": "4.0.1",
  "gitVersion": "7ea330946fa7880364d88c8d86026bbc9ffa48c",
  "ok": 1
}

画面 7 中的代码：
{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 1.0,
  "username": "zhangsan",
  "age": 20.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 2.0,
  "username": "li",
  "age": 21.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 3.0,
  "username": "wangwu",
  "age": 22.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 4.0,
  "username": "zhao",
  "age": 22.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 5.0,
  "username": "name_1",
  "age": 11.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 6.0,
  "username": "name_2",
  "age": 12.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 7.0,
  "username": "name_3",
  "age": 13.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 8.0,
  "username": "name_4",
  "age": 14.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 9.0,
  "username": "name_5",
  "age": 15.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 10.0,
  "username": "name_6",
  "age": 16.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 11.0,
  "username": "name_7",
  "age": 17.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 12.0,
  "username": "name_8",
  "age": 18.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 13.0,
  "username": "name_9",
  "age": 19.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 14.0,
  "username": "name_10",
  "age": 20.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 15.0,
  "username": "name_11",
  "age": 21.0
}

{
  "_id": ObjectId("5c0b1d1db0d07a321e24a154"),
  "id": 16.0,
  "username": "name_12",
  "age": 22.0
}

画面 10 中的命令：
db.getCollection('user').find({'age':22})

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1、2、3、11、12、13 中的 PPT 标题：
“1.6、UI客户端工具”
“Robo 3T是MongoDB的客户端工具，我们可以使用它来操作MongoDB。”

画面 1、11、12、13 中的架构图/流程图：
无。

画面 1、11、12、13 中的表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

