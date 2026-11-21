# 画面线理解：02.MongoDB入门之介绍

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\02.MongoDB入门之介绍【海量资源尽在 ubkz.com】.mp4
- 抽帧：8 帧 @ 04:05, 04:08, 05:50, 06:52, 06:58, 07:04, 07:08, 07:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:34:13

1) 这一组画面整体在讲如何在 EditPlus 编辑器中编写和修改一个包含嵌套对象的 JSON 数据结构，并穿插讲解 MongoDB 的入门与 Docker 安装。

2) 按时间顺序列出每张画面的要点：
   画面1：打开 EditPlus 编辑器，空白文档，准备开始编写内容。
   画面2：在 EditPlus 中创建新文件，光标位于第1行第1列，准备输入内容。
   画面3：在 EditPlus 中输入了第一个 JSON 对象，包含 id、name、age、address 字段。
   画面4：在 EditPlus 中继续输入，为第二个对象添加 address 字段下的嵌套对象，开始输入 id 和 title 字段。
   画面5：切换到 Adobe Reader，显示 PDF 文档内容，标题为“1.1、MongoDB简介”和“1.2、通过docker安装MongoDB”，并显示了 Docker 拉取命令。
   画面6：在 EditPlus 中继续编辑，完成第二个对象的 address 嵌套对象，输入了 id:1001 和 title:"北京市xxxxx"。
   画面7：在 EditPlus 中光标位于第二个对象的嵌套对象内部，准备继续编辑。
   画面8：在 EditPlus 中显示一个包含多个截图的下载页面，其中包含 EditPlus 编辑器的截图。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
   画面3：
   {
   "id":1,
   "name":"zhangsan",
   "age":20,
   "address":"上海市"
   }
   画面4：
   {
   "id":2,
   "name":"李四",
   "address":{
   id:1001,
   title:"北京市xxxxx",
   }
   }
   画面5：
   拉取镜像
   docker pull mongo:4.0.3

4) 出现的 PPT 标题、架构图/流程图的结构、表格数据：
   画面5：
   PPT标题：1. MongoDB入门
   子标题：1.1、MongoDB简介
   内容：
   MongoDB是一个基于分布式文件的数据库，由C++语言编写，为WEB应用提供高性能数据存储解决方案。
   MongoDB是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的，它支持的数据结构非常松散，是类似json的bson格式，因此可以存储比较复杂的查询类型。
   MongoDB最大的特点是它支持的查询语言非常强大，其语法有点类似于面向对象的查询语言，几乎可以实现类似关系数据库查询的绝大部分功能，而且还支持对数据建立索引。
   官网：https://www.mongodb.com
   子标题：1.2、通过docker安装MongoDB
   内容：
   拉取镜像
   docker pull mongo:4.0.3

5) 无
