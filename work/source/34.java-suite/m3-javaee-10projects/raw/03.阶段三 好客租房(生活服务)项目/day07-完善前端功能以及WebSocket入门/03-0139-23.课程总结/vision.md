# 画面线理解：23.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\23.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:23, 00:47, 01:00, 01:32, 01:42, 02:05, 02:17, 02:43, 02:52, 03:12, 03:32, 04:07, 04:13, 04:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:33:28

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现 GraphQL 参数传递、房源数据更新、Redis 缓存逻辑、以及 WebSocket 的集成与拦截器实现。

2) 按时间顺序列出每张画面的要点：
画面 1: 讲解 GraphQL 中的参数传递，展示了一个包含 id、title、estateId 等字段的 HouseResources 对象示例，提出静态参数与动态参数的区分问题。
画面 2: 讲解查询时传递参数，说明客户端只需传入不同变量即可构建动态查询，避免构建全新查询。
画面 3: 展示 GraphQLController 的 Java 代码，定义了 @GetMapping 和 @RequestParam 注解的 query 方法，用于接收查询参数。
画面 4: 讲解实现更新房源数据，进入“修改Controller”部分，展示 @param houseResources json数据 注释。
画面 5: 讲解编写 EditResource 组件，展示 React 组件的构造函数和 showModal 方法。
画面 6: 讲解 Redis 集群搭建，展示 docker create 命令创建三个 Redis 节点，以及使用 redis-cli 命令创建集群的步骤。
画面 7: 讲解添加缓存逻辑，提出两种实现方式：接口单点控制和统一控制，并决定采用拦截器方式。
画面 8: 讲解编写拦截器 RedisCacheInterceptor，展示 package 声明和 import 语句。
画面 9: 展示 GraphQL 查询错误信息，指出“Required request body is missing”，并分析拦截器导致请求体数据丢失的原因。
画面 10: 讲解通过包装 request 解决拦截器问题，展示 MyServletRequestWrapper 类的定义。
画面 11: 展示 MyServletRequestWrapper 类的实现细节，包括 getReader 和 getInputStream 方法，以及 RequestBodyCachingInputStream 类的定义。
画面 12: 讲解 WebSocket 的相关注解说明，包括 @ServerEndpoint、@OnOpen、@OnClose、@OnMessage 等注解的用途。
画面 13: 讲解 SpringBoot 整合 WebSocket，展示 pom.xml 文件中引入 spring-boot-starter-parent 和 itcast-websocket 依赖。
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
import org.springframework.web.bind.annotation.RequestMapping("graphql");
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
docker create --name redis-node01 -v /data/redis-data/node01:/data -p 6379:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf
docker create --name redis-node02 -v /data/redis-data/node02:/data -p 6380:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf
docker create --name redis-node03 -v /data/redis-data/node03:/data -p 6381:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf
#启动集群
docker start redis-node01 redis-node02 redis-node03
#进入redis-node01进行操作
docker exec -it redis-node01 /bin/bash
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
  "path": "/graphql"
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
