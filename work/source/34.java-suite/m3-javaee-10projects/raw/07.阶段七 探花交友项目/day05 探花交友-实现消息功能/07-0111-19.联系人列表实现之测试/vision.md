# 画面线理解：19.联系人列表实现之测试

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\19.联系人列表实现之测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:21, 00:36, 00:49, 01:20, 01:34, 01:46, 02:06, 02:11, 02:50, 03:10, 03:19, 03:26, 03:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:13:54

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Advanced REST Client 工具进行 API 请求测试，并结合 Genymotion 模拟器展示移动端应用的交互与测试场景。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 001: 进入 Advanced REST Client 的 History 页面，正在加载历史请求记录。
画面 002: 显示历史请求列表，包含多个 POST 和 GET 请求，目标地址涉及用户登录、联系人查询等接口。
画面 003: 与画面 002 相同，鼠标悬停在 History 选项上，无新操作。
画面 004: 选中一个请求后，显示响应详情，状态码 200，响应体为 JSON 格式，包含用户信息。
画面 005: 展示 JSON 响应体内容，包含用户头像 URL、昵称、城市等字段。
画面 006: 在 Advanced REST Client 中编辑一个 GET 请求，目标地址为 /messages/keyword=1。
画面 007: 切换到桌面，显示“黑马程序员”和“博学谷”的品牌标识。
画面 008: 启动 Genymotion 模拟器，显示一个 Android 应用界面，出现“FormatException: Invalid number”的错误提示。
画面 009: Genymotion 模拟器界面时间变为 11:51，错误提示内容未变。
画面 010: Genymotion 模拟器进入“选择联系人”页面。
画面 011: Genymotion 模拟器选中联系人“米朵妹妹”，进入聊天界面。
画面 012: Genymotion 模拟器返回“选择联系人”页面，显示“Assertion failed”错误。
画面 013: 在 Typora 编辑器中打开 day05.md 文件，左侧为文档大纲，右侧显示与画面 005 相同的 JSON 响应数据。
画面 014: Typora 编辑器中显示与画面 006 相同的请求编辑界面，下方是 Genymotion 模拟器的“选择联系人”页面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 004 响应体：
{
  "count": 0,
  "pagination": {
    "page": 1,
    "size": 10
  },
  "items": [
    {
      "id": "m11",
      "avatar": "https://itcast-taobao.oss-cn-shanghai.aliyuncs.com/images/logo/9.jpg",
      "nickname": "评价",
      "gender": "m",
      "age": 20,
      "city": "北京市"
    }
  ]
}

画面 005 响应体：
{
  "count": 0,
  "pagination": {
    "page": 1,
    "size": 10
  },
  "items": [
    {
      "id": "m11",
      "avatar": "https://itcast-taobao.oss-cn-shanghai.aliyuncs.com/images/logo/9.jpg",
      "nickname": "评价",
      "gender": "m",
      "age": 20,
      "city": "北京市"
    }
  ]
}

画面 006 请求地址：
GET /192.168.31.98/messages/keyword=1

画面 006 请求头：
Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNTIzNzQxNjMwLCJpYXQiOjE1MjM3MzU2MzAsInN1YiI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE5MjE2ODMzMTkiLCJ1c2VybmFtZSI6ImFkbWluIiwiYXV0aG9yaXphdGlvbiI6IjE
