# 画面线理解：05-FreeMarker的入门：入门案例

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\05-FreeMarker的入门：入门案例_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:40, 01:31, 01:58, 02:55, 04:50, 07:30, 08:01, 08:50, 10:03, 10:41, 12:44, 13:36, 14:01, 14:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:44:20

1) 这一组画面整体在讲如何使用 FreeMarker 模板引擎在 Java 中实现数据模型到文件的输出。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构，`Company` 类中包含 `@Table`、`@Data`、`@AllArgsConstructor` 等注解，用于定义数据库表映射和生成 getter/setter。
画面2：展示 `pom.xml` 文件，正在编辑 `<dependencies>` 标签，准备添加依赖。
画面3：在 `pom.xml` 中添加了 FreeMarker、JUnit、MySQL Connector 的依赖。
画面4：在项目中右键，选择“New” -> “Java Class”，准备创建测试类。
画面5：创建了 `FreeMarkerTest01.java` 文件，位于 `test/java` 目录下。
画面6：在 `FreeMarkerTest01.java` 中编写了 FreeMarker 的导入语句和类定义。
画面7：在 IDEA 中查看 `Configuration.class` 的源码，定位到 `setTemplateLoader` 方法。
画面8：在 `FreeMarkerTest01.java` 中编写了初始化 FreeMarker 配置和模板加载器的代码。
画面9：打开 `template01.ftl` 模板文件，内容为“欢迎你，${username}”。
画面10：在 `FreeMarkerTest01.java` 中编写了获取模板、构建数据模型的代码。
画面11：在 `FreeMarkerTest01.java` 中编写了处理模板、设置输出流的代码。
画面12：运行测试，成功输出文件内容“欢迎你，任意值”。
画面13：在 `FreeMarkerTest01.java` 中添加了 `import` 语句和注释。
画面14：运行测试，提示“Cannot resolve variable 'username'”，说明变量未正确传递。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast</groupId>
    <artifactId>codetutils</artifactId>
    <version>1.0-SNAPSHOT</version>
    <pr>
```

画面3：
```xml
<dependencies>
    <dependency>
        <groupId>org.freemarker</groupId>
        <artifactId>freemarker</artifactId>
        <version>2.3.28</version>
    </dependency>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.17</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.6</version>
    </dependency>
</dependencies>
```

画面8：
```java
import freemarker.cache.FileTemplateLoader;
import freemarker.template.Configuration;
import org.junit.Test;

public class FreeMarkerTest01 {

    @Test
    public void test01() throws IOException {
        //1.创建FreeMarker的配置类
        Configuration cfg = new Configuration();
        //2.指定模板加载器，将模板存入硬盘中
        FileTemplateLoader ftl = new FileTemplateLoader(new File("templates"));
        cfg.setTemplateLoader(ftl);
        //3.获取模板
        Template template = cfg.getTemplate("template01.ftl");
        //4.构造数据模型
        Map<String, Object> dataModel = new HashMap<>();
        //5.文件输出
    }
}
```

画面9：
```ftl
欢迎你，${username}
```

画面10：
```java
//4.构造数据模型
Map<String, Object> dataModel = new HashMap<>();
dataModel.put("username", "任意值");
```

画面11：
```java
//处理模板
// 一、设置模型
// 二、writer（文件输出）
template.process(dataModel, new FileWriter(new File("C:\\Users\\(thinkPad)\\Desktop\\ihm\\day12\\test\\a.txt")));
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不评价画面美观，不输出与课程无关的内容。
