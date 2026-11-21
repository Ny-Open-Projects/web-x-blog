# 06_动态ip代理池管理_检验ip2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\06_动态ip代理池管理_检验ip2【海量资源尽在 666java.com】.mp4
- 时长 5分31秒（音频 331s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好这个方法咱们可以去写个注释说什么呢?
[00:04] 教验教验IP是否可用好这个IP该怎么去教验呢?
[00:10] 其实刚才咱们说了这时候你主要是通过谁?
[00:14] 通过当前这个地址然后去教验当前的IP到底可用或者不可用然后下面咱们就可以去写一下其实这个工具列咱们已经有了咱们在这先去给他得对象
[00:29] 设置一个setable先让他不能用都不能用能用的时候咱们可以再设置回来好吧然后下面咱们就可以先去使用一个对象对象就是有个叫plussy lsy polydate这个对象其实咱们之前没见过我简单说一说用一个plussy polydate需要两个参数一个是当前的什么IP好第二个是当前的
[01:00] 就是端口号这样的话你就拗出来了当前的对象这对象可以看一眼这边是包含了host还有啥呢还有当前的错误码还有什么耗时时间还有错误信息好就这些东西它主要是封装了这几个参数那封装这几个参数有什么作用呢其实这时候咱们就可以干嘛呢就可以调用一个工具类
[01:29] 工具链的叫ProxyUtils是咱们自己这个Utils没有吗?
[01:37] 点儿这边有一个ValidateProxyIP你看到了吗?
[01:45] 它传的参数就是当前的ProxyValidate这个校验完之后呢你看可以看一下里边的代码来点进去这个就是复取了当前这个验证的URL其实就是它
[02:03] 就是他啊然后呢我要看啊然后呢然后就是这块内容啊这块呢就是去发了一个请求去发了一个请求啊这个请求呢可以看一下请求呢其实就是一个http client然后呢去发了个请求最终呢他会会响应一个东西那响应里边呢其实就包含两部分内容啊第一个是他的一个response啊当然其实咱们要一个就可以了这个最主要的就是当前这个result code
[02:33] 这个 code 其实就是说要是200的话才算是成功如果说不是200的话咱们统一都说当前的 IP 不可用所以说现在这个事就简单了然后下面咱们该怎么去写呢当然咱们也可以在这去写东西try然后把这句话放进去好吧有错误信心的咱们可以打印出来c hexcept然后咱们在这去打印 log.error
[03:06] 然后是一点get message好吧行那这样啊如果说你这部批准过之后呢咱们就可以去判断了啊那哪个呢判断当前plausi wallet批准完之后呢点有一个叫做get result code等于等于200的时候呢这时候就是成功了那成功的话怎么办呢成功的话呢输了你就把它重新设置为啥呢重新设置为好那这样的话这个IP啊是可用的
[03:39] 好那可用之后呢这时候呢咱们下面就可以继续往下看继续可以更新当前那个IP啊你这个IP啊已经能用了啊这时候呢咱们可以去设置setcode那这个code呢其实就是刚才咱们这个什么proxy.possibility.getresultcode好吧第二个呢咱们还可以设置一个东西set一个那种执行时间执行时间啊执行应该是秒数啊到底是
[04:09] 想用多长时间你可以去找到drget这样的话咱们就算是设置完了那设置完之后其实咱们也可以去设置一个错误上去万一他错了呢万一没走这一步是不是就错误信息所以说咱们在这儿然后有一个叫做set error这时候你就可以把前那个plotit.get error
[04:41] 那这个咱们是一个有可能会出现问题有可能会出现问题所以说您在这加个吐司润这样也可以这个是吐司润吗我看这本身就是死润是吧那这样咱们就不用再去设置了好吧不用再去设置了这块其实咱们在这去专门设了一个东西这个东西是啥呢可以看一下就是说这里边是有一个这种长度的限制防止这个
[05:10] 长度超了所以说呢咱们在这去加了一个这么个限制好咱们就把它呢给考过来这尝试多大呢70好吧那这样的话咱们就算是完了那这个验证IP的可用性啊咱们这个也写完了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现代理 IP 的校验与管理功能，包括创建校验类、调用工具类进行验证、并根据结果更新代理池状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 ProxyIpManager.java 中，展示代理 IP 校验的逻辑，包括判断代理是否可用并更新代理池状态。
画面 2: 代码光标移至 validateProxyIp 方法内部，准备编写校验逻辑。
画面 3: 在 validateProxyIp 方法中，创建 ProxyValidate 对象。
画面 4: 切换到 ProxyValidate.java 文件，查看其构造函数和成员变量定义。
画面 5: 在 ProxyIpManager.java 中，使用 Ctrl+Shift+Space 自动补全 ProxyValidate 类。
画面 6: 切换到 ProxyIpUtils.java 文件，查看 validateProxy 方法的实现，其中包含资源文件读取和 HTTP 请求处理。
画面 7: 在 ProxyIpManager.java 中，调用 ProxyIpUtils.validateProxy 方法进行代理校验。
画面 8: 在 ProxyIpManager.java 中，编写 try-catch 块，捕获校验过程中的异常。
画面 9: 在 ProxyIpManager.java 中，使用 if 条件判断校验结果是否为 200。
画面 10: 在 ProxyIpManager.java 中，为 ProxyValidate 对象设置返回码和持续时间。
画面 11: 在 ProxyIpManager.java 中，为 ProxyValidate 对象设置错误信息。
画面 12: 在 ProxyIpManager.java 中，为 ProxyValidate 对象设置错误信息，并调用 setFixedLengthString 方法。
画面 13: 在 ProxyIpManager.java 中，为 ProxyValidate 对象设置错误信息，并调用 setFixedLengthString 方法。
画面 14: 在 ProxyIpManager.java 中，为 ProxyValidate 对象设置错误信息，并调用 setFixedLengthString 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
//如果原始协议以及当前协议都不可用，则为临时性的代理，删除
if (nodeable && !clipPool.getEnable()) {
    log.info("删除代理ip,ip: {},port: {},clipPool.getIp(),clipPool.getPort());
    crawlerIpPoolService.updateCrawlerIpPool(clipPool);
} else {
    crawlerIpPoolService.updateCrawlerIpPool(clipPool);
    log.info("更新代理ip,ip: {},port: {},clipPool.getIp(),clipPool.getPort());
}
```

画面 2:
```java
//校验ip是否可用
@Param clipPool
private void validateProxyIp(clipPool clipPool) {
```

画面 3:
```java
ProxyValidate proxyValidate = new ProxyValidate();
```

画面 4:
```java
public class ProxyValidate {
    public ProxyValidate() {
    }

    public ProxyValidate(String host, int port) {
        this.host = host;
        this.port = port;
    }

    //主机
    private String host;
    //端口号
    private int port;
    //错误码
    private int returnCode;
    //错误信息
    private String error;
    //持续时间
    private long duration;
```

画面 5:
```java
ProxyValidate proxyValidate = new ProxyValidate();
```

画面 6:
```java
import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ProxyIpUtils {
    private static final ResourceBundle resourceBundle = ResourceBundle.getBundle("crawer");
    private static final String reqUrl = resourceBundle.getString("proxy.validate.url");

    public static void validateProxy(ProxyValidate proxyValidate) {
        log.info("开始校验代理IP: {} : {}", proxyValidate.getHost(), proxyValidate.getPort());
        long currentTime = System.currentTimeMillis();
        String errorMessage = null;
        int resultCode = 404;
        try {
            resultCode = processRequest(CrawlerProxyFactory.getHttpProxy(proxyValidate.getProxy()));
        } catch (IOException e) {
            errorMessage = e.getMessage();
        }
    }
```

画面 7:
```java
ProxyIpUtils.validateProxy(proxyValidate);
```

画面 8:
```java
private void validateProxyIp(clipPool clipPool) {
    clipPool.setEnable(false);
    ProxyValidate proxyValidate = new ProxyValidate(clipPool.getIp(), clipPool.getPort());
    try {
        ProxyIpUtils.validateProxy(proxyValidate);
    } catch (Exception e) {
        log.error(e.getMessage());
    }
}
```

画面 9:
```java
if (proxyValidate.getReturnCode() == 200) {
    clipPool.setEnable(true);
}
```

画面 10:
```java
clipPool.setEnable(true);
clipPool.setReturnCode(proxyValidate.getReturnCode());
clipPool.setDuration(proxyValidate.getDuration());
```

画面 11:
```java
clipPool.setEnable(true);
clipPool.setReturnCode(proxyValidate.getReturnCode());
clipPool.setDuration(proxyValidate.getDuration());
clipPool.setError(proxyValidate.getError());
```

画面 12:
```java
clipPool.setEnable(true);
clipPool.setReturnCode(proxyValidate.getReturnCode());
clipPool.setDuration(proxyValidate.getDuration());
clipPool.setError(proxyValidate.getError());
clipPool.setFixedLengthString(proxyValidate.getError(), 70);
```

画面 13:
```java
clipPool.setEnable(true);
clipPool.setReturnCode(proxyValidate.getReturnCode());
clipPool.setDuration(proxyValidate.getDuration());
clipPool.setError(proxyValidate.getError());
clipPool.setFixedLengthString(proxyValidate.getError(), 70);
```

画面 14:
```java
clipPool.setEnable(true);
clipPool.setReturnCode(proxyValidate.getReturnCode());
clipPool.setDuration(proxyValidate.getDuration());
clipPool.setError(proxyValidate.getError());
clipPool.setFixedLengthString(proxyValidate.getError(), 70);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

