# 21.开发环境搭建-Postman接口工具

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\21.开发环境搭建-Postman接口工具【海量资源尽在 666java.com】.mp4
- 时长 8分14秒（音频 495s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 下面呢我们来看一下另外一个接口测试的工具叫Postman想必有同学应该用过这个Postman因为在前边的课程当中可能有些老师呢给大家提供过这个Postman的接口测试工具啊那么和刚才我们讲的Swagger接口测试一样就是服务端他把接口写出来不用等到前端来测他自己就要来测这个接口的正确性对吧所以除了刚才我们说的Swagger
[00:27] 它文档提供了这么一个接口测试的功能以外其实还有一个神器就是Postman它专门来作为HTTP接口测试工具进行使用它的功能还是非常强大的首先你在本机安装Postman安装的方法这里边我就不再多说你在网上随意一搜就出来了然后一步一步安装完事然后接下来我们安装完了之后你是不是就要打开Postman那现在我想测试我们这里边
[00:57] 的一些接口那怎么测呢你看Postman首先打开完Postman这里面你看最左上角有一个new看见了吗那么现在呢我们要测试我们为啥测试因为我们闪具支付项目开发了很多这个功能接口我要测对不对其实这些接口都是应用层的接口我再强调一下因为我们的工程是application还有什么微服务就是double服务这个application是暴露给前端的接口
[01:27] 所以我们现在讲的SWAG也好POSTMAN也好都是针对application工程所写的Controller接口来测试的因为它暴露的是不是就是RESTful这些接口针对double协议的接口的测试我们将来写单元测试内就完事了就测试就行然后你不用用POSTMANPOSTMAN主要测http的好现在我们找到POSTMAN的窗口然后你看它是不是有一个什么new
[01:57] 这个按钮你点所以我点什么呢我们创建一个clash这个clash是啥呀这个clash呢就是你要测试很多很多的接口那我们可以给它找一个存放这些测试接口的一个位置就是一个集合比如说这里边我们可以说叫做闪看好啊闪聚支付项目接口测试集合
[02:27] 行不行然后这里边呢我们可以随意描述一下啊创建注意这时候是不是就创建完了那个我这里边上面是我之前测试的你看这看这啊看这这是不是就是我刚才创建的一个clack选这里头要放啥有时候老师你这里头要干啥呀因为你要测很多接口嘛那这接口测试一遍可能又测一遍所以这里边我们把这些测试的这些用力啊每次测试的用力啊都放到里头那怎么接下来怎么弄啊
[02:56] 接下来的话你再点new我们要测试的话你是不是就要请求服务端的接口测我们新建一个request对然后这里面我们测一下比如说根据ID查询商户信息行不行我要测这个行不行可以啊那你最终最终你准备把这个测试的这个用力放在哪呢就放在我刚才建的那个集合上你这要选中这集合然后呢保存各位这个就出来了
[03:26] 看吧出来了之后你看注意看啊我把这里边的所有都给你关掉啊看好啊保存我这里头太多了是吧算了啊我这就先不保存了啊上面这是我以前建的你不要管你现在就看什么呢你就看我刚才我刚才第一步是不是就创建了一个集合第二步我是不是又创建了一个request你点第二步创建这个request现在要在这测了怎么测
[03:57] 怎么测刚才你是不是手动在这输啊对你现在呢你把它放到这看见了吗放到这然后send看成功了就是你这输入URL然后点发送这就成功了然后点保存就是把刚才你测试的这些什么这些信息保存一下你说老师保存到哪呢就保存到这了你看这个时候如果你看我把它关掉
[04:25] Postman关掉然后我再次进来你刚才测试的那些信息你就能找到了这是不是就方便你第二次再次进行测试那你浏览器你测一遍你把浏览器窗口关了你还有吗没了对不对但Postman你看他就给你保留着对吧那有时候老是这Postman和刚才你讲的Swagger有啥区别我告诉你它比Swagger的功能强大很多很多来我一说一下Swagger呢虽然也能进行
[04:54] 比如说get post delete等等这些测试但是post们更强大嗯这强大到哪呢你看好啊点首先这个信息是不是可以保存对吧啊其次这是个get请求对吧你是不是完全可以测pose的行我再测一个pose的你看好啊测pose的时候我让你看一下看好pose的这里边我们可以pose一个hi吧行不行hihi里面pose一个内幕对不对好那么再新建一个看好啊
[05:22] 新建一个新建一个什么hi然后呢选择这个clack讯也保存这里边我们要测是不是hi呀hi那前面的东西都不变嘛只有后边的hi这个路径变了嘛来看一下啊注意这是不是就是我们的hi接口hi接口的话各位我们这要改成post了对吧那你说post我们是不是要传参呀
[05:51] 对不对传参数啊那你传参数咋传呀那是个内幕呀对不对value呢张三行不行发送嗯还张三你说老师这个我也没感觉到有多么的强大吧但是你看这儿啊你看他这个body里边他这是啥呀哎他这是虽然他还有这个最基本的这个key value数据他还有什么哎还可以写json还可以写js
[06:22] 还可以写插描还可以干嘛上传文件看见了吗二斤之格是对不对所以说Postman的这个功能是远比Swagger做接口测试的功能要强大对那有时候老师那我们是用Swagger还是用Postman测呀这里我建议你用Postman测那Postman
[06:46] 那如果你觉得他这个现在我们测试你要你要习惯他这个什么他这个测试的流程啊因为我们所有的这个后边很多的这个功能啊他会比较复杂你用Swagger就不太好测你比如说这里边又是要将来我们要测认证授权还要加入什么投信息对不对你看他都支持对吧所以其实用postman测试他的功能呢更强大更有利于我们的这种各种接口的测试
[07:13] 所以我建议用posman那Swagger呢这里边我要再次强调一下Swagger主要是给前后端人员来作为接口规范用的虽然Swagger有这个接口的测试工具你可以用我不反对但是你要明确一点更重要的是Swagger生成了这么一个接口文档这个接口文档将来可以导出成什么json或者插mail然后给前端人员他来去参考你的接口的描述呢去开发他的前端代码
[07:42] 你明白我的意思吧这主要是前五端分离开发用作接口规范来使用而Postman更重要的是作为什么我们服务端人员的接口测试工具好那这个就是Postman接口测试的演示那后边呢我还会经常性的来使用Postman来测试接口到时候呢我们在日常工作当中就会经常的去使用到这儿我们Postman的接口测试
[08:12] 章节就讲完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Postman 工具对 Spring Boot 项目中的商户服务接口进行测试，包括创建集合、添加请求、配置请求体并发送请求。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Swagger UI 界面，其中包含 GET /hello 和 POST /hi 接口，以及 GET /merchants/{id} 接口的参数和响应示例。下方显示了对应的 curl 命令。
画面 2: 展示了 Typora 文档中关于 Postman 的介绍，提示用户自行安装 Postman，并说明其用于 HTTP 接口功能测试。画面中显示了 Postman 的“新建”菜单，鼠标悬停在“Collection”上。
画面 3: 展示了 Typora 文档中关于 Postman 的介绍，提示用户自行安装 Postman，并说明其用于 HTTP 接口功能测试。画面中显示了 Postman 的“新建”菜单，鼠标悬停在“Collection”上。
画面 4: 展示了 IntelliJ IDEA 中的项目结构，选中了“shanjugay-merchant-application”模块。右侧编辑器中显示了 MerchantController.java 的代码，包含两个 @ApiOperation 注解的接口：一个用于根据 ID 查询商户，另一个用于测试。
画面 5: 展示了 Postman 中的“商户注册”请求，URL 为 http://localhost:57010/merchant/merchants/register。请求类型为 POST，授权方式为“继承自父级”。
画面 6: 展示了 Postman 中的“根据商户支付渠道编码获取渠道支付渠道”请求，URL 为 http://localhost:57010/merchant/my-pay-channels/platform/channel/platform/ChannelC...。请求类型为 GET，授权方式为“继承自父级”。
画面 7: 展示了 Postman 中的“根据商户 ID 查询商户”请求，URL 为 http://localhost:57010/merchant/merchants/1。请求类型为 GET，授权方式为“继承自父级”。请求体（Body）中以 JSON 格式输入了商户信息。
画面 8: 展示了 Postman 的启动加载界面，显示“Opening control valves to antimatter nacelles...”。
画面 9: 展示了 Postman 的更新提示，显示“6.7.4 (Latest)”版本，包含改进和修复的 Bug。
画面 10: 展示了 Postman 的“新建”窗口，提供了“Request”、“Collection”、“Environment”、“API Documentation”、“Mock Server”和“Monitor”等选项。
画面 11: 展示了浏览器访问 http://localhost:57010/merchant/hello 的结果，页面上显示了“hello”。
画面 12: 展示了 Postman 中的“POST”请求，URL 为 http://localhost:57010/merchant/h。请求体（Body）中输入了“hi,张三”。
画面 13: 展示了 Postman 中的“POST”请求，URL 为 http://localhost:57010/merchant/h。请求体（Body）中输入了“hi,张三”。
画面 14: 展示了 Typora 文档中关于在 Postman 集合中新增请求并录入请求信息的说明。画面中显示了 Postman 的“新建请求”对话框。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4 中的代码：
```java
@ApiOperation(value = "根据id查询商户")
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
    return merchantService.queryMerchantById(id);
}

@ApiOperation("测试")
@GetMapping(path = "/hello")
public String hello() {
    return "hello";
}

@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@PutMapping("/merchant")
@ApiOperation("测试")
@Put

