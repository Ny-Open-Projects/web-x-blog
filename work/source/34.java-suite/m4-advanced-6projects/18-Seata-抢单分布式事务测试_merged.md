# 18-Seata-抢单分布式事务测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那接下来我们把这个分布式事务这一块给测试一下

那我们启动了故事微服

也启动了我们的一个订单微服

还启动了我们的微服网关这一块

我们首先把这一块所有的订单都给清理一下

因为这一块要测试这个订单一个数据

所以订单这里我们都给清理一下

清理之后呢我们再来测试

测试呢由于这一块是我们非热点商品

我们找一个非热点的商品

那这个应该是非热点的

我们先看一下它这里库存有多少数量

目前是1000个对吧

1000个我们打开我们的Postman来进行测试一次

这一块我们输入一下进行测试

那我们看一下测试的一个结果如何

好这一块是下单成功了

我们看下单是否成功

相框库存数量减少了一个

对的

我们看一下订单的数量有没有发生变更

多了一个订单对吧

那这个时候是没有问题

我们接着为了测试分布的事物这一块

我们要给它制造一下异常

异常怎么制造呢

我们只需要把我们的订单微服务这里打开

在订单微服务

它的下单那一块进行一个操作就可以了

在这里

这是这一块

它一会儿肯定会经过这一块对不对

经过这一块呢

我给它制造异常

int q等于10除以0

大家不用想啊

只要能进入到这一块来

那么下单上面这个库存递减是一定是成功的

对不对

我们把这个微服务给重新启动一下

然后测试一下整体的一个效果如何

好重新启动一下

启动之后呢

我们再来进行一个测试哈

等它启动

那目前这一块

我们来看一下这个商品的库存递减少

库存数量是多少

目前是999

999订单这一块只有一个

那等会儿递减之后呢

这里肯定是不行的

肯定是没有的

对不对

好

我们再来看一下这一块程序启动哈

好程序这一块我们看看是报错了的

这一块是去连接我们的C塔

这里是有问题

对吧

我们重新启动一下这一块

它连C塔怎么会有问题呢

好

这里启动了

把它给停掉

行

重新启动

启动之后呢

我们再来进行一个测试哈

好

等它启动

那么这一块整体来说的话

应该是没有问题的

行

启动了

启动了

我们现在来进行一个测试

看看效果怎么样

把这一块再次点击下单操作

我们下单的时候呢

现在这一块肯定是失败的

对不对

肯定是失败的啊

那么失败之后呢

这一块

等会会打印我们的错误

那么打印错误呢

我们看一下库存减少没有

好

开始下单

这里是by zero

不用想

是我们刚才制造的一个异常

对不对

那我们看一下这个异常这里

by zero就不用想了

这个倒不是我们测试错误的第一步哈

我们主要是测试事物有没有回滚

那回滚没有了

我们先看一下订单这里下单没有

订单肯定是没有下的

因为都已经报异常了

不会往后面走了

我们来看数量这一块变了没有

数量如果是998

那就事物失效

如果是999

事物就生效

很明显999

于是分布的事物是生效的

对不对

好

这就是我们这一块分布的事物

接着我们再讲讲全局异常这一块

那么全局异常

为什么要给大家讲解一下呢

因为我们现在这一块用的版本是1.0以上的版本

如果是1.0以下的版本

比如说

我们现在这一块用的版本是1.0以上的版本

比如说0.8的版本

那么这个异常是不好去处理的

那那个时候这个异常呢

它是没法去按照我们的要求实现处理

要想按照我们的要求去实现处理

你得去参考一下这个地址

用我们AOP的解决方案去解决

那这个我们就不带大家去不带大家去写了

因为我们现在用的版本已经比较高

而且不建议大家用低版本

在这一块呢

如果是有问题的话

参考官方这里提供的这个解决方案

用的是我们的AOP机制去解决的

这样子的话就可以避免我们这一块全局

这块全局我们异常处理

把这个异常给拦截到了

导致事物不回滚的问题

这是这一块

用的是AOP机制

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段为一个关于分布式系统实战的Java技术课程，主要围绕“秒杀系统”展开。讲师通过IDEA开发环境和Navicat数据库工具，演示了如何构建一个包含订单服务、商品服务、网关服务和分布式事务处理的微服务架构。核心内容包括：
- **服务架构搭建**：使用Spring Boot、Nacos（服务注册与发现）、Seata（分布式事务）等技术。
- **核心业务逻辑**：订单创建流程，包括库存扣减、用户限购、分布式锁（Redisson）等。
- **异常处理**：创建全局异常处理器 `BaseExceptionHandler` 来统一处理系统异常。
- **技术难点演示**：展示了如何在订单服务中集成Seata的分布式事务，并处理可能出现的异常。

整个视频旨在教授如何在高并发场景下设计和实现一个健壮的分布式订单系统。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面对应的具体时间点，以下章节基于画面内容和逻辑顺序进行划分：

- **00:00 - 00:05**: 课程开场，展示项目结构，介绍 `GatewayApplication` 的启动类和 `CorsWebFilter` 过滤器。
- **00:06 - 00:10**: 展示 `OrderServiceImpl` 的 `add` 方法，讲解订单创建的核心逻辑，包括生成用户键、调用 `skuFeign` 扣减库存、以及使用 `IdWorker` 生成订单ID。
- **00:11 - 00:15**: 展示 `OrderApplication` 的启动类，配置 `@EnableFeignClients` 和 `@MapperScan`，并演示启动后控制台的日志输出。
- **00:16 - 00:20**: 演示 `OrderServiceImpl` 中的 `add` 方法，重点讲解 `if (count.getCode() == StatusCode.DECOUNT_OK)` 条件判断，以及后续的 `IdWorker.nextId()` 生成订单ID。
- **00:21 - 00:25**: 展示数据库 `seckill_goods` 表中的商品数据，以及 `seckill_order` 表中的订单数据，用于验证业务逻辑。
- **00:26 - 00:30**: 讲解并演示 `BaseExceptionHandler` 的代码，用于全局捕获和处理异常，包括打印堆栈信息和返回统一的错误响应。
- **00:31 - 00:35**: 展示 `TestAspect` 的代码，用于演示Seata的分布式事务管理，包括 `@GlobalTransactional` 注解和事务的开启与提交。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **PPT标题页**：显示课程大纲，包含“1.2.2 Redisson配置”、“2. 分布式事务”、“3. Seata分布式事务”、“4. WebSocket”、“5. Netty并发网络编程”等章节。
- **异常处理PPT**：展示 `BaseExceptionHandler` 的代码，用于处理所有请求路径的异常。
- **Seata事务PPT**：展示 `TestAspect` 的代码，用于演示Seata的分布式事务管理。

#### 代码关键内容

- **`GatewayApplication.java`**:
  ```java
  @SpringBootApplication
  public class GatewayApplication {
      public static void main(String[] args) {
          SpringApplication.run(GatewayApplication.class, args);
      }
  }
  ```

- **`OrderServiceImpl.java`**:
  ```java
  @GlobalTransactional
  @Override
  public int add(Order order) {
      String userKey = "USER" + order.getUsername() + "ID" + order.getSkulId();
      // 1. 透传库存
      Result<Sku> count = skuFeign.dcount(order.getSkulId(), order.getTotalNum());
      // 2. 透传成功->下单->记录当前用户抢单的时间点，24小时内不能抢购该商品
      if (count.getCode() == StatusCode.DECOUNT_OK) {
          int i = 10 / 0; // 模拟异常
          Sku sku = count.getData();
          order.setIdWorker.nextId();
          // 下单
      }
  }
  ```

- **`OrderApplication.java`**:
  ```java
  @SpringBootApplication
  @EnableDiscoveryClient
  @EnableFeignClients(basePackages = {"com.seckill.goods.feign", "com.seckill.message.feign"})
  @MapperScan(basePackages = "com.seckill.order.dao")
  public class OrderApplication {
      public static void main(String[] args) {
          SpringApplication.run(OrderApplication.class, args);
      }
  }
  ```

- **`BaseExceptionHandler.java`**:
  ```java
  @ControllerAdvice
  public class BaseExceptionHandler {
      private static Logger logger = LoggerFactory.getLogger(BaseExceptionHandler.class);

      @ResponseBody
      @ExceptionHandler(Exception.class)
      public Result error(Exception ex) {
          StringWriter stringWriter = new StringWriter();
          PrintWriter writer = new PrintWriter(stringWriter);
          ex.printStackTrace(writer);
          logger.error(stringWriter.toString());
          return new Result(false, StatusCode.ERROR, ex.getMessage());
      }
  }
  ```

- **`TestAspect.java`**:
  ```java
  @Aspect
  @Component
  public class TestAspect {
      private final static Logger logger = LoggerFactory.getLogger(TestAspect.class);

      @Before("execution(* com.seckill.service.*.*(..))")
      public void before(JoinPoint joinPoint) throws TransactionException {
          Method method = ((MethodSignature) joinPoint.getSignature()).getMethod();
          logger.info("方法名: " + method.getName());
          if ((int)(Math.random() * 100) % 2 == 0) {
              GlobalTransactional tx = GlobalTransactionalContext.getTxContext();
              tx.begin(300000, "test-client");
          } else {
              logger.info("无事务");
          }
      }

      @AfterThrowing(value = "execution(* com.seckill.service.*.*(..))", throwing = "ex")
      public void afterThrowing(JoinPoint joinPoint, Exception ex) throws TransactionException {
          logger.info("方法名: " + joinPoint.getSignature().getName());
          GlobalTransactionalContext.rollback();
      }

      @AfterReturning(value = "execution(* com.seckill.service.*.*(..))", returning = "result")
      public void afterReturning(JoinPoint joinPoint, Object result) throws TransactionException {
          if (StringUtils.isNotBlank((String) result)) {
              logger.info("方法名: " + joinPoint.getSignature().getName());
          }
      }
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：服务启动与架构展示**
  - **描述**：讲师在IDEA中启动 `GatewayApplication`，并展示其配置文件 `seckill-gateway.yml` 和 `seckill-goods.yml`。同时，通过控制台日志展示服务注册到Nacos的过程。
  - **技术点**：Spring Boot应用启动、Nacos服务注册、配置文件管理。

- **场景二：订单服务核心逻辑演示**
  - **描述**：讲师在 `OrderServiceImpl.java` 中展示 `add` 方法，重点讲解库存扣减、用户限购、以及使用 `IdWorker` 生成订单ID的逻辑。通过在 `if` 条件中添加 `int i = 10 / 0;` 来模拟异常，用于后续演示异常处理。
  - **技术点**：Feign远程调用、Redisson分布式锁、订单ID生成、异常模拟。

- **场景三：数据库操作与数据验证**
  - **描述**：讲师切换到Navicat数据库工具，展示 `seckill_goods` 表中的商品数据和 `seckill_order` 表中的订单数据，用于验证订单创建后的数据库状态。
  - **技术点**：MySQL数据库操作、数据一致性验证。

- **场景四：全局异常处理器创建**
  - **描述**：讲师在IDEA中创建 `BaseExceptionHandler` 类，并在PPT上展示其代码。该类使用 `@ControllerAdvice` 注解，用于全局捕获所有请求路径的异常，并通过 `@ExceptionHandler` 注解处理 `Exception` 类型的异常。
  - **技术点**：Spring MVC异常处理、日志记录、统一错误响应。

- **场景五：Seata分布式事务演示**
  - **描述**：讲师在 `TestAspect` 中展示如何使用 `@GlobalTransactional` 注解来管理分布式事务。通过在 `before` 方法中模拟事务的开启和提交，以及在 `afterThrowing` 方法中模拟事务的回滚。
  - **技术点**：Seata分布式事务、AOP切面编程、事务管理。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
