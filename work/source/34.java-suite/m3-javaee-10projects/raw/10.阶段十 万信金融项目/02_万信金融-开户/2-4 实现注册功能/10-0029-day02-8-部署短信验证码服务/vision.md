# 画面线理解：day02-8-部署短信验证码服务

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-8-部署短信验证码服务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:31, 02:51, 03:42, 04:06, 04:25, 05:27, 07:50, 08:02, 08:37, 10:34, 11:05, 11:59, 13:57, 14:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:17:48

1) 这一组画面整体在讲如何部署并接入短信验证码服务，包括安装Redis、运行sailing服务、配置Apollo并测试功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个系统架构图，包含“测试端/App”、“用户中心”、“UAS认证服务”、“统一账户”和“短信服务”五个模块，通过编号箭头展示各模块间的交互流程。
画面2：展示多个窗口，包括Apollo配置中心、Redis服务、sailing服务的代码和配置文件，以及系统架构图。
画面3：展示PPT内容，标题为“1.3 部署短信验证码服务”，说明服务基于sailing项目，需运行runSms.bat或runSms-student.bat。
画面4：展示Redis的Master-Slave复制配置说明，包含配置项如“requirepass”和“slave-serve-stale-data”。
画面5：展示PPT内容，标题为“1.2 安装Redis”，说明需确认6379端口未被占用，并展示Redis服务启动后的控制台输出。
画面6：展示PPT内容，标题为“1.3 部署短信验证码服务”，说明需运行runSms.bat或runSms-student.bat，并提供GitHub下载链接。
画面7：展示文件夹内容，包含runSms-student.bat、sailing.jar等文件。
画面8：展示命令行窗口，显示sailing服务启动日志，包括Spring Boot初始化、Tomcat启动等信息。
画面9：展示PPT内容，标题为“1.3 部署短信验证码服务”，说明需运行runSms.bat或runSms-student.bat，并提供GitHub下载链接。
画面10：展示PPT内容，标题为“2 接入短信验证码服务”，说明需在Apollo上配置account-service项目。
画面11：展示Apollo配置中心界面，显示application配置项，包括sms.url和sms.enable。
画面12：展示PPT内容，标题为“3. 增加验证码服务参数”，说明需在Apollo中配置sms.url和sms.enable。
画面13：展示一个登录界面，包含“请输入手机号”和“请输入验证码”输入框，以及“登录”按钮。
画面14：展示PPT内容，标题为“1.2 安装Redis”，说明需确认6379端口未被占用，并展示Redis服务启动后的控制台输出。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面3：
1.3 部署短信验证码服务
本服务是传智播客基于腾讯云实现的一个开源项目sailing，发送短信验证码的功能已经实现，大家直接运行脚本即可使用，无需进行其他操作，该服务会占用56085端口。
1. 运行runSms.bat会启动sailing.jar，该服务会把短信验证码发送到手机上（有使用次数限制，建议用于体验）
2. 运行runSms-student.bat会启动sailing-student.jar，该服务会把短信验证码发送到控制台上，不会发到手机上（没有使用次数限制，建议在开发过程中使用）
事件中只提供jar包和运行脚本，如果你对源码感兴趣，请自行去github上下载：
git clone https://github.com/fightingpigeon/sailing.git

画面6：
1.3 部署短信验证码服务
本服务是传智播客基于腾讯云实现的一个开源项目sailing，发送短信验证码的功能已经实现，大家直接运行脚本即可使用，无需进行其他操作，该服务会占用56085端口。
1. 运行runSms.bat会启动sailing.jar，该服务会把短信验证码发送到手机上（有使用次数限制，建议用于体验）
2. 运行runSms-student.bat会启动sailing-student.jar，该服务会把短信验证码发送到控制台上，不会发到手机上（没有使用次数限制，建议在开发过程中使用）
事件中只提供jar包和运行脚本，如果你对源码感兴趣，请自行去github上下载：
git clone https://github.com/fightingpigeon/sailing.git

画面11：
sms.url = http://localhost:56085/sailing/
sms.enable = true

画面12：
#短信验证码服务地址
sms.url = http://localhost:56085/sailing/
#开启短信验证码功能
sms.enable = true

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：架构图，包含“测试端/App”、“用户中心”、“UAS认证服务”、“统一账户”和“短信服务”五个模块，通过编号箭头展示各模块间的交互流程。
画面10：PPT标题为“2 接入短信验证码服务”，内容包括“1. 总览Apollo，找到account-service项目”、“2. 展开application配置项”、“3. 增加验证码服务参数”。
画面11：Apollo配置中心界面，显示application配置项，包括sms.url和sms.enable。
画面12：PPT标题为“3. 增加验证码服务参数”，内容包括“#短信验证码服务地址”、“#开启短信验证码功能”。
画面13：登录界面，包含“请输入手机号”和“请输入验证码”输入框，以及“登录”按钮。

5) 无。
