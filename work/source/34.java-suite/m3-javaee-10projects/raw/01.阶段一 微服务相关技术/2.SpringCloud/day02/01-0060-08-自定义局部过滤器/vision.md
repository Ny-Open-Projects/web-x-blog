# 画面线理解：08-自定义局部过滤器

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\08-自定义局部过滤器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:47, 03:41, 04:28, 05:37, 05:57, 07:01, 07:40, 08:45, 09:45, 11:21, 11:54, 12:28, 12:57, 13:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:25:00

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud Gateway 中自定义局部过滤器，通过配置文件动态获取请求参数并输出。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，介绍自定义局部过滤器的目标和需求。
画面2：在IDEA中创建名为 MyParamGatewayFilterFactory 的类。
画面3：在 MyParamGatewayFilterFactory 类中定义 Config 静态内部类。
画面4：展示 AbstractNameValueGatewayFilterFactory 的继承结构和 NameValueConfig 类。
画面5：展示 MyParamGatewayFilterFactory 类的完整代码结构。
画面6：在 MyParamGatewayFilterFactory 类中定义静态常量和配置类。
画面7：在 MyParamGatewayFilterFactory 类中实现 apply 方法。
画面8：在 apply 方法中获取请求参数并进行判断。
画面9：在 apply 方法中获取参数值并打印。
画面10：在控制台中查看服务启动日志。
画面11：在控制台中查看过滤器执行日志。
画面12：在浏览器中访问接口，查看返回结果。
画面13：展示课程PPT内容，介绍自定义局部过滤器的实现步骤。
画面14：展示 MyParamGatewayFilterFactory 类的完整代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
package com.itheima.gateway.filter;
public class MyParamGatewayFilterFactory {

画面3：
public static class Config {
}

画面4：
import org.springframework.cloud.gateway.filter.factory.AbstractNameValueGatewayFilterFactory;
public abstract class AbstractNameValueGatewayFilterFactory extends AbstractNameValueGatewayFilterFactory.NameValueConfig {
}

画面5：
import org.springframework.cloud.gateway.filter.factory.AbstractNameValueGatewayFilterFactory;
public abstract class AbstractNameValueGatewayFilterFactory extends AbstractNameValueGatewayFilterFactory.NameValueConfig {
}

画面6：
import org.springframework.cloud.gateway.filter.factory.AbstractNameValueGatewayFilterFactory;
public abstract class AbstractNameValueGatewayFilterFactory extends AbstractNameValueGatewayFilterFactory.NameValueConfig {
}

画面7：
import org.springframework.cloud.gateway.filter.factory.AbstractNameValueGatewayFilterFactory;
public abstract class AbstractNameValueGatewayFilterFactory extends AbstractNameValueGatewayFilterFactory.NameValueConfig {
}

画面8：
import org.springframework.cloud.gateway.filter.factory.AbstractNameValueGatewayFilterFactory;
public abstract class AbstractNameValueGatewayFilterFactory extends AbstractNameValueGatewayFilterFactory.NameValueConfig {
}

画面9：
import org.springframework.cloud.gateway.filter.factory.AbstractNameValueGatewayFilterFactory;
public abstract class AbstractNameValueGatewayFilterFactory extends AbstractNameValueGatewayFilterFactory.NameValueConfig {
}

画面10：
画面11：
画面12：
{
  "id": 5,
  "username": "itheima",
  "password": "123456",
  "name": "张三",
  "age": 21,
  "sex": 2,
  "birthday": "2005-07-07T16:00:00.000+0000",
  "created": "2014-09-22T03:41:15.000+0000",
  "updated": "2014-09-22T03:41:15.000+0000",
  "note": "光棍看雪第11条"
}

画面13：
实现步骤：
1. 配置过滤器；
2. 编写过滤器；
3. 测试

画面14：
package com.itheima.gateway.filter;
import org.springframework.cloud.gateway.filter.GatewayFilter;
import org.springframework.cloud.gateway.filter.factory.AbstractGatewayFilterFactory;
import org.springframework.http.server.reactive.ServerHttpRequest;
import org.springframework.stereotype.Component;
import java.util.Arrays;
import java.util.List;
@Component
public class MyParamGatewayFilterFactory extends AbstractGatewayFilterFactory<MyParamGatewayFilterFactory.Config> {
    static final String PARAM_NAME = "param";
    public MyParamGatewayFilterFactory() {
        super(Config.class);
    }

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“8. 自定义局部过滤器”，目标为“按照默认过滤器编写并配置一个自定义局部过滤器，该过滤器可以通过配置文件中的参数名称获取请求的参数值”，需求为“在过滤器中将http://localhost:10010/api/user/8?name=itcast中的参数name的值获取到并输出到控制台”，小结为“使用场景：请求鉴权、异常处理、记录调用时长等”。
画面13：标题为“实现步骤”，内容为“1. 配置过滤器；2. 编写过滤器；3. 测试”，小结为“配置：与其他过滤器的配置一致。实现过滤器”。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
