# 画面线理解：21.Logstash入门学习之Filebeat与Logstash整合

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\21.Logstash入门学习之Filebeat与Logstash整合【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:51, 02:36, 03:03, 03:44, 04:19, 05:06, 06:07, 06:46, 08:04, 08:57, 09:27, 09:55, 10:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:27:54

1) 这一组画面整体在讲如何配置 Filebeat 和 Logstash 来收集并处理 Nginx 的访问日志。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PPT 页面“5.3、接收Filebeat输入的日志”，图示说明 Nginx 生成日志文件，Filebeat 读取并发送至 Logstash。
画面2：SSH 登录到 Ubuntu 16.04.5 LTS 系统，提示符为 root@itcast01。
画面3：执行 `service nginx status` 命令，确认 Nginx 服务正在运行，主进程 ID 为 1244。
画面4：展示 PPT 页面“5.3.1、安装Nginx”，其中包含安装 Nginx 的命令和配置文件路径。
画面5：在 Filebeat 目录下执行 `ll` 命令，列出目录内容，包括 `filebeat.yml`、`haoke-nginx.yml` 等配置文件。
画面6：展示 `filebeat.yml` 配置文件内容，包含输入模块配置、输出 Elasticsearch 的 hosts 和 Kibana 的 host。
画面7：展示 PPT 页面“5.3.2、配置Filebeat”，其中包含 `haoke-nginx.yml` 配置文件内容，设置输入路径、tags、fields 和输出 Logstash 的 hosts。
画面8：执行 `./filebeat -e -c haoke-nginx.yml` 启动 Filebeat，终端显示连接 Logstash 失败，提示“connection refused”。
画面9：在 Logstash 目录下执行 `ll` 命令，列出目录内容，包括 `config/`、`logs/`、`modules/` 等。
画面10：进入 Logstash 的 config 目录，执行 `ll` 命令，列出 `haoke-pipeline.conf` 等配置文件。
画面11：执行 `bin/logstash -f haoke-pipeline.conf -config.reload.automatic` 命令启动 Logstash，终端显示配置成功。
画面12：Filebeat 启动后，终端显示连接 Logstash 失败，提示“connection refused”，随后 Logstash 启动成功。
画面13：在终端中执行 `cat` 命令查看 Filebeat 读取到的日志内容，显示日志的详细字段。
画面14：展示 PPT 页面“5.3.4、测试”，其中包含测试日志内容，显示日志的详细字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面6：
```yaml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/nginx/access.log
  tags: ["log"]

filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false

setup.template.settings:
  index.number_of_shards: 3

output.elasticsearch:
  hosts: ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
  setup.kibana:
    host: "192.168.1.7:5601"
```

画面7：
```yaml
#win haoke-nginx.yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/nginx/access.log
  tags: ["log"]
  fields:
    from: nginx
  fields_under_root: false

output.logstash:
  hosts: ["192.168.1.7:5044"]
```

画面13：
```json
{
  "message": "192.168.1.20 - [15/Jan/2019:23:35:10 +0800] \"GET / HTTP/1.1\" 304 0 \"-\" \"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36\"",
  "offset": 13169,
  "tags": [
    "log"
  ],
  "beat": {
    "version": "6.5.4",
    "name": "itcast01",
    "hostname": "itcast01"
  },
  "prospector": {
    "type": "log"
  },
  "source": "/var/log/nginx/access.log",
  "@timestamp": "2019-01-15T15:23:35.20+0800",
  "fields": {
    "from": "nginx"
  }
}
```

画面14：
```json
{
  "@timestamp": "2019-01-14T23:37:60+0800",
  "Fields": [
    "from": "nginx"
  ],
  "source": "/var/log/nginx/access.log",
  "host": {
    "name": "itcast01"
  },
  "beat": {
    "name": "itcast01",
    "version": "6.5.4",
    "hostname": "itcast01"
  },
  "version": "1",
  "offset": 600,
  "message": "192.168.1.20 - [14/Jan/2019:20:23:35 +0800] \"GET / HTTP/1.1\" 304 0 \"-\" \"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36\""
}
```

4) 出现的 PPT 标题、架构图/流程图的结构：
画面1：标题“5.3、接收Filebeat输入的日志”，图示：Nginx → 日志文件 → Filebeat → Logstash。
画面4：标题“5.3.1、安装Nginx”，包含命令和配置文件路径。
画面7：标题“5.3.2、配置Filebeat”，包含配置文件内容。
画面14：标题“5.3.4、测试”，包含测试日志内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
