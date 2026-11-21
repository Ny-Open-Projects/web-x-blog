# 画面线理解：3.12 设备数据处理 - 客户端数据模拟

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day3 数据采集服务
- 源文件：06.阶段六 冷链监控平台项目\day3 数据采集服务\3.12 设备数据处理 - 客户端数据模拟_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 02:11, 03:22, 04:17, 05:41, 07:17, 08:30, 09:10, 11:04, 13:14, 14:42, 16:29, 17:44, 18:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:08:30

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
