# 画面线理解：20.MongoDB的地理位置索引

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\20.MongoDB的地理位置索引【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:39, 02:06, 02:50, 03:23, 04:04, 05:12, 05:36, 06:11, 07:32, 08:40, 09:03, 09:40, 10:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:22:52

1) 这一组画面整体在讲什么（一句话）：
演示如何在 MongoDB 中创建地理空间索引，并插入和查询房屋位置数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 讲义第 28 页，标题为“5.5. MongoDB的地理位置索引”，内容介绍 MongoDB 支持存储位置的经纬度，可用于索引和查询附近数据。下方代码块显示了创建 2d 索引的命令。
画面 2: 同画面 1，PDF 讲义内容相同，但光标位置略有不同。
画面 3: 展示远程终端界面，提示符为 `root@itcast:~#`，终端为空白，准备执行命令。
画面 4: PDF 讲义第 28 页，代码块中高亮显示了创建 `loc` 字段 2d 索引的命令 `db.house.createIndex({loc:'2d'})`，并注释说明。
画面 5: 展示 EditPlus 编辑器，内容为创建 `loc` 字段 2d 索引的代码 `db.house.createIndex({loc:'2d'})`，并高亮显示了 `createdCollectionAutomatically`、`numIndexesBefore`、`numIndexesAfter` 和 `ok` 字段。
画面 6: 展示远程终端，执行了 `show tables` 命令，列出数据库中的表：`house`、`message`、`person`、`user`。接着执行了 `db.house.getIndexes()` 命令，输出了索引信息。
画面 7: PDF 讲义第 28 页，代码块中高亮显示了创建 `hid` 字段唯一索引的命令 `db.house.createIndex({hid:1},{unique:true})`，并注释说明。
画面 8: PDF 讲义第 28 页，代码块中高亮显示了插入测试数据的命令 `db.house.insert({...})`，并注释说明。
画面 9: 展示远程终端，执行了 `db.house.insert({...})` 命令，依次插入了 7 条房屋数据，每条数据包含 `hid`、`title` 和 `loc` 字段。
画面 10: 展示 EditPlus 编辑器，内容为插入测试数据的代码 `db.house.insert({...})`，并高亮显示了 `loc` 字段的经纬度坐标。
画面 11: PDF 讲义第 28 页，代码块中高亮显示了查询命令 `db.house.find(loc:{near:...,maxDistance:...})`，并注释说明。
画面 12: 展示远程终端，执行了 `db.house.find(loc:{near:...,maxDistance:...})` 命令，查询结果返回了 3 条房屋数据。
画面 13: 展示远程终端，执行了 `db.house.find(loc:{near:...,maxDistance:...})` 命令，查询结果返回了 2 条房屋数据。
画面 14: PDF 讲义第 28 页，代码块中高亮显示了创建 `loc` 字段 2d 索引的命令 `db.house.createIndex({loc:'2d'})`，并注释说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
#进入容器
docker exec -it mongodb /bin/bash
use testdb
db.house.createIndex({loc:'2d'}) #为house表的loc字段创建地理2d索引
{
  "createdCollectionAutomatically" : true,
  "numIndexesBefore" : 1,
  "numIndexesAfter" : 2,
  "ok" : 1
}
```
画面 4:
```javascript
#进入容器
docker exec -it mongodb /bin/bash
use testdb
db.house.createIndex({loc:'2d'}) #为house表的loc字段创建地理2d索引
{
  "createdCollectionAutomatically" : true,
  "numIndexesBefore" : 1,
  "numIndexesAfter" : 2,
  "ok" : 1
}
```
画面 5:
```javascript
db.house.createIndex({loc:'2d'})
{
  "createdCollectionAutomatically" : true,
  "numIndexesBefore" : 1,
  "numIndexesAfter" : 2,
  "ok" : 1
}
```
画面 7:
```javascript
db.house.createIndex({hid:1},{unique:true}) #为house表的hid字段创建唯一索引
```
画面 8:
```javascript
#插入测试数据
db.house.insert({hid:1,title:"整租 - 南门大楼 1居室 7500",loc:[121.4482236974557,31.1965239375045941]});
db.house.insert({hid:2,title:"陆家嘴板块，精装设计一室一厅，可拎包入住诚意租。",loc:[121.51804613891443,31.238878702131506]});
db.house.insert({hid:3,title:"整租 - 健安坊 1居室 4050",loc:[121.41483106993774,31.165077330435281]});
db.house.insert({hid:4,title:"整租 - 中凯城市之光·视野开阔，景色秀丽·拎包入住。",loc:[121.43528202056717,31.190687949417815]});
db.house.insert({hid:5,title:"整租 - 南京西路品质小区 21213三轨交汇·配套齐全·拎包入住。",loc:[121.43528282056717,31.190687949417815]});
db.house.insert({hid:6,title:"整租 - 简约风格·南户型·拎包入住·看房随时。",loc:[121.47521508401232,31.2385308719981]});
```
画面 11:
```javascript
#查询
db.house.find(loc:{near:[121.4831024185999,31.23515697141239],maxDistance:5/111.12})
```
画面 12:
```javascript
db.house.find(loc:{near:[121.4831024185999,31.23515697141239],maxDistance:5/111.12})
{
  "id" : ObjectId("5c1e9d04729d8b00b9db37"),
  "hid" : 6,
  "title" : "整租 - 简约风格·南户型·拎包入住·看房随时",
  "loc" : [121.47521508401232,31.2385308719981]
}
{
  "id" : ObjectId("5c1e9d04729d8b00b9db37"),
  "hid" : 2,
  "title" : "陆家嘴板块，精装设计一室一厅，可拎包入住诚意租。",
  "loc" : [121.51804613891443,31.238878702131506]
}
{
  "id" : ObjectId("5c1e9d04729d8b00b9db37"),
  "hid" : 7,
  "title" : "整租 - 桃源新村 1室0厅 5500元",
  "loc" : [121.4831024185999,31.23515697141239]
}
```
画面 13:
```javascript
db.house.find(loc:{near:[121.4831024185999,31.23515697141239],maxDistance:2/111.12})
db.house.find(loc:{near:[121.4831024185999,31.2351569714123
