# 画面线理解：12-ETL-维度数据采集-注意事项-NiFi采集乱码处理

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\12-ETL-维度数据采集-注意事项-NiFi采集乱码处理_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:20, 00:24, 01:02, 01:08, 02:08, 02:14, 02:38, 02:58, 03:00, 03:30, 03:48, 04:23, 04:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:45:35

1) 这一组画面整体在讲如何通过重启 Nifi 服务来解决数据表中维度字段乱码的问题，并展示数据清洗流程。

2) 按时间顺序列出每张画面的要点：
画面1：在 Hue 的 Table Browser 中查看 course_dim 表，数据中存在乱码（如“?????”）。
画面2：在 Navicat 中查看 MySQL 数据库 xc_online 的 course_base 表，数据完整无乱码。
画面3：在 Typora 中打开文档，显示“3.2.6.1 注意事项”部分，内容为解决 Nifi 数据乱码的步骤。
画面4：在 Xshell 中执行 docker ps 命令，查看正在运行的容器，包括 xc-online-nifi。
画面5：在 Typora 中显示文档“3.2.6.1 注意事项”部分，光标在“docker exec -it xc-online-nifi bash”命令上。
画面6：在 Xshell 中执行命令进入 Nifi 容器并重启服务。
画面7：在 Xshell 中执行命令，显示 Nifi 服务正在关闭。
画面8：在 Xshell 中执行命令，显示 Nifi 服务已成功启动。
画面9：在浏览器中打开 Nifi 的 UI 界面，显示启动中。
画面10：在 Nifi UI 中查看数据清洗流程，包含 ConvertAvroToJSON 和 PutHiveQL 等处理器。
画面11：在 Hue 的 Table Browser 中查看 course_dim 表，数据已更新，乱码消失。
画面12：在 Hue 的 Table Browser 中查看 course_dim 表，数据已更新，乱码消失。
画面13：在 Hue 的 Table Browser 中查看 course_dim 表，数据已更新，乱码消失。
画面14：在 Typora 中显示文档“3.2.6.1 注意事项”部分，光标在“docker exec -it xc-online-nifi bash”命令上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```
# 重启nifi容器
docker exec -it xc-online-nifi bash
# 重启nifi
$NIFI_HOME/bin/nifi.sh restart
# nifi重启成功后，再次刷新即可
```

画面6：
```
docker exec -it xc-online-nifi bash
[ root@xc-online-nifi opt ]# nifi.sh restart
```

画面7：
```
docker exec -it xc-online-nifi bash
[ root@xc-online-nifi opt ]# nifi.sh restart
```

画面8：
```
Bootstrap Config File: /opt/nifi-1.9.2/conf/bootstrap.conf
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面10：Nifi 流程图，包含以下组件及连接：
- ConvertAvroToJSON (1.9.2) → JsonToHiveProcessor (1.9.2)
- JsonToHiveProcessor → PutHiveQL

5) 不要评价画面美观，不要输出与课程无关的内容。
