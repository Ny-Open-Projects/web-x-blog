# 28.Elasticsearch中文分词之IK分词器补充（自定义词汇）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\28.Elasticsearch中文分词之IK分词器补充（自定义词汇）【海量资源尽在 ubkz.com】.mp4
- 时长 6分27秒（音频 388s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面呢我们来演示一下使用这个IK分支器如何去扩展这个词典或者是扩展我们这个词汇那么我们可以看到官方啊就是这个插件的这个网站啊它的一个这个描述在这个位置呢可以看到我们需要修改它的一个配置文件在配置文件中呢在这个位置加我们自己的一个扩展的一个字典那么我们来实际的操作一下啊那么因为这个相对还是比较简单的我们简单操作一下啊
[00:29] 那么我们先去进入到什么呢进入到我们这个还是需要先进入我们的容器啊那么通过他先进入进去然后呢然后我们要先进入他啊进入这个容器之后啊然后呢我们就看一下啊进入这个plugins然后呢我们去进入这个ik然后呢我们进入configconfig下面
[01:00] 然后在这个下面呢有一个IK的underlayer这个配置文件就它啊那么我们先来打开一下IK然后呢它的扩展的和词汇的位置呢就在这儿就在这儿当然我们打开这个文件呢会发现啊有一些这个乱码它仅仅是乱码那么其实我们可以通过这个cat来查看一下啊IK大写的K
[01:26] 然后呢可以看到它的里面的这个内容是OK的只是我们刚刚的VI这个编辑器的问题啊那么我们只需要在这个位置给它去设置就可以了下面我们来定义一个自己的一个呃吃点比如说就叫my.my.这个DICOK那么这个里面呢那我们把它再重写一下吧其实这个里面我们写的就是传辑播客我们大概写这么几个吧比如说我们写一个传辑播客还有个黑马程序员然后呢
[01:55] 比如说还有一个现在现在比较流行流行的这样的一些这个词汇比如说叫叫什么抖音是吧抖音抖音抖音还有比如说叫什么呢蓝瘦是吧叫做蓝瘦香菇香菇OK那么这个呢是一个词汇他之前肯定是没有这样的词汇的对吧那么可以把这个词汇呢我们去
[02:25] 扩展到我们这个制定语词汇中那我们可以cat来查看一下my.dic那么可以看到是不是有四个词汇我们扩展进去了然后我们就去打开我们这个ik的一个配置文件然后在这个扩展这个词这个下面我们去输入我们这个文件名叫my.dic好嘞保存退出那么cat查看一下
[02:51] 那么我可以看到是不是这个配置已经就改到这个位置来了OK没有问题好那么我们就退出然后呢把我们这个容器啊进行做一个重启然后呢我们去查看一下它的日志OK那么等待它的一个启动那么现在呢我们看到它已经启动起来了我们先来测试一下啊那么还是按照刚刚我们这个测试来看一下那么我在传字播客学习走那么它的一个结果呢是我在你看传字播客是不是就认为这是一个词汇了
[03:20] 那么前面的话是不是就会把传之播客都会拆成四个字啊那么比如说我们可以再加一些这个说法对吧我在传之播客学习那么挺好的啊挺好的欢迎欢迎欢迎来什么的黑马程序员程序程序员学习那么黑马程序员是高端的品牌啊高端品牌OK
[03:51] 进来好嘞那么我们写这么一段话走来看一下这个里面的分词的一个效果你看传输播客是一个词那么学习挺好的欢迎欢迎来然后黑马程序员是不是也是一个词汇那么黑马也是一个词汇程序员也是个词汇OK那么黑马程序员等等分了这么多词那么我们还可以再写什么呢比如说这个我在抖音抖音抖
[04:22] 抖音上发了一个最新的视频叫叫什么的蓝瘦香菇对吧蓝瘦香菇蓝瘦香菇好那么来看一下走那么你看我在抖音是不是一个词汇了对吧然后呢发了一个最新的一个视频叫做蓝瘦香菇是不是也是一个词汇了香菇也是一个词汇了OK好那么这个呢就是我们
[04:52] 可以去任意的去扩展它的一个词汇当然了在这个插件官方他提供了另外一种方式我觉得这种方式也是非常好的就是我们可以去热更新IK分词的这样的一个方法什么叫热更新呢其实我们刚刚这种更新的属于冷更新什么意思呢就是我们需要去修改那个文件修改文件之后我们需要重启我们的服务那么什么叫热更新呢就是我们更新之后不需要做重启
[05:20] 那么他是怎么做到的呢他是在这个位置去指定一个地址这个地址是一个URL的地址那么他有一个这个建议的就是我们把我们所需要的这个文件放到我们的一个NJX下面的一个NJX下面然后通过NJX去做访问我们这个文件那么就可以去做一个比如说这个文件一旦他发生了一个变更那么他的这个lastlast这个multifiled
[05:49] 然后以及它的eTag那么就会做一个修改就是说这个是它的最后的修改的一个时间和eTag的就会有一个变更那么检测到这两个内容的变更那么就会去自动重新加载这个文件到它的内部做一个重新reload这样的一个操作所以这个就叫一个热分词或者说热更新ok这种方式也是一个非常棒的一种方式ok那么大家可以自己去尝试一下
[06:15] 那么刚刚我们是通过这种叫冷更新这种方式去做一个这样的一个扩充好那么关于IK的一个自定义词汇我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
-rw-r--r-- 1 root root 54993 Dec 23 11:26 Elasticsearch-analysis-ik-6.5.4.jar
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
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] parsed [0] roles from file /usr/share/Elasticsearch/config/roles.yml
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] loaded plugin [ingest-geop]
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] parsed [0] roles from file /usr/share/Elasticsearch/config/roles.yml
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] loaded plugin [ingest-user-agent]
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] parsed [0] roles from file /usr/share/Elasticsearch/config/roles.yml
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] loaded plugin [ingest-geop]
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] parsed [0] roles from file /usr/share/Elasticsearch/config/roles.yml
[2019-01-12T12:58:56,545][INFO ][o.e.x.s.a.CppLogMessageHandler] [VsaZSG] loaded plugin [ingest-user-agent]
[2019-01-12T12:58:5

