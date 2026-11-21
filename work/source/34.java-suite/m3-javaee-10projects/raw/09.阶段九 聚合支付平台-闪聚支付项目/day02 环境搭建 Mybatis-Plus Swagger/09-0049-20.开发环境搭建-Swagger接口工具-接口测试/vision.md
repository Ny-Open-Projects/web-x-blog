# 画面线理解：20.开发环境搭建-Swagger接口工具-接口测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\20.开发环境搭建-Swagger接口工具-接口测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:42, 00:59, 01:20, 01:33, 01:59, 02:15, 02:31, 02:44, 03:07, 03:21, 03:39, 04:01, 04:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:47:28

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
1. 启动商户应用和商户中心服务，访问：http://localhost:57010/merchant/swagger-ui.html
2. 点击其中任一项即可打开接口详情，如下图所示：

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
