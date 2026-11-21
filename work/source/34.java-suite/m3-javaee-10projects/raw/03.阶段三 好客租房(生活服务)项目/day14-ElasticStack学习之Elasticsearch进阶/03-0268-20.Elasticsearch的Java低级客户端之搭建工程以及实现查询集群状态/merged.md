# 20.Elasticsearch的Java低级客户端之搭建工程以及实现查询集群状态

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\20.Elasticsearch的Java低级客户端之搭建工程以及实现查询集群状态【海量资源尽在 ubkz.com】.mp4
- 时长 11分43秒（音频 703s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们首先来学习的是REST的低级的客户端它呢就更接近于我们直接通过浏览器工具去访问啊,这种方式那我们来首先创建工程,我们来去写一些它的一些这个demo啊大家就能够理解它是怎么去用的了然后呢,GrabID,那么我们把它称之为就叫CNDITCastES吧然后呢,ArtifactID,那就叫ITCast-ES
[00:28] 那拷贝一下然后呢到这儿然后呢点击finish完成好那么这个我们工程呢就创建好了好那么工程创建好了然后呢别忘记这个地方我们是不是要去打一个把这个enableauto import把它去自动导入然后呢我们去接下来导入一些所需要的一些依赖那么我们就参考我们的讲义吧去导入一些所需要的一些依赖然后呢我们来看一下那么首先呢我们先把下面的这个build我们先
[00:57] 拷贝过来就是我们的一个指定我们的一个Java编译在哪个插件然后把它拷贝过来然后导照ok好嘞那么这个是不是指定我们的JDK的版本是1.8然后导入一些相关的一些依赖那么首先第一个需要导入的就是我们这个elastic rest client这个就是默认的它就是低版本或者低级的这样一个客户端那么把它拷贝过来
[01:26] 把这个JUD这些拷贝过来这个我们拷过来吧因为为什么我先拷贝过来再说那么我们为什么要去在这个位置去导入一个Jackson这样的一个包呢对前面我们说过低级的客户端呢是不是需要我们手动去做一些这个Jackson的一些这个分装那么我们可以借助于Jackson这个包工具包来做一些分装好嘞那么现在我们所需要的依赖导入进来了检查一下有没有那么在这个里面看一下是不是这个导入进来了OK
[01:55] 导入进来了那么导入进来之后呢我们是不是就可以去编写一些我们的测试用力对吧好那么接下来呢我们就在test下面啊在这个里面我们去编写一些测试用力那么我们首先创建一个包吧这个包呢就叫cn.itcast然后呢es然后呢所有的测试用力呢我们都把它丢到这个里面来啊ok好那么下面呢我们就写这样的一个测试用力那么就叫那么写一个吧
[02:25] 这叫什么呢叫testrestapi好那么我们写了这样的一个测试用例那么接下来我们来测试一下那么在我们的restapi里面最核心的一个对象就叫什么呢或者类就叫restclientrestclient然后我们去我们去这个不能注入那么我们并没有使用spam然后在这个位置我们就要去写一个
[02:56] 初始化的方法初始化的方法然后呢这个位置来一个什么呢就叫before吧在执行之前我们对这个client做一些初始化那么这个client怎么来的呢它是需要它等于什么呢它是需要一个client一个build去做一个构建那么我们还需要去定义一个restclient一个build对象那么build对象那么这个这个build对象它是怎么来的呢
[03:24] 他要通过rest client下面有一个build去给他去设置一个http post这样的对象那么我们去做一个设置然后就通过一个build去得到那么这个里面我们就需要给他设置多个new一个http post这样的一个对象那么这个对象我们需要去传递是不是传递我们的hosthost就是172
[03:54] 点16.55.185当然这个地址根据你的地址来然后呢第二个设置端口端口呢就是9200OK那么我们再来添加一个加一个逗号再来加一个那么这个位置加个逗号那么92009201和9202对吧那么我们是有三个那么有了这个build之后呢我们就可以通过它呢去点build得到一个我们的client对象那么有了这个client对象就可以去做一些操作了
[04:24] 那么其实呢我们可以在build这个里面呢再去设置一些比如说啊像这个fail的一个listener那么就去做如果说我们请求失败或者说有些失败处理的话那么会执行我们在那个监听器啊那么可以演示一下吧set一个set一个fail的一个listener然后呢去做一个new一个啊这样的一个listenerok然后呢我们再
[04:52] 这个里面啊再给他去重写啊他的一些这个方法那么我们给他去重写一些他的比如说这个叫比如说unfail这个方法那么在这个里面呢就是如果我们要是出错的话咱们可以打一句话就是出错出错然后呢加一个这个node哎OK把它输出出来就可以了好嘞那么这样的话呢我们就已经基本上完成了一个初始化初始化那么
[05:25] 这个呢就是我们的一个before那么我们其实有了这个before之后我们应该还写个什么呢就这个client它应该是要需要把这个client关闭掉如果我们用完之后把它需要关闭掉所以我们还应该写一个close这个方法那么这个方法呢是在什么时候之前呢可以来一个after然后呢我们就要用this.restclient.close那么我们在这个位置需要去先抛出一长吧抛出一长
[05:54] 哎抛出异常那么我们这个地方加一个注释就是说这个关闭的操作它应该在哪里关闭呢它应该是我们跟随跟随我们这个应用程序的启动关闭而关闭这个大家能够理解吧就是比如说假设我们用了Spring的话那么是不是应该在Spring容器启动的时候呢做一个创建然后呢我们Spring容器去销毁的时候呢去把它关闭掉是这样的意思啊好那么接下来呢我们就可以在下面呢是不是
[06:25] 写一些我们相关的一些操作对吧那么这个操作呢就跟我们去实际上去做这样的操作也是都一样了啊比如说啊那么我们是不是可以去查询一下我们集群的这样的一个状态哎这个状态现在没有了吗那么我们来看一下啊那么看一下我们这个例子啊那么我们是不是可以去查询一下我们的集群的一个状态那么怎么查询呢我们把它拷过来然后呢发起一个get请求那么往这一丢
[06:55] 走那么这样的话呢是不是就会查询到我们集群的一些这个信息那么我们呢这个是通过我们的浏览器的一个在那个插件是不是去完成的那么通过我们这个API呢它也是一样的啊怎么做呢我们来看一下我们写一个方法啊叫test叫info吧那么查询我们的一些集群的一些信息加一个test注解然后呢在这个里面是不是就需要去编写一些相关代码去做一个操作啊在这个里面呢我们就通过race.restclient什么呢
[07:25] preform request给它去添加一个request对象那我们来看一下这个request对象它是一个什么样的对象呢就是request对吧那么我们就去定义一个requestrequest然后呢request它等于new一个request那么在这个里面呢我们需要给它指定两个参数那么一个呢就是我们的method你要发起什么请求
[07:52] 另外一个就是我们请求的一个目标或者说我们的一个路径那么在这个里面我们给它设置的第一个就叫它是get请求那么第二个就我们刚刚所拷贝的路径把这个路径也拷贝过来那就它把cluster一个state路径拷贝过来那么然后我们就交给它就可以了交给它然后我们来看一下它是有异常异常我们就直接抛出
[08:19] 把它抛出一场然后呢我们来看一下它的一个返回值那么返回值是一个response那么前面我们说过response呢需要我们手动处理对吧那我们就直接打印吧那么responseresponse.get比如说可以查看它的一个状态对吧然后呢这个地方我们加一个打印吧叫请求成功了请求成功成功了不能叫成功啊完成
[08:50] 然后呢去加一个他哎OK好嘞嗯扫一个扫一个加号啊哎OK然后呢我们在下面再来打印打印什么呢打印我们的请求体就响应体对吧点get什么get这个edit那么这个get的edit呢它呢得到的是一个http这样的一个edit那么所以我们需要一个工具类啊就叫editedit utils
[09:23] 有个utils点to一个什么呢stream把它转成一个字符串哎呀OK好嘞那么我们来测试一下看它会输出什么样的一个信息呢来看一下OK那么这个结果呢就已经结束完成请求完成了那么我们可以看到在这一行的打印处呢是我们的这个第一句啊就是我们这个请求已经完成了它的状态码呢是200然后呢下面这个呢是不是就是我们请求的内容啊
[09:54] 对吧请求内容那么我可以把它贴出来丢到这个里面来看一下然后format一下因为内容比较多然后可以看到有这么多的一些信息对吧OK这个就是服务端给我们响应回来的一些信息那么可以看到在这个位置是可以看到我们的一些集群的node里的信息对吧这个信息这个信息OK好嘞那么其实我们演示这种其实告诉大家就是说是不是跟我们去做我们的一些
[10:25] 就是我们通过这样的一些客户端工具访问那么其实是非常的类似非常类似当然了我们也可以在我们的这个request里面去添加一些参数比如说我们去按的一个parameter什么参数呢比如说我们可以让它去美化一下对吧party然后去设置它是一个true然后我们去再执行OK那么现在它已经就已经就反应
[10:55] 响应回来了对吧那我们来看一下响应的一个结果那么显然是做了一些这个美化对吧做了一些美化OK好嘞好那么这个呢就是我们所写的第一个这个例子第一个例子其实我们跑这个第一个例子之后大家应该也就基本能够明白了那么我们其实在这个位置来写我们的这个endport就是我们请求的一个路径然后设置一个方法然后添加一个参数然后呢我们再去
[11:22] 做一个这样的一个请求拿到一个响应那么拿到响应之后呢你该怎么玩就怎么玩了那么所以这个是相对比较低级的这样的一些这个客户端那么就是非常纯粹的去分装了一个rest这样的一个客户端ok好那么关于一个最基本的一个使用呢我们就先讲到这里那么后面的一些这个一些其他的例子呢我们后面再讲

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建并编写一个测试类，使用 Elasticsearch 的 RestClient 客户端进行 HTTP 请求，并通过 JUnit 进行测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 打开 IntelliJ IDEA，选择项目 "itcast-es"。
画面 2: 显示 pom.xml 文件内容，包含依赖项，如 junit、jackson-databind。
画面 3: 显示 pom.xml 文件中 <build> 部分，包含 <plugin> 配置，用于 Maven 编译。
画面 4: 创建 TestRestApi.java 文件，开始编写测试类。
画面 5: 在 TestRestApi.java 中导入 RestClient 和 RestClientBuilder，并开始编写初始化方法。
画面 6: 在 TestRestApi.java 中，为 RestClientBuilder 设置失败监听器。
画面 7: 在 TestRestApi.java 中，使用 HttpHost 构造函数设置 Elasticsearch 的主机和端口。
画面 8: 在 TestRestApi.java 中，完成 RestClient 的构建并设置失败监听器。
画面 9: 在 TestRestApi.java 中，添加 close() 方法用于关闭客户端。
画面 10: 在 TestRestApi.java 中，添加 testInfo() 方法，用于发起 HTTP 请求。
画面 11: 在 TestRestApi.java 中，使用 Request 类创建请求对象。
画面 12: 在 TestRestApi.java 中，使用 RestClient 发起请求并处理响应。
画面 13: 在 TestRestApi.java 中，为 testInfo() 方法添加参数，用于测试。
画面 14: 在 TestRestApi.java 中，运行 testInfo() 方法，显示测试通过并输出响应内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
</dependency>

<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.9.4</version>
</dependency>
```

画面 3:
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.2</version>
        </plugin>
    </plugins>
</build>
```

画面 4:
```java
package cn.itcast.es;

import org.Elasticsearch.client.RestClient;

public class TestRestApi {

}
```

画面 5:
```java
import org.Elasticsearch.client.RestClient;
import org.Elasticsearch.client.RestClientBuilder;
import org.junit.Before;

public class TestRestApi {
    private RestClient restClient;

    @Before
    public void init() {
        RestClientBuilder restClientBuilder = Re
```

画面 6:
```java
restClientBuilder.setFailureListener(new
this.restClient = restClientBuilder.build();
```

画面 7:
```java
new HttpHost(hostname: "172.16.55.185", port: 9200,
new HttpHost(hostname: "172.16.55.185", port: 9201)
```

画面 8:
```java
@Override
public void onFailure(Node node) {
    System.out.println("出错 -> " + node);
}

this.restClient = restClientBuilder.build();
```

画面 9:
```java
@After
public void close() throws Exception {
    // 网络应用的关闭而关闭
    this.restClient.close();
}
```

画面 10:
```java
@Test
public void testInfo() {
    Request request = new Request();
    this.restClient.performRequest();
}
```

画面 11:
```java
Request request = new Request();
```

画面 12:
```java
@Test
public void testInfo() throws IOException {
    Request request = new Request(method: "GET", endpoint: "/cluster/state");
    Response response = this.restClient.performRequest(request);
    System.out.println("请求完成 -> " + response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面 13:
```java
@Test
public void testInfo() throws IOException {
    Request request = new Request(method: "GET", endpoint: "/cluster/state");
    request.addParameter(name: "pretty", value: "true");
    Response response = this.restClient.performRequest(request);
    System.out.println("请求完成 -> " + response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

画面 14:
```java
@Test
public void testInfo() throws IOException {
    Request request = new Request(method: "GET", endpoint: "/cluster/state");
    request.addParameter(name: "pretty", value: "true");
    Response response = this.restClient.performRequest(request);
    System.out.println("请求完成 -> " + response.getStatusLine());
    System.out.println(EntityUtils.toString(response.getEntity()));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

