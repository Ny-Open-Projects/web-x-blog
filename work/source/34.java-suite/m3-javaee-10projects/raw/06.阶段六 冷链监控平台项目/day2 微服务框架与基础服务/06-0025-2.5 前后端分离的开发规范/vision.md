# 画面线理解：2.5 前后端分离的开发规范

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.5 前后端分离的开发规范_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 01:25, 03:07, 04:45, 06:30, 07:32, 08:35, 10:48, 13:07, 15:13, 15:48, 16:40, 17:04, 17:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:53:14

1) 这一组画面整体在讲什么（一句话）：
讲解前后端分离开发规范，重点介绍 RESTful API 的设计原则、请求方法、域名、版本、路径、过滤信息、状态码及响应数据格式。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 标题：3. 前后端分离开发规范
- 子标题：3.1 背景
- 内容：阐述前后端分离的背景及问题，即前后端接口对接工作量大，导致前端开发人员需关注后端接口。
- 图表：展示“前端浏览器”向“应用服务器”请求动态页面，应用服务器再向“数据库”请求数据的流程。

画面 2：
- 标题：3.1.1 前后端不分
- 内容：说明前后端分离模式下，前端页面看到的效果是由后端控制，后端需提供静态页面和动态数据。
- 图表：展示浏览器获取静态页面（由静态文件服务器返回）、运行JS请求后端数据（由应用服务器返回）、App请求数据（由应用服务器返回）的完整流程。

画面 3：
- 标题：3.2 API接口
- 子标题：3.3.1 概念
- 内容：介绍 RESTful API，定义其为基于 HTTP 协议的 Web API 设计风格，适用于前后端分离应用。

画面 4：
- 标题：3.3.2 域名
- 内容：建议将 API 部署在专用域名下，如 https://api.example.com；若简单，可考虑放在主域名下，如 https://example.org/api/。
- 标题：3.3.3 版本
- 内容：建议将 API 的版本号放入 URL，如 http://www.example.com/app/1.0/foo。

画面 5：
- 标题：3.3.3 版本
- 内容：介绍另一种做法，将版本号放在 HTTP 头信息中，如 Accept: vnd.example.com.foo+json; version=1.0。

画面 6：
- 标题：3.3.4 路径
- 内容：路径又称“端点”，表示 API 的具体网址，每个网址代表一种资源。
- 示例：列出不好的路径命名，如 /getProducts、/listorders、/retrieveClientOrderByOrderId=1。
- 内容：建议使用名词，如 GET /products、POST /products、GET /products/4、PATCH 或 PUT /products/4。

画面 7：
- 标题：3.3.6 过滤信息
- 内容：介绍查询字符串，如 ?limit=10、?offset=10、?page=1&per_page=10、?sortby=name&order=asc。
- 标题：3.3.7 状态码
- 内容：列出常见状态码，如 200（成功）、201（创建）、204（无内容）、400（错误）、401（未授权）、403（禁止）、404（未找到）、500（服务器错误）。

画面 8：
- 标题：3.4 开发规范
- 子标题：3.4.1 规范原则
- 内容：接口返回数据应仅做数据处理，禁止多个接口调用；禁止跨域；禁止业务逻辑处理；禁止返回 HTML 页面；禁止返回 XML 数据；禁止返回 JSON 数据。
- 子标题：3.4.2 基本格式
- 内容：GET、POST 请求等必须包含 key/value 的 body，所有请求数据包装为 JSON 格式，并存放到 body 中。
- 示例：GET 请求 body 为 {“username”: “admin”, “password”: “123456”, “captcha”: “scfd”, “rememberMe”: “1”}。

画面 9：
- 标题：3.4.3 响应实体信息
- 内容：展示响应实体信息的 JSON 格式，如 {“code”: 200, “data”: {“entity”: {“id”: 1, “name”: “XXX”, “code”: “XXX”}}}。

画面 10：
- 标题：3.4.4 响应列表格式
- 内容：展示响应列表格式的 JSON 格式，如 {“code”: 200, “data”: {“list”: [{“id”: 1, “name”: “XXX”, “code”: “XXX”}, {“id”: 2, “name”: “XXX”, “code”: “XXX”}]}。

画面 11：
- 标题：3.4.5 响应分页格式
- 内容：展示响应分页格式的 JSON 格式，如 {“code”: 200, “message”: “success”, “recordCount”: 2, “totalCount”: 2, “pageSize”: 10, “pageNo”: 1, “data”: {“list”: [{“id”: 1, “name”: “XXX”, “code”: “XXX”}, {“id”: 2, “name”: “XXX”, “code”: “XXX”}]}。

画面 12：
- 标题：3.3.2 域名
- 内容：建议将 API 部署在专用域名下，如 https://api.example.com；若简单，可考虑放在主域名下，如 https://example.org/api/。
- 标题：3.3.3 版本
- 内容：建议将 API 的版本号放入 URL，如 http://www.example.com/app/1.0/foo。

画面 13：
- 标题：3.4 开发规范
- 子标题：3.4.2 基本格式
- 内容：GET、POST 请求等必须包含 key/value 的 body，所有请求数据包装为 JSON 格式，并存放到 body 中。
- 示例：GET 请求 body 为 {“username”: “admin”, “password”: “123456”, “captcha”: “scfd”, “rememberMe”: “1”}。
- 图表：展示 POST 请求的界面，包含请求头、请求体、响应头、响应体等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3：
RESTful接口示例如下：
| 请求方法 | 请求地址 | 后端操作 |
| --- | --- | --- |
| GET | /students | 获取所有学生 |
| POST | /students | 增加学生 |
| GET | /students/1 | 获取编号为1的学生 |
| PUT | /students/1 | 修改编号为1的学生 |
| DELETE | /students/1 | 删除编号为1的学生 |

画面 4：
http://www.example.com/app/1.0/foo
http://www.example.com/app/1.1/foo
http://www.example.com/app/2.8/foo

画面 5：
Accept: vnd.example.com.foo+json; version=1.0
Accept: vnd.example.com.foo+json; version=1.1

画面 6：
GET /products : 海选所有产品
POST /products : 将产品新增到集合
GET /products/4 : 获取产品 4
PATCH (或) PUT /products/4 : 修改新产品 4

画面 7：
?limit=10 : 指定返回记录的数量
?offset=10 : 指定返回记录的开始位置
?page=1&per_page=10 : 指定返回记录的页数，以及每页的记录数
?sortby=name&order=asc : 指定返回记录按某个属性排序，以及排序顺序。
?animal_id=1 : 指定查询条件

画面 8：
GET请求：
xxx/login/body={"username":"admin","password":"123456","captcha":"scfd","rememberMe":"1"}

画面 9：
{
  "code": 200,
  "data": {
    "entity": {
      "id": 1,
      "name": "XXX",
      "code": "XXX"
    }
  }
}

画面 10：
{
  "code": 200,
  "data": {
    "list": [
      {
        "id": 1,
        "name": "XXX",
        "code": "XXX"
      },
      {
        "id": 2,
        "name": "XXX",
        "code": "XXX"
      }
    ]
  }
}

画面 11：
{
  "code": 200,
  "message": "success",
  "recordCount": 2,
  "totalCount": 2,
  "pageSize": 10,
  "pageNo": 1,
  "data": {
    "list": [
      {
        "id": 1,
        "name": "XXX",
        "code": "XXX"
      },
      {
        "id": 2,
        "name": "XXX",
        "code": "XXX
