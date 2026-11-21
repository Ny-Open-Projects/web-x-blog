# 画面线理解：14.打包项目之打包-haoke-manage

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\14.打包项目之打包itcast-haoke-manage【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:15, 03:26, 04:22, 05:57, 06:44, 08:01, 09:42, 11:25, 13:05, 15:13, 16:31, 18:09, 19:31, 20:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:55:33

1) 这一组画面整体在讲什么（一句话）：
演示如何为一个基于 Spring Boot 和 Dubbo 的分布式项目进行打包，并在远程服务器上部署和启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档，内容为“项目打包”章节，包含项目域名规划表和第一步“添加springboot的打包插件”的提示。
画面 2: 在 IntelliJ IDEA 中，展示 `pom.xml` 文件中配置的 Spring Boot Maven 插件，用于执行 `repackage` 目标。
画面 3: 在 IntelliJ IDEA 中，展示项目结构，选中 `itcast-haoke-manage-dubbo-server-ad-service` 模块。
画面 4: 在 IntelliJ IDEA 中，展示 `application.properties` 文件，其中包含 Dubbo 服务的配置（如 `dubbo.application.name`、`dubbo.registry.address`）和数据库连接信息。
画面 5: 在 IntelliJ IDEA 中，展示项目结构，选中 `src/main/resources` 目录。
画面 6: 在 IntelliJ IDEA 中，展示 `application.properties` 文件，其中包含 Redis 和 MongoDB 的配置信息。
画面 7: 在 IntelliJ IDEA 中，展示项目结构，选中 `itcast-haoke-manage-api-server` 模块。
画面 8: 在 Xshell 终端中，执行 `mvn clean package` 命令，创建 `itcast-haoke-manage.zip` 文件，并进入项目目录。
画面 9: 在 Xshell 终端中，进入 `itcast-haoke-manage-dubbo-server-house-resources-dubbo-service` 模块目录。
画面 10: 在 Xshell 终端中，执行 `mvn clean package` 命令，生成 `itcast-haoke-manage-dubbo-server-house-resources-dubbo-service-1.0-SNAPSHOT.jar` 文件，并复制到目标目录。
画面 11: 在 Xshell 终端中，进入 `itcast-haoke-manage-api-server` 模块目录。
画面 12: 在 Xshell 终端中，启动 ZooKeeper 服务。
画面 13: 在 Xshell 终端中，启动 Dubbo 服务，显示连接 ZooKeeper 的日志。
画面 14: 在 Xshell 终端中，启动 Dubbo 服务后，出现 Spring Boot 启动失败的错误日志，提示 `graphQL` 相关的 Bean 创建异常。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```markdown
3、项目打包

项目的域名规划（虚拟域名）：
| 项目 | 域名 | 机器 |
|---|---|---|
| itcast-haoke-manage-api-server | api.manage.haoke.com | 192.168.1.7 |
| itcast-haoke-manage-web | www.haoke.com | 192.168.1.18 |
| itcast-haoke-im | im.haoke.com | 192.168.1.19 |

3.1、打包springboot项目
第一步：添加springboot的打包插件
```

画面 2:
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
                <mainClass>cn.itcast.haoke.dubbo.server.DubboProvider</mainClass>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

画面 4:
```properties
# dubbo的application名称
dubbo.application.name = dubbo-provider-house-resources
# zk注册中心
dubbo.registry.address = zookeeper://192.168.1.7:2181
dubbo.registry.client = zkclient
# redis集群配置
spring.redis.jedis.pool.max-wait = 5000
spring.redis.jedis.pool.maxIdle = 10
spring.redis.jedis.pool.minIdle = 10
spring.redis.timeout = 10
spring.redis.cluster.nodes = 192.168.1.18:6380,192.168.1.7:6381
spring.redis.cluster.max-redirects=5
spring.data.mongodb.uri=mongodb://192.168.1.7:27017/testdb
spring.data.elasticsearch.cluster-name=es-itcast-cluster
spring.data.elasticsearch.clusternodes=192.168.1.7:9301,192.168.1.7:9302,192.168.1.7:9302
```

画面 6:
```properties
# dubbo的application名称
dubbo.application.name = dubbo-consumer-haoke-manage
# zk注册中心
dubbo.registry.address = zookeeper://192.168.1.7:2181
dubbo.registry.client = zkclient
# redis集群配置
spring.redis.jedis.pool.max-wait = 5000
spring.redis.jedis.pool.maxIdle = 10
spring.redis.jedis.pool.minIdle = 10
spring.redis.timeout = 10
spring.redis.cluster.nodes = 192.168.1.18:6380,192.168.1.7:6381
spring.redis.cluster.max-redirects=5
spring.data.mongodb.uri=mongodb://192.168.1.7:27017/testdb
spring.data.elasticsearch.cluster-name=es-itcast-cluster
spring.data.elasticsearch.clusternodes=192.168.1.7:9301,192.168.1.7:9302,192.168.1.7:9302
```

画面 8:
```bash
creating: itcast-haoke-manage/src/main/resources
creating: itcast-haoke-manage/src/main/resources/mapper
creating: itcast-haoke-manage/src/main/resources/mapper/house_resources
creating: itcast-haoke-manage/src/main/resources/mapper/house_resources/ThHouseResourcesMapper.xml
creating: itcast-haoke-manage/src/test/java
root@itcast01:publish# cd itcast-haoke-manage/
root@itcast01:itcast-haoke-manage# ll
```

画面 9:
```bash
root@itcast01:itcast-haoke-manage-dubbo-server-house-resources-dubbo-service# cd target/
root@itcast01:target#
```

画面 10:
```bash
root@itcast01:itcast-haoke-manage-dubbo-server-house-resources-dubbo-service# mv itcast-haoke-manage-dubbo-server-house-resources-dubbo-service-1.0-SNAPSHOT.jar /haoke/publish/haoke/
root@itcast01:target# cp itcast-haoke-manage-dubbo-server-house-resources-dubbo-service-1.0-SNAPSHOT.jar /haoke/publish/haoke/
```

画面 13:
```bash
2019-02-28 22:29:55.679 INFO 11774 --- [main] ConditionEvaluationReportLoggingListener : 
2019-02-28 22:29:55.681 ERROR 11774 --- [main] o.s.boot.SpringApplication : Application run failed
org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'graphQLController': Unsatisfied dependency expressed through field 'graphQL'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'graphQLProvider': Invocation of init method failed; nested exception is java.io.FileNotFoundException: class path resource (haoke.graphqls) cannot be resolved as absolute file path because it does not reside in the file system: jar:file:/haoke/publish/haoke/itcast-haoke-manage-api-server-1.0-SNAPSHOT.jar!/BOOT-INF/classes!/haoke.graphqls
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
