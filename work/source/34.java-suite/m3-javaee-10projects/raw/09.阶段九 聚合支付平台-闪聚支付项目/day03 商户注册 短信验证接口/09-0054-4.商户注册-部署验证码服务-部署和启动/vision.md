# 画面线理解：4.商户注册-部署验证码服务-部署和启动

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\4.商户注册-部署验证码服务-部署和启动【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:02, 01:26, 01:48, 02:10, 02:31, 03:35, 04:20, 05:26, 05:50, 06:33, 07:13, 07:38, 08:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:50:44

1) 这一组画面整体在讲什么（一句话）：
演示如何下载、导入并配置一个用于短信验证码服务的 Spring Boot 项目，包括 Redis 配置和腾讯云短信服务的接入。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“1.3.1 下载源码”部分，提供 git 克隆命令：git clone https://github.com/fightingape/sailing.git。
画面 2: PDF 文档中“1.3.2 使用idea打开项目”部分，展示项目在 IDEA 中的工程结构，包含 src、resources、docker 等目录。
画面 3: Windows 资源管理器中显示“sailing”文件夹，路径为：D:\teach\shancup\module2\code\sailing。
画面 4: IDEA 中打开的“VerificationGenerator.java”文件，显示 Redis 配置（host: localhost, port: 6373, timeout: 10000）和 SMS 配置（qcloud, appid, appKey, templateId, sign）。
画面 5: PDF 文档中“1.3.2 使用idea打开项目”部分，再次展示项目在 IDEA 中的工程结构。
画面 6: PDF 文档中“1.3.3 开通腾讯云短信服务”部分，说明需要开通腾讯云短信服务并获取 SDKAppID 和 AppKey。
画面 7: Windows 资源管理器中显示“sailing”文件夹，路径为：D:\teach\shancup\module2\code\sailing。
画面 8: IDEA 中打开的项目结构，鼠标悬停在“resources”文件夹上。
画面 9: PDF 文档中“1.3.3 开通腾讯云短信服务”部分，说明需要配置短信参数，提供配置文件路径：sailing/src/main/resources/application.yml。
画面 10: IDEA 中打开的“application.yml”文件，显示 SMS 配置（qcloud, appid, appKey, templateId, sign）和 Swagger 配置（enable: true）。
画面 11: IDEA 中打开的“SmsNumberVerificationHandler.java”文件，显示注释“// 使用请求示例说明”和代码“smsService.sendSms(mobile, code, getEffectiveTime())”。
画面 12: IDEA 中“SailingBootstrap.java”文件的运行界面，显示已连接到目标（地址：127.0.0.1:63661，传输：socket）。
画面 13: PDF 文档中“1.3.3 开通腾讯云短信服务”部分，说明需要开通腾讯云短信服务。
画面 14: PDF 文档中“1.3.3 开通腾讯云短信服务”部分，说明需要配置短信参数，提供配置文件路径：sailing/src/main/resources/application.yml。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
git clone https://github.com/fightingape/sailing.git

画面 4:
redis:
  host: localhost
  port: 6373
  shutdown-timeout: 100
  pool:
    max-idle: 8
    min-idle: 0
    max-active: 8
    max-wait: 10000
  timeout: 10000
sms:
  qcloud:
    appid: 0
    appkey: appkey
    templateid: 0
    sign: 签名

画面 9:
sms:
  qcloud:
    appid: 14080000
    appKey: 36ff75d14d0d2342344cdcf335cc25852
    templateId: 234323
    sign: 签名

画面 10:
sms:
  qcloud:
    appid: 0
    appkey: appkey
    templateid: 0
    sign: 签名
swagger:
  enable: true
logging:
  config: classpath:log4j2.xml

画面 11:
// 使用请求示例说明
smsService.sendSms(mobile, code, getEffectiveTime());

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6:
标题：1.3.3 开通腾讯云短信服务
内容：
1) 开通腾讯云短信服务
   - https://cloud.tencent.com/product/sms/getting-started
   - 1. 开通短信服务成功后，获取 SDKAppID 和 AppKey
   - 2. 申请签名并确认审核通过
   - 3. 申请模板并确认审核通过
2) 配置短信参数
   - 1. 打开项目中sailing/src/main/resources/application.yml
   - 2. 将腾讯云短信服务获取到参数做如下配置：

画面 13:
标题：1.3.3 开通腾讯云短信服务
内容：
1) 开通腾讯云短信服务
   - https://cloud.tencent.com/product/sms/getting-started
   - 1. 开通短信服务成功后，获取 SDKAppID 和 AppKey
   - 2. 申请签名并确认审核通过
   - 3. 申请模板并确认审核通过

画面 14:
标题：1.3.3 开通腾讯云短信服务
内容：
1) 开通腾讯云短信服务
   - https://cloud.tencent.com/product/sms/getting-started
   - 1. 开通短信服务成功后，获取 SDKAppID 和 AppKey
   - 2. 申请签名并确认审核通过
   - 3. 申请模板并确认审核通过
2) 配置短信参数
   - 1. 打开项目中sailing/src/main/resources/application.yml
   - 2. 将腾讯云短信服务获取到参数做如下配置：

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
