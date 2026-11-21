---
title: "Postman 上手：集合管请求，接口测试一次搭建反复使用"
date: 2026-11-18
categories: [Java后端进阶全套, M3 十大中级项目, 阶段十 万信金融项目]
tags: [Java, 项目实战]
---

# Postman 上手：集合管请求，接口测试一次搭建反复使用

> 🔒 安全提示：文中示例的口令/密钥均为课程教学环境演示口径，生产环境的安全要求见《安全与合规须知》。

Swagger 页面自带调试，点两下就能验证接口通不通，但它的输入形态受限于文档注解，遇到要带请求头、传 JSON 请求体的场景就不够用了。Postman 补的正是这块：一款功能强大的 HTTP 接口测试工具，浏览器能发的请求它都能发，而且能把发过的请求存下来反复用。把它的两个核心概念和基本操作走一遍，后续每个功能开发完，都能用它立刻做功能测试。

## 先给结论

- Postman 定位是 HTTP 接口测试工具：选请求方式、填地址、带参数、Send、看响应，原本浏览器干的活它都能干，构造能力更强。
- 两个核心概念：集合 Collection 对应一个微服务工程，请求 Request 对应 Controller 里的一个方法。
- 测试节奏固定：本机安装并注册登录，建集合，集合里建请求，Send 发送。
- 请求头放 Headers 区；JSON 请求体走 Body 的 raw 选项并选 JSON 类型，配后端 `@RequestBody` 接收。
- 每个测试都要 Ctrl+S 保存，不保存的请求关掉 Postman 就没了。

## 两个概念：集合与请求

Postman 这个单词本意是邮递员，在编程语境里它是一款 HTTP 接口测试工具。业务功能开发完总要测试，以前的动作是打开浏览器、往 Controller 发请求、传数据、收响应；有了 Swagger 之后可以在文档页面发；Postman 是第三条路，也是构造自由度最高的一条。

界面里最重要的组织结构是两层。上层叫集合，Collection，界面上并列的那些条目就是；点开一个集合，里面是一条条已发过的请求。选中某条请求，主工作区从上到下依次是请求方式选择、请求地址栏、参数区、响应区。两层结构的组织建议很简单：一个微服务工程对应一个集合，集合里的一个请求对应 Controller 里的一个方法。用户中心测得多了，它的集合里就攒下一组可复用的测试用例。

```mermaid
flowchart LR
    A["用户中心微服务工程"] -->|"一个工程 对应一个集合"| B["集合 consumer-service"]
    B -->|"一个请求 对应一个方法"| C["测试hello<br/>GET /consumer/hello"]
    B --> D["测试hi<br/>POST /consumer/hi"]
    B --> E["更多接口的请求…"]
```

照这个规则建集合与请求，测试资产和工程结构一一对应，谁都能看懂哪条请求测的是哪个接口。

## 测试用户中心的两个接口

安装与注册登录按官方流程自行完成，进入主界面后开始建测试。目标是被测的 `ConsumerController` 里的两个方法：

```java
package com.study.finance.consumer.controller;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@Api(value = "用户服务的Controller", tags = "Consumer", description = "用户服务API")
public class ConsumerController {

    @ApiOperation("测试hello")
    @GetMapping(path = "/hello")
    public String hello() {
        return "hello";
    }

    @ApiOperation("测试hi")
    @ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
    @PostMapping(path = "/hi")
    public String hi(String name) {
        return "hi," + name;
    }
}
```

**第一，建集合。** 点 New，选 Collection，起名 `consumer-service`，集合列表里出现一个空集合。

**第二，建第一个请求。** 再点 New，选 Request，起名「测试hello」，保存位置选刚建的集合。请求方式对照代码选 GET，地址栏填 `http://localhost:53050/consumer/hello`，端口 53050 是用户中心服务端口，`/consumer` 是 context-path，`/hello` 是接口路径。这个接口没有参数，参数区留空，点 Send 发送。此时服务还没启动，请求发不出去，先把注册中心启动，再启动用户中心，都就绪后回到 Postman 再点 Send，响应区返回 `hello`。

**第三，测带参接口。** 同样在集合里再建一个请求「测试hi」，请求方式对照代码选 POST，地址改成 `http://localhost:53050/consumer/hi`。这个方法带一个 String 参数，在 Params 区按 key、value 成对填，key 写参数名 name，value 随便给一个，比如张三，Send 后响应区返回 `hi,张三`。两个参数就填两行，以此类推。两条请求与 curl 的对应写法如下（示例为按本课演示补全）：

```bash
# 测试hello：GET 无参数
curl -X GET "http://localhost:53050/consumer/hello"
# 期望响应：hello

# 测试hi：POST 带 name 参数
curl -X POST "http://localhost:53050/consumer/hi?name=张三"
# 期望响应：hi,张三
```

启动顺序有讲究：注册中心是服务发现的前提，先起注册中心再起用户中心，只测用户中心接口时启动这两个就够。

## 请求头与 JSON 请求体

实际开发里传参数不止查询串一种。要放请求头信息，切到 Headers 区，按 key、value 填键值对，常见的如内容类型、令牌（示例占位：`Authorization: Bearer example-token-123456`）。要传 JSON 请求体，对应后端用 `@RequestBody` 接收 JSON 数据的场景：点 Body，选 raw，类型选 JSON，然后在文本区自己构造一份 JSON，点 Send 即可：

```json
{
  "mobile": "13800000000",
  "password": "example-pass-123456"
}
```

请求头与请求体这两处是 Postman 比 Swagger 页面更能打的场景，后面课程碰到 `@RequestBody` 接收 JSON 的接口时，测试都会在这里完成。

## 保存：测试是资产，不是一次性消耗品

请求编辑过后条目上会出现小红点，意思是改动未保存。按 Ctrl+S 保存，小红点消失。未保存意味着什么？Postman 关闭再打开，这次测试就不存在了，地址、参数全部要重敲。所以养成一个习惯：觉得有用的测试都随手 Ctrl+S 存下来。存下的请求在左侧集合里常驻，下次打开 Postman 点开就能接着测，改改参数值即可复用，时间越攒越值钱。

与 Swagger 的分工也就清楚了：Swagger 页面跟着文档走，适合快速验证联通性与契约；Postman 负责构造复杂场景、沉淀用例。后续每个功能开发完，两个工具轮着用，各测各的强项。

## 常见误区

- **服务没起就点 Send。** 错例：Postman 里直接发请求，连接被拒。正解：先启动注册中心，再启动用户中心，服务就绪后再发送；注册中心是服务发现的前提。
- **测完不保存。** 错例：参数调通就关掉 Postman，下次重敲一遍。正解：每个有用请求 Ctrl+S 保存进集合，小红点消失才算存上。
- **请求方式与代码不一致。** 错例：接口是 `@PostMapping`，Postman 里选了 GET。正解：建请求前先对照 Controller 的映射注解，GET 配 GET、POST 配 POST。
- **JSON 体用表单方式传。** 错例：JSON 数据填在 form 表单区，后端 `@RequestBody` 解析失败。正解：Body 选 raw 并选 JSON 类型，同时 Headers 里的内容类型与之匹配。

## 面试可能被问到的问题

1. 面试官追问：「Postman 和 Swagger 都能发请求，区别是什么？」
   答：Swagger 跟文档绑定，适合快速验证接口联通与契约，输入形态受注解描述限制；Postman 是独立的 HTTP 测试工具，能自由设置请求头、请求体，支持 JSON、表单等形式，还能把请求保存成集合反复使用，负责更复杂的场景构造与用例沉淀。
2. 面试官追问：「集合和请求在你们的实践中怎么组织？」
   答：一个微服务工程对应一个集合，比如用户中心对应 consumer-service 集合；集合里一个请求对应 Controller 里的一个方法，命名与接口对应。这样测试资产与工程结构一一映射，团队里谁都能找到要复测的用例。
3. 面试官追问：「Postman 里怎么给接口传 JSON 请求体？」
   答：Body 选 raw，类型选 JSON，在文本区写好 JSON 后发送；后端对应方法用 `@RequestBody` 接收。不能把 JSON 填在表单区，否则后端解析不到。
4. 面试官追问：「请求头参数在哪设置，什么场景会用到？」
   答：在 Headers 区按 key、value 设置。传内容类型、携带令牌做鉴权、传自定义追踪标识这些场景都要动请求头，Swagger 页面对这类场景支持有限，Postman 里是常规操作。
5. 面试官追问：「为什么强调每个请求都要保存？」
   答：未保存的请求在 Postman 关闭后就丢失，重新构造要花时间；保存进集合的请求是可复用的测试用例，下次打开直接改参数值重发。测试随开发持续积累，覆盖面才会越滚越大。

## 配套资料

- 代码：`materials/code/10/wanxinp2p/wanxinp2p/`，`wanxinp2p-consumer-service` 模块 `controller` 包下的 `ConsumerController.java` 与 `resources/application.properties` 为真实文件，被测接口与端口、context-path 均出自其中；内层目录沿用原始命名，与正文 `com.study.finance` 改写口径不一致，引用路径到工程目录为止。
- 讲义：`materials/docs/10/万信金融-第1章-讲义-开发环境搭建v1.0.md`，其中 2.2 节接口调试利器 Postman（安装注册、集合与请求、GET 与 POST 参数设置、Ctrl+S 保存技巧）为本课出处。
- 说明：Postman 无配套源码包，文中 curl 与 JSON 请求示例为按本课演示操作补全；示例中的令牌与密码均为 `example-*` 占位。
