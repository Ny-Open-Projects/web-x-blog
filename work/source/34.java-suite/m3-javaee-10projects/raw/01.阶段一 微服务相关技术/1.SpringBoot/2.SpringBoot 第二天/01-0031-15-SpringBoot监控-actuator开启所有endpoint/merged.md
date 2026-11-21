# 15-SpringBoot监控-actuator开启所有endpoint

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\15-SpringBoot监控-actuator开启所有endpoint_【海量资源尽在 ubkz.com】.mp4
- 时长 6分12秒（音频 372s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 介绍完Spring提供的这个监控功能的基本使用那么接下来我们来说一下它所有的完整的使用那么基本就提供了健康和info两个信息那么其他的你需要去开启一个配置才能够生效所以接下来我们来配置一下打开IDR在这里边我们就去将所有的监控URL我们这个地方不叫URL我们叫endpoint
[00:31] 给它暴露暴露出来那么暴露这个单词呢叫做exposing啊expose好那么外部端的一个expose的include啊and points就是你and points你可以把它理解为一个and points呢就是一个URL可以来访问的然后呢它include默认只暴露了hertz健康的和info的信息对吧你要暴露所有的呢怎么办呢你把这个配置改为新就可以了暴露所有的嘛OK啊
[00:57] 那么暴露完所有之后接下来我们就可以来重新启动一下我们当前的这个应用了重新启动之后呢我们再来访问这个路径跟的这个路径那你看现在是不是很多了很多了之后呢我们把它粘过来Ctrl V好你看现在是不是有一大堆的信息了那么这么一大堆的信息呢我们同样的呢可以来看一下一些比较常用的比如说第一个这个BeansBeans呢就可以看到你Spring的IOC容器里边一共有多少个BeansOK点一下
[01:29] 我的天这么多是吧Ctrl A Ctrl C好我们在这个格式化器里边来看一下很多个bin啊每一个bin呢比如说随便找一个bin然后呢我们在这个里边你看啊bin对吧然后呢它的scope是singletongue的type类型是什么什么的我们找一个我们看得懂的Ctrl F搜一下比如说我们刚才有redis它一定有一个redis的templateredistemplate这个bin
[01:59] 因为我们导了这个坐标的对吧好搜一下Redis Template搜一下不是这个好往下找这个地方马上就到你看这个地方是不是Redis Template这个bin的名称对吧然后呢它的scope是单立的single term的类型呢就是这个Redis Template的这个类型然后resource它说从哪个里边来的呢从Redis的autoconfigured class里边来的对吧它依赖谁呢依赖Redis Connection Factory你看
[02:28] 整个的bin的描述是非常详细的对吧OK啊然后呢还有一些其他的一些信息啊都是有的哈所以呢这个地方呢redis的template我们看了一下其他的bin的信息呢也都是类似哈你想看这个bin的情况都是可以看的这是第一个bin那么除了bin之外呢还有我们往下看啊比较常用的健康的就不看了然后接下来envenv呢表示了我们的配置的环境的就是配置文件里边那些属性的信息啊我们可以点一看一下
[02:59] 有很多因为除了我们自己配置的别人项目模块里边还有很多自动的一些配置信息好control v粘过来粘过来之后呢就有很多很多我们把它你看这个地方对吧你看上边的都是人家定义的一些信息这些信息我们就不看了然后我们拉到最下边下边你看这个定义很熟悉吧info.name从哪的呢application.configure从哪个文件呢application.properties里边配置的
[03:28] Properties有啥呢键叫info.name张三我们是不是自己写的呀对吧age23包括我们显示完整的健康信息以及开启所有的这个endpoints新是不是都可以看到是env对吧那么除了这个之外呢还有一些比如说可以来看一下这个堆栈信息当然这个玩意你一点就会下载下载一个堆栈的信息的一个文件你需要通过专业的工具来分析这个我们就先暂时不看了
[03:57] 然后呢在这个地方呢还有一些比如说mappings这个mappings呢也可以看一下mappings呢表示了我们当前所有的URL的路径我们可以看一下好ctrl a ctrl cctrl a ctrl vok这些路径呢当然这些路径呢就是访问暴露的一些路径当然我们可以这样我们在这里边呢可以来写一个对应的Controller我们就直接写一个user Controller好
[04:26] user Controller我们在这里边快速写一下rest Controller然后我们给它加一个request mapping叫做-user吧然后在里边提供一个方法public返回一个字幕串叫做find allfind allfind all完事了之后我们直接给它返回一个socc ess success然后在这个地方我们就用request mapping
[04:54] 给它标注一下这个路径叫做Find All就完事了完事了之后重新启动一下启动完事之后呢我们直接来访问刚才我们看到的这个地方的这个路径这个路径呢我们看一下叫做Mappings好刷一下刷完了之后Ctrl A Ctrl C然后呢把它重新格式化一下看一下它有没有对应的我们刚才找的那个写的那个user的Find Alluser-Find All有吧对吧这是我的路径吧
[05:25] 然后这个路径呢从哪来呢user Controller的翻调方法啊是吧然后呢这个地方呢这个Controller然后这个参数哎这个不是参数啊这是返回值的信息描述的信息然后呢有没有参数啊对吧没有是吧没有参数所以呢这些信息呢都可以描述出来这个接口将来我们Controller是来定义接口这个接口的一些详细的调用的信息都可以所以呢这个地方呢是这个叫做一个mappings的一个信息OK
[05:53] 那么接下来往下看还有什么可以看的吗还有其他的呢我们待会儿就再来说那你会发现这么多信息供我们去选择去使用OK吧那么这就是我们所说的这个actuator这么一个监控的基本的使用了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Spring Boot Actuator 的健康检查和端点暴露配置，以及如何通过 HTTP 请求访问这些端点并查看其返回的 JSON 结构。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了访问 http://localhost:8080/actuator 返回的 JSON 数据，其中包含多个端点的链接，如 health、info、beans 等。
画面 2: 在 IDEA 中编辑 application.properties 文件，配置了健康检查的详细程度和暴露的端点。
画面 3: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "links" 部分。
画面 4: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "components" 部分。
画面 5: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "dependencies" 部分。
画面 6: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "beans" 部分。
画面 7: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "redisTemplate" 部分。
画面 8: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "conditions" 部分。
画面 9: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "info" 部分。
画面 10: 在 IDEA 中右键点击项目，选择“Build Module 'Spring Boot-actuator'”进行构建。
画面 11: 在 IDEA 中查看 UserController.java 文件，其中包含一个 @RestController 和 @RequestMapping("/user") 注解。
画面 12: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "mappings" 部分。
画面 13: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "requestMappingConditions" 部分。
画面 14: 在浏览器中访问 http://localhost:8080/actuator 返回的 JSON 数据，其中包含多个端点的链接，如 health、info、beans 等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 2:
```
info.name=shangsan
info.age=23
# 开启健康检查的详细信息
management.endpoint.health.show-details=ALWAYS
# 将所有监控端点暴露在默认路径下
management.endpoints.web.exposure.include=*
```

画面 9:
```
{
  "name": "applicationConfig",
  "properties": {
    "value": "shangsan",
    "origin": "class path resource (application.properties)"
  },
  "info.age": "23",
  "origin": "class path resource (application.properties)"
}
```

画面 11:
```
package com.ethan.springboottactuator;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/user")
public class UserController {
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。

