# day06-14-开户第一阶段-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-14-开户第一阶段-功能测试_【海量资源尽在 666java.com】.mp4
- 时长 13分27秒（音频 806s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好截止到目前呢我们已经把开户功能当中的第一阶段啊就是生成开户数据这块所有的代码全部编写完了编写完毕之后呢咱接下来就要进行对功能测试就这块功能测功能测试这块你看我简单里边基本上没有写任何东西因为咱这个测试在之前已经进行过很多次了这个整个套路啊或者需要注意的地方大家应该心里都清楚了
[00:31] 那我们这个测试呢目前还是通过谁啊Postman进行了那么相关的准备工作呢我提前已经做好了为了节省时间比如说第一个准备工作就是你要想一想都需要启动哪些什么呀微服那这边的话大家看一下这边这套东西全部都得启动为什么呢因为我们这次测试呢它会有点麻烦麻烦到哪了呢因为在开入功能之前咱们的注册呀登录这些事不全部实现了网关呢包括UA什么全部都有对不对
[01:02] 那你现在在测试开户功能的时候那你就得干什么呀得登录登录完之后呢你在发请求的时候就得带着什么呀令牌要不然你这个这个像开户这种功能你根本就无法进行测试所以说呢这几个微服务全部都要启动这我都已经全部启动过了那当然Apollo也要启动这不用说了还有什么要启动还有哪些需要启动别的应该就没啥了吧对不对Apollo然后这一堆微服务全部启动
[01:35] 就OK了启动完之后呢我们怎么测试呢那我们就打开Puzzleman打开Puzzleman之后呢Puzzleman里边这个准备工作我也做过就是这个新建一个请求填一下这个地址还有参数这准备工作我也全部做完了做完之后呢咱一起看一下你看我们现在要想这个测试第一阶段生成开入数据我们要往哪发请求啊大家看这个图往哪发请求是不是往用户中心
[02:06] 用中心呢我们找到用中心我们找到那个Controller你在测试的时候也是如此啊结合那个时序图然后找一找代码就这个control control这了可能这里边咱是不是写了一个方法叫create control嘛然后这里边是不是配了一个防御路径my consumers对不对那你就往这发请求啊然后呢你看这是不是post的请求对不对那你就在postman里面哎这选择post然后呢这呢开始写这个什么呀请求路径
[02:36] 然后呢你注意看我们这儿是过什么过网关的啊一定要过网关53010是网关的地址因为我们前面说过嘛前端发的所有的请求都要过什么呀经过网关嘛从我们这儿直接写的就是网关的地址将来网关是不是会转发请求到这里然后呢就是传哪些数据具体传哪些数据你是不是还得看代码那我们这里边呢你要看这个consumer request你看这里边
[03:04] 就是什么用户名啊真实姓名啊身份证号啊银行别什么银行编码银行卡号手机号等挑几个必要的我们给他加上去就行你看我这里边挑哪几个啊在body里边我们还是以Jason的格式传输剧的我这边挑了一个他在这个什么呀用户的真实姓名就身份证号那个姓名还有什么呀这是银行卡号这是那个什么银行的编号这个是什么呀这个是银行卡号上面是身份证号
[03:34] ID那么这是他的手机号手机号手机号我们这个手机号这个这个这个这个你不能随便按一下前面你随便写无所谓这个手机号你最好是从表里边你的你的登录这里边都有啥咱用11吧你看咱这儿耳的命就是咱以前登录视频耳的命登录的吧他是1111那我们
[04:02] 所以你在测试的时候也要查这个东西啊这个数据有的数据不是你随便乱写的啊这得写悠悠这是我传输的数据然后光传这些数据还不行这些数据我们将来是不是封装到什么地方是封装到这儿那光传这个还不行我们前面说我们是不是这个登录啊包括认证拦截功能是不是全部都实现过那这个时候呢你前端发请求到我们的这个后端微幅的时候就必须携带什么呀令牌
[04:29] 你要是不携带令牌大家应该有印象是网关那一块就就就过不了是不是网关都过不了那你的请求肯定也到不了这个地方所以说呢我们这次啊你在测试这个功能的时候你看我这还带着什么东西令牌呢带了一个令牌当然这个令牌你得先登录一下登录成功之后获取令牌令牌粘到这然后你再进行测试就行所以这是这套东西我先给你介绍一下因为我这个相当于这个准备工作我已经做过那咱接下来就进行测试
[04:59] 那测试的时候你得先进行什么呀我们说得先进行登录啊你看咱以前这个登录功能是不是都测试过了对不对你点击啊点一下给它打开这里边这些东西你就不用动嘛咱以前这个测试过了你直接点击什么呀send然后你看我们这是不是就得到了一个新的一个访问令牌给它粘一下这个时候一定要细心啊多一个字少一个字都不行啊Ctrl C然后呢粘到这粘到这啊粘完粘完之后呢你就点击send
[05:30] 开始这个测试这个什么呀生成开入数据这个功能好我们点一个send好这边已经报错了未知错误那未知错误的话这是咱封装的这个提示信息对吧咱去consumer里边找一找具体的错误提示他说这个什么呀什么我一哭是吧你这哭吗他说这个手机号哎你看他这个你看这啊这什么手机号手机号获取到了吗
[06:06] 手机号的确获取到了是吧手机号是获取到了然后呢你看往下走的时候他抱了空往下走这是哪这是不是查那个谁啊查卡号的他说这个卡号为空对吧卡号为空卡号银行卡号银行卡号咱传了呀是不是在铺子里面传了吗咱看一下cut number6个8了对不对传了呀那你看到这说这个参数为空那这为空
[06:37] 那按说那那有可能这里边就是空了呀是不是那没有接收到这个数据吗我们再看一下这个代码哦大家有的同学估计当时写的按门的时候就看出来这儿你看这儿缺什么东西哎呀这很容易忘了以前也忘了缺什么东西是不是缺个注解吧叫at什么呀对request body吗这个忘了啊request body这我不用解释吧因为前端你也看到了
[07:09] 他传回来是不是杰森给人的数据我们在这要通过这个注解给他封装成这个对象这刚才这少加了少加的话你想你虽然普通卖里边传这个什么呀这个什么银行卡号但是这没有加这个注解其实他接受不到我这个错误有点低级了这个当时可能忘记做这个事了我们把扛随望是不是得重启一下这个我们要重启一下稍等片刻好这边已经重启完了重启完之后呢咱接下来再次进行测试
[07:57] 我就直接进行send了啊走又报错了这真是一步一坑啊是不是这边又报了一个什么呀空这个空是什么空呢这个空哎这次你看我们这个卡号是不是就接收到了吧六六个八嘛对不对但他接下来又报空了那我们大概确定一下这个错误发生的位置你看这这个查银行卡号这个代码是在哪查银行卡号这个代码应该是在右层了啊
[08:27] 你看他把这个数据是扔到业务层了扔到业务层就是这块带你看查手机号这个搜狗语句是不是都已经出来没有问题你看这对不对查手机号然后下面这是不是查这个银行卡是不是已经被绑定了你看这个查询搜狗语句也出来了但是他做完之后就报空人了忘了一空你看零偷偷零表示这个没查出来这肯定没查出来因为那个银行卡我随便写的他肯定查不出来
[08:58] 但是接下来就爆了一个空接下来爆空呢应该就是这块爆空对不对这块代码这块代码爆空那是谁为空啊那大家看一下由于我这个银行卡号是不存在随便写的所以说这个对象一定为空是吧但这这个对于逻辑来说它是空的也是正常的那我们往下走这是不等于空然后哦那这会爆空你看我们刚才说了这个银行卡号不存在它就是空空的话你看这
[09:26] 空对象去调用方法那不就把我控制人了吗是不是那这个地方咱当时这是条件是判断啥的呀咱这是判断这个他传过来这个银行卡我们要查一查他是不是已经被绑定被使用了是不是这不等于no证明是这个银行卡已经存在了这个条件咱写反了这应该是并且不是或者这应该是并且
[09:56] 什么意思呢怎么判断这个银行卡有没有被绑定呢我们得通过两个条件同时满足一个是这个银行卡必须已经存在就是它不为闹同时呢它的这个银行卡的这个状态必须是那个已经同步的状态你看这个status in它是这个什么呀你点进去看看是不是表示已经同步了对不对已经同步了什么意思呢这给大家解释一下如果银行卡已经存在了但是也不能表示它就已经被绑定了
[10:27] 他有可能就是说用户某个用户在开户的时候只走了第一阶段他就又后悔了又又不想开户但这个时候呢有可能他的银行卡信息已经干什么呀在我们的表里边存在了但是实际上他并没有进行绑定就是在银行那边并没有保存他的信息并没有进行绑定真的被使用所以说你只是靠他呃这个银行卡存在不存在就下这个结论不行
[10:53] 必须是两个条件一个是银行卡已经存在而且它这个状态已经是同步的同步的意思就是银行那边这个数据也已经存在已经保存了说这这个条件应该是两天应该是并且的关系啊不能是或者是并且这当时应该是写法呃然后呢那我们接下来还得再重启一下consumer再重启这都是一些细节问题咱们再重启然后再进行测试好我们这边马上就要启动完毕了
[11:38] 把您启动啊启动完之后我们再次进行测试啊还是点击这儿的哎这次这是这是成功了吗是不是是成功了啊你看看我们返回的这个数据里边你看这些数据是不是咱那个啥是不是就是存款代理服务这边签名完之后返回的数据吧你看这里边数据当时咱说的咱可以找一找代码对应一下了这个代码啊
[12:09] 咱这个代码应该是不是去存管代理服务这边去找去这边找呃应该是业务层业务层啊业务层的对这块地方也不是这上面你看这是不是那个服务的类型吗叫个人开户吗你看反正的数据里面有有吧然后这是咱平台的那个编号吗就这个platform number然后还有这个这是咱的那个那个那个数据吗
[12:41] IQDATE就是它嘛这个只不过是进行了base64的一个什么呀一个一个编码所以你看就变成这个样子然后这个就是那个什么呀签名啊这种那个签名就这个它也进行了这个编码就变成这个样子然后最后返回来还有这个谁呀这个这个第二阶段我们请求开货的时候发送的那个地址嘛这个完整的一个地址这是银行存款服务那边的一个地址
[13:12] 将来第二阶段就是往这儿就是前端就往这儿发请求来请求开户所以你看当我们看到这个数据的时候就证明咱目前就是开户功能的第一阶段这个代码就测试通过

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在用户中心服务中实现“生成开户数据”的接口，包括在Controller中定义接口、在Service中实现业务逻辑、以及通过Postman进行接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，明确当前任务是“3.3.1 需求分析”和“3.3.2 接口定义”，并指出需要在“warxinp2p-ap”工程的ConsumerAPI接口中新增createConsumer方法。
画面2：在IDEA中定位到ConsumerController类，显示其继承自ConsumerAPI接口，并包含一个测试方法“@ApiOperation("Hello")”。
画面3：在Postman中准备调用“开户生成开户数据”接口，Body中填写了测试数据，包括“name”、“idCard”、“bankCode”、“certificates”和“mobile”。
画面4：在Postman中切换到Query Parameters，设置“access_token”参数用于认证。
画面5：在IDEA中查看ConsumerController的代码，高亮显示了“@ApiOperation("生成开户请求数据")”注解和“createConsumer”方法的定义。
画面6：在IDEA中查看ConsumerController代码，高亮显示了“@ApiImplicitParam”注解，用于定义“consumerRequest”参数。
画面7：在IDEA中查看ConsumerController代码，高亮显示了“@PostMapping”注解和“createConsumer”方法的实现，其中调用了“consumerService.createConsumer(consumerRequest)”。
画面8：在IDEA中查看ConsumerController代码，高亮显示了“@ApiOperation("过网关保护资源，进行认证拦截测试")”注解。
画面9：在IDEA中查看ConsumerServiceImpl类，高亮显示了“createConsumer”方法的实现，其中包含对用户是否已开户的判断和对银行卡状态的判断。
画面10：在IDEA中查看ConsumerServiceImpl类，高亮显示了“if (bankCardDTO == null || bankCardDTO.getStatus() == StatusCode.STATUS_IN.getCode())”条件判断。
画面11：在IDEA中查看ConsumerServiceImpl类，高亮显示了“consumerRequest.setId(consumerDTO.getId())”和“consumerRequest.setMobile(CodeUtil.getMobileCode())”代码。
画面12：在Postman中发送请求，成功返回了响应，显示“code: 0”和“msg: “成功””。
画面13：展示多个开发工具窗口，包括IDEA、Postman、SQLyog、ApolloPortal等，说明这是一个多模块、多服务的分布式系统。
画面14：在Postman中查看成功请求的响应，显示了“code: 0”、“msg: “成功””和“result”对象，其中包含“certificates”、“platformNo”、“signature”和“url”等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 生成开户请求数据
 * @param consumerRequest 开户信息
 * @return
 */
RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);
```

画面5：
```java
@ApiOperation("生成开户请求数据")
@ApiImplicitParam(name = "consumerRequest", value = "开户信息", required = true, dataType = "ConsumerRequest")
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest) {
```

画面6：
```java
@ApiOperation("生成开户请求数据")
@ApiImplicitParam(name = "consumerRequest", value = "开户信息", required = true, dataType = "ConsumerRequest")
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest) {
```

画面7：
```java
@ApiOperation("生成开户请求数据")
@ApiImplicitParam(name = "consumerRequest", value = "开户信息", required = true, dataType = "ConsumerRequest")
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest) {
    consumerRequest.setMobile(SecurityUtil.getUser().getMobile());
    return consumerService.createConsumer(consumerRequest);
}
```

画面9：
```java
@Override
@Transactional
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    // 判断该交易的执行行是否已开户
    if (ConsumerDTO consumerDTO = bankCardService.getBankCard(consumerRequest.getMobile())) {
        throw new BusinessException(ConsumerErrorCode.E_140105);
    }

    // 判断提交过来的银行卡是否已绑定
    BankCardDTO bankCardDTO = bankCardService.getBankCard(consumerRequest.getBankNumber());
    if (bankCardDTO == null || bankCardDTO.getStatus() == StatusCode.STATUS_IN.getCode()) {
        throw new BusinessException(ConsumerErrorCode.E_140151);
    }
```

画面10：
```java
// 判断提交过来的银行卡是否已绑定
BankCardDTO bankCardDTO = bankCardService.getBankCard(consumerRequest.getBankNumber());
if (bankCardDTO == null || bankCardDTO.getStatus() == StatusCode.STATUS_IN.getCode()) {
    throw new BusinessException(ConsumerErrorCode.E_140151);
}
```

画面11：
```java
// 更新用户的ID
consumerRequest.setId(consumerDTO.getId());
// 产生请求流水号和商户号
consumerRequest.setMobile(CodeUtil.getMobileCode());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3.3 第一阶段: 生成开户数据”，子标题为“3.3.1 需求分析”和“3.3.2 接口定义”。
画面13：展示了一个多窗口的开发环境，包括IDEA、Postman、SQLyog、ApolloPortal等，但未提供具体的架构图或流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

