# 3.12 设备数据处理 - 客户端数据模拟

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day3 数据采集服务
- 源文件：06.阶段六 冷链监控平台项目\day3 数据采集服务\3.12 设备数据处理 - 客户端数据模拟_【海量资源尽在 666java.com】.mp4
- 时长 18分45秒（音频 1126s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好我们在前面给大家介绍了设备冷链设备监控平台里边有一个非常重要的节点就是我们native服务器它用来接收设备提交的报文数据而这个报文数据的格式呢是一个用竖斜杠分割的字符串那么这个字符串其实是不能或者说不容易把它转换成我们的这种叫加网对象
[00:28] 我们家屋对象和JSON字符串是非常容易的进行转换的所以呢我们NetE服务器接收到我们的设备发送过来的数据之后呢我们要把它转换成JSON字符串同时把它发送到Kafka堆列里面去那这样的话就是我们一个需要开发两个程序一个是设备的一个模拟端我们模拟一下设备来发送报文数据另外一个就是我们的NetE服务器接收数据转换数据和发送数据
[00:54] 这样的一个过程那么下面我们来开发我们的设备端的发送发送程序我们在前面给大家介绍内提客户端和服务器端的程序示例的时候我们当时开发了一个示例代码而这个示例代码里边我们发送的报为呢是一个测试数据就是非常简单的测试数据这样的一个程序那么下面我们来开发我们发送过去的一个数据也就是说我们模拟的数据
[01:24] 那么在这个过程里边我给大家提前把我们的message entity这个对象给它添加好了而添加这个对象之后呢它就是包含了我们报文的里边的各个的字段这个字段我们没有添加get set的方法因为我们使用了一个add data这个注解而这个add data注解呢是一个lanbook的这样的一个jar 包它提供了一个功能我们把这lanbook
[01:51] 给引入到我们工程之后呢我们就可以在我们的实体对象里边添加at date这样的一个注解不用编写我们的get set方法了那下一个我们需要引入的就是我们的就是我们的那个json字符串而json字符串的一个格式是因为我们要把我们的我们的加入对象和我们的json字符串进行关联我们看一下我们的json字符串我们需要把它
[02:18] 添加进来接着这份证我们使用的是一个叫fastjson我们在这里面把fastjson给他添加进来那么后面还有一个卡不卡是需要我们把服务器端接收程序里面用到的我们今天只用到了一个叫lanbook还有一个我们的fastjson那我们来看一下我们的client handler
[02:42] Client Handler里边我们希望在这个程序里边能够给我们怎么说呢能够给我们添加一下我们的这个随机模拟的数据而这个随机模拟数据我可以使用一个我们的构造函数也就是Client Handler里边我们可以给它加一个构造函数这个构造函数里边把我们想要传递的数据给它添加进来那我们
[03:11] 定义一个变量这个变量叫做message就是我们要发送的数据而我们添加我们的构造函数client handler然后我们有一个参数叫做message这个时候我们就可以把我们的message复制给我们复制过来了那复制过来之后呢我们在我们的channel active这个方法里边
[03:44] 我们就直接使用我们的这个message了这是我们的client handler里边要添加的一个东西那下一步的情况下我们需要在我们的client程序里边或者说我们在另外一个程序我们需要添加在这里边我们需要添加一个message而这个message到底是个什么呢我们需要构造我们的构造设备模拟数据
[04:19] 比如说我们在这儿我们定义一个变量message等于那么我们在我们的newclient的时候我们就可以添加这个message了对吧而这个说这个模拟数据呢我们可以直接就是说我们用我们的这个数据的格式来给的给的添加进来我们看一下数据的这个格式这个数据格式是sht然后后边是1s幅刷sht然后
[04:51] 包括我们的这个设备的编码对吧设备编码可能会有很多啊我们随机随机写一个然后温度的数据20度然后湿度的数据89%然后再来我们设备的状态1然后再加上我们当前的一个时间对吧我记得是当前的一个当前的一个时间2019090912
[05:21] 1200这样的一个数据那么最后的话我们再加上一个我们的结尾的符sh5sh5l后面我看看是什么b1.2.1.2b1.2.1.2这样的一个
[05:54] 此时我们在发送数据的时候我们就把这个字符帅给他发送过来了对不对那但是有一个问题是说我们希望这个模拟程序这个模拟的数据是一个可变的而这个可变的情况下那么我们就希望哪些东西变了实际上是这个是传递过来的这个是可变的这个温度湿度状态这个值是可变的而我们的时间呢是直接根据当前的时间来创建就行了那下一步我们就开发一个一个
[06:25] 函数我们这个函数呢是模拟是产生模拟的这个数据模拟的报文数据那么我们定义这个函数string get message那么get message的情况下我们再来看一下我们这个报文这个报文里边我们希望给它传递过来的是什么呢或者说我们
[06:58] 温度湿度我们可以是模拟的但是我们的这个设备的编码其实我们在我们的系统库里边系统的设置里边有一个设备的编码我们要给它设置设置一个设备的时候我们可以增加一个设备那么设备是有编码的我们在这里边把我们的编码给它添加进来也就是说我们的这个设备编码是作为我们这个函数的一个一个参数我们的使用
[07:29] meter stringmeter code那在这里边的时候我们就可以增加我们的这个增加我们的字符串了而这个字符串呢我们希望的是使用我们的一个message也就是对象来对它进行转换的在提前我已经把这个message给它添加进来了对吧我们现在就只需要我们定义一个messagemessage entity我们是
[08:04] 这个对象这个对象等于6一个message.entity然后我们设置我们的set我们的metacode那下面的话我们就设置设置随机温度设置随机湿度然后设置随机状态接着是我们要设置当前时间然后最后我们把我们的
[08:58] 我们的这个对象给它返回过来就是对象的一个我们要return一个字符tryreturn m1.m1.什么呢device message这个device message实际上是说我们要把我们这个字符try要转换这个加个对象要转换成一个字符try而这个转换字符try的这个过程我们需要在我们的函数里边或者说我们在实体里边要添加进来因为我们
[09:29] 使用Lambook已经把我们的get set的方法给它取消掉了或者说是不用写了但是我们需要添加一个就是叫什么呢叫做get message吧也就是说把当前的对象我要转换成一个字符串那么我们可以添加一个string buffer然后sp等于new string buffer然后此时我们要给它添加
[10:12] 我们的字部上了SHT然后我们可以一直给它添加上点append那么这append呢我们加上一个数学杠然后再appendthis.getmetacode那同样道理我们一直给它添加我们所有的字段我们要添加我们的getterm温度
[11:08] 我们再给它添加我们的湿度然后我们还可以给它添加我们的这个叫状态值再包括包括我们的这个精度和纬度精度纬度然后最后再加上我们的结尾幅而这个结尾幅呢是叫做SH5L1.2
[12:22] 点12OK然后此时我们要把它转移过来托斯军那么经过这个过程呢我们其实就可以把加了对象转换成我们的一个字符刷了而我们在这里边我们就可以使用message点get我们的message对吧那么我们回到我们的这个函数里边我们在这个过程里边我们的message就
[12:59] 能够直接使用我们这个方法get msg然后这个时候我们要给它传入一个code加上这个code的话是me001 002 1234等等这样的一个我们就可以传过来那下面的话我们就需要把我们的随机温度随机湿度和随机状态给它添加进来了那么这个随机温度呢我们可以使用一个
[13:25] 加网里边JDK它本身就提供了一些random的一些方法然后我们在这里边给大家只是简单的说一个其实就OK了那我们get random的这个方法呢我们可以因为温度是比如说从零下20度或者零下50度到120度这样的一个范围内那我可以随便的但是湿度的话可能是说我从0%到100%这个也是不一样的那我可以在这里边我
[13:55] 创建一个随机的数字啊也就是说我们再增加一个方法而这个方法呢是获得两个数字间的随机数字那在这里我就可以定义一个get random那么get random的话我们有一个最小的然后再来一个最大的
[14:30] 数字然后呢我们的random我们就定义一个random等于newrandom当然这是只是我写的一个小方法然后呢大家可以用其他方法来实现我们的random的就是随机数字的一个生成第二nextint然后呢我们使用的叫我们的叫最大的然后呢我们再除以一个最大的减最小的然后再加1
[15:05] 然后再加上我们的最小最后我们再把这个i-fi回过来这个我们就可以获得了两个数字之间的一个最大值最小值那么我们随机温度的时候我们就可以在这里边来添加了那么我最大值比如说我在这里边我设置m1.set我们的温度我可以使用get randomrandom什么呢random我们从100最小的话应该是最小-100
[15:38] 那么到我们最大的到100度那么在这个数字里边我可以增加一个这个时候我们就就把我们的这个温度值给添加进来了湿度的话一样道理那么我们要使用这个set我们的湿度而这个湿度我可以用从0到100就是getrandom的一个0到100OK我们就把湿度给它添加进来了那下一步的话我们再使用一个我们的
[16:10] 这个随机状态而这个随机状态呢我们可以使用什么呢我们可以定义一个状态我们定义状态我们使用了是要把这个数字integerinteger.value of我们要把它get random那么从0到100然后除以3那我就把我们的这个状态给它设置上了
[16:47] 下面设置我们的当前时间当前时间的这个设置也比较简单一些我们使用simple data format这个类型format等于new simple format然后这个呢实际上设置我们当前时间的格式我们使用年月日时分秒这种格式然后下一个的话我们就设置一个data而这个data呢等于new data
[17:20] 然后使用我们的system.currenttime这个方法而这个方法呢实际上是获得的是一个毫秒级别的这个时间然后我们再设置我们的这个时间format.format这个时间这样的话就把我们整个整个的这个模拟产生报文的
[18:05] 这个字符串就创建上了那下一步的话我们就可以把我们的这个程序再启动一下然后我们再看一看因为我们在上一次我们发送报文的时候我们要启动我们的服务器端然后启动服务器端的时候我们再启动客户端我们就能够得到我们这个数据了我们先来看一眼我们把服务器端启动起来然后我们再启动我们的客户端OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于Netty的客户端-服务端通信程序，包括需求分析、客户端连接配置、消息实体类设计以及服务端启动代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示需求分析PPT，包含系统架构图，涉及硬件设备（如GPS、SIM卡）、Netty服务端、Kafka、Flink、Redis、Mysql、Druid等组件，以及一个示例报文格式。
画面2：展示服务端代码结构，定义了实体对象MessageEntity类，包含serialVersionUID、metercode、hostid等字段。
画面3：展示ClientHandler类的代码，定义了客户端连接服务的connect()方法，开始配置Netty的EventLoopGroup、Bootstrap等。
画面4：继续展示connect()方法，配置ChannelOption.SO_KEEPALIVE和handler(ChannelInitializer)，并设置设备报文。
画面5：在connect()方法中，设置设备报文字符串msg，内容为“SHT11200123301[20189][2019090912109]SSSL_1_0”。
画面6：在connect()方法中，添加连接服务器的代码，调用bootstrap.connect(ip, port)。
画面7：展示Client类的main方法，用于启动客户端。
画面8：在Client类中，定义了getMsg方法，用于生成模拟报文。
画面9：在getMsg方法中，定义了MessageEntity对象，并设置其属性。
画面10：在Client类中，调用getMsg方法生成报文，并连接服务器。
画面11：在getMsg方法中，设置设备的IP地址。
画面12：在getMsg方法中，设置设备的随机湿度和随机状态。
画面13：在getMsg方法中，设置设备的随机状态，并调用ms.setState(state)。
画面14：展示Server类的代码，用于启动Netty服务端，监听指定端口。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
报文格式转换：
{
  "tctime": "20190901185717",
  "term": "0K",
  "hardware": "SHT11200123301",
  "data": "20189",
  "time": "2019090912109",
  "sssl": "SSSL_1_0"
}

画面2：
public class MessageEntity implements Serializable {
    private static final long serialVersionUID = 1L;
    /**
     * 设备码
     */
    private String metercode;
    /**
     * 设备主题
     */
}

画面3：
import java.nio.ByteBuffer;
public class ClientHandler extends SimpleChannelInboundHandler<ByteBuf> {
    private String msg;
    public ClientHandler() {
        this.msg = "SHT11200123301[20189][2019090912109]SSSL_1_0";
    }
    @Override
    public void channelRead0(ChannelHandlerContext ctx, ByteBuf byteBuffer) throws Exception {
        // 处理接收到的数据
        String str = byteBuffer.toString(StandardCharsets.UTF_8);
        System.out.println("收到数据：" + str);
    }
    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        cause.printStackTrace();
        ctx.close();
    }
}

画面4：
public void connect() {
    //1. 定义线程池
    EventLoopGroup worker = new NioEventLoopGroup();
    //2. 定义引导器
    Bootstrap bootstrap = new Bootstrap();
    //3. 配置启动的属性
    bootstrap.group(worker)
            .channel(NioSocketChannel.class)
            .option(ChannelOption.SO_KEEPALIVE, true)
            .handler(new ChannelInitializer<SocketChannel>() {
                @Override
                protected void initChannel(SocketChannel ch) throws Exception {
                    //4. 让处理程序
                    // 根据设备报文
                    String msg = "SHT11200123301[20189][2019090912109]SSSL_1_0";
                    ch.pipeline().addLast(new ClientHandler(msg));
                }
            });

画面5：
String msg = "SHT11200123301[20189][2019090912109]SSSL_1_0";

画面6：
//5. 连接服务器
ChannelFuture future = bootstrap.connect(ip, port);
future.channel().closeFuture();

画面7：
public static void main(String[] args) {
    //启动客户端
    new Client("12.0.0.1", port:10010).connect();
}

画面8：
private String getMsg(String meterCode) {
    MessageEntity me = new MessageEntity();
    me.setMetercode(meterCode);
    //设置随机湿度
    //设置随机温度
    //设置随机状态
    //设置当前时间
    return me.getMessage();
}

画面9：
public String getMessage() {
    StringBuffer sb = new StringBuffer();
    sb.append("SHT")
      .append("11200123301")
      .append("12109")
      .append("SSSL_1_0");
    return sb.toString();
}

画面10：
//5. 连接服务器
ChannelFuture future = bootstrap.connect(ip, port);
future.channel().closeFuture();

画面11：
//设置设备的IP地址
String ip = "127.0.0.1";

画面12：
//设置随机湿度
me.setTem(getRandom(-100, 100));
//设置随机温度
me.setHum(getRandom(0, 100));
//设置随机状态
int state = Integer.valueOf(getRandom(0, 100));
me.setState(state);

画面13：
//设置随机状态
int state = Integer.valueOf(getRandom(0, 100));
me.setState(state);
//设置当前时间
me.setCtime(System.currentTimeMillis());

画面14：
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelOption;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.util.CharsetUtil;

public class Server {
    private int port;
    public Server(int port) {
        this.port = port;
    }

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：3.1 需求分析
架构图：
- 硬件设备（包含：温度湿度一体模块、显示屏、GPS、SIM卡、天线、存储）指向“Netty服务端”
- “Netty服务端”指向“Kafka”
- “Kafka”指向“Flink”
- “Flink”指向“统计报表”
- “Netty服务端”指向“Redis”
- “Redis”指向“Mysql”
- “Mysql”指向“业务管理”
- “业务管理”指向“统计报表”
- “Druid”指向“统计报表”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

