# 画面线理解：05.Elasticsearch快速入门之单机版安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\05.Elasticsearch快速入门之单机版安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:36, 02:13, 02:57, 03:26, 04:18, 06:15, 06:52, 07:58, 08:46, 09:14, 09:54, 10:17, 10:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:27:28

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中手动解压、配置并启动 Elasticsearch 6.5.4 单节点服务，包括修改配置文件、调整 JVM 参数和系统内核参数，并通过 REST API 验证服务状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Elasticsearch 官网的 RESTful API 示例代码，其中包含 `Resilient->search($params);`。
画面 2: 在终端中执行 `rm -rf *` 清理目录，然后列出目录内容，显示 `elasticsearch-6.5.4.tar.gz` 文件，接着执行 `rm -rf es` 删除旧目录。
画面 3: 列出 `elasticsearch-6.5.4` 解压后的目录结构，包含 `bin`、`modules`、`plugins` 等子目录。
画面 4: 在终端中执行 `cd es` 进入目录，然后执行 `chown -R elasticsearch:elasticsearch es` 修改目录权限。
画面 5: 在 PDF 文档中显示单机版安装步骤，包含命令：`useradd elasticsearch` 和 `tar -xvf elasticsearch-6.5.4.tar.gz -C /haoke/es/`。
画面 6: 在终端中编辑 `elasticsearch.yml` 配置文件，设置 `network.host: 172.16.55.185` 和 `http.port: 9200`，并提示 `E138: Can't write viminfo file /viminfo`。
画面 7: 在终端中编辑 `/etc/sysctl.conf` 文件，显示内核参数配置，如 `net.ipv4.conf.all.rp_filter=1`。
画面 8: 在终端中进入 `bin` 目录，列出可执行脚本，然后执行 `./elasticsearch` 启动服务。
画面 9: 在浏览器中访问 `172.16.55.185:9200`，显示 Elasticsearch 的响应信息。
画面 10: 在 Advanced REST Client 中构造 POST 请求，发送 JSON 数据：`{"email": "xxx", "password": "xxx"}`。
画面 11: 在终端中查看 Elasticsearch 启动日志，显示 `high disk watermark [90%] exceeded` 警告和 `shards will be relocated away from this node` 信息。
画面 12: 在 PDF 文档中显示 Docker 安装部分，包含命令 `kill 68072`。
画面 13: 在终端中执行 `kill 68072` 结束进程，然后执行 `su - elasticsearch` 切换用户，执行 `cd /haoke/es/` 进入目录，执行 `./elasticsearch` 启动服务。
画面 14: 在 PDF 文档中显示修改配置文件的步骤，包括 `vim conf/elasticsearch.yml`、`vim conf/jvm.options`、`vim /etc/sysctl.conf`，并提示 `启动ES服务`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```php
$response = Resilient->search($params);
```
画面 2:
```bash
rm -rf *
ll
rm -rf es
```
画面 3:
```
elasticsearch-6.5.4/bin/elasticsearch-plugin.bat
elasticsearch-6.5.4/bin/elasticsearch-env.bat
elasticsearch-6.5.4/bin/elasticsearch-keystore.bat
elasticsearch-6.5.4/README.txt
elasticsearch-6.5.4/LICENSE.txt
elasticsearch-6.5.4/modules/x-pack-monitoring/
elasticsearch-6.5.4/modules/x-pack-monitoring/plugin-descriptor.properties
elasticsearch-6.5.4/modules/x-pack-monitoring/elasticsearch-rest-client-sniffer-6.5.4.jar
elasticsearch-6.5.4/modules/x-pack-monitoring/LICENSE.txt
elasticsearch-6.5.4/modules/x-pack-monitoring/plugin-security.policy
elasticsearch-6.5.4/modules/mapper-extras/
elasticsearch-6.5.4/modules/mapper-extras/plugin-descriptor-6.5.4.jar
elasticsearch-6.5.4/modules/mapper-extras/plugin-security.policy
elasticsearch-6.5.4/modules/percolator/
elasticsearch-6.5.4/modules/percolator/plugin-descriptor-6.5.4.jar
elasticsearch-6.5.4/modules/percolator/plugin-security.policy
elasticsearch-6.5.4/modules/ingest-common/
elasticsearch-6.5.4/modules/ingest-common/plugin-descriptor-6.5.4.jar
elasticsearch-6.5.4/modules/ingest-common/joni-2.1.6.jar
elasticsearch-6.5.4/modules/ingest-common/jcodings-1.0.12.jar
```
画面 4:
```bash
chown -R elasticsearch:elasticsearch es
```
画面 5:
```bash
#创建Elasticsearch用户，Elasticsearch不支持root用户运行
useradd elasticsearch
#解压安装包
tar -xvf elasticsearch-6.5.4.tar.gz -C /haoke/es/
```
画面 6:
```yaml
# Set the bind address to a specific IP (IPv4 or IPv6):
network.host: 172.16.55.185

# Set a custom port for HTTP:
http.port: 9200

# For more information, consult the network module documentation.

# Discovery
# Pass an initial list of hosts to perform discovery when new node is started:
# The default list of hosts is ["127.0.0.1", "[::1]"]
# discovery.zen.ping.unicast.hosts: ["host1", "host2"]

# Prevent the "split brain" by configuring the majority of nodes (total number of master-eligible nodes / 2 + 1):
discovery.zen.minimum_master_nodes: "1"
```
画面 7:
```
#kernel.domainname = example.com
#kernel.printk = 3 4 1 3
# Functions previously found in netbase
# Uncomment the next two lines to enable Spoof protection (reverse-path filter)
# Turn on Source Address Verification in all interfaces to
# prevent some spoofing attacks
net.ipv4.conf.default.rp_filter=1
net.ipv4.conf.all.rp_filter=1

# Uncomment the next line to enable TCP/IP SYN cookies
# See http://lwn.net/Articles/277146/
# Note: This may impact IPv4 TCP sessions too
net.ipv4.tcp_syncookies=1

# Uncomment the next line to enable packet forwarding for IPv4
"etc/sysctl.conf" [readonly] 63L, 210C
```
画面 8:
```bash
cd ..
cd bin
ls
./elasticsearch
```
画面 9:
```
172.16.55.185:9200
```
画面 10:
```json
{
  "email": "xxx",
  "password": "xxx"
}
```
画面 11:
```
[2018-12-31T20:26:20,275][WARN ][o.e.c.r.a.DiskThresholdMonitor] [x30rcg] high disk watermark [90%] exceeded on [x30rcg][fS6qY3lC8LC0][1][haoke/es/elasticsearch-6.5.4/data/nodes][0] free: 2.5gb[8.9%], shards will be relocated away from this node
[2018-12-31T20:26:20,280][WARN ][o.e.c.r.a.DiskThresholdMonitor] [x30rcg] high disk watermark [90%] exceeded on [x30rcg][fS6qY3lC8LC0][1][haoke/es/elasticsearch-6.5.4/data/nodes][0] free: 2.5gb[8.9%], shards will be relocated away from this node
[2018-12-31T20:26:20,280][WARN ][o.e.c.r.a.DiskThresholdMonitor] [x30rcg] high disk watermark [90%] exceeded on [x30rcg][fS6qY3lC8LC0][1][haoke/es/elasticsearch-6.5.4/data/nodes][0] free: 2.5gb[8.9%], shards will be relocated away from this node
[2018-12-31T20:26:20,280][WARN ][o.e.c.r.a.DiskThresholdMonitor] [x30rcg] high disk watermark [90%] exceeded on [x30rcg][fS6qY3lC8LC0][1
