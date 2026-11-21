# 画面线理解：16.前后端集成测试-功能测试-支付渠道参数配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\16.前后端集成测试-功能测试-支付渠道参数配置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:47, 01:57, 02:53, 03:08, 03:42, 04:01, 04:08, 04:36, 05:00, 05:30, 05:59, 06:09, 06:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:43:14

1) 这一组画面整体在讲什么（一句话）：
演示如何在“闪聚宝”支付平台的商户后台进行资质申请、应用配置及支付渠道参数设置的全流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“资质申请”页面，列出测试接口如“/merchant/upload”和“/merchant/my/merchants/save”，并提示登录后进入资质申请页。
画面2：在浏览器中查看“我的支付”页面，右侧开发者工具显示“Request Payload”中包含“contactAddress”、“businessLicenseImg”等字段。
画面3：在“应用设置”页面，显示“基础信息”步骤，要求填写“应用名称”和“应用公司”。
画面4：在“应用设置”页面，切换至“服务类型”步骤，显示“支付ID”为1，“支付名称”为“微信JSAPI”，“支付编码”为“WX_JSAPI”。
画面5：在数据库管理工具中，查看“shanjipay_merchant_ser”表，显示商户信息，如“merchantId”为“1211219635996014974”，“merchantName”为“测试商户”。
画面6：在数据库管理工具中，查看“shanjipay_transaction”表，显示交易记录，如“merchantId”为“1211219635996014974”，“appChannel”为“WX_JSAPI”。
画面7：在“应用设置”页面，切换至“配置参数”步骤，填写“配置名称”为“test1234567890”，“商户appId”为“aa”，“应用公钥”为“bb”。
画面8：在数据库管理工具中，查看“shanjipay_transaction”表，显示“APP_CHANNEL”为“WX_JSAPI”。
画面9：在数据库管理工具中，查看“shanjipay_transaction”表，显示“APP_CHANNEL”为“ALIPAY_WAP”。
画面10：在“应用管理”页面，显示“应用ID”为“776:01114653 a74c-ua10a5b0”，“应用名称”为“test1234567890”，“应用分组”为“225”。
画面11：在“应用设置”页面，显示“配置参数”步骤，包含“支付ID”为1，“支付名称”为“微信JSAPI”，“支付编码”为“WX_JSAPI”。
画面12：在“资质申请”页面，展示“配置参数”页面，显示“支付ID”为1，“支付名称”为“微信JSAPI”，“支付编码”为“WX_JSAPI”，并提示“配置参数页面会显示对应服务类型下的原始支付渠道”。
画面13：在“资质申请”页面，列出测试接口如“/merchant/my/platform-channels”和“/merchant/my/pay-channel-params”，并提示“应用创建成功后，会自动跳转到绑定服务类型页面”。
画面14：在“资质申请”页面，展示“支付渠道参数配置”页面，要求填写“支付参数”，如“商户号”、“商户秘钥”、“支付渠道”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5 SQL：
SELECT * FROM shanjipay_merchant_ser WHERE merchantId = '1211219635996014974';
画面6 SQL：
SELECT * FROM shanjipay_transaction WHERE merchantId = '1211219635996014974';
画面7 表单数据：
配置名称：test1234567890
商户appId：aa
应用公钥：bb
应用私钥：cc
画面8 SQL：
SELECT * FROM shanjipay_transaction WHERE merchantId = '1211219635996014974';
画面9 SQL：
SELECT * FROM shanjipay_transaction WHERE merchantId = '1211219635996014974';
画面10 表格数据：
应用ID：776:01114653 a74c-ua10a5b0
应用名称：test1234567890
应用分组：225
画面12 表格数据：
支付ID：1
支付名称：微信JSAPI
支付编码：WX_JSAPI
画面13 表格数据：
接口名称：获取平台服务类型
接口路径：GET /merchant/my/platform-channels
接口分类：商户平台-渠道和支付参数
接口名称：为应用绑定平台服务类型
接口路径：POST /merchant/my/apps/appld/platform-channels
接口分类：商户平台-渠道和支付参数
接口名称：获取某应用下平台支付渠道参数
接口路径：GET /merchant/my/pay-channel-params/apps/appld/platform-channels
接口分类：商户平台-渠道和支付参数
接口名称：根据平台服务类型获取支付参数
接口路径：GET /merchant/my/pay-channels/platform-channel/platformChannelId
接口分类：商户平台-渠道和支付参数
接口名称：商户配置参数
接口路径：POST /merchant/my/pay-channel-params
接口分类：商户平台-渠道和支付参数
画面14 表单数据：
商户号：1234567890
商户秘钥：1234567890
支付渠道：微信JSAPI
支付编码：WX_JSAPI

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1 PPT标题：“1.5 资质申请”
画面1 表格数据：
测试接口列表：
证件上传：POST /merchant/upload
商户资质申请：POST /merchant/my/merchants/save
画面12 PPT标题：“配置参数页面会显示对应服务类型下的原始支付渠道”
画面13 PPT标题：“测试接口列表如下”
表格数据：
接口名称 | 接口路径 | 接口分类
获取平台服务类型 | GET /merchant/my/platform-channels | 商户平台-渠道和支付参数
为应用绑定平台服务类型 | POST /merchant/my/apps/appld/platform-channels | 商户平台-渠道和支付参数
获取某应用下平台支付渠道参数 | GET /merchant/my/pay-channel-params/apps/appld/platform-channels | 商户平台-渠道和支付参数
根据平台服务类型获取支付参数 | GET /merchant/my/pay-channels/platform-channel/platformChannelId | 商户平台-渠道和支付参数
商户配置参数 | POST /merchant/my/pay-channel-params | 商户平台-渠道和支付参数
画面14 PPT标题：“支付渠道参数配置”
表格数据：
支付ID | 支付名称 | 支付编码
1 | 微信JSAPI | WX_JSAPI
2 | 支付宝手机网站支付 | ALIPAY_WAP

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
