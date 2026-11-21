# 画面线理解：10.搭建主从复制架构之搭建从库（slave）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\10.搭建主从复制架构之搭建从库（slave）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:17, 00:30, 00:42, 01:12, 01:44, 01:58, 02:43, 03:33, 04:01, 04:35, 05:00, 05:15, 07:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:34:44

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 环境下通过 Docker 搭建 MySQL 从库，并配置其连接主库以实现主从复制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示 Typora 编辑器中的文档内容，标题为“3.6. 搭建从库”。
- 文档中包含搭建从库的步骤：创建目录、创建配置文件、输入配置内容、创建 Docker 容器、启动容器。
- 文档中显示的代码片段：
  ```
  #创建目录
  mkdir /data/mysql/slave01
  cd /data/mysql/slave01
  mkdir conf data
  chmod 777 * -R

  #创建配置文件
  cd /data/mysql/slave01/conf
  vim my.cnf

  #输入如下内容
  [mysqld]
  server-id=2 #服务id，不可重复
  sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'

  #创建容器
  docker create --name percona-slave01 -v /data/mysql/slave01/data:/var/lib/mysql -v /data/mysql/slave01/conf:/etc/my.cnf.d -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

  #启动
  docker start percona-slave01 && docker logs -f percona-slave01
  ```

画面 2:
- 展示一个 PPT 幻灯片，内容为多个窗口的截图，包括 Typora、终端、Navicat 等，用于说明课程内容的多工具协同。
- 幻灯片中显示 IP 地址“192.168.1.18”。

画面 3:
- 展示终端窗口，执行了创建目录、进入目录、创建子目录、修改权限等命令。
- 命令执行结果：
  ```
  root@itcast02:conf# mkdir /data/mysql/slave01
  root@itcast02:conf# cd /data/mysql/slave01
  root@itcast02:slave01# ll
  drwxr-xr-x 2 root root 4096 Feb 2 23:56 ./
  drwxr-xr-x 4 root root 4096 Feb 2 23:56 ../
  root@itcast02:slave01# mkdir conf data
  root@itcast02:slave01# ll
  drwxr-xr-x 4 root root 4096 Feb 2 23:56 ./
  drwxr-xr-x 2 root root 4096 Feb 2 23:56 ../
  drwxr-xr-x 2 root root 4096 Feb 2 23:56 conf/
  drwxrwxrwx 2 root root 4096 Feb 2 23:56 data/
  root@itcast02:slave01# chmod 777 * -R
  root@itcast02:slave01# ll
  drwxr-xr-x 4 root root 4096 Feb 2 23:56 ./
  drwxr-xr-x 2 root root 4096 Feb 2 23:56 ../
  drwxr-xr-x 2 root root 4096 Feb 2 23:56 conf/
  drwxrwxrwx 2 root root 4096 Feb 2 23:56 data/
  ```

画面 4:
- 继续在终端中执行命令，进入 conf 目录并创建配置文件。
- 命令：
  ```
  root@itcast02:slave01# cd conf
  root@itcast02:conf# ll
  total 8
  drwxrwxrwx 2 root root 4096 Feb 2 23:56 ./
  drwxr-xr-x 4 root root 4096 Feb 2 23:56 ../
  root@itcast02:conf# vim my.cnf
  ```

画面 5:
- 展示 Typora 文档，内容与画面 1 相同，但光标位于“输入如下内容”部分。
- 文档中显示的代码片段：
  ```
  #创建目录
  mkdir /data/mysql/slave01
  cd /data/mysql/slave01
  mkdir conf data
  chmod 777 * -R

  #创建配置文件
  cd /data/mysql/slave01/conf
  vim my.cnf

  #输入如下内容
  [mysqld]
  server-id=2 #服务id，不可重复
  sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'

  #创建容器
  docker create --name percona-slave01 -v /data/mysql/slave01/data:/var/lib/mysql -v /data/mysql/slave01/conf:/etc/my.cnf.d -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

  #启动
  docker start percona-slave01 && docker logs -f percona-slave01
  ```

画面 6:
- 终端中执行了创建 Docker 容器和启动容器的命令。
- 命令：
  ```
  root@itcast02:conf# docker create --name percona-slave01 -v /data/mysql/slave01/data:/var/lib/mysql -v /data/mysql/slave01/conf:/etc/my.cnf.d -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
  94de9d98b5e6dbb68b57b7e15cfd0dd15f934ee73f8f298e33ac2de685e
  root@itcast02:conf# docker start percona-slave01 && docker logs -f percona-slave01
  ```

画面 7:
- 展示 Docker 容器启动后的日志输出。
- 日志内容：
  ```
  2019-02-03T15:57:53.127763Z [Note] InnoDB: 96 redo rollback segment(s) found. 96 redo rollback segment(s) are active.
  2019-02-03T15:57:53.129413Z [Note] InnoDB: 32 non-redo rollback segment(s) are active.
  2019-02-03T15:57:53.131335Z [Note] InnoDB: Waiting for purge to start
  2019-02-03T15:57:53.131857Z [Note] InnoDB: 5.7.23 started; log sequence number 11904542
  2019-02-03T15:57:53.135834Z [Note] Plugin 'FEDERATED' is disabled.
  2019-02-03T15:57:53.135834Z [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/lib/plugin_pool
  2019-02-03T15:57:53.135834Z [Note] InnoDB: Found ca.pem, server-cert.pem and server-key.pem in data directory
  2019-02-03T15:57:53.135834Z [Note] InnoDB: Skipping generation of SSL certificates as certificate files are present in data directory
  2019-02-03T15:57:53.190187Z [Note] InnoDB: Buffer pool(s) load completed at 190203 15:57:53
  2019-02-03T15:57:53.199062Z [Note] IPv6 is available.
  2019-02-03T15:57:53.203077Z [Note] Event Scheduler: Loaded 0 events
  2019-02-03T15:57:53.203292
