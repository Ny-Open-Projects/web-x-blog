# day06-19-开户第三阶段-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-19-开户第三阶段-功能实现1_【海量资源尽在 666java.com】.mp4
- 时长 8分2秒（音频 482s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好Rookie的MQ这个环境我们搭建好之后呢接下来我们就要动动手开始编写代码实现开户业务的第三阶段这个功能那我们从哪开始呢这个地方呢我们还要看一看这个图看这儿啊3.1这个地方按照这个业务执行的流程啊银行存款系统这边把业务处理完之后他会尽最大的努力去通知或者说去毁掉我们的哪个服务啊对存款代理服务是吧
[00:30] 所以我们首先编码从哪开始首先要从存款代理服务这边开始那我们先干嘛呢先干嘛我们说了银行存款系统会毁掉我们的存款代理服务其实具体来说就是访问我们这边的一个什么呀Controller然后把结果呢就告知给我们所以说呢我们首先要在存款代理服务这边单独建立一个Controller来供谁去毁掉供银行的存款系统去毁掉
[00:58] 说咱这边你看讲义我们是不是也是从存款代理服务开始单独创建这么一个卡抽了我们去找到我们的存款代理服单独新建一个卡扣了这对吧单独新建这个地方咱就不要接口直接创建一个类好这个类呢我们就创建完创建完之后呢我们再次给大家强调一下啊这个卡扣了是专门用来接收银行存款系统的开入结果
[01:40] 就是他那个毁掉的一个通知那这里边的一些呃这个注解啊我就不再挨个敲了因为这个内容比较多但是呢这些都相对说比较简单一些啊你比如说这个呃swegg的一些注解包括spermvc的一些注解这些呢我就直接粘过来了我们节省点时间这里边这就是一个swegg的一个描述吗这个我就不用解释了吧还是s的control了
[02:07] 然后呢我们在control里边是不是一定要定义一个方法呢因为它回调一定是访问我们control里边具体某个方法那咱接下来呢把这个方法先定义一下这呢我们就给讲义呢给它保持一致在这呢我们定义一个方法这里边大家要注意我们要讨论一下这个方法的返回值还有什么呀对还有这个参数发明这叫啥无所谓就这个名字起的有点太长了先不用管它
[02:44] 那返回值一定得有为啥得有啊前面咱分析过了啊我们前面说过说这个呃银行的存款系统这边是不是会不断的回调我们的这边这个什么呀control了对不对直到我们这边干什么呀是不是要返回一些信息要响应一些信息对不对比如说我们返回一个OK啊就是告诉我这边已经成功的接收消息已经处理了对不对他这边才干什么呀对他这边就不再继续进行什么呀回调
[03:14] 所以说呢他在毁掉我们的Controller的时候呢我们这边一定是要进行响应的就是一定要有返回值的那我们这呢就需要设计一个什么呀返回值就字数刷类型的就行string具体反而啥那这个简单我们就返回了ok是不是就就可以那要不要参数呢要参数这个参数至关重要其实我们刚才说了呃银行存款系统是不是毁掉我们的Controller其实他在毁掉的时候
[03:43] 不就是吊攒这个方法他在吊攒这个方法的时候呢他就会传过来一堆参数其实他那个结果啊包括相关的一些数据就是通过这个参数而升进来那都需要哪些参数呢参数有点多啊我在这呢就不带挨个给大家敲了我直接给大家粘过来然后给大家解释一下就行了就这块有点多啊然后我顺便把上面这一堆sweag的这个注解这些东西也全都粘过了啊包括这个请求地址全部都粘过了
[04:22] 大家可以看一下这里边反正因为他参与比较多你这个sweag可能就干什么就需要挨个进行一个什么解释大家可以看一下这里边每个参与都是什么意思第一个参数咱以前见过就是存款接口那个名应该是叫什么叫开户第二个就是咱平台编号之前也说过还有第三个就是签名是不是
[04:53] 第四个呢其实才是真正的业务数据我们其实主要用的就是这个IQD主要用它大概就是这几个层上四个层上其实咱其实主要用到就这一个前三个咱目前应该用不着目前用不着但是他银行那边的确跟咱这个发回来这些数据了但是咱目前只用这一个然后呢再看一下我们这边的请求请求方式是get请求对吧请求地址是这个什么呀
[05:24] 然后呢这个这儿我们写死了一个参数这我们简单给大家说一说写死了一个参数这个参数呢其实就是这个谁呀就是我们刚才说的这个谁呀Service内我们在这人工给他写死那这个我们刚才说我们之前见过这个其实就是个人开户的那那那个那个那个单词吧或者关键字吧这个是不能随便乱写的我们在这直接写死为什么我们要写死因为我们这个方法就是处理什么呀开户
[05:54] 就是处理开放所以说我在这就给他写死了其实这些东西我们暂时都用不着其实你也不用管他我们一会儿呢重点是关注这个就行这是什么呀这是我们定义了一个方法对吧讨论一下它的反应值以及相关的一些什么呀参数那接下来我们在这个方法里边都需要实现哪些功能呢对不对都需要实现哪些功能呢那这里边我们还得看这个图
[06:23] 前面我们说过了这里边都需要实现哪个功能第一个你在图里边能看到就是我要我这边要更新一些数据这边告诉你有有些交易记录状态是不是要改改原来是未同步这样对不对现在改成已同步然后这边还要干什么还要给consumer这边发消息同时这边是不是还要给他返回一个一个自负算值对不对所以说大概是应该是干几件事三件事我们在这就先把步骤或者注释先写一下
[06:54] 第一件事就是更新数据第二件事就是干什么对发送消去给谁给c o n用户中心中心对吧然后就是返回结果代码我们现在就可以写了直接返回一个什么OK就行这个结果我们刚才说这个结果是反而给谁的对这个结果是返回给银行的
[07:34] 就是银行这边毁掉我们的control让嘛毁掉完之后我们的卡这有个返回值会给谁给银行银行这边一看是ok证明完事了这边就不再进行了什么呀毁掉就咱前面都分析过所以说咱这儿是把谁存款代理服务这边我们先单独创建了一个control这配了一些参数然后返回值那么里边这个功能咱接下来一点一点开发就ok了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在用户中心系统中，通过新建一个控制器来接收银行存管系统的开户回调通知，并处理相关业务逻辑。

2) 按时间顺序列出每张画面的要点：
画面1：讲解 RocketMQ 的安装与启动命令，以及检查用户中心和存管代理服务的 pom 依赖。
画面2：展示新建控制器类 `DepositoryNotifyController` 的代码，包含 `@Api`、`@ApiOperation`、`@ApiImplicitParams` 等注解。
画面3：在 IDEA 中右键点击 `Controller` 包，选择新建 `Java Class`。
画面4：展示 `DepositoryNotifyController` 类中 `@ApiOperation` 注解的完整内容。
画面5：展示 `@RequestMapping` 注解的完整内容。
画面6：展示系统架构图，包含“浏览器/APP”、“用户中心”、“存管代理服务”、“存管系统”和“开卡银行”五个模块及其交互流程。
画面7：在代码中添加注释“//1.更新数据”。
画面8：在 IDEA 中展示 `DepositoryNotifyController` 类的完整代码结构。
画面9：在代码中高亮显示 `@ApiImplicitParam` 注解中 `value` 的内容。
画面10：在代码中高亮显示 `@ApiImplicitParam` 注解中 `value` 的内容。
画面11：在代码中高亮显示 `@RequestMapping` 注解中 `params` 的内容。
画面12：再次展示系统架构图。
画面13：展示 `DepositoryNotifyController` 类中 `@ApiOperation` 注解的完整内容。
画面14：在代码中高亮显示 `@ApiImplicitParam` 注解中 `value` 的内容。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```
start mqnamesrv.cmd
start mqbroker.cmd -n 127.0.0.1:9876 autoCreateTopicEnable=true
java -jar RocketMQ-console-ng-1.0.1.jar --server.port=60000 --
RocketMQ.config.namesrvAddr=127.0.0.1:9876
```
画面3：
```
New
    Java Class
    Kotlin Class
    Groovy Class
    Scala Class
    Interface
    Enum
    Abstract Class
    Record
    Script File
    FreeMarker File
    JSP File
    HTML File
    XML File
    YAML File
    Properties File
    JSON File
    TXT File
    Markdown File
    CSV File
    SQL File
    Dockerfile
    .bat File
    .sh File
    .properties File
    .xml File
    .yaml File
    .json File
    .txt File
    .md File
    .csv File
    .sql File
    .dockerfile File
    .bat File
    .sh File
```
画面4：
```
@Api(value = "银行存管系统通知服务", tags = "depository-agent")
@RestController
public class DepositoryNotifyController {

    @ApiOperation("接受银行存管系统开户回调结果")
    @ApiImplicitParams({
        @ApiImplicitParam(name = "serviceName", value = "请求的存管接口名",
                required = true, dataType = "string", paramType = "query"),
        @ApiImplicitParam(name = "platformNo", value = "平台编号，平台与存管系统签约时获取",
                required = true, dataType = "string", paramType = "query"),
        @ApiImplicitParam(name = "signature", value = "对reqData参数的签名",
                required = true, dataType = "string", paramType = "query"),
        @ApiImplicitParam(name = "reqData", value = "业务数据报文，json格式",
                required = true, dataType = "string", paramType = "query")
    })
    @RequestMapping(value = "/gateway", method = RequestMethod.GET, params = "serviceName=PERSONAL_REGISTER")
```
画面5：
```
@RequestMapping(value = "/gateway", method = RequestMethod.GET, params = "serviceName=PERSONAL_REGISTER")
```
画面7：
```
//1.更新数据
```
画面8：
```
package cn.itcast.wanxingzp.depository.Controller;

import io.Swagger.annotations.Api;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "银行存管系统通知服务", tags = "depository-agent")
@RestController
public class DepositoryNotifyController {

    @ApiOperation("接受银行存管系统开户回调结果")
    @ApiImplicitParams({
        @ApiImplicitParam(name = "serviceName", value = "请求的存管接口名",
                required = true, dataType = "string", paramType = "query"),
        @ApiImplicitParam(name = "platformNo", value = "平台编号，平台与存管系统签约时获取",
                required = true, dataType = "string", paramType = "query"),
        @ApiImplicitParam(name = "signature", value = "对reqData参数的签名",
                required = true, dataType = "string", paramType = "query"),
        @ApiImplicitParam(name = "reqData", value = "业务数据报文，json格式",
                required = true, dataType = "string", paramType = "query")
    })
    @RequestMapping(value = "/gateway", method = RequestMethod.GET, params = "serviceName=PERSONAL_REGISTER")
    public String receiveDepositoryCreateConsumerResult(
            @RequestParam("serviceName") String serviceName,
            @RequestParam("platformNo") String platformNo,
            @RequestParam("signature") String signature,
            @RequestParam("reqData") String reqData) {
```
画面9：
```
@ApiImplicitParam(name = "reqData", value = "业务数据报文，json格式",
                required = true, dataType = "string", paramType = "query")
```
画面10：
```
@ApiImplicitParam(name = "reqData", value = "业务数据报文，json格式",
                required = true, dataType = "string", paramType = "query")
```
画面11：
```
@RequestMapping(value = "/gateway", method = RequestMethod.GET, params = "serviceName=PERSONAL_REGISTER")
```
画面14：
```
@ApiImplicitParam(name = "reqData", value = "业务数据报文，json格式",
                required = true, dataType = "string", paramType = "query")
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面6：
架构图结构：
- “浏览器/APP” → “用户中心”（1.1）
- “用户中心” → “存管代理服务”（1.2）
- “存管代理服务” → “存管系统”（1.5）
- “存管系统” → “开卡银行”（2.4）
- “开卡银行” → “存管系统”（2.5）
- “存管系统” → “用户中心”（2.6）
- “用户中心” → “浏览器/APP”（2.8）
- “用户中心” → “存管代理服务”（3.3）
- “存管代理服务” → “存管系统”（3.2）
- “存管系统” → “用户中心”（3.4）

画面12：
架构图结构：
- “浏览器/APP” → “用户中心”（1.1）
- “用户中心” → “存管代理服务”（1.2）
- “存管代理服务” → “存管系统”（1.5）
- “存管系统” → “开卡银行”（2.4）
- “开卡银行” → “存管系统”（2.5）
- “存管系统” → “用户中心”（2.6）
- “用户中心” → “浏览器/APP”（2.8）
- “用户中心” → “存管代理服务”（3.3）
- “存管代理服务” → “存管系统”（3.2）
- “存管系统” → “用户中心”（3.4）

5) 无

