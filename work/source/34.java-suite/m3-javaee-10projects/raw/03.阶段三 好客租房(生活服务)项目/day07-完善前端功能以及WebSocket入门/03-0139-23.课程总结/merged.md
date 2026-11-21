# 23.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\23.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 5分16秒（音频 316s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们对我们今天的课程呢做一个简单的一个小节那么来看一下今天我们讲了哪些内容那么首先第一个呢是我们为前端的做了一个Mock的服务这样做的目的呢就是让前端系统直接跟我们的后端服务做一个对接
[00:17] 而不是去依赖于node.js的服务这第一个内容第二个我们学习了一下GraphQL中的参数我们重点讲的是一个它的变量的一个传递变量的一个定义包括它的一些变量参数的一些传递那么传递的方式是不是通过这种方式去做一个传递就是我们先做这样的一个定义在上面这个位置是不是做这样的一个定义然后下面是不是就可以去使用这样的一个参数了
[00:46] 那么在我们的这个在我们去传递参数的时候呢传递的是一个吧Able就是一个json的一个字串OK好那么在我们服务端处理的时候啊要注意的是服务端处理我们需要去分别去去处理它的get请求和post请求并且呢我们需要去处理它的这通过一个什么呢是不是一个叫做execution input这个对象去做一个构造然后呢再去做一个查询啊
[01:16] OK那么这个代码呢大家也可以自己动手去挑一下然后呢后面我们是基于前面所学习的GrabQI中的这个变量参数的一个传递然后呢去实现了房源列表的一个查询那么OK好那么在后面呢我们实现了我们的房源数据的一个更新然后在这个里面呢我们也希望大家呢去动手去写一下这个页面中的一些这个逻辑写一些逻辑OK好
[01:44] 然后呢在后面呢我们去为我们的这个接口呢添加了缓存缓存功能啊那么缓存呢我们使用的是Redis并且呢我们去搭建了Redis的集群那么在搭建Redis集群的时候呢我们遇到了一些问题对吧然后又去也逐一的去解决了这些问题那么也希望大家从中的能够去学习到一些解决问题的一些这种解决方案和一些思路啊OK好那么在我们去
[02:13] 添加这个缓存的时候对吧添加缓存的时候呢我们去做了两个事情是吧第一个呢就是使用拦截器在我们进行查询之前呢先做一个命中然后呢第二件事情呢就是在我们的数据在返回之前呢我们去把这个数据拿到然后呢就把它保存到我们的一个redis中那么做命中的时候我们使用的是拦截器这个是可以做到的对吧但是呢我们
[02:41] 在去写数据的时候你发现在拦截器是做不到的因为我们在拦截器中拿不到我们响应的那个response body这样的一些数据所以呢我们使用了一个新的一个技术啊叫什么技术呢就是下面的在这个位置啊使用了一个叫做response body的一个race这样的一个呃整个比较高级的用法去拦截我们的一个响应
[03:06] 然后就可以拿到我们的数据了那么OK那么在前面我们写物的时候呢它也会遇到一个问题就是我们那个request中的那个输入流呢它呢只能读取一次那么如果你在那个拦截器中去读取的话那么在后面的Controller中呢就读不到了所以呢我们通过这种包装request的方式呢去进行做一个解决那么OK这个这种解决方案呢也希望大家能够把它学到手OK好那么最后呢我们讲了WebSocket
[03:34] 那么使用这个WebSocket呢其实就是去建立我们的客户端与服务端的一个长连接那么这样的话呢我们就可以实时的去去将服务端的一些数据推送到我们的客户端那么客户端也可以去实时去访问我们的服务端这样的话呢它的这种效率就更高啊那么像这种WebSocket呢更适合去做一些这种消息啊还是做一些这种即时通讯啊这样的一些业务的啊OK然后呢我们就基于我们的
[04:03] 这个WebSocket它的一些底层的一些API有些这种注解然后我们就做了一个快速的一个入门OK然后后面我们是不是整合到我们的spamboot中去做了一个这样的一个使用那么会发现在整合spamboot之后是变得使用更加的简单了本身它原来就很简单变得更加简单了OK那么在最后我们讲了一下WebSocket的拦截器那么在拦截器里面我们可以去做我们的一些在握手之前的一些业务
[04:33] 包括你可以做一些用户的教验呢设置一些参数啊等等等等OK好那么有了我们的这个WebSocket之后那么我们是不是就可以继续去做后面的内容了那么后面我们要做什么内容呢就是我们要基于WebSocket来开发我们那个即时通讯这样的一个功能而今天我们去做的事情呢就是我们去完善了我们的一些这个网站的功能
[04:57] 然后我们去添加了这种缓存然后我们又去学习了WebSocket然后为我们后面去实现我们的即时通讯做一个技术的铺垫就做一个技术的储备OK好那么这个就是我们今天的一些内容好那么今天我们的内容就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现 GraphQL 参数传递、房源数据更新、Redis 缓存逻辑、以及 WebSocket 的集成与拦截器实现。

2) 按时间顺序列出每张画面的要点：
画面 1: 讲解 GraphQL 中的参数传递，展示了一个包含 id、title、estateId 等字段的 HouseResources 对象示例，提出静态参数与动态参数的区分问题。
画面 2: 讲解查询时传递参数，说明客户端只需传入不同变量即可构建动态查询，避免构建全新查询。
画面 3: 展示 GraphQLController 的 Java 代码，定义了 @GetMapping 和 @RequestParam 注解的 query 方法，用于接收查询参数。
画面 4: 讲解实现更新房源数据，进入“修改Controller”部分，展示 @param houseResources json数据 注释。
画面 5: 讲解编写 EditResource 组件，展示 React 组件的构造函数和 showModal 方法。
画面 6: 讲解 Redis 集群搭建，展示 Docker create 命令创建三个 Redis 节点，以及使用 redis-cli 命令创建集群的步骤。
画面 7: 讲解添加缓存逻辑，提出两种实现方式：接口单点控制和统一控制，并决定采用拦截器方式。
画面 8: 讲解编写拦截器 RedisCacheInterceptor，展示 package 声明和 import 语句。
画面 9: 展示 GraphQL 查询错误信息，指出“Required request body is missing”，并分析拦截器导致请求体数据丢失的原因。
画面 10: 讲解通过包装 request 解决拦截器问题，展示 MyServletRequestWrapper 类的定义。
画面 11: 展示 MyServletRequestWrapper 类的实现细节，包括 getReader 和 getInputStream 方法，以及 RequestBodyCachingInputStream 类的定义。
画面 12: 讲解 WebSocket 的相关注解说明，包括 @ServerEndpoint、@OnOpen、@OnClose、@OnMessage 等注解的用途。
画面 13: 讲解 Spring Boot 整合 WebSocket，展示 pom.xml 文件中引入 spring-boot-starter-parent 和 itcast-WebSocket 依赖。
画面 14: 讲解 WebSocket 拦截器，展示 package 声明和 import 语句，包括 ServerHttpRequest、ServerHttpResponse、WebSocketHandler、HandshakeInterceptor 等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 1:
```java
{
  HouseResources(id: 8) {
    id
    title
    estateId
    buildingUnit
    buildingFloorNum
    mobile
    useArea
    pic
  }
}
```

画面 3:
```java
import java.util.Map;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping("GraphQL");
@Controller
@CrossOrigin
@AutoWired
private GraphQL graphQL;
private static final ObjectMapper MAPPER = new ObjectMapper();
/**
 * 实现GraphQL查询
 * @param query
 * @return
 */
@GetMapping
@ResponseBody
public Map<String, Object> query(@RequestParam("query") String query,
        @RequestParam(value = "variables", required = false) String variablesJson,
        @RequestParam(value = "operationName", required = false) String operationName) {
```

画面 4:
```java
/**
 * 修改房源
 * @param houseResources json数据
 * @return
 */
```

画面 5:
```javascript
labelCol: {
  xs: { span: 24 },
  sm: { span: 7 },
},
wrapperCol: {
  xs: { span: 24 },
  sm: { span: 12 },
  md: { span: 10 },
},
@connect()
Form.create extends React.Component{
  constructor(props){
    super(props);
    this.state={
      visible:false,
      pics:new Set();
    }
  }
  showModal () -> {
    this.setState({
      visible: true
    });
  }
```

画面 6:
```bash
Docker create --name redis-node01 -v /data/redis-data/node01:/data -p 6379:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf
Docker create --name redis-node02 -v /data/redis-data/node02:/data -p 6380:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf
Docker create --name redis-node03 -v /data/redis-data/node03:/data -p 6381:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf
#启动集群
Docker start redis-node01 redis-node02 redis-node03
#进入redis-node01进行操作
Docker exec -it redis-node01 /bin/bash
#组建集群
redis-cli --cluster create 172.17.0.1:6379 172.17.0.1:6380 172.17.0.1:6381 --cluster-replicas 1
```

画面 7:
```java
package cn.itcast.haoke.dubbo.api.interceptor;
import com.fasterxml.jackson.databind.ObjectMapper;
```

画面 8:
```java
package cn.itcast.haoke.dubbo.api.config;
import cn.itcast.haoke.dubbo.api.interceptor.RedisCacheInterceptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
```

画面 9:
```json
{
  "timestamp": "2018-12-02T16:31:32.372+0000",
  "status": 400,
  "error": "Bad Request",
  "message": "Required request body is missing: public java.util.Map<java.lang.String, java.lang.Object>",
  "path": "/GraphQL"
}
```

画面 10:
```java
package cn.itcast.haoke.dubbo.api.interceptor;
import org.apache.commons.io.IOUtils;
import javax.servlet.ReadListener;
import javax.servlet.ServletInputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletRequestWrapper;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.IOException;

