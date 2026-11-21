# 画面线理解：06-有状态服务和无状态服务

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\06-有状态服务和无状态服务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:43, 01:18, 02:51, 02:59, 04:11, 04:12, 04:31, 04:57, 05:19, 05:31, 05:56, 06:01, 06:10, 07:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:11:34

1) 这一组画面整体在讲什么（一句话）：
讲解有状态服务与无状态服务的区别，以及基于JWT的API鉴权机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前章节为“2 有状态服务和无状态服务”，重点在“2.1 什么是服务中的状态”。
画面2：鼠标选中标题“无状态服务”，准备讲解该小节。
画面3：展示“2.2 无状态服务”小节内容，包含无状态服务的定义和一个流程图，图中显示前端向服务端发送POST /login请求，服务端验证登录并生成token，然后前端携带token访问数据。
画面4：流程图中增加“校验token”步骤，显示前端发送带有Authorization: Bearer.token的GET /user请求，服务端校验token。
画面5：画面切换至“2.3 有状态服务”小节标题。
画面6：画面保持在“2.3 有状态服务”小节标题。
画面7：画面保持在“2.3 有状态服务”小节标题。
画面8：画面切换回“2.2 无状态服务”小节内容，流程图完整展示。
画面9：画面切换至“2.3 有状态服务”小节内容，展示有状态服务的定义。
画面10：画面切换至“2.3 有状态服务”小节内容，展示有状态服务的定义和底部的黑马程序员信息。
画面11：画面展示“2.3 有状态服务”小节内容，流程图中增加“sessionid”和“服务端session”云朵，表示服务端存储session信息。
画面12：画面保持在“2.3 有状态服务”小节内容，流程图中“sessionid”指向“服务端session”。
画面13：画面保持在“2.3 有状态服务”小节内容，流程图中“sessionid”指向“服务端session”。
画面14：画面切换至“3 基于JWT的API鉴权”小节标题，流程图中“sessionid”指向“服务端session”，并显示“3 基于JWT的API鉴权”标题。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无代码、配置、命令、目录结构、SQL、XML/YAML 配置出现。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3-4：架构图/流程图结构：
- 前端 (browser) → 服务端 (Server)：用户登录 POST /login
- 服务端 (Server) → 前端 (browser)：HTTP 200 OK {token: "..."}
- 前端 (browser) → 服务端 (Server)：访问数据 Get /user Authorization: Bearer.token
- 服务端 (Server) → 前端 (browser)：HTTP 200 OK {}

画面5-6-7-8-9-10-11-12-13-14：架构图/流程图结构：
- 前端 (browser) → 服务端 (Server)：用户登录 POST /login
- 服务端 (Server) → 前端 (browser)：HTTP 200 OK sessionid
- 前端 (browser) → 服务端 (Server)：访问数据 Get /user sessionid
- 服务端 (Server) → 前端 (browser)：HTTP 200 OK {}

画面11-12-13-14：架构图/流程图结构：
- 前端 (browser) → 服务端 (Server)：用户登录 POST /login
- 服务端 (Server) → 前端 (browser)：HTTP 200 OK sessionid
- 服务端 (Server) → 服务端session（云朵）：sessionid
- 前端 (browser) → 服务端 (Server)：访问数据 Get /user sessionid
- 服务端 (Server) → 服务端session（云朵）：sessionid
- 服务端 (Server) → 前端 (browser)：HTTP 200 OK {}

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
