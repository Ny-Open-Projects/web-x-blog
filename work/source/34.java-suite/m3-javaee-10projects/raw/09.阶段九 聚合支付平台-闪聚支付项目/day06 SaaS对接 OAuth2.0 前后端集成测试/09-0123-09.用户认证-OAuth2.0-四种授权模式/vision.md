# 画面线理解：09.用户认证-OAuth2.0-四种授权模式

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\09.用户认证-OAuth2.0-四种授权模式【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:35, 02:09, 03:03, 03:24, 04:38, 06:14, 06:43, 07:37, 09:25, 10:19, 12:08, 12:56, 13:26, 14:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:38:52

1) 这一组画面整体在讲 OAuth2.0 的四种授权模式（授权码模式、密码模式、客户端模式、简化模式）及其流程和参数说明，并引出 SaaS 概念。

2) 按时间顺序列出每张画面的要点：

画面1：
要点：展示 OAuth2.0 授权码模式的流程图，包含“资源拥有者”、“浏览器”、“客户端”和“授权服务器”四个组件，以及步骤 (1) 到 (5) 的交互流程。

画面2：
要点：详细说明授权码模式步骤 (1)，展示授权请求 URL：/uaa/oauth/authorize?client_id=p2pweb&response_type=code&app&redirect_uri=http://xx.xx/notify，并列出参数：client_id、response_type、scope、redirect_uri。

画面3：
要点：展示“黑马程序员”登录界面的截图，说明用户通过第三方授权登录的场景。

画面4：
要点：说明授权码模式步骤 (2) 和 (3)，展示获取授权码的 URL：/uaa/oauth/token?client_id=p2pweb&client_secret=gdjbc&grant_type=authorization_code&code=5Pgfc&redirect_uri=http://xx.xx/notify，并列出参数：client_id、client_secret、grant_type、code、redirect_uri。

画面5：
要点：重复画面4的内容，强调授权码模式步骤 (4)，客户端使用授权码换取 access_token。

画面6：
要点：切换到密码模式，展示其流程图，包含“资源拥有者”、“客户端”和“授权服务器”三个组件，以及步骤 (1) 和 (2) 的交互流程。

画面7：
要点：在目录结构中高亮显示“2.3.2.2 密码模式”，准备讲解密码模式。

画面8：
要点：展示密码模式步骤 (2) 的请求 URL：/uaa/oauth/token?client_id=p2pweb&client_secret=fgsdrf&grant_type=password&username=shangsan&password=123456，并列出参数：client_id、client_secret、grant_type、username、password。

画面9：
要点：展示简化模式的流程图，包含“资源拥有者”、“浏览器”、“客户端”和“授权服务器”四个组件，以及步骤 (1) 到 (5) 的交互流程。

画面10：
要点：展示简化模式步骤 (1) 的授权请求 URL：/uaa/oauth/authorize?client_id=p2pweb&response_type=code&scope=app&redirect_uri=http://xx.xx/notify，并列出参数：client_id、response_type、scope、redirect_uri。

画面11：
要点：在简化模式的 URL 中高亮显示 client_id 参数。

画面12：
要点：在简化模式的 URL 中高亮显示 response_type、scope 和 redirect_uri 参数。

画面13：
要点：展示“闪聚支付平台”的多租户结构图，包含“闪聚支付平台”、“系统A”、“系统B”、“系统C”、“系统D”、“系统E”等模块，以及“租户A购买服务(权限集合)”的说明。

画面14：
要点：切换到“闪聚支付 第2章 讲义-对接SaaS”，展示“1 对接SaaS”和“1.1 基础概念”下的“1.1.1 SaaS”部分，内容为 SaaS 的定义和与传统软件的区别。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：

画面2：
```
/uaa/oauth/authorize?
client_id=p2pweb&response_type=code&app&redirect_uri=http://xx.xx/notify
```

画面4：
```
/uaa/oauth/token?
client_id=p2pweb&client_secret=gdjbc&grant_type=authorization_code&code=5Pgfc&redirect_uri=http://xx.xx/notify
```

画面8：
```
/uaa/oauth/token?
client_id=p2pweb&client_secret=fgsdrf&grant_type=password&username=shangsan&password=123456
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：

画面1：
- 资源拥有者 → 浏览器 (步骤2)
- 浏览器 → 授权服务器 (步骤2)
- 授权服务器 → 浏览器 (步骤3)
- 浏览器 → 客户端 (步骤4)
- 客户端 → 授权服务器 (步骤5)

画面6：
- 资源拥有者 → 客户端 (步骤1)
- 客户端 → 授权服务器 (步骤2)
- 授权服务器 → 客户端 (步骤3)

画面9：
- 资源拥有者 → 浏览器 (步骤2)
- 浏览器 → 授权服务器 (步骤2)
- 授权服务器 → 浏览器 (步骤3)
- 浏览器 → 客户端 (步骤4)
- 客户端 → 授权服务器 (步骤5)

画面13：
- 闪聚支付平台 → 系统A、系统B、系统C、系统D、系统E
- 租户A购买服务(权限集合) → 系统A、系统B、系统C、系统D、系统E

5) 无。
