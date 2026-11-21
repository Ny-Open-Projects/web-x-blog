# 04.Graphql中的变量参数的服务端处理

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\04.Graphql中的变量参数的服务端处理【海量资源尽在 ubkz.com】.mp4
- 时长 19分33秒（音频 1173s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下在服务端来处理我们的请求的这个参数啊那么我们需要去改造一下我们之前所写的Grabber SQL这个Controller然后呢我们来看一下这个里面我们要修改的有两个方法一个就是我们这个get这个方法一个就post这个方法那么我们首先来修改get这个方法那我们可以来测试一下
[00:24] 那么刚刚我们所测试的是POST的请求它的发起请求的一个情况那么接下来我们来看一下如果它是get请求那么又会怎么样呢那么如果get请求的话我们可以看到它会将我们的这些请求参数是不是会丢到后面这个位置来对吧所以说我们可以看到你看在后面这个位置里面有把ABOS那么这个是不是就是我们请求的参数所以我们就需要拿到它然后做一些处理OK
[00:52] 那么我们就来拿一下吧拿一下谁呢拿一下他那么第一个呢是query那么第二个呢是不是就应该叫做request param又注意他是不是使用这个value等于啊等于谁呢是不是等于我们刚刚看到的这个吧ables这个参数名那么要注意的是我们要把它设置为什么呢request等于什么的false为什么要等于false呢因为是我们
[01:18] 这个query这个参数是每一次你做get请求的时候必须要有的参数但是这个abos并不一定对吧所以说我们把它设置为并不是必须的ok那么如果有的话那么我们就去拿到它它其实拿到是一个json对不对拿到是一个jsonok那么这个参数我们是不是就拿到了那么拿到之后我们又该如何去做一个处理呢我们来看一下
[01:43] 在我们之前的处理中我们是调用grabHql的一个execute的方法然后去做一个执行我们点击进去来看一下当我们去传入到query到这个方法的时候它其实最终是不会分装一个execute input的对象然后去做一个执行
[02:06] 那么其实呢我们这个时候呢就不应该自己传入这个query了而是应该自己去构造一个这个execute的啊input的一个对象那我们来看一下这个对象中又有哪些属性那我们其实可以看到它的属性还是比较多的在这个里面需要注意三个啊第一个呢就是query其实就是我们之前所写的query的字符串还有一个呢就是vables这个是不是刚才我们说看到的一个变量那么ok那么它的类型呢是一个map类型
[02:35] 所以说我们一会儿需要给他做一个类型的一个转换那么还有一个呢叫做Option Name这个就是一个操作操作的一个名字这个其实也需要去做一个传递也就是说这个操作这个名字是怎么来的呢其实就是刚刚我们所写的什么呢在我们前面是不是所写的这个定义这个变量的这个位置有一个HK还记得吗其实他
[03:01] 就是那个什么呢ObservationName就是我们操作的那个Name那么我们这个也需要去传递一下所以说我们其实要处理的是有三个参数一个是Query一个是ObservationName一个是Viables这三个那么我现在是不是只写了两个那我们再来写第三个它然后在这个里面我们再来给它添加一个请求的参数那么依然往后面去添加这个位置来写一个RequestParam
[03:31] value等于value等于它然后来一个required等于force然后我们后面写一个stringstring它那么拿到它它是一个支付串所以直接就是objection name那么拿到之后怎么处理我们刚刚说的那么在这个位置我们是不是就可以去做一个处理了对吧那么我们去进入EQ的方法
[03:56] 然后我们把这个call过来这个是不是它底层的execution input这个对象我们现在是不是使用这个对象去做一个查找查询了对吧那么我们在这个位置把它call过来call过来之后execute执行就不是执行query了而是执行这个execute input这个对象ok最后去做一个输出那么我们可以看到在这个位置是不是有一个query是不是同样它也有一个什么的叫做什么的operation name其实就是刚刚我们所看到的这个operation name
[04:24] 那么把它拿过来然后呢还有一个叫什么呢叫做Varables要注意的是这个Varables呢它是需要的是一个Mapped是需要的一个Mapped类型的一个参数那么Mapped类型而我们现在拿到的是一个什么呢JSON就是我们刚刚所在我们的这个位置所设置的这个JSON的这个数据那么现在我们就遇到问题了对吧那么我们将如何将我们这个JSON这部串
[04:52] 然后呢反序列化得到一个map啊得到一个map那么这个时候是不是就需要借助于我们的jepson来做一个完成啊哎ok在这个位置我们来做一个处理那我们来看一下他所需要的呢是map类型的一个aibos那么我们把这个拷过来那么需要这样的一个类型然后呢他是怎么去得到呢是不是需要通过我们通过他是不是做一个反序列化
[05:19] 对吧那么怎么样反序列化呢是不是要借助于前面的一个Mapper就是我们的jackson然后呢有一个叫read什么的valueread value传递两个参数第一个参数呢就是我们这个jackson这个支付创那第二个参数呢那就是一个类型那么什么类型呢就map类型我们需要给它作为构造那么怎么构造呢我们通过这个Mapper.gettypefactory通过这个类型工厂
[05:44] 我们去做一个conceptor map做一个这样的一个类型类型的一个构造然后我们来看一下第一个类型那将是什么hashi map然后点class第二个就是key的类型又是tree点什么呢class然后它的value类型我们来看一下那么value类型是object所以在这个位置我们需要给它来一个是什么呢来一个是object
[06:13] 叫object.classok这样的话我们是不是就得到了一个我们这个map对吧看一下它报错那么报错呢是有异常那么有异常呢我们来给它补货一下吧补货这个异常那么补货一下trycat补货那么如果我们去如果我们能够去正常的去反序列的话得到一个map的话那么就去做一个查询ok
[06:42] 好那么去做一个查询就可以了放到这那么如果要是出错的话那么我们就return什么呢是不是可以和下面这个一样对吧显示这样的一个错误的信息哎ok好那么这样的话我们是不是他是不是就改造完成了哎我们并没有去做查询了啊这个还没有用啊这位置要记得return一下returns呢race点什么呢grabql点is cute
[07:08] 是不是我们要通过你是Q的引步的这个对象去做一个查询然后呢去拿到他的一个标准的一个输出好这样的话是不是我们就改造完成了对不对然后呢我们来看一下这个是不是仅仅改造了什么呢get这个请求对吧那么下面这个pose请求是不是同样也需要去做改造那么和这个是不是也是非常类似的改造啊所以呢我们是不是就可以把这个代码去做一个抽取这样我们先写吧写完之后呢我们再去做一个抽取
[07:38] 那么在下面这个post的这个请求中啊那么我们其实可以看到在前面的我们发现他在做post请求的时候你看一下啊做post请求的时候是不是就是传递了一个这个json那么我们是不是就可以直接是不是在这个位置直接在我们的这个这个位置直接让他反序的话是不是就可以得到一个map那这样的话我们是不是就方便多了哎OK那我们这样
[08:04] 那么咱们把这个pose改造一下那我拿到的就不是json了我直接就拿到一个mapmap谁呢param那就叫他param吧然后呢拿到他之后啊那么我们是不是就可以去拿到这个里面的两个这个内容对吧一个呢叫做query一个query一个叫viablesok好 那个接下来我们去拿他的一个这个内容啊那么下面的这个查询那么我们是不是就可以把它去改造一下了
[08:33] 那么我们先定义一个这个叫query我们拿这个queryquery等于这个pyram就是拿到一个参数点什么呢get谁呢get是不是有一个叫query还看一下是不是就他那么ok拿到get的query拿到应该是引号query拿到他之后我们去给他做一个强转那么强转成一个字符号那么其实就是拿到一个查询这个字符号
[09:04] 然后呢我们来看一下下面呢我们还需要拿到的是这个吧Abos那么显然这个拿到的是不是也应该是一个Jason支付创那么叫JasonOK那么这个叫Abos是不是拿到的是一个这个Jason支付创那么拿到这个Jason支付创之后呢我们就需要去给他去做一个反序列化跟我们刚刚的这个是不是就一样了对吧拿到他做一个反序列化OK那么我们就把它靠到这里来
[09:33] 那他是不是也一样OK那么还有什么呢其实在这个里面他应该还有一个叫Option Name就是我们的操作的名称那么我们这样咱们直接也去拿到他OK那么如果是这样的话那我们是不是就可以直接这样去转就可以了那转成一个String例型那么我们是不是这样的话就不用这样做强转了对吧直接拿到他一会儿我们测一下看行不行
[10:00] 好那么我们还有一个参数是不是叫optional这个name拿到它拿到它然后呢我们下面是不是就可以做一个这个构造了对吧然后呢我们把这个是不是就call过来把这个代码call过来往这一贴是不是就一样了就一样了然后下面这个代码是不是就不需要了哎呀OK好这样的话我们是不是就拿到我们这个参数了那么下面我们来看一下这个位置和这个位置它的这个
[10:30] 代码是不是都是一样的对吧所以我们是不是有必要去做一个抽取把它抽一下抽什么呢抽取它的一个查询的方法那么这个方法的返回值是不是就让它返回这个map就是我们那个标准的输出然后我们去做一个叫executeexecute什么的query然后我们去把这个是不是给它call过来那么call过来之后我们来看一下需要哪些内容首先第一个是不是就是叫query对吧
[11:01] 第二个呢是这个叫OptionName那么把这个拿过来然后呢第三个呢就是这个吧Able那么把Able呢这个Map这种类型那么这样咱们给他也拿过来或者说我们是不是可以这么来玩叫什么呢叫把这个Jason是不是可以拿过来叫Able Jason哎OK拿到他之后呢我们是不是在这个里面去做一个转换就可以了把它拿过来好那么做这样的一个转换
[11:31] 那么如果他有异常怎么办呢这个异常我们就给他去做一个抛出抛出这个异常然后呢让上面这个方法去做一个处理那么这个我们是不是就不需要了对吧不需要那我们就直接去调用类似点什么呢就是isq的query第一个呢是不是就query对象第二个呢就是玩第二个呢是来看一下第二个呢是这个objection name那么我们来看一下objection name
[11:58] 就他那第三个车是我们这个吧AbleSuggestOK好那么这样的话我们是不是就实现了我们这样的一个处理对吧哎OK好那么上面这个是不是也是一样对吧那么咱们把这个也给他靠过来啊也给他靠过来然后呢这个就不需要了达到账直接是不是就可以做一个return啊直接做一个return
[12:24] 好这样的话是不是就OK了好那么下面我们是不是就可以来做一个测试我们看它是否能够去处理我们船坞的这个变量的参数呢OK那么现在呢我们把这个服务器呢我们来重启一下啊重启一下走好那么现在我们重启好了我们来做一个测试啊那么现在呢我们通过这种方式去做一个测试那么这样我先去这个位置打一个断点
[12:51] 打一个正点然后我们来看一下他是否能够拿到我们所需要的参数走发起请求我们来看一下那么query那么现在是不是已经拿到我们查询的字幕创对吧是不是就是这样的一个字幕创OK看上面这个那就是这样的一个字幕创然后我们可以看一下viables是不是就拿到这样的一个字幕创没有问题OptionName是文档没有问题好然后我们进入到这个方法中
[13:20] 是不是我们自己写这个方法然后我们去做一个反序列化是不是得到了一个Able的这样的一个这样的一个map对吧map是不是也是OK的没有问题然后下面我们是不是就可以做一个执行了走走走走去做一个查询然后走我们来看一下返回的数据对不对返回数据来看一下那么这个数据是不对的你可以看到在这个位他提醒我们说message因为出错了一个message是
[13:48] 这个类型转化出处那么我们要求是浪类型我们刚刚在这个位置所定义的是硬的类型对吧显然是不对的所以把它改成浪我们再去发起请求走然后呢我们继续往下面走那这样我们直接通过看能不能查到数据呢可以发现是不是依然可以查询到数据啊哎呀OK那么这个是get请求我们来测试一下post请求看OK吗走那么post请求我们来看一下post现在有点问题啊那我们来看一下post请求不行
[14:17] 那么我这样我们打一个断点我们来看一下那么在这个位置他是否能够拿到我们的数据呢来看一下Post的请求Post请求没有进入吗来看一下他说是JSON却不能做一个反序列化一个java lang的一个什么的stream然后呢却不能去转那么不能去转的话那么我们就需要
[14:45] 给他这么来玩一下那么这个地方还不能怎么去转那就拿到谁呢拿到object拿到一个object就好了然后呢在这个位置我们就给他做一个强转既然上面这个位置他不能转那就做一个强转那么这样咱们把他去call过来然后呢这个也call过来好这样的话就搞定啊这样就搞定然后呢我们需要把他服务的重启一下走好那么重启之后呢我们来看一下那么点击这个发送请求走
[15:16] 那么现在我们可以看到请求是不是来了那我们看他拿的数据对不对然后query没有问题这个var evils那么可能会有问题了然后通过来看一下那么他报什么错他报的错误是不能去做转换就是说现在他本身就是一个map类型不能去转成是一个stream类型
[15:37] OK那么所以我们可以看到在这个位置他其实直接拿到的是不是就一个map所以我们就不需要去做一个转化了那么我们直接就拿到map然后来一个叫eboost这样的话他直接拿到既然是map
[15:54] 那就OK了那直接用就可以了但是要注意的是当我去传到这个里面的话那么要注意的是这个里面是不是还需要做一个转换所以说我们这个逻辑可能不能这么写了那么我们还要这样来写还是我们把这个丢到栅栏要求它传入的是一个map我们把这个逻辑再拿到最上面去让它自己做一个处理OK自己做一个处理那么把它传过去
[16:21] 好然后呢这个里面是不是就可以传入这个吧avos好这样的话就ok了这个位置呢是不是缺一个强转对吧缺一个强转那就转成这个map好了做一个强转ok好那么这样的话呢在这个里面呢去执行这个executioninput就可以了然后呢这个位置把这个咱们把这个异常这个抛出也给它去掉
[16:46] 这个里面他就没有异常的抛出对吧ok好那么我们再次重启Tomcat我们来做一个测试好那么现在重启好了我们来继续做一个测试然后走发起请求我们来看一下他拿到的一个参数然后我们往下面走下一步走拿到数据没问题走来看一下他是不是直接就能够拿到是一个map这样的一个对象那么我们直接去使用就ok了那么operation name这个显示就是none对吧然后我们去做一个执行然后
[17:16] 通过我们直接点这个通过吧走好通过那么我们来看一下这个里面是不是依然也是拿到数据了没有问题OK那么也就是说我们现在无论是get请求还是pose请求是不是都已经支持我们这种变量的这种形式OK那么其实我们这个测试并没有结束为什么呢我们来看一下如果我不使用变量我回到我最初的这个状态就是我直接就是一个我的查询我没有这个变量
[17:45] 对吧多了那么应该这么删把它删掉然后通过这种状态我们去做一个查询那么这个变量我们也不需要把它折掉然后这个ID我直接写死我就写成8好那么我在这个位置直接把它写成8写成8然后写成8然后我们再去发起pose请求看它会怎么样走那么在这个里面我们来看一下它拿到了query没有任何问题对吧是OK的然后继续往下面走
[18:14] 拿到这个by abos它呢是一个什么呢它也是一个它也是一个这个size为0的一个map没有问题那么obj也是也是那对吧没有问题然后那么通过走那么这样的话我们来看一下它能不能拿到数据呢依然是不是可以拿到数据啊那就意味着我们现在的这个是不是处理是不是已经就OK了对吧已经就OK了没有任何问题好那么这个那么没问题
[18:42] 那就没问题了那么我们看一下get请求测试一下看有没有问题走那么get请求进入在这个位置那么我们直接通过看他能不能查到数据呢依然也是OK的好那么也就是说我们现在已经兼容了有那个变量和没有变量的一个处理OK那么我们这个代码是吧就OK了好那么这个蒋义忠这个代码跟我们写这个代码呢也基本上是一样的OK
[19:07] 好那么也希望大家呢自己可以尝试着去写一下这样的一些代码啊那么这个就是我们的一个测试啊OK那么要记得是呃当我们这样测试通过之后你要去测一下没有这个变量的一个查询他到底OK不OK啊要记得把它测试一下哎OK好那么关于服务端去处理我们这个变量参数的一个讲解我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Boot 项目中通过 GraphQL 实现服务端参数处理，包括 GET 和 POST 请求的变量解析与执行。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中“2.3、服务端处理参数”章节，其中包含 GraphQL 变量示例 `{ "id": 8 }`。
画面2：展示 `GraphQLController.java` 文件中 `@GetMapping` 方法，接收 `query` 和 `variables` 参数，调用 `graphQL.execute`。
画面3：展示 `GraphQLController.java` 文件中 `@GetMapping` 方法，使用 `ExecutionInput` 构建并执行 GraphQL 查询。
画面4：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，尝试将 `variablesJson` 反序列化为 `Map<String, Object>`。
画面5：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，尝试将 `variablesJson` 反序列化为 `Map<String, Object>`，并构建 `ExecutionInput`。
画面6：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，使用 `JsonNode` 解析 JSON，提取 `query` 字段。
画面7：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，使用 `param.get` 获取 `query`、`variables`、`operationName`。
画面8：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，调用 `this.executeQuery` 方法。
画面9：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，尝试调用 `this.executeQuery` 方法，但出现语法错误。
画面10：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，调试时查看变量值，`variablesJson` 为 `{"id":8}`。
画面11：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，调试时查看变量值，`variablesJson` 为 `{"id":8}`。
画面12：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，尝试调用 `this.executeQuery` 方法，但出现语法错误。
画面13：展示 `GraphQLController.java` 文件中 `@PostMapping` 方法，尝试调用 `this.executeQuery` 方法，但出现语法错误。
画面14：展示 PDF 文档中返回的 GraphQL 查询结果，包含 `HouseResources` 对象的详细信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
{
  "id": 8
}
```

画面2：
```java
package cn.itcast.haoke.api.Controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import GraphQL.GraphQL;
import GraphQL.ExecutionInput;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GraphQLController {

    private GraphQL graphQL;

    private static final ObjectMapper MAPPER = new ObjectMapper();

    @GetMapping
    public Map<String, Object> query(@RequestParam("query") String query,
                                     @RequestParam(value = "variables", required = false)String variables,
                                     @RequestParam(value = "operationName", required = false)String operationName) {
        return this.graphQL.execute(query).toSpecification();
    }

    @PostMapping
    @ResponseBody
    public Map<String, Object> postQuery(@RequestBody String json) {
        try {
            return this.graphQL.execute(json).toSpecification();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
```

画面3：
```java
@GetMapping
public Map<String, Object> query(@RequestParam("query") String query,
                                 @RequestParam(value = "variables", required = false)String variables,
                                 @RequestParam(value = "operationName", required = false)String operationName) {
    ExecutionInput executionInput = ExecutionInput.newExecutionInput()
            .query(query)
            .operationName(operationName)
            .variables(variables)
            .build();
    return this.graphQL.execute(executionInput).toSpecification();
}
```

画面4：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody String json) {
    try {
        Map<String, Object> variables = MAPPER.readValue(json, MAPPER.getTypeFactory().constructMapType(HashMap.class, String.class, Object.class));
        Input executionInput = ExecutionInput.newExecutionInput()
                .query(query)
                .operationName(operationName)
                .variables(variables)
                .build();
        return this.graphQL.execute(executionInput).toSpecification();
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

画面5：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody String json) {
    try {
        Map<String, Object> variables = MAPPER.readValue(json, MAPPER.getTypeFactory().constructMapType(HashMap.class, String.class, Object.class));
        ExecutionInput executionInput = ExecutionInput.newExecutionInput()
                .query(query)
                .operationName(operationName)
                .variables(variables)
                .build();
        return this.graphQL.execute(executionInput).toSpecification();
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

画面6：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody String json) {
    try {
        JsonNode jsonNode = MAPPER.readTree(json);
        if (jsonNode.has("query")) {
            String query = jsonNode.get("query").textValue();
            return this.graphQL.execute(query).toSpecification();
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

画面7：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        String variablesJson = (String) param.get("variables");
        Map<String, Object> variables = MAPPER.readValue(variablesJson, MAPPER.getTypeFactory().constructMapType(HashMap.class, String.class, Object.class));
        JsonNode jsonNode = MAPPER.readTree(json);
        if (jsonNode.has("query")) {
            String query = jsonNode.get("query").textValue();
            return this.graphQL.execute(query).toSpecification();
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

画面8：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        String variablesJson = (String) param.get("variables");
        Map<String, Object> variables = MAPPER.readValue(variablesJson, MAPPER.getTypeFactory().constructMapType(HashMap.class, String.class, Object.class));
        ExecutionInput executionInput = ExecutionInput.newExecutionInput()
                .query(query)
                .operationName(operationName)
                .variables(variables)
                .build();
        return this.graphQL.execute(executionInput).toSpecification();
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

画面9：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        String variablesJson = (String) param.get("variables");
        String operationName = (String) param.get("operationName");
        return this.executeQuery(query, operationName, variablesJson);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面10：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        String variablesJson = (String) param.get("variables");
        String operationName = (String) param.get("operationName");
        return this.executeQuery(query, operationName, variablesJson);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面11：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        String variablesJson = (String) param.get("variables");
        String operationName = (String) param.get("operationName");
        return this.executeQuery(query, operationName, variablesJson);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面12：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        Map variables = (Map) param.get("variables");
        String operationName = (String) param.get("operationName");
        return this.executeQuery(query, operationName, variables);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面13：
```java
@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try

