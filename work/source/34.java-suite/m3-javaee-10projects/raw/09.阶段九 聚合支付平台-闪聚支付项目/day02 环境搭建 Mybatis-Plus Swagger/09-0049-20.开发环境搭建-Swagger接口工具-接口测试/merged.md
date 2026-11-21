# 20.开发环境搭建-Swagger接口工具-接口测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\20.开发环境搭建-Swagger接口工具-接口测试【海量资源尽在 666java.com】.mp4
- 时长 4分17秒（音频 257s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下边呢我们来看一下Swagger接口的测试在生成的Swagger文档上边呢它很清楚的描述了我们微服务给前端所提供的各种什么接口但是那有人说老师那这个前端会怎么用呢咱们先说就是你生成完这个接口对于服务端开发人员怎么用
[00:24] 前端其实你不要管人家人家主要看这个接口的描述对不对那你作为服务端那这个文档对服务端人员就没有用吗你要注意前后端分离开发这个文档就是规范就是约束大家都依据这个文档对于服务端人员这个文档除了你看看它的接口描述之外其实还有一个非常重要的功能啥功能啊你想呀
[00:48] 你写完这个接口了我就问你个问题刚才我们在浏览器去执行测试对不对那我目的是啥我的目的是不是就是为了测试我刚才是不是执行这么一个测试我目的是不是为了测试这个接口对不对但你测试这个接口我是不是手动在这输URL对Swagger可以它也提供了一种测试的方法因为它本身就是来使显示这个所有的这个接口文档
[01:17] 它就实现了一个测试啥测试啊你看嘛Hello比如说拿Hello这个接口来说你看这里边是不是有一个叫Try it out是吧点一下你看好它就说了那你是不是开始执行啊测试一下点各位出来了Response body显示响应了一个Hello我说这啥意思啊你注意
[01:42] 我们如果测试的话你是不是手动在URL当中输入URL来回测测试你看是不是一个Hello包括我们测试这个对不对那其实Sweiger文档呢它也给你提供了这些接口的测试并且呢它可远比你要自己在URL当中输入URL来怎么样来输入测试这些数据要方便的多也就是Sweiger UI
[02:08] 它呢可以让你在这个界面上面try it out然后呢去测试你比如说我再给你测一个你比如说这个商户你看见吗这个商户各位我们点你看它就会说了来输入ID吧输入1点按走各位看它给你测试出来了有意思吧这个响应的数据那你是不是通过Swagger这个测试就可以清楚的知道这些接口我开发有没有问题所以对于服务端人员
[02:38] 你不用依赖于前端你就自己可以测这个接口而对于前端人员他拿到你的这个Swagger文档他会怎么做呀对他会去看你这个接口的这个描述然后呢他会进行什么他的前端程序的编写大家理解我意思吧对这个文档前端人员看呢他主要是看嘛看你的接口描述那服务端人员呢除了看接口描述以外他可以进行什么他自己接口的测试对你比如说再来测一个比如说这个hi
[03:07] 对吧这个hi这个接口刚才是老师从讲义上直接考过来的大家可以看这个hi这个接口是不是要传入一个内幕值并且它是post的其实这里你就发现有问题了如果是post的测试你在URL里边去输入URL回测这是盖的请求你post的测试是不是比较难测但是Swagger它就可以帮你测你看Swagger测它咋测你找到hi这个接口然后点击你看是不是有一个内幕参数那你比如说这里边我们输入张三
[03:36] 然后呢我们点击走各位你看嗨张三这是响应的书记大家理解吗对我们通过Swagger接口Swagger文档就可以来进行什么整个接口的测试这就是我们说的什么哎你生成完接口文档它的用法前端人员看着接口文档哎然后呢看看你的接口描述进行前端程序的编写副端人员看着接口呢除了看接口文档描述
[04:08] 还要干嘛还要可以进行测试对不对OK那么对于SWAG的这个接口测试我就演示到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Swagger UI 测试闪聚支付商户平台的 API 接口，包括 GET /hello 和 POST /h1 接口的参数、响应及实际调用效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Swagger UI 主页，包含 GET /hello、POST /h1、GET /merchants/{id} 三个接口。
画面 2: 展示 POST /h1 接口的参数详情，其中 name 为必填字符串参数，响应码 200。
画面 3: 浏览器地址栏为空，页面空白。
画面 4: 展示 GET /hello 接口的参数详情，无参数，响应码 200。
画面 5: 展示 GET /hello 接口的 Curl 命令：curl -X GET "http://localhost:57010/merchant/hello" -H "accept: */*"。
画面 6: 浏览器地址栏显示 localhost:57010/merchant/hello，页面返回 "hello"。
画面 7: 展示 POST /h1 接口的响应详情，响应体为 JSON 格式，包含 merchantName、merchantNo 等字段。
画面 8: 展示 GET /hello 接口的响应详情，响应体为 "hello"，响应头包含 content-length、content-type、date。
画面 9: 展示 Swagger UI 主页，包含 GET /hello、POST /h1、GET /merchants/{id} 三个接口。
画面 10: 展示 POST /h1 接口的参数详情，其中 name 为必填字符串参数，响应码 200。
画面 11: 浏览器地址栏显示 localhost:57010/merchant/hello，页面返回 "hello"。
画面 12: 展示 POST /h1 接口的 Curl 命令：curl -X POST "http://localhost:57010/merchant/h1?name=张三" -H "accept: */*"。
画面 13: 展示 GET /hello 接口的参数详情，无参数，响应码 200。
画面 14: 展示 Swagger UI 主页，包含 GET /hello、POST /h1、GET /merchants/{id} 三个接口，下方有文字说明“点击其中任一项即可打开接口详情，如下图所示：”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
curl -X GET "http://localhost:57010/merchant/hello" -H "accept: */*"

画面 7:
{
  "id": 1,
  "merchantName": "测试商户",
  "merchantNo": null,
  "merchantAddress": null,
  "merchantType": null,
  "idCardNo": null,
  "idCardAftering": null,
  "password": null,
  "merchantName": null,
  "contactsAddress": null,
  "merchantStatus": null,
  "merchantId": null
}

画面 8:
hello

画面 12:
curl -X POST "http://localhost:57010/merchant/h1?name=张三" -H "accept: */*"

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14:
标题：2.1.4 Swagger测试
内容：
1. 启动商户应用和商户中心服务，访问：http://localhost:57010/merchant/Swagger-ui.html
2. 点击其中任一项即可打开接口详情，如下图所示：

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

