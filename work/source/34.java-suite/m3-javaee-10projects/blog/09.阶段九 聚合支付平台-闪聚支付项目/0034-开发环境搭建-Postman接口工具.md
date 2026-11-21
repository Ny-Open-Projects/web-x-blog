# Postman 接口测试实战：把每个请求沉淀进集合，服务端自测的主战场

Swagger 文档页能发请求之后，另一个现实问题跟着来了：测试记录留不下来。页面上点一次 Execute 就是一次性的，第二天回归还得重新填一遍参数；遇到要加请求头的接口、要传 JSON 体的接口，页面表单也越来越不够用。服务端开发者需要一把趁手的测试工具：请求能保存、能分组、能反复重放。Postman 就是这把工具，这一课把它装起来，为商户平台应用建集合、发请求、存用例，并把它与 Swagger 的分工划清楚。

## 先给结论

- Postman 是专门的 HTTP 接口测试工具，与 Swagger 的测试能力互补：Swagger 页面用来看文档、随手快测，Postman 负责系统性的自测与回归；服务端开发完接口用 Postman 过一遍，是行业里通行的习惯。
- 测试范围要分清：两者测的都是 application 应用工程暴露的 RESTful 接口；微服务之间的 Dubbo 接口不走 HTTP，用单元测试覆盖即可。
- 使用主线四步：安装 Postman，新建 Collection 集合（建议一个微服务对应一个集合，本课为商户平台应用单建「闪聚支付-商户应用」），在集合里新建 Request 录入 URL 与请求方式，点 Send 发送。
- 每个请求用 Ctrl+S 保存进集合，Postman 关掉再开记录还在；浏览器地址栏测完关窗即失，这是集合化最直接的价值。
- Postman 的请求体支持表单键值对、JSON、XML 等文本格式以及二进制文件上传，请求头可自由添加，后续做认证授权要带 token 的场景全都能接住。

## 服务端为什么还需要 Postman

接口写完不等前端来调，服务端自己先测，这个原则在 Swagger 那一课已经立住了。Postman 承担的是同一件事的另一半：Swagger 的强项是「文档」，接口长什么样、参数怎么填，页面一站看全；它的弱项是「记录」，Try it out 的每次执行都是过眼云烟，没有地方沉淀。而接口测试恰恰是个重复劳动：一个接口今天测一遍，明天改了参数再测一遍，下周联调出问题还要重放。没有保存机制的测试工具，重复成本会随着接口数量线性上涨。

Postman 的解法是把「测试」本身对象化。每一个测试请求可以保存成一个用例，用例归属一个集合，集合按微服务组织。于是测试历史从「浏览器窗口的临时状态」变成「可版本化、可传递的资产」，同事接手时把集合发过去，接口怎么调一目了然。

## 集合与请求：把测试沉淀下来

Postman 安装包从官网获取，按向导一步步装完即可，无需额外配置。装完后的使用主线是一套固定动作，画出来很清楚：

```mermaid
flowchart LR
    A["New 新建 Collection"] --> B["命名集合<br/>闪聚支付-商户应用"]
    B --> C["New 新建 Request"]
    C --> D["录入 URL 与请求方式"]
    D --> E["Send 发送请求"]
    E --> F["Ctrl+S 保存进集合"]
    F --> G["重启 Postman 记录仍在<br/>下次回归直接重放"]
```

关键路径在集合的划分上：一个微服务对应一个集合，商户平台应用的接口都放进「闪聚支付-商户应用」这一个集合里。粒度再细，集合数量膨胀，找接口反而费劲；粒度再粗，多个服务的接口混在一起，回归时容易漏测。按服务分恰好与项目结构对齐。随着课程推进，商户注册、渠道参数查询等后续模块的请求也会陆续进到这个集合里，集合会越长越大，这正是它该有的样子。

保存还有一层含义值得强调：集合里存的是完整请求，URL、请求方式、参数、请求头一体保存。回归测试时点开条目直接 Send，参数不需要重填。对比浏览器地址栏的方式，差距就在这里，地址栏只支持 GET，关窗即失，什么也留不下。

## 发第一个请求：查商户与带参提交

测试对象还是商户平台应用那三个接口，Controller 的真实代码在工程里长这样：

```java
package com.study.pay.merchant.controller;

@RestController
@Api(value = "商户平台应用接口", tags = "商户平台应用接口")
public class MerchantController {

    @org.apache.dubbo.config.annotation.Reference
    MerchantService merchantService;

    @ApiOperation(value = "根据id查询商户信息")
    @GetMapping("/merchants/{id}")
    public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
        MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
        return merchantDTO;
    }

    @ApiOperation("测试")
    @ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "string")
    @PostMapping(value = "/hi")
    public String hi(String name) {
        return "hi," + name;
    }
}
```

新建 Request 命名为「根据商户 ID 查询商户」，请求方式选 GET，URL 录入商户平台应用的地址，注意别漏掉主配置覆盖的 context-path：

```bash
# GET 请求：根据 id 查询商户，57010 是商户平台应用端口，/merchant 是 context-path
curl -X GET "http://localhost:57010/merchant/merchants/1"
```

Send 之后响应区回显商户表那条测试数据，商户名称、审核状态等字段与数据库记录一致，说明链路通了。换成带参数的 POST 请求更能看出 Postman 的方便：新建 Request 命名为「hi 接口测试」，方式改 POST，URL 换成 `/hi`，在 Body 页签选 `x-www-form-urlencoded`，键填 `name`、值填「张三」，Send 后返回 `hi,张三`。等价的命令行写法是把参数拼进查询串：

```bash
# POST 请求：表单参数 name 提交
curl -X POST "http://localhost:57010/merchant/hi?name=张三"
```

Body 页签值得展开看一眼，Postman 支持的类型远比表单丰富：`form-data` 可混合键值对与文件上传；`x-www-form-urlencoded` 是标准表单编码；`raw` 里能选 JSON、XML、HTML 等任意文本格式，前端调 JSON 接口时的报文就用它构造；`binary` 支持二进制文件直传。Headers 页签则可以给请求加任意请求头。这两处平时不动，等到做认证授权、文件上传时就是刚需。

## Postman 与 Swagger 的分工

两个工具并存的局面会贯穿整个项目，分工不划清就会来回摇摆。判定标准只有一条：看使用者的身份与目的。

| 维度 | Swagger 页面 | Postman |
| --- | --- | --- |
| 使用者 | 前后端双方 | 服务端为主 |
| 核心价值 | 接口规范与文档，随代码自动生成 | 用例沉淀与重放，集合化管理 |
| 保存能力 | 无，每次现填 | Ctrl+S 入集合，重启仍在 |
| 参数能力 | 表单化，注解决定 | 表单、JSON、文件、请求头全支持 |
| 典型场景 | 联调时前端查接口约定 | 接口写完自测、改完回归 |

Swagger 生成的文档还能导出成 JSON 等格式交给前端作为开发依据，这条「文档流转」的通道是 Postman 不具备的；反过来，Postman 里保存的用例集合是 Swagger 页面给不了的。两者是协作链上的前后两环，不是竞争关系。日常节奏可以固定下来：后端写完接口补好注解，重启服务把文档链接发给前端；自己则用 Postman 把接口测一遍，用例存进集合，之后每次改动都重放集合做回归。

## 常见误区

- **所有请求都临时手敲，不存集合。** 错例：每次测试现拼 URL，联调三天后谁也想不起上周参数怎么填的。正解：每个请求 Ctrl+S 存进对应微服务的集合，命名写清业务含义，回归时直接重放。
- **集合不分微服务，一个集合塞所有接口。** 错例：商户、交易、验证码的接口全堆在一个集合里。正解：按一个微服务一个集合的口径建，与项目结构对齐，回归不漏测。
- **用 Postman 去测 Dubbo 接口。** 错例：想验证商户服务的 Dubbo 接口，在 Postman 里按 RPC 方式拼请求。正解：Postman 与 Swagger 都只服务 HTTP 的 RESTful 接口，Dubbo 接口写单元测试验证。
- **URL 漏掉 context-path。** 错例：录入 `http://localhost:57010/merchants/1` 得到 404。正解：主配置把访问路径覆盖成了 `/merchant`，完整地址是 `http://localhost:57010/merchant/merchants/1`。
- **把 POST 请求放浏览器地址栏测。** 错例：地址栏粘贴 POST 接口地址，返回的永远是 GET 语义的响应。正解：POST 及带请求体的请求一律进 Postman 或 Swagger 页面发。

## 面试可能被问到的问题

1. 面试官追问：「Swagger 和 Postman 都能测接口，项目中怎么选？」
   答：两者定位不同。Swagger 的本质是接口文档，测试只是附带能力，适合单接口即时验证与前后端对齐接口约定；Postman 的本质是测试工具，集合、环境变量、请求头、文件上传能力完整，适合服务端自测与回归。项目里的固定分工是看文档用 Swagger 页面，跑用例用 Postman。
2. 面试官追问：「为什么 Postman 的集合要按微服务划分？」
   答：集合是测试用例的组织单位，按微服务划分与项目结构对齐，一个服务的接口集中在一处，回归时按集合遍历即可不重不漏；混放会导致接口归属不清，服务多了以后查找和维护成本都会上升。
3. 面试官追问：「Postman 测不了哪些接口？」
   答：测不了非 HTTP 协议的接口，比如本项目微服务之间的 Dubbo RPC 接口，它们不走 HTTP 报文。这类接口用单元测试直接调 Java 接口验证，Postman 和 Swagger 都只覆盖 application 应用工程暴露的 RESTful 接口。
4. 面试官追问：「Postman 里怎么模拟前端传 JSON 的请求？」
   答：请求方式选 POST，Body 选 raw 并把格式切到 JSON，按接口的参数模型写报文体；同时确认 Headers 里 Content-Type 为 application/json，Postman 选 raw JSON 时会自动带上。之后 Send 的报文与前端实际发出的完全一致，排查参数问题就有一致性保证。
5. 面试官追问：「认证授权上线的接口，Postman 怎么继续测？」
   答：在 Headers 里手工加认证头，如携带 token 的 Authorization 头；或用 Postman 的授权页签配置，请求发出时自动附加。这也是 Postman 相对 Swagger 页面的优势之一：需要登录态的接口在文档页面里很难测，在集合里则可以像正常客户端一样带凭证调用。

## 配套资料

- 讲义：`materials/docs/10/闪聚支付-第1章-讲义-开发环境搭建v1.0.md`，2.2 接口调试利器 Postman（自行安装、新建集合「闪聚支付-商户应用」、集合中新建请求录入信息、Send 发送、Ctrl+S 保存技巧）为本课出处。
- 代码：`materials/code/10/`，聚合支付工程商户平台应用模块的 `MerchantController`（内层目录名含项目原始命名，与正文包名口径不一致，不在此展开），正文 Controller 为真实文件按 `com.study.pay` 口径改写后的节选。
- 说明：该阶段课程资料归档在 `materials/docs/10/` 与 `materials/code/10/`（不存在 09 编号目录，引用路径截至该层级）；curl 命令与响应描述为按课程操作补全的演示说明，Postman 安装步骤以官网向导为准。
