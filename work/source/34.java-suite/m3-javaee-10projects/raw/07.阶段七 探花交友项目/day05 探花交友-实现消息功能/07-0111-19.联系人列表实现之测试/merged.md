# 19.联系人列表实现之测试

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\19.联系人列表实现之测试_【海量资源尽在 666java.com】.mp4
- 时长 3分34秒（音频 215s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来测试一下那么首先呢我们还是要去发送验证码然后呢去登录一下然后呢我们去走那么我们还是我们要通过我们的6962这个去做一个这个查询了然后呢然后呢这个6962我们来拷贝一下然后呢去做一个做一个这个登录
[00:28] 好得到一个这个token然后呢我们通过这个去做一个查询做一个查询然后呢我们查询呢我们就来找一下就在这吧那么就他然后呢我们对他呢去发起一个get请求就可以了好然后呢走那么这个呢我们是没有这个查询列表的对吧没有去做没有去根据关键字去查询的那么这个就会查询啊所有的这个数据啊
[00:58] 那么我们这款呢会有一个问题就是A者会有点问题当然我们可能这个是没数据啊那我们来检查一下那么这个是UserInfo这个是多少啊100这个用户那我们来找一下100这个用户它的确是A者是没有数据的对吧那我们来随便给他加一些这个数据啊21啊随便我们来写一点这个数据然后呢我们再来查询一下好这样的这个是不是结构就OK了啊好然后呢我们接下来呢
[01:27] 就来根据一个我们查询的关键字去做一个查询比如说我们跟一个这个关键字为这个波对吧做查询走那么查询到结果呢就会只有一条了那么都是OK的啊好那么接下来呢我们就把我们的模拟器呢我们就跑起来然后呢我们来测试一下啊好那么我们还是呢通过我们刚刚这个手机号呢去登录一下啊那么02026962
[01:56] 然后呢我们去获取验证码123456啊输入然后呢我们进入我们的这个消息啊当然这个这个错误呢是我们这个就是时间这一块在我们的APP这块时间呢会有点问题啊就是到时候我们会做一个处理啊然后呢我们去先来看这一块就是我们去查看联系人点击他
[02:22] 然后就会去查询我们刚刚这个列表了对吧然后就返回正常数据了比如说我们现在输入一个H做一个搜索现在可能还是我们的APP这块有点问题然后输入之后没有反应那么可能是在这块实现方面会有点问题
[02:48] 但是我们的这个接口其实已经提供了只是App端会有点问题那么这个应该问题并不大然后我们点击每一个用户就可以进行做聊天了比如说我们选择黑马选择他然后就可以给他去发送一些消息对吧发送然后走就这个消息就已经发出去了然后我们可以选择他也可以我们选择这个
[03:14] 也可以去做一些发送但是这块呢还是说的那个时间那个问题会有点问题啊好那么这个呢就是我们这个联系人联系人列表的这样的一个实现啊那么失败我们已经就实现完成了OK好那么关于我们这个联系人列表的一个这个测试呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

