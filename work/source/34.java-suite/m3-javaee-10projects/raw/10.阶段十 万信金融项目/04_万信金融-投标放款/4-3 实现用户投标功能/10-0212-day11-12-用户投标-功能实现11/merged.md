# day11-12-用户投标-功能实现11

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-12-用户投标-功能实现11_【海量资源尽在 666java.com】.mp4
- 时长 10分41秒（音频 641s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们主要是把保存交易记录这个功能实现了一下当然这里边主要是涉及到要实现什么呀对实现密等性那整个这块搞定之后咱接下来继续往下推进接下来是要对数据进行签名然后呢再发到银行存款系统那边那其实接下来这两部代码我们前面在开户啊包括什么呀发标是不是其实都实现过这个代码而且基本上都是一模一样的套路是不是
[00:32] 那签名怎么签呢是不是先把这个数据给他转成什么格式对先转换成json格式啊那接下来就是调用json.他的什么方法tojsonstream然后呢先对这个参数做一个转换转换之后呢我们这边呢就用一个字符串来接收就叫什么呀jsonstream吧
[01:05] 然后我们转成JSON之后还不行我们需要为了传输方便我们需要对它进行什么BASE64编码是不是那咱接下来调咱的工具类哪工具类叫ENCENC什么CRY是吧ENCRY YouTube第二它的哪个方法就是Encode对不对别调错了一个是Decoder一个是Encode
[01:33] 这俩方正好相反我们应该这次调呢是什么呀Anchor的对不对然后呢把上面这个什么呀Jayson Truck给他扔进去进行base64的一个什么呀编码然后呢编码后的结果呢我们再声明一个编量REQDATA接收一下接收完之后呢我们接下来是不是就可以往什么呀银行存款系统那边进行发送
[02:02] 那有的学生说老师这这里边好像还没签名呢吗对就是没签名吧你忘了咱以前是连签名带发送带这个什么呀处理返回后的这个结果全部一股脑封装到是不是哪个方法里边来有一个方法叫sendhttpget你还有印象吗咱现在也是要用这个方法这个方法也是通用的以后你就记住一点凡是你要通过这个存款代理服务跟谁呀
[02:30] 跟银行那边打交道的话全部都是要通过这个方案不管你是什么业务都是要通过这个方案这个方案是通用的所以你再回过这个方案你看这个方案里边我们在这是不是就会对这个数据进行什么对进行签名你看就是这一块当然了这个签名你在这看不到因为咱当时第一次用这个方法的时候我们跟大家说过它是不是有一个拦截器在这个拦截器当中你发请求之前它自动进行签名
[02:58] 使用起来非常方便然后呢下面这一块就是开始往银行那边发数据发完数据之后这边就是开始进行根据结果进行什么呀对后续的一些处理了所以说其实我们这块准备好这些数据之后接下来就是开始调这个什么呀send http get发开始发请求那发请求的时候你看看他这里边是不是要一个什么呀请求地址对吧这个请求地址大家应该还有印象
[03:24] 这个银行那边啊就是银行存款系统那个请求地址我们是得拼接一下我们一般都是先调用configure Service的get什么呀depositurl这个方法导到他的这个基本访问路径然后呢我们本次呃要请求的银行那边的这个接口呢是叫-ser vse前面让大家查过那个呃银行存款系统那个接口文档啊你可以查一下我们应该具体是往这干什么呀
[03:54] 对发请求了啊所以我们拼借一个我们要请求到这个地址然后把它先存起来一会就要用url那接下来的话我们就直接调用这个send htget方法啊然后第一个参数是啥对第一个参数就是呃就是什么呀第一个参数就是我们的Service name啊其实就是相当于这个业务的类型啊Service name业务类型就是你是你在这是要进行什么呀
[04:27] 发标还是开户还是投标对不对一个业务的名字那我们这样进行了是不是就是什么我们在进行的是投标投标的一个一个预处理对不对这个值呢我们要跟讲义保持一致不能随便乱写就这个值那我连同后边一块考过来啊要的几个数据是因为这这块咱之前都写过这个代码少一个引号
[04:59] 第一个参数我们刚才解释过第二个参数不就是这个具体的请求地址我们在这做了一个拼接对吧第三个参数就是什么呀第三个参数你往上看呗不就是咱那个那个对传过来的数据做的一个一个一些处理嘛对不对最后一个参数不就是咱查出来的这个什么呀交易记录嘛我们把这个东西呢全部扔给谁啊send to http get方案里啊这里这个方案里边呢就会做后续的一些处理这里边是不是要准备四大参数啊这一块东西你要是时间长忘了的话你可以看看这个
[05:31] 我们前面有个银行存款系统接口说明了你看是不是这里边不是那四大参数吗然后我们现在调呢这个接口是这个什么预预授权处理吧这里边刚才咱给的指示就这个值吗里边有详细的一些介绍当然这块电话其实咱们前面在开户呀包括发票的时候也是刚写过了然后我们调完这个方案之后呢
[05:58] 这个方案是不是有返回的有值对不对所以说我们接下来电话完之后要接收这个值或者说你直接也可以干什么返回我们直接就返回了也不再声明电量接收再返回了直接就return就ok了这么一return之后的话我们右层的代码基本上也就写完了这块代码你虽然看着好像没多少行但是其实整个下来代码挺多的你比如说密等性这块代码是不是都封装到这个方案里边
[06:28] 然后呢这个签名啊发送这个数据到银行存款系统啊以及接收它的反而结果做后续处理这些代码全部封装到什么呀SyndicATP GET方案里边因此呢这两个方案大家要注意以后啊这两个方案就是通用的方法凡是通过存款代理服务跟什么呀银行系统那边打交道的话基本上都要用到这两个方法这是大家需要简单总结一下那么要层这块代码咱写完之后咱既然顺手就把control的代码给它
[06:58] 完善一下咱找一找这个Controller就这个Controller代码对不对你看咱当时这是一个空时线那这块代码跟之前也是一样的非常简单我们主要就是调用一下什么业务层的这个方法就行了deposter recorder Service点点什么点哪个方法这个方法然后我们把这个参数给它扔过去就行了业务层那边咱代码是不是刚写完对吧然后它处理完之后我们就进行什么
[07:31] 对进行返回就行了那我先接受一下它这个反而是吧这个反而是类型大家看一下还是有点长的咱考一下吧卡死了我们把这几是吧给它考过来我们先接收一下啊depository这名字咋这么长啊depositoryresponse
[08:07] 然后接下来呢我们可不能直接返回这个depository response这个套路大家应该都熟悉了我们应该怎么着啊我们是不是还要从这里边把我们想要的数据取出来然后封装成什么呀对rest response然后返回对不对那考虑到呢这种需求啊或者说这种代码我们以后可能会经常用而且呢这也是通用的一个一个一个需求对不对所以我们准备把这个什么呀
[08:38] 从这里边取数据然后封装成rest response这块代码我们专门封装成一个方法那以后使用起来的时候是不是会更加方便一些这个代码比较简单我就不再给大家编写了大家看一下讲义吧好我们直接就粘到这了这个代码都是咱以前写过的只不过就是封装了一下单独抽到一个方法里边来而已来大家看一下这个代码吧
[09:21] 好大家看一下我们这个方案无非是就传进来这么一个一个一个对象对吧传进来之后呢我们从这里边取这个返回的数据啊还有什么呀取这个什么消息的内容啊具体的数据内容啊对不对这这其实是应该是一个那个状态码这是这个数据对不对取出来之后呢我们分别调setter方法封装到这个什么呀rest response里边然后返回这个什么呀rest response所以说呢有了这个方案之后我们以后
[09:51] 凡是碰到类似这种情况我们是都可以直接调用这个方法就完成了这个封装以及干什么呀返回给什么呀前端页面是不是那我们在这怎么写你这直接调用了呗直接return然后调用这个方法然后把上面这个什么对象给他拿过来就OK了这是扛出来这个代码了我们也完善了一下就是大家注意一点我们这做了一个一个封装抽取以后
[10:21] 使用起来会更方便一些这是目前咱们就把什么功能全部搞定了对用户投标功能全部搞定了大家看一下这个图我们这里边是不是一共涉及到两个接口一个接口4一个什么接口5目前全部搞定咱一会就要进行功能测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个用户预交易服务的实现，包括控制器层接收请求、服务层处理业务逻辑（含数据加密与发送至存管系统）、以及相关的系统架构流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 代码文件：`DepositoryRecordServiceImpl.java`
- 代码内容：
```java
@Override
public DepositoryResponseDTO DepositoryBaseResponse userAutoPreTransaction(UserAutoPreTransactionRequest userAutoPreTransactionRequest) {
    DepositoryRecord depositoryRecord = new DepositoryRecord(userAutoPreTransactionRequest.getRequestNo(), userAutoPreTransactionRequest.getPlatformNo(), userAutoPreTransactionRequest.getReqData());
    if (responseDTO != null) {
        return responseDTO;
    }
    depositoryRecord = getEntityByRequestNo(userAutoPreTransactionRequest.getRequestNo());
    //2. 签名
    //3. 发送数据到银行存管系统
}
private DepositoryResponseDTO DepositoryBaseResponse sendEntityGet(
        String serviceName, String url, String reqData,
        DepositoryRecord depositoryRecord,
        String platformNo, String signature) {
```
画面 2:
- 代码文件：`DepositoryRecordServiceImpl.java`
- 代码内容：
```java
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object = new Object();
Object object =

