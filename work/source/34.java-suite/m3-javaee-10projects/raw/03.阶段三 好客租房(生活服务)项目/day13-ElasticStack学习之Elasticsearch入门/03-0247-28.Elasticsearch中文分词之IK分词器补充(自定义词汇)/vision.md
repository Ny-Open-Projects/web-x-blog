# 画面线理解：28.Elasticsearch中文分词之IK分词器补充（自定义词汇）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\28.Elasticsearch中文分词之IK分词器补充（自定义词汇）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:28, 00:59, 01:22, 02:28, 02:49, 03:06, 03:35, 03:42, 03:49, 04:10, 04:22, 04:30, 04:57, 06:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:42:08

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Elasticsearch 中安装、配置并测试 IK 分词器插件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 进入 Elasticsearch 服务器的终端，位于根目录。
画面 2: 进入 plugins 目录，进入 ik 插件目录，查看 config 文件夹。
画面 3: 进入 ik 的 config 目录，查看文件列表，尝试查看 ik 文件夹失败。
画面 4: 查看 IKAnalyzer.cfg.xml 配置文件内容，显示注释和属性配置。
画面 5: 在终端中查看 my.dic 文件内容，显示自定义词典内容。
画面 6: 启动 Elasticsearch，日志显示 IK 分词器加载配置文件并成功加载。
画面 7: 使用 Postman 发送 POST 请求到分析接口，输入文本“欢迎来到黑马程序员”，返回分词结果。
画面 8: 输入文本“徐老师来送山”，返回分词结果。
画面 9: 输入文本“我在准备学习，加油，欢迎来到黑马程序员”，返回分词结果。
画面 10: 输入文本“黑马程序员”，返回分词结果。
画面 11: 输入文本“我在准备学习，加油，欢迎来到黑马程序员”，返回分词结果。
画面 12: 输入文本“我在准备学习，加油，欢迎来到黑马程序员”，返回分词结果。
画面 13: 在浏览器中查看 Elasticsearch 的搜索结果，显示高亮匹配的文本。
画面 14: 在浏览器中查看 IK 分词器的配置文档，显示字典配置和热更新方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```bash
[root@itcast plugins]# cd plugins/
[root@itcast plugins]# ll
total 12
drwxr-xr-x 3 root root 4996 Dec 31 12:49 ingest-geop
drwxr-xr-x 2 root root 4996 Dec 17 11:24 data
drwxr-xr-x 28 root root 4996 Jan 17 12:51 logs
drwxr-xr-x 5 root root 4996 Jan 17 12:42 modules
[root@itcast plugins]# cd ik/
[root@itcast ik]# ll
total 1432
-rw-r--r-- 1 root root 263965 May 6 2018 commons-codec-1.9.jar
-rw-r--r-- 1 root root 61829 May 6 2018 commons-logging-1.2.jar
-rw-r--r-- 1 root root 54993 Dec 23 11:26 elasticsearch-analysis-ik-6.5.4.jar
-rw-r--r-- 1 root root 36724 May 6 2018 httpclient-4.5.2.jar
-rw-r--r-- 1 root root 1805 Dec 23 11:26 plugin-descriptor.properties
-rw-r--r-- 1 root root 125 Dec 23 11:26 plugin-security.policy
[root@itcast ik]# cd config/
[root@itcast config]# ll
total 6264
-rw-r--r-- 1 root root 625 Jan 1 12:54 IKAnalyzer.cfg.xml
-rw-r--r-- 1 root root 5293922 Aug 26 17:52 extra main.dic
-rw-r--r-- 1 root root 63188 Aug 26 17:52 extra_single_word.dic
-rw-r--r-- 1 root root 10855 Aug 26 17:52 extra single word low freq.dic
-rw-r--r-- 1 root root 156 Aug 26 17:52 stopword.dic
-rw-r--r-- 1 root root 3858510 Aug 26 17:52 main.dic
-rw-r--r-- 1 root root 13 Jan 1 12:52 my.dic
-rw-r--r-- 1 root root 123 Aug 26 17:52 preposition.dic
-rw-r--r-- 1 root root 164 Aug 26 17:52 quantifier.dic
-rw-r--r-- 1 root root 192 Aug 26 17:52 suffix.dic
-rw-r--r-- 1 root root 752 Aug 26 17:52 surname.dic
```

画面 3:
```bash
[root@itcast config]# vi IKAnalyzer.cfg.xml
[root@itcast config]# cat ik
cat: ik: No such file or directory
[root@itcast config]# cat IKAnalyzer.cfg.xml
[root@itcast config]# vi my.dic
```

画面 4:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
<!--comments:IK Analyzer 扩展配置-->
<!--用户可以在这里配置自己的扩展字典-->
<entry keys="ext_dict"></entry>
<!--用户可以在这里配置自己的扩展停止词典-->
<entry keys="ext_stopwords"></entry>
<!--用户可以在这里配置远程扩展词典-->
<entry keys="remote_ext_dict">words_location</entry>
<!--用户可以在这里配置远程扩展停止词典-->
<entry keys="remote_ext_stopwords">words_location</entry>
</properties>
```

画面 5:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
<!--comments:IK Analyzer 扩展配置-->
<!--用户可以在这里配置自己的扩展字典-->
<entry keys="ext_dict"></entry>
<!--用户可以在这里配置自己的扩展停止词典-->
<entry keys="ext_stopwords"></entry>
<!--用户可以在这里配置远程扩展词典-->
<entry keys="remote_ext_dict">words_location</entry>
<!--用户可以在这里配置远程扩展停止词典-->
<entry keys="remote_ext_stopwords">words_location</entry>
</properties>
```

画面 6:
```log
[2019-01-12T12:58:56,545][INFO ][o.e.p.PluginsService] loaded plugin [ingest-geop]
[2019-01-12T12:58:56,545][INFO ][o.e.p.PluginsService] loaded plugin [ingest-user-agent]
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] parsed [0] roles from file /usr/share/elasticsearch/config/roles.yml
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] loaded plugin [ingest-geop]
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] parsed [0] roles from file /usr/share/elasticsearch/config/roles.yml
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] loaded plugin [ingest-user-agent]
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] parsed [0] roles from file /usr/share/elasticsearch/config/roles.yml
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] loaded plugin [ingest-geop]
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] parsed [0] roles from file /usr/share/elasticsearch/config/roles.yml
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] loaded plugin [ingest-user-agent]
[2019-01-12T12:58:5
