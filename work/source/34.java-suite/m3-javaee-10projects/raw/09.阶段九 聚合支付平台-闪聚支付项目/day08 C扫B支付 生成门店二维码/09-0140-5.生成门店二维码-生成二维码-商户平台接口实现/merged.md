# 5.生成门店二维码-生成二维码-商户平台接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\5.生成门店二维码-生成二维码-商户平台接口实现【海量资源尽在 666java.com】.mp4
- 时长 10分57秒（音频 657s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下边呢我们就继续来写生成二维码刚才我们完成了生成二维码的URL下边我们在商户平台应用来生成二维码的图片那么好这里边我们首先需要配置一些信息因为我们知道商户平台应用肯定是要调交易服务的这个接口来生成二维码对吧他调交易服务是不是拿到二维码的地址啊然后呢再生成图片那么这里边你也看到了交易服务需要传传很多的参数看见了吗所以这里边呢
[00:28] 有两个参数需要注意一个是标题一个是定单描述所以看我们的讲义啊我们是需要在商户平台应用当中啊我们来把这个标题给它配置一下老师为啥配置标题呢因为这个标题不可能写死吧
[00:47] 就是不同的商户进来你扫不同商户的门店的这个二维码它会显示的效果是啥呢比如你写你扫一个比如说这个某某饭店的它的这个二维码是吧那它就会显示标题叫某某饭店商品然后呢下面的内容叫像某某饭店付款你大概理解这意思吧所以这个参数你不能写死是有一定规则的好了那这个是不是就写好了写好了之后呢接下来
[01:16] 我们就开始来写我们的什么样这个方法了那这个方法呢其实就是一个http的接口然后我们请求三层二维码首先传进去是应用ID对吧还有门店ID然后呢这里头的内容各位我们来看啊我们先把这个接口把它定义出来这是三户平台应用嘛很显然我们找到三户平台应用的工程来里边写往里边写啊
[01:45] 那这里边呢它要暴露一个http的接口很显然我们是不是需要在Controller当中来写这个方法呀那这里边呢我们是生成一个什么叫做二维码对吧生成二维码那这里边是不是有一个叫store Controller啊是不是就是门店列表查询是吧当然你也可以在app这里边去写啊在app也行在这个这个门店里边也行都行好我们在门店上
[02:14] 那我就写那这里面呢需要传餐嘛传哪个餐一个是我们说的store id这个store id要注意它是一个浪形没错吧好还有一个是门店的id门店的idstore id就是门店的id吧那还有啥应用的id吧因为你生产二维码一个门店一个应用都需要是不是啊
[02:41] 那你最终返回的这个二维码我问你是不是一个图片当初我们测试过它就是一个图片的一个base64编码所以它是个串大家看到吗这就是我们的接口就成了所以它是两个参数两个参数一个应用一个是门店对吧好这个过程我就不再写了贴进去大家看一下这是
[03:08] Sweiger的注解我们写了很多次了这个是URL这个URL你一定不要手翘啊拷贝因为这个URL前端都已经写死掉它了所以你要少一个字母多一个字母就可能前五端连条失败了那这里面你可以看到APP ID和STOID是不是就通过pass传递所以在这儿是不是有pass对吧好了那下面呢我们来看这里面要做什么事啊首先你最终要掉谁你要搞清楚对吧你掉谁啊
[03:34] 你是不是要调我们说的这个交易服务对吧交易服务那你调交易服务刚才我们交易服务是不是写了一个接口叫做获取什么二维码的URL吧所以你调这个而调这个接口它需要传一个什么一个参数这个参数呢是需要你在这个商户的这个
[04:03] Service当中我们去对把它完善一下的看好啊在这儿也就是在这儿呢我们去准备这个数据嘛准备数据准备数据的话这里边我们是需要我们看一下啊具体需要什么参数啊那我们点开看一下这里边需要商户ID还有这几个数据是吧好那我们想办法来拿到吧商户的ID就从这儿拿我们还是获取商户的ID
[04:32] 获取商户ID你是最终商户不知道登录我们从这个security youtube当中来拿对这个商户ID是不是就搞定搞定了我们就可以把它放进去对吧好那还有什么呢你看这是门店的ID门店ID你就直接往里面放看一下set下面门店ID好然后还有什么呢叫做APP ID好APP IDOK了吧还有两个参数
[05:05] 还有两个参数这两个参数是不是就是我们说的标题我们说的内容啊那标题和内容刚才我们在讲义上看到它是不是需要在这个Necros里面把它配置了看见了吗Necros的配置它是这么一个字幕串我们是不是需要通过往里边怎么弄啊咱先把这个数据咱先把这个数据先拿到哪里啊先拿到我们的这个看好啊拿到我们这个control的方法当中我们呢把它注进去看好
[05:36] 怎么注入啊那这里面呢就是Value注解然后呢这是散具配C to B.t这是不是就是拿到了一个标题对吧好那么另外一个我们再看另外一个是不是就是body啊另外一个body的话这里面也是这么的看懂了吗好
[06:02] 那OK那我现在就拿到了但是这个串呢但这个串你要注意这个串啊其实你要它是这么一个模样看见了吧这个模样的话那你说我们是不是得把这个百分号S这里头传东西了怎么传看好啊标题的话我们用这个也原来我们应该用过Stream Format然后呢在这个里边百分号S我们用我们用
[06:33] 哪个商户进来的我们就用商户名称替代比如说是某某餐厅那就是某某餐厅商品向某某餐厅付款懂吧所以这里边呢我们要用商户的名称对用用商户的名称来替换百分号S懂吧那怎么办怎么办我怎么拿到商户的名称呢那我就需要在这儿用商户的Service来查一下
[07:03] 我是不是就拿到了这个商户的信息了对不对那我现在拿到了这个商户的信息了我是不是就可以在这儿去get出来这个商户的名称啊这是不是就是我们说的这个什么subject对不对这是我们说的这个subject最终我们格式化后的这个什么一个串吧那么同样的道理内容这一块呢
[07:32] 这个这个定档的内容啊你也这么做这个呢只不过就换成body对吧他呢就得到一个body最后格式化的后的串假如某某餐厅进来哎他的这个页面上会显示某某餐厅商品你是要C扫码支付吗对吧好到这儿我们是不是就可以把这个参数给他放进去了对吧那这样的话我们是不是就把参数给整理齐了呀
[08:00] 那现在我们说参数齐了之后下一步要做啥呢是不是就要调用这个接口交易服务接口是不是就拿到了一个URL对吧这个URL是不是就我们说的怎么样一个具体的地址嘛就这地址是吧拿到这个地址我们是不是要调用工具类断码三层二维码的图片没错吧那三层二维码的图片这里边呢我们来看啊调用工具类那就是QR
[08:30] 有一个Util是吧然后呢你有一个好那下面我们说它就有一个方法叫是吧Create你把这个URL这是一个URL对吧你把它传进去最终这图片呢比如说我们是宽高都是200我问你这过程我是不是就搞定对不对那么我搞定了这个东西之后呢这个地址是不是就是我们说的什么二维码
[08:59] 图片的base64编码没错吧那你最后是不是返回的就是这个东西啊所以我们就return就完事了这就是生成了一个什么二维码的图片整个方法大家清楚了吧来总结一下啊首先当这个前端呢一点生成二维码这个链接
[09:28] 那这个生成二维码的链接它就会干嘛它就会把门店的ID和应用的ID传到我们说的这个接口中通过这个pass传传进来之后它就开始去整理这些参数这些参数将来就是二维码URL里面所需要的参数懂吧需要的参数那么
[09:54] 看好这里边整理的这些参数当中应该还落了一个因为这个我们看一下我们看讲义整理的这个参数当中有一个参数要注意有一个参数是啥呢注意看我们可以看一下这个交易交易服务的接口看点进去你看他需要他真正需要的参数你看是这么多看见吗是什么是不是六个六个
[10:18] 而商户平台应用给他传递的参数是传了五个因为其中有一个叫写死的一个叫散具C扫币的一个什么服务类型的编码是交易服务写死了所以商户平台应用只给他传五个参数就完事了然后呢他就开始调用交易服务生成一个URL然后把这个URL调用二维码工具类生成图片然后图片最终生成的是一个图片的贝斯64编码然后反馈这就是整个生成
[10:47] 这个商户应用门店的什么对二维码这个方法我们就完成开发了稍后呢我们进行测试好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲商户平台应用生成二维码的接口实现，包括配置参数、控制器编写、服务层逻辑和系统交互流程。

2) 按时间顺序列出每张画面的要点：
画面1: 展示Nacos配置中心界面，配置ID为“merchant-application.yaml”，Group为“SHANJUPAY_GROUP”，配置内容为YAML格式，内容为：
```yaml
c2b:
  subject: "商户商品"
```
画面2: 展示Nacos配置中心界面，配置ID为“merchant-application.yaml”，Group为“SHANJUPAY_GROUP”，配置内容为空。
画面3: 展示IDE中“StoreController.java”文件，定义了StoreDTO类，包含merchantId、appId、storeId、subject字段。
画面4: 展示IDE中“StoreController.java”文件，定义了@GetMapping("/my/stores/merchants/page")方法，用于分页查询商户门店列表。
画面5: 展示IDE中“StoreController.java”文件，定义了@GetMapping("/my/apps/{appId}/stores/{storeId}/app-store-qrcode")方法，用于生成商户门店二维码。
画面6: 展示IDE中“TransactionService.java”文件，定义了createStoreQrcode方法，用于生成二维码。
画面7: 展示IDE中“StoreController.java”文件，定义了createScanStoreQCode方法，用于生成二维码。
画面8: 展示IDE中“StoreController.java”文件，定义了@GetMapping("/my/stores/merchants/page")方法，用于分页查询商户门店列表。
画面9: 展示IDE中“StoreController.java”文件，定义了@GetMapping("/my/stores/merchants/page")方法，用于分页查询商户门店列表。
画面10: 展示IDE中“StoreController.java”文件，定义了createScanStoreQCode方法，用于生成二维码。
画面11: 展示IDE中“StoreController.java”文件，定义了createScanStoreQCode方法，用于生成二维码。
画面12: 展示PPT页面，标题为“3.4 生成二维码”，子标题为“3.4.1 系统交互流程”，图示为商户平台应用生成二维码的系统交互流程图。
画面13: 屏幕空白。
画面14: 展示PPT页面，标题为“3.4 生成二维码”，子标题为“3.4.3.1 接口实现”，图示为商户平台应用生成二维码的接口实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```yaml
c2b:
  subject: "商户商品"
```
画面5:
```java
@GetMapping("/my/apps/{appId}/stores/{storeId}/app-store-qrcode")
public String createScanStoreQCode(Long storeId, String appId) throws BusinessException {
    //商户ID
    Long merchantId = SecurityUtil.getMerchantId();
    //生成二维码链接
    QrCodeDto qrCodeDto = new QrCodeDto();
    qrCodeDto.setMerchantId(merchantId);
    qrCodeDto.setAppId(appId);
    qrCodeDto.setStoreId(storeId);
    //获取二维码服务
    String storeQrCodeUrl = transactionService.createStoreQrcode(qrCodeDto);
    //返回二维码链接
    return storeQrCodeUrl;
}
```
画面6:
```java
@Override
public String createStoreQrcode(QrCodeDto qrCodeDto) throws BusinessException {
    //校验商户信息
    verifyAppId(qrCodeDto.getMerchantId(), qrCodeDto.getAppId(), qrCodeDto.getStoreId());
    //获取二维码服务
    PayOrderDTO payOrderDTO = new PayOrderDTO();
    payOrderDTO.setMerchantId(qrCodeDto.getMerchantId());
    payOrderDTO.setAppId(qrCodeDto.getAppId());
    payOrderDTO.setStoreId(qrCodeDto.getStoreId());
    payOrderDTO.setSubject(qrCodeDto.getSubject());
    payOrderDTO.setChannel("shanju_c2b");
    //生成二维码
    String qrCodeUrl = qrCodeUtil.createQrCode(payOrderDTO, 200, 200);
    return qrCodeUrl;
}
```
画面7:
```java
@GetMapping("/my/apps/{appId}/stores/{storeId}/app-store-qrcode")
public String createScanStoreQCode(Long storeId, String appId) throws BusinessException {
    //商户ID
    Long merchantId = SecurityUtil.getMerchantId();
    //生成二维码链接
    QrCodeDto qrCodeDto = new QrCodeDto();
    qrCodeDto.setMerchantId(merchantId);
    qrCodeDto.setAppId(appId);
    qrCodeDto.setStoreId(storeId);
    //获取二维码服务
    String storeQrCodeUrl = transactionService.createStoreQrcode(qrCodeDto);
    //返回二维码链接
    return storeQrCodeUrl;
}
```
画面10:
```java
@GetMapping("/my/apps/{appId}/stores/{storeId}/app-store-qrcode")
public String createScanStoreQCode(Long storeId, String appId) throws BusinessException {
    //商户ID
    Long merchantId = SecurityUtil.getMerchantId();
    //生成二维码链接
    QrCodeDto qrCodeDto = new QrCodeDto();
    qrCodeDto.setMerchantId(merchantId);
    qrCodeDto.setAppId(appId);
    qrCodeDto.setStoreId(storeId);
    //获取二维码服务
    String storeQrCodeUrl = transactionService.createStoreQrcode(qrCodeDto);
    //返回二维码链接
    return storeQrCodeUrl;
}
```
画面11:
```java
@GetMapping("/my/apps/{appId}/stores/{storeId}/app-store-qrcode")
public String createScanStoreQCode(Long storeId, String appId) throws BusinessException {
    //商户ID
    Long merchantId = SecurityUtil.getMerchantId();
    //生成二维码链接
    QrCodeDto qrCodeDto = new QrCodeDto();
    qrCodeDto.setMerchantId(merchantId);
    qrCodeDto.setAppId(appId);
    qrCodeDto.setStoreId(storeId);
    //获取二维码服务
    String storeQrCodeUrl = transactionService.createStoreQrcode(qrCodeDto);
    //返回二维码链接
    return storeQrCodeUrl;
}
```
画面14:
```java
@GetMapping("/my/apps/{appId}/stores/{storeId}/app-store-qrcode")
public String createScanStoreQCode(Long storeId, String appId) throws BusinessException {
    //商户ID
    Long merchantId = SecurityUtil.getMerchantId();
    //生成二维码链接
    QrCodeDto qrCodeDto = new QrCodeDto();
    qrCodeDto.setMerchantId(merchantId);
    qrCodeDto.setAppId(appId);
    qrCodeDto.setStoreId(storeId);
    //获取二维码服务
    String storeQrCodeUrl = transactionService.createStoreQrcode(qrCodeDto);
    //返回二维码链接
    return storeQrCodeUrl;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面12:
标题：3.4 生成二维码
子标题：3.4.1 系统交互流程
图示：系统交互流程图，包含“商户”、“商户平台应用”、“交易服务”、“支付渠道代理服务”、“第三方支付”五个角色，箭头从“商户”指向“商户平台应用”，从“商户平台应用”指向“交易服务”，从“交易服务”指向“支付渠道代理服务”，从“支付渠道代理服务”指向“第三方支付”，从“第三方支付”指向“商户平台应用”，从“商户平台应用”指向“商户”。

5) 不要评价画面美观，不要输出与课程无关的内容。

