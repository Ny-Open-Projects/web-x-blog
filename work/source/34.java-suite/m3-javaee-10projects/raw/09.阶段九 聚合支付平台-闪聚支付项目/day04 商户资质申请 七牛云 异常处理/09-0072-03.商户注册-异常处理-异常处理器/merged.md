# 03.商户注册-异常处理-异常处理器

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\03.商户注册-异常处理-异常处理器【海量资源尽在 666java.com】.mp4
- 时长 16分1秒（音频 961s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们继续来实现我们系统的异常处理流程那在刚才我们是不是定义了我们的自定义异常类型啊那么接下来我们就可以在代码当中来抛出我们自定义异常类型然后呢抛到control了呢我们就要捕获我们的异常所以抛出的代码一会我们写非常简单在我们的代码里面输入new我们的business exception就行了但是我们现在要捕获这个异常呢
[00:30] 定义一个异常的拦截器异常处理器好那现在呢我们准备来做这件事那么捕获出异常最终啊会给用户响应我们说包含error code和error message的这么一个信息所以啊我们单独再定义一个什么专门用来返回异常信息的这么一个类型里边呢就正好包括了这两个属性大家看到了吗所以你在笃闷当中啊我们来定义一下
[01:00] 在这好那这个代码就比较简单大家可以看到包括两个属性然后呢构造方法然后呢加一个long block的注解是不是guideside的方法不用写了这是sweager的注解一个说明所以这个代码我就不再去敲这个属性了所以大家呢拷贝过去就行了那你将来拿到我的代码你可以直接把这个拷过去好下面呢我要说重点了
[01:27] 就是这个类将来我们的异常处理器呢会返回这个类型的数据将来正好给前端对吧那现在呢我们要做的事是啥呀我们要定义这么一个异常处理类那我现在问大家个问题啊嗯我现在要定义这个类似于拦截器的这个异常处理器啊那你告诉我我是在这个商户服务当中写还是商户平台应用的这个工程中写嗯大家思考来大家看着这个异常处理流程来思考一下就这
[01:57] 大家看根据我们的流程这个异常呢往上抛最终抛到了application当中的Controller对不对那我问你到Controller我们是不是要补货了对不对所以各位你告诉我我应该在哪个工程写这个异常处理线有同学应该说对了在包含有Controller的这个工程当中来写当前我们完成了这两个工程一个是商户
[02:31] 注册服务一个是商户注册应用这个应用里边它是不是对接前端它是不是往外暴露http接口里边是不是有Controller所以我们要在这个工程当中来写一个拦截器对那写这个异常处理器呢它要去来进行异常补货和处理好那我们明确了我们写代码的位置接下来我们就来看那怎么写那这里边呢我要给大家说一个注解了我们在没写代码之前我就要说一个注解这个注解呢叫Controller
[03:01] adviceadvice这个词呢大家应该学过Spring AOP的就不陌生了吧这个词叫增强对吧一般来说我们面向切面编程对我们是不是就是相当于写一个代理的什么类型然后呢做增强没错这个注解就是Spring MVC 3.2提出来的它呢可以实现对Controller进行面向切面编程
[03:31] 那有时候老是面向切面编程到底你想实现什么额外的功能呢我们说了吗你是不是要捕获Controller抛出的异常啊所以我们只要用这个注解标记的类那么它呢就可以实现对Controller进行切面编程那么进行切面编程具体要实现什么功能这个advice这个注解啊它可以和三个注解配合使用完成不同的功能注意当
[03:57] Controller Advice和Exception Handler来结合使用它可以捕获异常它可以实现全局异常的处理注意你看这个单词你大概就知道对吧专门进行捕获异常的当这个Controller Advice和Model Attribute这个注解进行配合使用它可以实现全局数据绑定因为大家之前学过Model Attribute是不是就相当于请求的数据绑定到我们的数据对象中是不是
[04:26] 所以它可以实现全局数据绑定当controladvice和enatebender这个属性注解进行结合使用它可以实现全局数据的预处理所以这三个特性我们今天用第一个后两个回头我们用到的时候再说
[04:45] 好我们知道了我们如何实现全局异常处理就是我们要面对Controller进行切面编程对Controller进行增强怎么增强就是捕获它的异常进行处理好那现在呢我们来看那么首先我们需要在我们的这个商户平台应用的这个里头啊我们新添一个包商户平台应用里边我们刚才说嘛要捕获Controller的异常嘛所以这里边我们要在这儿
[05:15] 新添一个包而这个包当中我准备写我们的异常处理器这个异常处理器我们把它命名为Globe Exception Handler从字面以上你大概能知道它是全局异常处理的意思对不对好那现在呢我们就把它定义出来刚才说过它是一个什么叫全局异常处理对不对那怎么实现呢我刚才是不是说了这里边我们要用一个叫做Controller Advice
[05:44] Controller Advice这个注解我们刚才说的很清楚它与谁配合使用可以实现全局异常处理它和一个叫做Exception Handler对不对它来配合使用实现全局异常处理你懂我意思吧那有的老师咋配合使用呢这是不是一个类啊
[06:14] 用这个advice标记一下都表示这个类呢是对control耳镜增强面向前面编程了那么这里头呢我们就要去干嘛就要去捕获异常那你捕获异常嘛类当中肯定是写方法嘛所以这里面呢我们就会写一个什么写一个方法看啊我写一个方法哎那这个方法注意看哎这个方法当中注意我是不是要捕获住异常了捕获异常你怎么捕获我不是说了吗
[06:45] 你是不是要用一个注解所以这里面其实注解是用在这懂吧你捕获异常捕获啥异常呢凡是系统抛出的异常我都捕获所以我认为exceptionexception有时候老师你不是捕获我们自定义的异常吗你是不是定义了一个自定义的异常类型你别忘了所有的异常类型它的根是不是都是exception所以我们准备捕获exception
[07:16] 懂吧所以这里边呢我们就在这里边我们把这个exception这个异常类型定义好这就表示我们捕获exception异常当然自定义异常属于它的子类也捕获到那你捕获住了之后呢我们经过处理这里边是不是就是异常处理异常处理完了之后你是不是要返回给前端呢返回给前端什么数据格式呢
[07:42] 我们刚才说过吗包括error code和error message吗所以刚才我是不是定义了一个叫做什么rest error response对吧但是你返回的这个类型这个数据你是不是最终转换成json呢所以你要用response什么body来标记懂吗另外还有我们说了吗
[08:07] 你返回的这个错误根据我们的规范你是不是都要抛出500的这种状态对不对所以我们还需要用一个注解来标识对我们要抛出什么500的这个错误那说老是抛出500的错误它是啥呢对我们要用一个http states来标识一下那么它这里边有很多的这个错误状态对不对那里边其中
[08:37] 有一个叫做server error其实这个server error你会发现它是不是就是500看见吗对这就是我们说这个方法上面要加一些注解那这里头有啥东西因为你是对谁对这个Controller进行增强所以那你把Controller的这些比如说http serverlet responsehttp serverlet request
[09:05] 你只要想用这些东西都可以拿到但是有一个最最关键的东西你要拿到这个东西是啥对你要捕获异常你拿不到异常你咋捕获所以你要拿异常懂吧大家看现在我是不是就把异常的信息给拿到了行三对吧这就相当于捕获住异常了这就不是异常信息吗这里面我们是不是就要干嘛
[09:32] 是不是就要解析我们的异常信息对不对那你说怎么解析异常信息怎么解释异常信息你是不是得看我们的异常处理流程刚才说的很清楚当捕获住异常之后有俩分支我们说对于是系统自定义的异常你就直接取出error code和error message如果不是我们系统自定义的异常那你要统一把它归为99999系统未知错误异常理解吗
[10:02] 对所以现在我们要做的一件事是啥是捕获住异常之后呢我们要对它进行一个什么一个解析那怎么进行解析了那还不简单吗根据刚才我们的流程我们说什么呀写下如果是系统自定义的异常我们呢就直接看好取出error code和error message
[10:32] 懂我意思吧那好那有人老师那你咋知道是系统自定义义常那也很简单呀这个类型的数据是拿到了我只要判断一下这个是不是business exception不就OK了对吧如果这个义务条件满足这是不是就表示我们要解析系统自定义义常的信息啊internet of这个关键字大家学Java基础是不是学过就表示它是它的一个什么
[11:04] 对吧它是它的一个类型所以这里边我们是不是就可以怎么动就可以把它转换一下注意我们就把它转换强转我们是不是就拿到了我们系统自定义的异常那么我们拿到了系统自定义的异常信息那还不简单吗这时候我们就直接get我们是不是就拿到了这个error code这是不是就是取出了我们异常的代码
[11:34] 错误代码和错误信息在哪去在这嘛get拿到了吧对不对再get拿到了吧这是不是就是错误代码错误信息好那你拿到了这个东西之后呢返回restresponse刚才我们说了嘛是不是要返回它呀对不对返回它你看它是不是有一个error message那么你就把正好把这个给它填进去各位告诉我
[12:06] 这是不是就成了对吧那报错了是啥意思原来它都是一个stream对吧所以这里边呢我们就把它转一下这是不是就OK了那说老师那你如果说不是这个系统自定义的异常呢不是系统自定义的异常我们干嘛呀统一定为99999系统未知错误异常懂吗
[12:41] 好那现在呢我们就可以直接返回newrest系统位置错误一层你看这个错误代码当中有没有你看是不是有一个99999对不对哎他就非常方便啊这里边我们就可以直接在这儿来用这个我们的快捷方式是不是就拿到了哎然后呢这个是error code对吧然后呢还有一个message
[13:15] 这是不是就完事了对不对那这里边呢我们来看这是啥意思一个是error code一个是message那我们现在是不是要留一个这是哪里一个还是那个字符串的问题我们把它加一个字符串就完事了这个这个代码能看懂吧好我们把它转一下好那这样的话是不是就是我们这个异常处理的流程是不是按照老师刚才给大家说的这个分两个分支吗一个是
[13:48] 如果是系统自定义一场我们就直接拿如果不是系统自定义一场我们就把它统一为什么99999未知错误一场就完事了哎写好了好那么如果我们有一场信息了我还是非常建议你去把它干嘛呀去把它打印出来哎所以这里边呢我们完全可以怎么弄啊哎在这呢我们叫加一个日志吧嗯sl4j啊我们用这个哎这个我们用常量好
[14:20] 然后这个呢就是log好然后呢log backtree然后呢get因为最终你抛出一藏吧还是需要去把它给输出出来的嘛输出程式是吗然后呢在这儿呢我们就可以如果是自己系统自定义的藏呢我们就可以来打一然后这里边呢就叫做message来最终把这个e这个对象填进去那这儿呢就可能就是系统自定义上我们就用error了啊我们就error那这个呢就是
[14:50] 系统抛出的未知错误异常吧所以这就是系统异常好然后把它放进去好这样的话我们是不是就完成了这个异常处理器的这个什么这个编写吧好那现在我们把这个异常处理器编写完了之后呢我们把这个流程再梳理一遍啊看看是不是按照我们刚才所说的按照我们的异常处理流程来实现的好吧好异常处理流程呢是我们要抛出自定义的异常
[15:19] 那么自定义义常最终会被异常处理器捕获异常处理器捕获了之后分两个分支第一个分支它会判断是否是系统自定义的义常如果是我们就让它直接取出当时抛出的error code和error message这些信息然后返回给前端返回给前端的话这里边用一个response注解然后转成json给前端对吧好然后如果不是到这执行那就是系统级义常这里边就是未知错误义常
[15:48] 我们呢也给它返回一个99999的系统位置错误一场好这个就是我们的异常处理流程它的实现就是异常处理器的编写

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Spring Boot 项目中，通过自定义异常类和全局异常处理器，实现对业务异常和系统异常的统一处理和响应。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：讲解在 shanjupay-common 工程的 com.shanjupay.common.domain 包下添加错误响应包装类 RestErrorResponse。
画面2：展示 RestErrorResponse 类的完整代码，包含 @ApiModel 注解和构造方法。
画面3：在 IDE 中展示 shanjupay-common 模块的目录结构，选中了 com.shanjupay.common 包。
画面4：讲解全局异常处理器使用 @ControllerAdvice 注解实现，介绍其用法。
画面5：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 @ControllerAdvice 注解上。
画面6：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 @ExceptionHandler 注解上。
画面7：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 @ResponseBody 注解上。
画面8：回顾定义全局异常处理器的讲解内容。
画面9：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 if (e instanceof BusinessException) 语句上。
画面10：在 IDE 中展示 CommonErrorCode.java 文件，展示自定义的错误码枚举。
画面11：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 return new RestErrorResponse(String.valueOf(code), CommonErrorCode.UNKNOWN.getDesc()) 语句上。
画面12：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 return new RestErrorResponse(String.valueOf(code), CommonErrorCode.UNKNOWN.getDesc()) 语句上。
画面13：讲解抛出自定义异常的流程，指出需要在接口中抛出 BusinessException。
画面14：回顾在 shanjupay-common 工程的 com.shanjupay.common.domain 包下添加错误响应包装类 RestErrorResponse。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
package com.shanjupay.common.domain;
import io.Swagger.annotations.ApiModel;
@ApiModel(value = "RestErrorResponse", description = "错误响应参数包装类")
@Data
public class RestErrorResponse {
private String errCode;
private String errMessage;
public RestErrorResponse(String errCode,String errMessage){
this.errCode = errCode;
this.errMessage = errMessage;
}
}

画面2：
package com.shanjupay.common.domain;
import io.Swagger.annotations.ApiModel;
@ApiModel(value = "RestErrorResponse", description = "错误响应参数包装类")
@Data
public class RestErrorResponse {
private String errCode;
private String errMessage;
public RestErrorResponse(String errCode,String errMessage){
this.errCode = errCode;
this.errMessage = errMessage;
}
}

画面3：
Project Structure:
shanjupay
├── shanjupay-common
│   ├── pom.xml
│   ├── shanjupay-merchant-api
│   ├── shanjupay-merchant-Service
│   └── src
│       └── main
│           └── java
│               └── com
│                   └── shanjupay
│                       └── common
│                           └── domain
│                               ├── BusinessException
│                               ├── CommonErrorCode
│                               ├── ErrorCode
│                               ├── PageVO
│                               ├── RestErrorResponse
│                               └── RestResponse

画面4：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面5：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面6：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面7：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面8：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面9：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面10：
public enum CommonErrorCode implements ErrorCode {
    _10001("10001", "商户名与账户不匹配"),
    _10002("10002", "验证码错误"),
    _10003("10003", "查询结果为空"),
    _10004("10004", "ID格式不正确或超出long范围"),
    _10005("10005", "上传失败"),
    _10006("10006", "发送短信失败"),
    _10007("10007", "传入对象为空"),
    _10008("10008", "手机号格式不正确"),
    _10009("10009", "商户名为空"),
    _10010("10010", "商户名已存在"),
    _10011("10011", "手机号为空"),
    _10012("10012", "手机号已存在"),
    _10013("10013", "密码为空"),
    _10014("10014", "密码不正确"),
    _10015("10015", "账号不存在"),
    _10016("10016", "账号已存在"),
    _10017("10017", "密码长度不正确"),
    _10018("10018", "验证码已过期"),
    _10019("10019", "验证码错误"),
    _10020("10020", "验证码已过期"),
    _10021("10021", "验证码错误"),
    _10022("10022", "验证码已过期"),
    _10023("10023", "验证码错误"),
    _10024("10024", "验证码已过期"),
    _10025("10025", "验证码错误"),
    _10026("10026", "验证码已过期"),
    _10027("10027", "验证码错误"),
    _10028("10028", "验证码已过期"),
    _10029("10029", "验证码错误"),
    _10030("10030", "验证码已过期"),
    _10031("10031", "验证码错误"),
    _10032("10032", "验证码已过期"),
    _10033("10033", "验证码错误"),
    _10034("10034", "验证码已过期"),
    _10035("10035", "验证码错误"),
    _10036("10036", "验证码已过期"),
    _10037("10037", "验证码错误"),
    _10038("10038", "验证码已过期"),
    _10039("10039", "验证码错误"),
    _10040("10040", "验证码已过期"),
    _10041("10041", "验证码错误"),
    _10042("10042", "验证码已过期"),
    _10043("10043", "验证码错误"),
    _10044("10044", "验证码已过期"),
    _10045("10045", "验证码错误"),
    _10046("10046", "验证码已过期"),
    _10047("10047", "验证码错误"),
    _10048("10048", "验证码已过期"),
    _10049("10049", "验证码错误"),
    _10050("10050", "验证码已过期"),
    _10051("10051", "验证码错误"),
    _10052("10052", "验证码已过期"),
    _10053("10053", "验证码错误"),
    _10054("10054", "验证码已过期"),
    _10055("10055", "验证码错误"),
    _10056("10056", "验证码已过期"),
    _10057("10057", "

