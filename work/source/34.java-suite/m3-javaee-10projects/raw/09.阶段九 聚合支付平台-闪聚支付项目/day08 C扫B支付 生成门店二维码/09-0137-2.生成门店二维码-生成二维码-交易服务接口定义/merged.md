# 2.生成门店二维码-生成二维码-交易服务接口定义

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\2.生成门店二维码-生成二维码-交易服务接口定义【海量资源尽在 666java.com】.mp4
- 时长 9分40秒（音频 580s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下面呢我们就来实现生成二维码刚才我们分析呢需要两个接口一个是交易服务要提供一个生成二维码的URL一个呢是商户平台应用要生成二维码的图片好那么我们先做交易服务生成二维码的URL那么我们先了解一下就是这个URL到底是个什么URL将来这个二维码呢就是让用户来扫码支付的就是C扫币它的二维码
[00:29] 那么一扫的话就会进入一个什么进入一个支付的入口那为什么叫支付的入口呢因为我们知道呢这个扫扫码可能是微信也可能是支付宝对吧所以我们让他进入到一个入口那这个入口呢他会去判断是哪个客户端来扫的码然后呢最终会存定向到一个支付确认的页面所以各位咱们需要知道的是什么呢就是这个
[00:58] 生成二维码的URL这是给谁用的就是给C扫币用户扫码用的对吧而这个URL呢现在我们把它命名为支付入口具体这个入口里边如何做做哪些那我们单独有一个小节呢是讲这个支付入口的下面我们就看那么这个接口我们怎么定义首先我们要去这个生成这个URL你要知道这个
[01:28] URL里边要包括哪些参数是不是你是哪个商户生成的你是哪个应用的哪个门店的这三个参数是不是不用我多解释大家应该能想得通吧因为这个二维码是一定要隶属于某个应用哪一个门店哪个应用哪个门店都隶属了那肯定还隶属于哪个商户对不对另外还有一个就是标题和内容因为我刚才说过最终我们会
[01:58] 展示一个支付确认的页面那这个支付确认的页面是不是至少得说你是买了什么商品对吧大概的一个内容描述所以这两个参数呢交易服务呢也提供出去然后呢你如果传了那么他呢就把这两个参数呢放在这个URL里面大家理解了吗所以这个支付入口这个URL后边它会自动
[02:29] 应该不是自动是交易服务帮他做要生成这个URL呢他就会包括对这一堆的什么参数大家理解吗有人说老师那这个URL最终干啥呀它是一个支付入口后边有一个单独的小节我们去讲这个支付入口怎么实现现在大家就只需要知道这个URL我们说它的生成规则是啥需要哪些参数那我们
[02:56] 说那最终我们要实现的内容方式呢其实就是这个传入一堆的参数然后呢我们把这堆参数呢通过转成Jason对象然后呢base64编码然后呢把它作为URL的一个参数那最终是不是就返回一个URL那将来请求这个URL那好这就到我们的这个支付入口了对这就是我们说的这个接口的一个
[03:23] 大概的一个实现方式啊一会儿呢我们实现的时候大家就非常清楚了好那下面我们就来定义这个接口因为我们刚才说过嘛它要生成URLURL后边是不是要挂很多的参数啊所以这里边呢我们就单独建一个DTO然后呢里边来啊来把这个支付入口所需要的参数呢都罗列进去后边呢传递这个参数就比较方便来我们把这个DTO建一下现在我们要做的是不是在交易服务生成
[03:52] 这个二维码的URL对不对所以很显然我们应该在交易服务这个API的这个工程中我们去把这个DTO啊给它建上去对吧好那这里边呢我们就创建一个这个好那这个整个过程这个DTO呢我就不再去敲了就直接拷贝了这些参数就是我们生成二维码URL
[04:22] 然后呢它携带的一堆的参数好那么这个DTO建好了之后呢下面我们就可以来创建这个接口这个接口呢我们是在这个交易服务当中对吧交易服务你看原来我们是不是有一个叫做当时渠道参数配置的时候有一个Service现在呢很显然我们还得建一个Service这个Service的一个接口吧然后这个呢就是看好啊
[04:51] 这是交易服务另外一个Service我单独定义的叫交易服务交易相关的一个服务接口那你现在要做这个怎么样的接口呀生成二维码URL对吧那URL肯定是个字无创生成二维码你要给我传参就是这个二维码将来生成完了之后它后边携带一堆参数这堆参数刚才我是不是专门创建了一个DTO
[05:22] 看懂了吗当然后边还可以让他去把这个自定义异常给他抛出去如果一旦有这个什么异常了好这样的话我来写个注释好那这个就是三层门店二维码它的URL的一个接口那这个对象类型当中应该包括哪几个参数呢我们说应该包括商务ID对吧APP ID门店ID以及标题内容
[05:55] 那么返回什么呢它会返回一个支付入口而返回的这个支付入口它需要把什么呀这个支付入口它是一个URL嘛这个URL它要携带参数什么参数呢注意看啊将上边的上边的什么将传入的参数啊转成Jason然后呢再用base64编码对
[06:26] 这就是我们说最终要返回的这个URL它到底是一个什么样子的懂了吧那么这样的话我们就可以在这个交易服务的哪里啊下边我们就可以来去定义它了那定义的方式也很简单也就是在这呢我们写一个实现的什么类哎错了啊把它这个名称给它改一下通常我们名称后面加IMPL对吧
[06:58] 好那这个它是一个将来是个远程调用的接口嘛所以这里面我们要用Service double的这个注解当然为了方便打日志写了一个long book的一个注解是不是OK了然后呢它需要实现谁是不是这个接口OK了吧好那么在这个接口当中我们需要去写哪些东西呢刚才不说了吗你你首先是不是最终的目的啊最终的目标
[07:29] 是要生成一个什么支付入口的URL而这个URL需要携带携带啥刚才不说了吗携带一堆的参数而这个参数呢是需要将这个对象里面的这个数据呢拼装成json然后呢用base64进行编码那最终我就返回这么一个URL就行了懂了吗好
[08:00] 那么按照我们的这个需求我们再看还少什么你将来各位你传进去的这个商户应用和门店那我问你你不能传什么他都可以生成一个支付入口这个支付入口一定是合法的吧啥是合法的你比如说这个商户和应用根本都不配套就这个应用不属于这三户那你生成的这个URL能用吗不能用所以前边我们要校验什么呀
[08:29] 我们要校验一下商户和应用和门店这些ID的什么它的合法性有时候老师但这个合法性咋校验呀合法性咋校验呀其实我们分两步校验吧比如我们校验这个应用是否属于商户行不行然后我们再校验什么我们再校验这个门店是否属于商户说白了就是看
[09:01] 这个应用和门店是不是商户的对不对那教练通过了之后这里边我们就开始干嘛我们就开始这个这个组装数据为啥组装数据因为你最终组装URL所需要的数据之后你是不是才能把它用贝斯流传编码然后生成这个URL
[09:25] 对这就是整个的一个接口的一个逻辑啊最终会生成一个URL好了那么到这呢我们先把这个接口咱们先把它定义出来稍后我们再实现整个接口的内容好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解C扫B支付中交易服务生成二维码URL的接口定义与实现，包括DTO类和接口服务的代码编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档大纲，当前定位在“3.4.2.1 接口定义”，内容为“生成门店的C扫B二维码”，并显示了接口定义的Java代码片段。
画面2：展示“3.4.2.1 接口定义”下的“接口参数”部分，输入为“商户id、应用id、门店id、标题、内容”，输出为“支付入口”，并显示了DTO类的代码。
画面3：与画面2内容相同，仅光标位置不同。
画面4：与画面2内容相同，光标位置不同，下方出现“select a language”提示框。
画面5：IDE界面，展示项目结构，选中“shanju-pay-transaction-api”模块，右侧编辑器显示“QRCodeUtil.java”中的main方法，用于测试生成二维码。
画面6：IDE界面，选中“QRCodeDTO.java”文件，准备进行编辑。
画面7：文档界面，显示“3.4.2.1 接口定义”下的“接口参数”部分，输入为“商户id、应用id、门店id、标题、内容”，输出为“支付入口”，并显示了DTO类的代码。
画面8：IDE界面，编辑“QRCodeDTO.java”文件，光标位于“private String appId;”行。
画面9：IDE界面，编辑“TransactionService.java”文件，光标位于“String createStoreQRCode(QRCodeDto qrCodeDto) throws BusinessException;”方法签名处，下方显示了方法的自动补全建议。
画面10：IDE界面，编辑“TransactionService.java”文件，光标位于“String createStoreQRCode(QRCodeDto qrCodeDto) throws BusinessException;”方法签名处，显示了方法的注释。
画面11：IDE界面，右键“TransactionService.java”文件，弹出菜单，选择“Implement Methods”。
画面12：弹出“Select Methods to Implement”对话框，显示“createStoreQRCode(QRCodeDto qrCodeDto):String”方法，下方有“Copy Javadoc”和“Insert @Override”复选框。
画面13：IDE界面，编辑“TransactionService.java”文件，光标位于“return null;”行，方法体中包含注释“//将参数生成一个支付入口（url），需要将传入的参数转换成json，用base64编码”。
画面14：文档界面，展示“1.1 C扫B的概念”，内容为“C扫B，即顾客(Customer)扫描商户(Business)提供的二维码来完成支付。下图是支付宝提供的C扫B业务流程：1、商家出示付款二维码。2、客户打开支付宝或微信的扫一扫，扫描二维码。3、确认支付，完成支付。”

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
private String appid;
private Long storeId;
private String subject;//商品标题
private String body;//订单描述
```
画面2：
```java
@Data
@NoArgsConstructor
public class QRCodeDto implements Serializable {
    private Long merchantId;
    private String appId;
    private Long storeId;
    private String subject;//商品标题
    private String body;//订单描述
}
```
画面4：
```java
@Data
@NoArgsConstructor
public class QRCodeDto implements Serializable {
    private Long merchantId;
    private String appId;
    private Long storeId;
    private String subject;//商品标题
    private String body;//订单描述
}
```
画面5：
```java
void main(String[] args) throws IOException {
    QRCodeUtil qrCodeUtil = new QRCodeUtil();
    String url = qrCodeUtil.createQRCode("http://192.168.159.1:56010/transaction/success");
    System.out.println(url);
}
```
画面6：
```java
package com.shanju.pay.transaction.api.dto;
```
画面7：
```java
@Data
@NoArgsConstructor
public class QRCodeDto implements Serializable {
    private Long merchantId;
    private String appId;
    private Long storeId;
    private String subject;//商品标题
    private String body;//订单描述
}
```
画面8：
```java
import java.io.Serializable;
```
画面9：
```java
public interface TransactionService {
    String createStoreQRCode(QRCodeDto qrCodeDto) throws BusinessException;
}
```
画面10：
```java
/**
 * 交易订单相关服务接口
 */
public interface TransactionService {
    /**
     * 生成门店二维码
     * @param qrCodeDto 传入merchantId,appId,storeId,channel,subject,body
     * @return 支付入口URL，将二维码的参数组成json并用base64编码
     * @throws BusinessException
     */
    String createStoreQRCode(QRCodeDto qrCodeDto) throws BusinessException;
}
```
画面13：
```java
@Override
public String createStoreQRCode(QRCodeDto qrCodeDto) throws BusinessException {
    //将参数生成一个支付入口（url），需要将传入的参数转换成json，用base64编码
    String url = null;
    return url;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
标题：闪聚支付 第3章讲义-C扫B支付
子标题：1 需求分析
子标题：1.1 C扫B的概念
内容：
C扫B，即顾客(Customer)扫描商户(Business)提供的二维码来完成支付。下图是支付宝提供的C扫B业务流程：
1、商家出示付款二维码。
2、客户打开支付宝或微信的扫一扫，扫描二维码。
3、确认支付，完成支付。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

