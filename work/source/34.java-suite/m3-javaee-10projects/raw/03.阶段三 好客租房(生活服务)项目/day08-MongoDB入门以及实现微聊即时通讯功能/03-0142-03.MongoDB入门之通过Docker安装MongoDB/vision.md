# 画面线理解：03.MongoDB入门之通过Docker安装MongoDB

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\03.MongoDB入门之通过Docker安装MongoDB【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 02:42, 03:11, 03:25, 03:31, 03:33, 03:35, 03:51, 04:10, 04:16, 04:20, 04:28, 04:38, 06:21, 06:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:34:39

1) 这一组画面整体在讲如何通过 Docker 安装并启动 MongoDB 容器，并演示了基本的数据库操作。

2) 按时间顺序列出每张画面的要点：
画面1: 空命令行界面，等待输入。
画面2: 执行 docker create 命令创建名为 mongodb 的容器，因名称冲突报错，随后执行 docker rm 删除旧容器。
画面3: 执行 docker start 启动容器，随后执行 docker ps 查看容器状态，显示 mongodb 容器已启动。
画面4: 与画面3相同，显示 docker ps 列表。
画面5: 与画面3相同，显示 docker ps 列表。
画面6: 展示 PDF 文档内容，标题为“1.2、通过docker安装MongoDB”，列出相关命令。
画面7: 与画面3相同，显示 docker ps 列表。
画面8: 与画面6相同，展示 PDF 文档内容。
画面9: 与画面3相同，显示 docker ps 列表。
画面10: 执行 docker rm 删除旧容器，然后重新创建并启动容器，进入容器内部。
画面11: 进入容器后执行 mongo 命令，进入 MongoDB 命令行。
画面12: 在 MongoDB 命令行中显示启动日志和提示信息。
画面13: 在 MongoDB 命令行中执行 show dbs 命令，列出数据库。
画面14: 与画面6相同，展示 PDF 文档内容。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2:
docker create --name mongodb -p 27017:27017 -v /data/mongodb/data/db mongo:4.0.3
docker rm mongodb

画面3:
docker ps

画面6:
1. #拉取镜像
docker pull mongo:4.0.3
2. #创建容器
docker create --name mongodb -p 27017:27017 -v /data/mongodb/data/db mongo:4.0.3
3. #启动容器
docker start mongodb
4. #进入容器
docker exec -it mongodb /bin/bash
5. #使用MongoDB客户端进行操作
mongo
6. > show dbs #查询所有的数据库
admin 0.000GB
config 0.000GB
local 0.000GB

画面10:
docker rm mongodb
docker create --name mongodb -p 27017:27017 -v /data/mongodb/data/db mongo:4.0.3
docker start mongodb
docker exec -it mongodb /bin/bash

画面11:
mongo

画面13:
> show dbs
admin 0.000GB
config 0.000GB
local 0.000GB

4) PPT 标题、架构图/流程图的结构、表格数据：
画面6:
标题: 1.2、通过docker安装MongoDB
标题: 1.3、MongoDB基本操作
表格数据:
1. #拉取镜像
docker pull mongo:4.0.3
2. #创建容器
docker create --name mongodb -p 27017:27017 -v /data/mongodb/data/db mongo:4.0.3
3. #启动容器
docker start mongodb
4. #进入容器
docker exec -it mongodb /bin/bash
5. #使用MongoDB客户端进行操作
mongo
6. > show dbs #查询所有的数据库
admin 0.000GB
config 0.000GB
local 0.000GB

5) 无
