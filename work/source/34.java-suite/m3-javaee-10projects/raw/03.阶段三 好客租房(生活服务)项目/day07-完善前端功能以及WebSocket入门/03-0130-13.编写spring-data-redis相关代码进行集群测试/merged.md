# 13.编写spring-data-redis相关代码进行集群测试

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\13.编写spring-data-redis相关代码进行集群测试【海量资源尽在 ubkz.com】.mp4
- 时长 7分13秒（音频 433s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面呢我们来编写代码来测试一下我们的集群那么前面呢我们只是通过命令好像的方式去做了一个测试发现它是OK的但是呢我们最终呢还是需要去通过我们的程序去做一个使用的所以呢我们通过代码来来做一个测试那么首先第一个呢我们导入一些相关的依赖那么我们去导入一个这个Spring Boot的一个Data Release就是Spring Date Release把这个导入进来然后再去导入一个Jadis的一个客户端
[00:28] OK那么下面的comments.io是我们在后面我们会用的我们就把它一起导入进来了那么把它拷贝一下然后找到我们这个工程然后是在上面这个工程在这个里面我们把这个依赖导入进来就到这好那么导入进来它可能是需要下载一些依赖包好那么导入进来之后我们就需要去给它做一些配置咱们把这个先给它配置过来Ctrl C拷贝
[00:57] 然后呢我们找到这个resource下面是不是有个application properties那么给它配置到这个里面来这个呢是编码发生了一些这个问题啊那么我先把它拷过来吧拷过来然后呢来看一下那么这个呢是我们之前所写的一个注释叫什么呢这个是不是我们那个doubledouble的一个应用应用名称对吧然后呢下面这个呢是我们的注释中心
[01:29] ZK注册中心OK好那么现在呢这个呢就是我们的一个配置啊这个配置好那么这样的话呢我们就把一个配置就搞定了那么在这个里面呢我们要其实要强调的一点是这个这个是不是就配置我们集群的一个这个地址啊但是呢我们你配置之后它并不是直接能使用啊还需要我们去写一个配置内而去去读取这样的一个配置项
[01:59] 我们来看一下配置类怎么去写那么这样咱们把配置类就抠过来这样来抠那么我先写拷贝一个名字那么需要找到我们的一个config类在下面把它丢过来然后我们去给他去加这样的一个注解然后去让他去做一个配置文件的一个读取OK是不是读取的前缀就是这个stream ready是一个cluster那么我可以看到
[02:31] 是不是就是这几个就这两个配置就这两个配置就这两个配置就它读取这两个配置那么读取到之后我们就需要给它是不是设置两个属性设置两个属性那么设置两个属性来看一下是不是在这个位置设置两个属性两个属性一个就是Nodes一个就是最大的一个Directors就是我们知道在做集群去查询之后或者说
[03:00] 做操作的时候它会有一个重定项所以这个设置最大一个重定项的一个次数那么我们现在的设置的次数是5就最大是5次做一个重定项ok好然后我们来看一下这个里面还需要给它设置一些它的一些构造方法然后这个就是这个是一个get和set的方法那这样的我们咱就给它来生成吧来生成这个get和set的方法去生成get和set
[03:29] 当然了其实我们去加一个date注解是不是也可以那这样吧那我就加一个date注加一个date注解好这样的话我们是不是就省着去生成get和set的方法好那么有了get和set的方法之后那么我们config这个类是不是就搞定了那么搞定之后下面我们就需要去写一个我们的一个连接写一个连接那么我们去写一个readist class的config这个类那么
[03:58] 前面是不是我们已经读取了配置文件了下面我们来写一下这个类那么把这个类的内容我们就直接贴过来吧来拷贝一下然后呢Ctrl C然后呢丢到这个Config这个里面来看一下把这个代码的格式呢我们去格式化一下然后在这个里面呢我们是不是把刚才的Publish的这个类注入进来注入进来之后呢就会拿到它的一些这个Nodes以及它的一个Max Redirects然后呢我们去
[04:29] 去得到一个这个redis的一个连接工厂去new一个jadis的一个连接工厂然后在下面这个位置呢我们去返回一个redis的template因为我们最终操作是不是需要通过这个redis的template去做一个操作那么要注意的是在这个位置我们所在上面这个位置啊在这个位置呢我们去new的是一个cluster的一个配置啊注意这cluster配置所以说我们这是一个集群的一个配置哎呀ok
[04:58] 好那么有了这个模板之后呢我们就可以去做我们的一些这个操作了对吧好那么下面呢我们写一个我们的测试用例那么写一个测试用例那么我们先把这个包呢先创建出来这个包呢是我们要把它写到我们的测试test这个包下面去来看一下是在我们这个test包下面那么加了这个下面创建一个这个包OK那么这个包就创建好了
[05:26] 那么创建好之后我们需要把这个测试用力靠过来这个我就不写了前面大家在使用这个SpringDataRelease用的也是比较熟了所以我就不一行一行去敲这个代码了然后直接贴过来我们去测试就好了然后我们来看一下在这个里面我们是不是直接注入我们刚刚的这个容器中的这个template模板那么有了这个模板之后我们就可以做下面这个操作然后我们在这
[05:54] 就去什么呢就去做一个复循环做一个复循环去写入我们的数据写入100条这个数据然后呢我们下面呢就去把这个100条这个数据呢再给它读到再给它控制台打印出来然后最后给它删除这样我先不做删除先保留先保留我们来看一下我们的一个数据先看一下数据有没有写进去好那么我们就执行这个操作吧然后呢走去等待它的一个执行
[06:24] 那么可以看到那么数据现在已经是查询到了打印出来了那就说明他一定是不写到redis中了对不对那么其实我们可以去测一下那么他有没有去写入进去来一个case新那是不是可以看到是不是已经有数据是不是写入进来了那么来我们做一个get操作那么是不是依然可以拿到数据没有任何问题好那么现在我们是不是就已经跑通了是吧当然了这个删除
[06:55] 大家可以去测一下他也没有问题因为拿到k然后能写进去能读出来大家肯定能够删除这个没有任何问题的那么到这里说明我们的集群是不是就大件成功了ok我们只是对他作为一个这样的一个测试ok好那么关于我们的编码的一个测试我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置和测试 Redis 集群，包括添加依赖、编写配置类、注册连接工厂和编写测试用例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Redis 集群节点信息，通过 `redis-cli` 查看，显示了多个节点的 IP 和角色（master、myself.master）。
画面 2: 展示了 Maven 依赖配置，用于引入 Spring Boot 的 Redis 支持。
画面 3: 展示了 Spring Boot 的 Redis 集群配置文件内容，包含连接池参数和节点地址。
画面 4: 展示了 IDE 中的项目结构，定位到 `ClusterConfigurationProperties` 类。
画面 5: 展示了 `ClusterConfigurationProperties` 类的代码，定义了 `nodes` 和 `maxRedirects` 字段。
画面 6: 展示了 IDE 中的右键菜单，用于对 `ClusterConfigurationProperties` 类进行操作。
画面 7: 展示了 `RedisClusterConfig` 配置类的代码，用于注册 Redis 连接工厂。
画面 8: 展示了 `ClusterConfigurationProperties` 类中添加了 `@Data` 注解。
画面 9: 展示了 `RedisClusterConfig` 类中定义了 `RedisTemplate` 的 Bean。
画面 10: 展示了测试类 `TestRedis` 的代码，用于测试 Redis 操作。
画面 11: 展示了测试类 `TestRedis` 的代码，使用 `@RunWith(SpringRunner.class)` 和 `@SpringBootTest` 注解。
画面 12: 展示了测试类 `TestRedis` 的代码，使用 `@Test` 注解定义测试方法。
画面 13: 展示了在终端中执行 Redis 命令，查询键值对。
画面 14: 展示了测试类 `TestRedis` 的代码，使用 `@RunWith(SpringRunner.class)` 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
root@itcast:/data# redis-cli
127.0.0.1:6379> CLUSTER NODES
46e558c2d296a506955cc6e700834037c31d9 172.16.55.185:6380 172.16.55.185:6380 master - 0
1543766975796 2 connected 5461-10922
b42d6ccc54409f1d8f35fa/ad08b0962a6ac4a 1/2.16.55.185:6381 172.16.55.185:6381 master - 0
154376697489 3 connected 10923-16383
4c60f45d17277783181c64c6c141354f0e28d18 177.16.55.185:6379 177.16.55.185:6379 myself, master - 0
1543766974000 1 connected 0-5460
```

画面 2:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>2.9.0</version>
</dependency>
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.10.0</version>
</dependency>
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-io</artifactId>
    <version>2.6</version>
</dependency>
```

画面 3:
```properties
# redis集群配置
spring.redis.jedis.pool.max-wait = 5000
spring.redis.jedis.pool.max-idle = 100
spring.redis.jedis.pool.min-idle = 10
spring.redis.timeout = 10
spring.redis.cluster.nodes = 172.16.55.185:6379,172.16.55.185:6380,172.16.55.185:6381
spring.redis.cluster.max-redirects=5
```

画面 4:
```
package cn.itcast.haoke.dubbo.api.config;
```

画面 5:
```java
package cn.itcast.haoke.dubbo.api.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;
import java.util.List;

@Component
@ConfigurationProperties(prefix = "spring.redis.cluster")
public class ClusterConfigurationProperties {
    private List<String> nodes;
    private Integer maxRedirects;
}
```

画面 6:
```
// 右键菜单内容
```

画面 7:
```java
package cn.itcast.haoke.dubbo.api.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisClusterConfiguration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.StringRedisSerializer;

@Configuration
public class RedisClusterConfig {
    @Autowired
    private ClusterConfigurationProperties clusterProperties;

    @Bean
    public RedisConnectionFactory connectionFactory() {
        RedisClusterConfiguration configuration = new RedisClusterConfiguration();
        configuration.setNodes(clusterProperties.getNodes());
        configuration.setMaxRedirects(clusterProperties.getMaxRedirects());
        return new RedisConnectionFactory(configuration);
    }
}
```

画面 8:
```java
import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;
import java.util.List;

@Component
@ConfigurationProperties(prefix = "spring.redis.cluster")
@Data
public class ClusterConfigurationProperties {
    private List<String> nodes;
    private Integer maxRedirects;
}
```

画面 9:
```java
@Bean
public RedisTemplate<String, String> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
    RedisTemplate<String, String> redisTemplate = new RedisTemplate<>();
    redisTemplate.setConnectionFactory(redisConnectionFactory);
    redisTemplate.setKeySerializer(new StringRedisSerializer());
    redisTemplate.setValueSerializer(new StringRedisSerializer());
    redisTemplate.afterPropertiesSet();
    return redisTemplate;
}
```

画面 10:
```java
import java.util.Set;

@RunWith(SpringRunner.class)
public class TestRedis {

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @Test
    public void testSave() {
        for (int i = 0; i < 100; i++) {
            this.redisTemplate.opsForValue().set("key_" + i, "value_" + i);
        }
        Set<String> keys = this.redisTemplate.keys("key_*");
        for (String key : keys) {
            String value = this.redisTemplate.opsForValue().get(key);
            System.out.println(value);
        }
        this.redisTemplate.delete(key);
    }
}
```

画面 11:
```java
package cn.itcast.haoke.dubbo.api;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class TestRedis {
```

画面 12:
```java
@Test
public void testSave() {
    for (int i = 0; i < 100; i++) {
        this.redisTemplate.opsForValue().set("key_" + i, "value_" + i);
    }
    Set<String> keys = this.redisTemplate.keys("key_*");
    for (String key : keys) {
        String value = this.redisTemplate.opsForValue().get(key);
        System.out.println(value);
    }
    this.redisTemplate.delete(key);
}
```

画面 13:
```
172.16.55.185:6380> get key_58
"Value 58"
```

画面 14:
```java
package cn.itcast.haoke.dubbo.api;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class TestRedis {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“5.4.2、编写配置文件”。
画面 3: PPT 标题为“5.4.2、编写配置

