# 画面线理解：05.阿里云OSS存储之SDK的使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\05.阿里云OSS存储之SDK的使用【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:28, 02:12, 02:56, 04:40, 05:27, 06:24, 07:52, 08:43, 10:00, 11:10, 12:36, 13:41, 14:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:52:04

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成阿里云 OSS 服务，实现图片上传功能，包括添加依赖、配置文件和编写配置类。

2) 按时间顺序列出每张画面的要点：
画面 1: 课程文档页面，标题为“2.4、实现图片上传”，说明在 itcast-haoke-manage-api-server 中实现图片上传功能。
画面 2: 阿里云 OSS 官方文档页面，展示“文件上传”和“流式上传”等概念。
画面 3: 阿里云 OSS 官方文档页面，展示“流式上传”部分的 Java 代码示例。
画面 4: IntelliJ IDEA 编辑器中显示 Maven 依赖配置，包含 aliyun-sdk-oss、lombok 和 joda-time。
画面 5: IntelliJ IDEA 编辑器中显示 Maven 依赖配置，包含 zookeeper、zkclient、lombok 和 joda-time。
画面 6: IntelliJ IDEA 编辑器中显示 AliyunConfig.java 文件，正在编写 @Bean 注解的 OSSClient。
画面 7: IntelliJ IDEA 编辑器中显示 resources 目录，弹出“New File”对话框，准备创建 aliyun.properties 文件。
画面 8: IntelliJ IDEA 编辑器中显示 AliyunConfig.java 文件，已编写 @PropertySource 注解和构造方法。
画面 9: IntelliJ IDEA 编辑器中显示 AliyunConfig.java 文件，弹出“Generate”菜单，准备生成 Getter 方法。
画面 10: IntelliJ IDEA 编辑器中显示 aliyun.properties 文件，已编写 endpoint、accessKeyId 和 accessKeySecret 的配置。
画面 11: 阿里云 RAM 控制台页面，显示“用户AccessKey”列表，正在加载。
画面 12: 课程文档页面，标题为“2.4.3、编写AliyunConfig”，显示 aliyun.endpoint、aliyun.accessKeyId、aliyun.accessKeySecret、aliyun.bucketName 和 aliyn.urlPrefix 的配置示例。
画面 13: 课程文档页面，标题为“2.4.3、编写AliyunConfig”，显示 AliyunConfig.java 文件的完整代码。
画面 14: 课程文档页面，标题为“2.4.3、编写AliyunConfig”，显示 AliyunConfig.java 文件的完整代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```xml
<dependency>
    <groupId>com.github.sgroschupf</groupId>
    <artifactId>zkclient</artifactId>
    <version>0.1</version>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.4</version>
</dependency>
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.9.3</version>
</dependency>
```

画面 5:
```xml
<dependency>
    <groupId>org.apache.zookeeper</groupId>
    <artifactId>zookeeper</artifactId>
    <version>3.4.13</version>
</dependency>
<dependency>
    <groupId>com.github.sgroschupf</groupId>
    <artifactId>zkclient</artifactId>
    <version>0.1</version>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.4</version>
</dependency>
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.9.3</version>
</dependency>
```

画面 6:
```java
package cn.itcast.haoke.dubbo.api.config;

import com.aliyun.oss.OSSClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AliyunConfig {

    @Bean
    public OSSClient ossClient() {
    }
}
```

画面 8:
```java
package cn.itcast.haoke.dubbo.api.config;

import com.aliyun.oss.OSSClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource("classpath:aliyun.properties")
public class AliyunConfig {

    @Bean
    public OSSClient ossClient() {
        return new OSSClient(endpoint, accessKeyId, accessKeySecret);
    }
}
```

画面 9:
```java
package cn.itcast.haoke.dubbo.api.config;

import com.aliyun.oss.OSSClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration
@PropertySource("classpath:aliyun.properties")
@ConfigurationProperties(prefix = "aliyun")
public class AliyunConfig {

    private String endpoint;
    private String accessKeyId;
    private String accessKeySecret;
    private String bucketName;
    private String urlPrefix;

    @Bean
    public OSSClient ossClient() {
        return new OSSClient(endpoint, accessKeyId, accessKeySecret);
    }
}
```

画面 10:
```properties
aliyun.endpoint = "http://oss-cn-hangzhou.aliyuncs.com";
aliyun.accessKeyId = "<yourAccessKeyId>";
aliyun.accessKeySecret = "<yourAccessKeySecret>";
```

画面 12:
```properties
aliyun.endpoint:oss-cn-qingdao.aliyuncs.com
aliyun.accessKeyId:LTIAFc7FusP7Rfq
aliyun.accessKeySecret:2Vvo3qlMwvTy81xcmFsCfU2ZcHCK
aliyun.bucketName:itcast-haoke
aliyun.urlPrefix:http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2.4、实现图片上传”，说明在 itcast-haoke-manage-api-server 中实现图片上传功能。
画面 12: PPT 标题为“2.4.3、编写AliyunConfig”，显示 aliyun.endpoint、aliyun.accessKeyId、aliyun.accessKeySecret、aliyun.bucketName 和 aliyn.urlPrefix 的配置示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
