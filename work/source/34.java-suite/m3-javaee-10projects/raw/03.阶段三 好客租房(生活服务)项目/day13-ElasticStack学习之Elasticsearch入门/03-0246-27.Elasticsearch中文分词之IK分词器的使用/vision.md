# 画面线理解：27.Elasticsearch中文分词之IK分词器的使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\27.Elasticsearch中文分词之IK分词器的使用【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 02:47, 03:20, 03:58, 05:36, 05:48, 06:02, 06:33, 06:57, 07:17, 08:13, 08:41, 09:09, 09:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:41:17

1) 这一组画面整体在讲如何在 Elasticsearch 中安装并测试 IK 中文分词插件。

2) 按时间顺序列出每张画面的要点：
画面1：展示《中文分词》章节内容，说明中文分词难点及示例“我爱/炒肉丝”。
画面2：展示 GitHub 仓库页面，介绍 IK Analysis for Elasticsearch 插件及其支持的版本。
画面3：展示 GitHub 仓库的代码目录结构，包含 config、src、licenses 等文件夹。
画面4：展示插件安装说明，包含下载预编译包或使用插件安装命令，以及创建索引和映射的快速示例。
画面5：在终端中列出 /tmp 目录下的文件，显示下载的 ik-6.5.4.zip 文件。
画面6：在终端中执行 docker cp 命令，将 ik-6.5.4.zip 文件复制到 Elasticsearch 容器内。
画面7：在终端中进入 Elasticsearch 容器，进入 plugins 目录。
画面8：在终端中解压 ik-6.5.4.zip 文件，列出解压后的文件。
画面9：展示 Elasticsearch 启动日志，显示 IK 分词插件已加载。
画面10：展示 PDF 文档中测试 IK 分词的命令和结果示例。
画面11：在 Postman 中发送 POST 请求测试 IK 分词，请求体为 {"analyzer": "ik_max_word", "text": "我是中国人"}。
画面12：在 Postman 中修改请求体，测试文本“我喜欢吃苹果”。
画面13：在 Postman 中修改请求体，测试文本“北京的天气真好”。
画面14：展示 PDF 文档中 IK 分词插件的安装方法和测试命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
{
  "token": "If the document doesn't already exist",
  "start_offset": 0,
  "end_offset": 3,
  "type": "word",
  "position": 0
}
画面2：
IK version  ES version
master  6.x -> master
6.3.0  6.3.0
6.2.4  6.2.4
画面4：
1.download or compile
  • optional 1 download pre-build package from here: https://github.com/medcl/elasticsearch-analysis-ik/releases
    create plugin folder cd your-es-root/plugins && mkdir ik
    unzip plugin to folder your-es-root/plugins/ik
  • optional 2 - use elasticsearch-plugin to install (supported from version v5.5.1):
    ./bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v5.3.8/elasticsearch-analysis-ik-5.3.8.zip
    NOTE: replace 5.3.8 to your own elasticsearch version
2.restart elasticsearch
Quick Example
1.create a index
curl -XPUT http://localhost:9200/index
2.create a mapping
画面5：
root@itcast:/tmp# ll
画面6：
root@itcast:/tmp# docker cp /tmp/elasticsearch-analysis-ik-6.5.4.zip elasticsearch:/usr/share/elasticsearch/plugins/
画面7：
[root@itcast elasticsearch]# cd plugins/
[root@itcast plugins]# ll
画面8：
[root@itcast ik]# ll
画面9：
[2019-01-11T12:43:36,634][INFO ][o.e.p.PluginsService] [VsaJSG] loaded module [x-pack-watcher]
[2019-01-11T12:43:36,637][INFO ][o.e.p.PluginsService] [VsaJSG] loaded plugin [analysis-ik]
[2019-01-11T12:43:36,637][INFO ][o.e.p.PluginsService] [VsaJSG] loaded plugin [ingest-geopoint]
[2019-01-11T12:43:36,637][INFO ][o.e.p.PluginsService] [VsaJSG] loaded plugin [ingest-user-agent]
[2019-01-11T12:43:36,637][INFO ][o.e.x.s.FileRolesMessageHandler] [VsaJSG] parsed [0] roles from file /usr/share/elasticsearch/config/roles.yml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] controller [64 bit] Version 6.3.4 (build 1608688527239) Copyright © 2018 Elasticsearch BV
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] using discovery type [single-node] and host controller [settings]
[2019-01-11T12:43:36,637][INFO ][o.e.n.Node] [VsaJSG] initialized
[2019-01-11T12:43:36,637][INFO ][o.e.n.Node] [VsaJSG] started
[2019-01-11T12:43:36,637][INFO ][o.e.n.Node] [VsaJSG] publish address [172.16.55.185:9300], bound addresses [172.16.55.185:9200]
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/config/analysis-ik/config.xml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/plugins/ik/config/analysis-ik/config.xml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/plugins/ik/config/analysis-ik/config.xml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/plugins/ik/config/analysis-ik/config.xml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/plugins/ik/config/analysis-ik/config.xml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/plugins/ik/config/analysis-ik/config.xml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/plugins/ik/config/analysis-ik/config.xml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/plugins/ik/config/analysis-ik/config.xml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/plugins/ik/config/analysis-ik/config.xml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/plugins/ik/config/analysis-ik/config.xml
[2019-01-11T12:43:36,637][INFO ][o.e.x.m.p.CoptDiscoveryModule] [VsaJSG] tried to load config from /usr/share/elasticsearch/plugins/ik/config/analysis-ik/config.xml
[2019-01-11T1
