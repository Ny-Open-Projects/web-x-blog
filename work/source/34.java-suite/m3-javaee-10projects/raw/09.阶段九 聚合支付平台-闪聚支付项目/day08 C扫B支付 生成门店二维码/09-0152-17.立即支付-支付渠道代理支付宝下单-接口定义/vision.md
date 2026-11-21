# 画面线理解：17.立即支付-支付渠道代理支付宝下单-接口定义

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\17.立即支付-支付渠道代理支付宝下单-接口定义【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:07, 01:44, 02:44, 03:34, 04:18, 05:11, 06:51, 08:29, 09:37, 11:32, 12:37, 13:44, 16:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:58:12

1) 这一组画面整体在讲什么（一句话）：
本课程讲解如何搭建支付通道代理工程，实现调用支付宝WAP下单接口的支付功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“立即支付”章节的需求分析，包含交互流程图，描述用户、商户、聚合支付平台、交易服务、支付渠道代理服务、第三方支付之间的交互流程。
画面2：在IntelliJ IDEA中打开项目，右键点击“Project Structure...”选项，准备配置项目结构。
画面3：在“Select File or Directory to Import”对话框中，选中“shanjupy-payment-agent-api”模块，准备导入项目。
画面4：在Nacos配置中心新建配置，Data ID为“payment-agent-service.yaml”，Group为“DEFAULT_GROUP”，配置格式为“YAML”。
画面5：在IDEA中打开“bootstrap.yml”配置文件，内容包含server端口、Nacos地址、Spring Boot应用名、云服务配置等。
画面6：展示“5.2 搭建支付通道代理工程”章节标题，下方有业务流程图，描述从“开始”到“用户扫描二维码”的支付流程。
画面7：展示“5.3.1.2 接口定义”章节，内容为在PayChannelAgentService中定义接口，用于调用支付宝手机WAP下单接口。
画面8：在IDEA中打开“PayChannelAgentService.java”文件，准备编写接口实现。
画面9：在“PayChannelAgentService.java”文件中，编写调用支付宝WAP下单接口的代码，包含构造AlipayTradeWapRequest对象并设置参数。
画面10：展示“支付宝接口参数”表格，包含app_id、method、format、return_url、charset、sign_type等参数的类型、是否必填、最大长度、描述和示例值。
画面11：展示“支付宝接口参数”表格中“body”、“subject”、“out_trade_no”、“timeout_express”等字段的详细信息。
画面12：与画面11相同，鼠标在“timeout_express”字段上。
画面13：与画面11相同，鼠标在“timeout_express”字段上。
画面14：在“PayChannelAgentService.java”文件中，编写实现createPayOrderByAliWAP方法的代码，包含异常处理和返回值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5 bootstrap.yml：
server:
  port: 56070 #启动端口，命令行注入
spring:
  application:
    name: payment-agent-service
  cloud:
    nacos:
      server-addr: ${nacos.server.addr}
      namespace: a11b383-311-78c1-90d8-92d2508
      discovery:
        server-addr: ${nacos.server.addr}

画面7 PayChannelAgentService.java：
package com.shanjupy.payment.agent.api;

public interface PayChannelAgentService {
    /**
     * 调用支付宝手机WAP下单接口
     * @param aliConfigParam 支付渠道配置的参数（配置的支付的必要参数）
     * @param alipayBean 业务参数（商户订单号，订单描述，订单金额）
     * @return
     * @throws BusinessException
     */
    PaymentResponseDTO createPayOrderByAliWAP(AlipayConfigParam aliConfigParam, AlipayBean alipayBean)

画面9 PayChannelAgentService.java：
AlipayTradeWapRequest alipayRequest = new DefaultAlipayTradeWapRequest();
alipayRequest.setNotifyUrl("http://www.xxx.com/notify_url.jsp"); //在公司家地址中设置回调地址
alipayRequest.setReturnUrl("http://www.xxx.com/return_url.jsp"); //在公司家地址中设置返回地址
String form = "";
try {
    //请求支付宝下单接口，发起http请求
    String result = alipayRequest.getAlipayService().createPayOrder(alipayRequest);
    form = result;
} catch (Exception e) {
    e.printStackTrace();
}

画面10 支付宝接口参数表格：
| 参数 | 类型 | 是否必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| app_id | String | 是 | 32 | 支付宝分配给开发者的应用ID | 201407230000 |
| method | String | 是 | 126 | 接口名称 | alipay.trade.wap.pay |
| format | String | 否 | 40 | 仅支持JSON | JSON |
| return_url | String | 否 | 256 | HTTP/HTTPS开头的URL | https://m.ali pay.com/QR8NF23 |
| charset | String | 否 | 10 | 请求使用的编码格式，如utf-8,gbk,gb2312等 | utf-8 |
| sign_type | String | 是 | 10 | 商户生成签名字符串所使用的签名算法类型，目前支持RSA2和RSA，推荐使用RSA2 | RSA2 |

画面11 支付宝接口参数表格：
| 参数 | 类型 | 是否必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| body | String | 否 | 128 | 商品描述，如果商品描述是多种商品，请将商品描述字符串累加传给body。 | iPhone6 16G |
| subject | String | 是 | 256 | 商品的标题/交易标题/订单标题等。 | 大乐透 |
| out_trade_no | String | 是 | 64 | 商户网站唯一订单号 | 705011111111S0 01111119 |
| timeout_express | String | 否 | 6 | 该笔订单允许的最晚付款时间，逾期将关闭交易，取值范围：1m-15d，m-分钟，h-小时，d-天，tc-当天（1c-当天的情况下，无论交易何时创建，都在0点关闭）。该参数数值不接受小数点，如1.5h，可转换为90m。注：若为 | 90m |

画面14 PayChannelAgentService.java：
public PaymentResponseDTO createPayOrderByAliWAP(AlipayConfigParam aliConfigParam, AlipayBean alipayBean) throws BusinessException {
    //调用支付宝下单接口
    AlipayTradeWapRequest alipayRequest = new DefaultAlipayTradeWapRequest();
    alipayRequest.setNotifyUrl("http://www.xxx.com/notify_url.jsp"); //在公司家地址中设置回调地址
    alipayRequest.setReturnUrl("http://www.xxx.com/return_url.jsp"); //在公司家地址中设置返回地址
    String form = "";
    try {
        //请求支付宝下单接口，发起http请求
        String result = alipayRequest.getAlipayService().createPayOrder(alipayRequest);
        form = result;
    } catch (Exception e) {
        e.printStackTrace();
    }
    return new PaymentResponseDTO(form);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“5 立即支付”，子标题“5.1 需求分析”，下方有交互流程图，从“用户”指向“商户”，再指向“聚合支付平台”，然后指向“交易服务”，再指向“支付渠道代理服务”，最后指向“第三方支付”。
画面6：PPT标题为“5.2 搭建支付通道代理工程”，下方有业务流程图，从“开始”指向“打开门店管理”，再指向“选择应用”，再指向“远程门店生成二维码”，最后指向“用户扫描二维码”。
画面10：表格数据为“支付宝接口参数”，包含app_id、method、format、return_url、charset、sign_type等参数的类型、是否必填、最大长度、描述和示例值。
画面11：表格数据为“支付宝接口参数”，包含body、subject、out_trade_no、timeout_express等字段的详细信息。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
