# 画面线理解：05_自媒体_fastdfs代码封装

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\05_自媒体_fastdfs代码封装【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 01:57, 02:27, 02:41, 03:14, 03:57, 04:32, 05:00, 05:46, 07:00, 07:27, 07:46, 07:58, 09:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:42:35

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Boot 项目中集成 FastDFS 文件存储服务，包括配置文件、自动配置类、客户端工具类的编写与使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档内容，标题为“4.2 素材上传接口”下的“4.2.2 接口定义”，包含接口标准信息：接口名称 /api/v1/media/material/upload_picture，需求DTO MultipartFile，响应DTO WmMaterial。
画面2：展示 VMware Workstation 界面，显示虚拟机列表，当前选中的是“phyougou-image-server_133”。
画面3：展示 IntelliJ IDEA 中的登录服务代码，包含用户登录逻辑，使用了 WulianMapper 查询用户信息并进行密码比对。
画面4：展示 pom.xml 文件内容，包含对 Apache Curator 和 FastDFS Spring Boot Starter 的依赖配置。
画面5：展示项目资源目录结构，选中了 fast-dfs.properties 文件。
画面6：展示文档内容，标题为“4.1.2 FastDfsConfig”，说明该类用于自动化配置 FastDFS 核心参数并设置连接池。
画面7：展示 IntelliJ IDEA 中右键菜单，准备新建一个 Java 类。
画面8：展示 FastDfsConfig.java 文件内容，包含创建 PooledConnectionFactory 和 TrackerConnectionManager 的代码。
画面9：展示 fast-dfs.properties 文件内容，其中 tracker-server 配置为 192.168.25.133:22122。
画面10：展示文档内容，标题为“4.1.3 FastDfsClient”，包含上传文件方法的 JavaDoc 注释。
画面11：展示 FastDfsClient.java 文件内容，包含上传文件方法的实现，使用 storageClient 调用上传接口。
画面12：展示 FastDfsClient.java 文件内容，展示上传文件方法的完整代码，包括处理文件名和扩展名。
画面13：展示 FastDfsClient.java 文件内容，展示上传文件方法的完整代码，包括处理文件名和扩展名。
画面14：展示项目结构和 InitConfig.java 文件内容，该类用于初始化 FastDfsClient 实例并注入到 Spring 容器中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
4.2 素材上传接口
4.2.1
4.2.2 接口定义
(1) 基本定义
参考标准 请参考通用接口规范
接口名称 /api/v1/media/material/upload_picture
需求DTO MultipartFile
响应DTO WmMaterial
(2) CODE定义
```

画面4：
```xml
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-framework</artifactId>
    <version>${curator.version}</version>
</dependency>
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-recipes</artifactId>
    <version>${curator.version}</version>
</dependency>
<dependency>
    <groupId>com.luban</groupId>
    <artifactId>fastdfs-spring-boot-starter</artifactId>
    <version>${fastdfs.version}</version>
    <exclusions>
    </exclusions>
</dependency>
```

画面5：
```
fast-dfs.properties
fast.dfs.connect-timeout=3000
fast.dfs.so-timeout=6000
fast.dfs.tracker-server=192.168.25.133:22122
```

画面6：
```java
/**
 * 自动化配置核心数据的连接池
 */
@Configuration
@ConfigurationProperties(prefix = "fast.dfs")
@PropertySource({"classpath:fast-dfs.properties"})
public class FastDfsConfig extends FeatsAutoConfiguration {
    public FastDfsConfig(GdfsProperties properties) {
        super(properties);
    }
    @Bean
    public PooledConnectionFactory pooledConnectionFactory() {
        PooledConnectionFactory pooledConnectionFactory = new PooledConnectionFactory();
        pooledConnectionFactory.setConnectTimeout(getConnectTimeout());
        pooledConnectionFactory.setSoTimeout(getSoTimeout());
        return pooledConnectionFactory;
    }
}
```

画面8：
```java
public PooledConnectionFactory pooledConnectionFactory() {
    PooledConnectionFactory pooledConnectionFactory = new PooledConnectionFactory();
    pooledConnectionFactory.setConnectTimeout(getConnectTimeout());
    pooledConnectionFactory.setSoTimeout(getSoTimeout());
    return pooledConnectionFactory;
}

@Bean
public TrackerConnectionManager trackerConnectionManager(GdfsConnectionPool gdfsConnectionPool) {
    return new TrackerConnectionManager(gdfsConnectionPool, Arrays.asList(trackerServer));
}
```

画面9：
```
fast.dfs.connect-timeout=3000
fast.dfs.so-timeout=6000
fast.dfs.tracker-server=192.168.25.133:22122
```

画面10：
```java
/**
 * 上传文件方法
 * @Title: uploadFile
 * @Description: /
 * @param fileName 文件全路径
 * @param extName 文件扩展名，不包含（.）
 * @return
 * @throws Exception
 */
public String uploadFile(String fileName, String extName) throws Exception {
    StorePath s = storageClient.uploadFile(FileUtils.readFileToByteArray(new File(fileName)), extName);
    String result = s.getFullPath();
    return result;
}
```

画面11：
```java
/**
 * 上传文件方法
 * @Title: uploadFile
 * @Description: /
 * @param fileName 文件全路径
 * @param extName 文件扩展名，不包含（.）
 * @return
 * @throws Exception
 */
public String uploadFile(String fileName, String extName) throws Exception {
    StorePath s = storageClient.uploadFile(FileUtils.readFileToByteArray(new File(fileName)), extName);
    String result = s.getFullPath();
    return result;
}
```

画面12：
```java
/**
 * 上传文件方法
 * @Title: uploadFile
 * @Description: /
 * @param fileContent 文件的内容，字节数组
 * @param extName 文件扩展名
 * @return
 * @throws Exception
 */
public String uploadFile(byte[] fileContent, String extName) throws Exception {
    StorePath s = storageClient.uploadFile(fileContent, extName);
    String result = s.getFullPath();
    return result;
}
```

画面13：
```java
/**
 * 上传文件方法
 * @Title: uploadFile
 * @Description: /
 * @param fileName 文件全路径
 * @param extName 文件扩展名，不包含（.）
 * @return
 * @throws Exception
 */
public String uploadFile(String fileName, String extName) throws Exception {
    StorePath s = storageClient.uploadFile(FileUtils.readFileToByteArray(new File(fileName)), extName);
    String result = s.getFullPath();
    return result;
}
```

画面14：
```java
package com.heima.common.fastdfs;

import com.lubanuguo.fastdfs.domain.StorePath;
import com.lubanuguo.fastdfs.service.FastFileStorageClient;
import org.apache.commons.io.FileUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.File;

@Component
public class FastDfsClient {
    @Autowired
    FastFileStorageClient storageClient;
    /**
     * 上传文件方法
     * @Title: uploadFile
     * @Description: /
     * @param fileName 文件全路径
     * @param extName 文件扩展名，不包含（.）
     * @return
     * @throws Exception
     */
    public String uploadFile(String fileName, String extName) throws Exception {
        StorePath s = storageClient.uploadFile(FileUtils.readFileToByteArray(new File(fileName)), extName);
        String result = s.getFullPath();
        return result;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“4.2 素材上传接口”，子标题“4.2.2 接口定义”，包含表格数据：接口名称、需求DTO、响应DTO。
画面6：PPT 标题为“4.1.2 FastDfsConfig”，说明该类用于自动化配置 FastDFS 核心参数并设置连接池。
画面14：PPT 标题为“InitConfig.java”，说明该类用于初始化 FastDfsClient 实例并注入到 Spring 容器中。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
