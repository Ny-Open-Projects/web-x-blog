# day01-19-Swagger常用注解

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-19-Swagger常用注解_【海量资源尽在 666java.com】.mp4
- 时长 9分47秒（音频 587s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才我们把Swagger是不是已经集成到哪个微服工程里面了集成哪个微服工程里面对我们是不是集成到Consumer就是用户中心这个微服工程里面这个环境已经有了或者准备工作已经做到位了那现在Swagger就能帮我们生成文章了吗那我觉得不可能那要是现在他就能帮我们把文章生成我觉得他也太神了有点吓人了他没这么智能我想说他不可能的因为他怎么可能知道我这里边谁是Controller
[00:32] 对他怎么知道我这个control了里边都有哪些方法他怎么知道我这个方法是什么意思有没有参数有没有反应值对不对他他不可能这么智能那也就是说呢我们还是需要做一些事情去告诉他这个信息然后他拿着我们这些信息呢去生成一个文档大概是这么一个一个一个过程那我们怎么告诉他这些信息呢那我们就需要用到啊Frag提供了一堆什么呀注解你看这儿他说了
[01:02] 我们可以在加类当中目前主要是Ctrl 这儿来添加什么注解SWG 的这些注解然后呢SWG 呢就扫描这些注解里边内容去生成什么样稳当所以接下来我们要熟悉这些注解那这个注解呢还是有点多的啊有点多但是这些东西大家不用记啊你一开始不熟的话就翻翻这个讲义翻翻稳当将来写个几次之后慢慢就熟悉了那咱看一看吧这些注解呢是整体可以分成两类或者两大块的一大块是写到类上面
[01:32] 就是用来描述类的这个信息一块呢写到方法上面是描述方法的信息你比如第一个注解它叫at API它就是用来描述什么描述类的它应该放到类的上面比如你可以说一说通过这个注解说一说这个Controller是干啥这个Controller是不是是实验登录的对不对这Controller是表示用户中心的一个Controller对不对你可以写一句话来描述一下然后你再看后边这个注解叫at API operation
[02:02] 这个注解就是用于描述什么方法它是用到方法上这是两个总整体的一个一个一些注解啊一个是放到内上的一个是放到什么方法上那我们重点是要讲这个方案上的这个注解因为我们发请求其实说白了是不是最终是为了调上控制当中的某个方法我们得知道这个方法它的作用这个方案有没有参考这个方案有没有反应值对不对所以你会发现下边这一堆注解其实都是配合它去使用
[02:32] 配合这个诸葛比如说啊at api param他就是用来描述一个参数啊就是如果这个方案就一个参数你就用他就行哎描述一下这个参数他是表示什么意思啊这个参数是用来接收姓名的还是接收年龄的对不对那如果你这个参数啊他是一个对象是封装好的一个对象哎你得用这个诸葛去描述然后呢再配合这个诸葛at api对吧model property来描述这个对象里面每个属性都是什么意思这堆都是
[03:03] 用来描述什么方法的参数然后下边这一堆就是用来描述什么方法的什么范围值就是响应嘛我们是不是把方法的这个范围值响应给谁啊钱端了是不是或者显然给调用方了啊所以说这块呢是用来描述这个范围值那再往下呢还有一些注解比如说哎如果如果出错了我们会返回什么信息他就是如果我这个参数是多个你得换成这个注解换成这个注解
[03:32] 一个参数你可以用这个多个参数你得用这个那如果针对参数的话他也有很多信息要描述比如这个参数它是什么数据类型对不对这最基本的了这个参数什么意思表示什么意思对不对你再描述所以你看他还有一些子属性比如说参数的什么类型对吧你这个数据传参的方式是RESTful风格还那种请求问号请求字符算那种风格对不对
[04:00] 你是jason形式传过来的还是这个不就是普通的一个值对不对等等等等这就是数据到什么样类型都有什么类型参数的名字参数表什么意思参数是不是必须得给等等他有没有什么默认值等等说这个注解比较多我就不再挨个俩说了你下去可以自己查查文档那咱们接下来就看一个例子看一个例子大家看一下我们consumer Controller里边他已经使用了swegg的
[04:31] 注解就刚才我们说到这个注解咱们先看一看这个例子首先大家看我们是不是在类的上面用了什么注解叫at什么呀api是不是你看他都干了什么事用value属性描述了一下我这个Controller这个类是干嘛哎这个Controller是我们用服的一个control是不是哎这个tag呢其实就是一个标签分类这是一个更详细的一个描述信息你可以自己再写一下啊这些内容就是自己加的啊自己加的但是你要注意
[05:06] 这个注解是用到类上的那哪个注解是用到方案上面的就这个at API operation你看这是我们的方法吗是不是在方案上面写的at API operation对不对那这里边就给了一个字符串用来描述这个方法是干啥啊干啥那比如说我给你举个例子如果我这个方案是实现登录功能这应该怎么写啊你这就显示什么呀登录功能对不对你告诉他哎这个方案是干啥的就行
[05:37] 当然呢我这个例子比较简单用啥简单因为我这里边有没有方法对不是有没有方法是有没有参数呀没有参数所以比较简单那接下来的话我再写一个带参的这个方法把这个这里边涉及到的这个什么跟参数有关的这些注解我们也用我们这个还是反正这还是字符串吧写一个方法叫嗨吧
[06:06] 然后我们要加一个参数加一个什么参数呢就就就就死出人类型了吧最常见的一个啊嗯然后功能的话咱就简单一点吧直接return拼一个字不算返回吧嗨打个招呼对不对加上谁啊那功能很简单因为咱这不是研究功能啊咱是研究这个sweig的注解那对于这么一个方法我想加sweig的这个注解应该怎么加应该怎么加
[06:36] 那其实你不用想了我们说了方法上面首先要加哪个注解就这个注解at API operation它是不是对整个方法的一个什么呀一个描述对不对那我这就随便写个测试hi方法对不对随便写一个然后呢然后呢我发现了这个方法有什么呀对有参数有参数我们叫描述这个参数它是什么意思啊叫什么名啊它这个是什么数据类型啊等等等等
[07:05] 这些信息我们都得通过注解告诉给谁啊告诉给Fed那我用哪个注解呢用哪个注解你看吧我们现在有几个参数一个参数一个参数你就用它就够如果你将来有两个或者两个以上的参数你是不是换上它对不对那我们现在就用这个注解就行一个参数放到这那这里边都需要写什么东西呢都需要想象东西你看这个表呗这表里边我们说了是不是有这么多属性你可以用啊
[07:35] 有指定类型的对不对有指定这个参数名的等等等等那在这个小谷上你就可以写首先呢我要告诉他这个参数的名字参数的名字用内幕属性去指定那咱这个参数名字是不是就叫内幕你就写的内幕就行那我们还可以告诉他什么信息还可以告诉他这个参数是什么意思我们这个参数是不是就是一个姓名是不是参数表什么意思用value属性来描述这里边你就写个什么呀
[08:07] 这个姓名就行那还需要描述什么信息啊它是不是必填的对不对叫recurred给一个值出就表示将来啊你往这发请求的时候呢这个这个什么呀这个值是必须传过来的这个布尔类型必须要给引号那还需要给什么信息啊我们最起码这个参数的类型给告诉他我们这个参数是不是自传类型对吧
[08:37] 那这个应该靠什么呀靠这个是呀BetaType是不是那我这就加一个DataType那什么类型呢我们这什么类型是不是字符串类型对不对写个String就行这样基本上描述的就差不多了然后呢我们再加上一个这个注解我们可不能忘了仿路径是不是再配一配对不对这个仿路径啊我们的Swegg也能进行扫描虽然这个注解不属于Swegg但是它也能扫描它有这个功能
[09:08] 那我们这里边就配一个一个啥随便写一个吧好吧就杠杠害吧这是我又给大家举了一个例子啊我们在熟悉熟悉这个斯白格相关的一些注解其他没有演示到注解暂时就不再给大家演示后边咱陆续都用到用到时候再说啊这块东西虽然你看上多但其实很简单就是一些注解啊每个注解都比较什么意思对吧那咱后边用一用就行就给大家举了一个例子啊咱一会呢
[09:39] 就会让SIG去扫描这些东西然后让它生成什么样文档一会我们测试的时候再说

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Boot 项目中使用 Swagger 注解来生成 API 文档，重点演示了 @ApiImplicitParam 注解的使用方法和参数配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IntelliJ IDEA 中的项目结构，选中了 ConsumerController.java 文件，准备编写代码。
画面 2: 展示了 PDF 文档中关于 Swagger 常用注解的介绍，包括 @Api、@ApiOperation、@ApiParam 等。
画面 3: PDF 文档继续展示 Swagger 注解，重点是 @ApiModelProperty、@ApiResponse、@ApiIgnore。
画面 4: PDF 文档中展示了 @ApiImplicitParam 注解的属性表格，包括 paramType、dataType、name、value、required 等。
画面 5: PDF 文档中再次展示 @ApiImplicitParam 注解的属性表格，内容与画面 4 相同。
画面 6: 在 IDEA 中，展示了 ConsumerController.java 文件的初始代码，包含 @RestController 和 @Api 注解。
画面 7: 屏幕截图显示了多个窗口，包括 PDF 文档和 IDEA，用于说明如何查看和使用 Swagger 文档。
画面 8: PDF 文档中再次展示 Swagger 注解的介绍，内容与画面 2 相同。
画面 9: PDF 文档中再次展示 @ApiImplicitParam 注解的属性表格，内容与画面 4 相同。
画面 10: 在 IDEA 中，展示了 ConsumerController.java 文件中添加了 @ApiImplicitParam 注解的代码，用于接收参数 name。
画面 11: 在 IDEA 中，展示了 ConsumerController.java 文件中添加了 @ApiImplicitParam 注解的代码，参数 required 设置为 true。
画面 12: PDF 文档中再次展示 @ApiImplicitParam 注解的属性表格，内容与画面 4 相同。
画面 13: 在 IDEA 中，展示了 ConsumerController.java 文件中添加了 @ApiImplicitParam 注解的代码，参数 dataType 设置为 "String"。
画面 14: 在 IDEA 中，展示了 ConsumerController.java 文件中添加了 @ApiImplicitParam 注解的代码，参数 required 设置为 true，dataType 设置为 "String"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6 代码：
```java
package cn.itcast.wanxingzp.consumer.Controller;

import io.Swagger.annotations.Api;
import io.Swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "用户服务的Controller", tags = "Consumer", description = "用户服务API")
@RestController
public class ConsumerController {

    @ApiOperation("测试hello")
    @GetMapping(path = "/hello")
    public String hello(){
        return "hello";
    }
}
```

画面 10 代码：
```java
@ApiImplicitParam(name = "name", value = "姓名", required = "true")
public String hi(String name){
    return "hi,"+name;
}
```

画面 11 代码：
```java
@ApiImplicitParam(name = "name", value = "姓名", required = true)
public String hi(String name){
    return "hi,"+name;
}
```

画面 13 代码：
```java
@ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
public String hi(String name){
    return "hi,"+name;
}
```

画面 14 代码：
```java
@ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
public String hi(String name){
    return "hi,"+name;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2、3、8、9、12: PPT 标题为“2.1.3 Swagger常用注解”，内容包括：
- @Api：修饰整个类，描述Controller的作用
- @ApiOperation：描述一个类的一个方法，或者说明一个接口
- @ApiParam：单个参数的描述信息
- @ApiModelProperty：用对象接收参数时，描述对象的一个字段
- @ApiResponse：HTTP响应其中1个描述
- @ApiIgnore：使用该注解忽略这个API
- @ApiError：发生错误返回的信息
- @ApiImplicitParam：一个请求参数
- @ApiImplicitParams：多个请求参数的描述信息

画面 4、5、9、12: PPT 表格数据：
| 属性       | 取值     | 作用                     |
|------------|----------|--------------------------|
| paramType  | path     | 以地址的形式提交数据     |
|            | query    | 直接跟参数完成自动映射赋值 |
|            | body     | 以流的形式提交 仅支持POST |
|            | header   | 参数在request headers 里边提交 |
|            | form     | 以form表单的形式提交 仅支持POST |
| dataType   | Long     | 参数的数据类型 只作为标志说明，并没有实际验证 |
|            | String   |                          |
| name       |          | 接收参数名               |
| value      |          | 接收参数的意义描述       |
| required   | true     | 参数是否必填             |
|            | false    | 非必填                   |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

