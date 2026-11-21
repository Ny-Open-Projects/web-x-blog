---
disableNunjucks: true
title: 11-3 mongoDB GUI 软件推荐使用
date: 2026-11-17 14:16:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课简单用了 mongo shell，它是 MongoDB 自带的命令行工具。但数据库这种需要高度可视化的东西，用命令行有时非常费时费力，看得也不清楚。所以在深入 MongoDB 之前，先推荐两款 GUI 工具。

第一款是 MongoDB 官方出品的 Compass，访问官网直接点 Download Compass 下载。它支持数据导入导出（Import your data）、查询（Query your data）、聚合（Aggregation），还内置了一个 Shell 可以直接敲命令，并且支持多个操作系统。

第二款是我接下来要演示的 Robo 3T。它最早叫 Robomongo，域名也是这个名字，做得不错，被 3T 公司收购后改名 Robo 3T。注意 3T 公司有两个软件：一个是我们说的 Robo 3T，完全免费、支持多平台的开源软件，GitHub 上有 8.7K Star，使用的人非常多；另一个是 3T 在 Robo 3T 基础上推出的收费软件 Studio 3T，扩充了很多功能，不差钱可以去试试，提供三十天试用。

我用 MongoDB 以来一直用的是 Robomongo，也就是现在的 Robo 3T，基本功能都有，运行稳定，所以推荐它。下面简单演示一下使用。

安装后是一个机器人样子的图标，点击进入。首先弹出 MongoDB Connections 连接界面，没连接过的话是空的，需要 create 一个连接。前提是 MongoDB 服务肯定要启动。连接配置填默认即可，特别注意默认启动的 MongoDB 服务端口号是 27017，所以连 27017。填完点 Test，两个指示都变绿说明连接成功，点 Save 保存。我这里已有连接，直接选 27017 这个点 Connect 进入数据库。

先从左边介绍：左侧一看就知道是已有的 database，系统默认的几个 database 放在上面，我们的 hello 数据库在下面。点击 hello 可以看到它下面的一系列功能，第一个自然是集合 collections，这里有一个 user 集合。双击 user 进入数据，中间区域被填充，顶部显示当前在 27017 端口 hello 数据库下的 user collection，里面有两条数据。

数据是树形结构，可以点开展开查看。它支持多种视图：默认树形，还有 table 表格形式，以及 JSON 格式，选自己喜欢的即可，我选树形。对数据的所有管理都能在这个界面完成。比如插入数据：右键选 Insert Document，粘贴一段 JSON 数据（name 为 Viking 那段），点 Validate 验证 JSON 有没有问题，显示 Valid 就没问题，点 Save 后数据从两条变成三条。更新也简单：双击某条文档（每条叫一个 document），在弹窗里改值，比如名称改成 Lucy、年龄改成 40，点 Save 后值就被更新了。删除则点击 delete document 即可。还有 copy JSON、view 之类的功能，看名称就知道干什么，自己试一下就行。

最后是内置的 mongo shell。这个 shell 和上节课用的 mongo 一模一样。敲一条测试命令：db.user.find({name: 'Viking'})，输入时会有提示，非常方便。输完点绿色运行键，查出一条数据，正是刚才那条 Viking 记录，说明 shell 语句运行成功。最下面还有 logs 区域，是你所有操作的历史，可以看出进行过哪些操作。

这就是最基本的操作。这个软件免费、简单、稳定、易用，Star 数多、用的人多，我认为就是个好工具。两款软件都可以去尝试，按情况选择你觉得好的。这节课就到这里，去下载安装一下吧。
