# 画面线理解：06-FreeMarker的入门：字符串模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\06-FreeMarker的入门：字符串模板_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:30, 01:19, 02:08, 03:10, 03:25, 04:00, 04:34, 04:51, 05:41, 06:18, 06:33, 07:14, 08:14, 09:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:45:10

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中使用 FreeMarker 模板引擎，通过 Java 代码加载模板、设置数据模型并输出处理后的文本。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Windows 桌面，有“黑马程序员”和“博学谷”标志，无代码或操作。
画面 2: 在 IntelliJ IDEA 中打开 FreeMarkerTest01.java，展示第一个 FreeMarker 程序的代码框架，包含创建模板加载器、获取模板、设置数据模型和处理模板的注释。
画面 3: 在 IntelliJ IDEA 中打开 FreeMarkerTest02.java，展示一个使用 @Test 注解的测试类，代码中包含 JUnit 注解和 Java 标准库的导入。
画面 4: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 5: 在 IntelliJ IDEA 中，显示了 freemarker-2.3.20.jar 的源码，展示了 StringTemplateLoader 类的实现，包括 putTemplate、findTemplateSource 等方法。
画面 6: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 7: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 8: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 9: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 10: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 11: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 12: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 13: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 14: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

//第一个FreeMarker程序（数据+模板→文件输出）
//1.操作步骤
public class FreeMarkerTest01 {
    //创建新类
    public static void main(String[] args) {
        //1.创建模板加载器
        FileTemplateLoader ftl = new FileTemplateLoader(new File("templates"));
        //2.获取模板
        Template template = ftl.getTemplate("template01.ftl");
        //3.构造数据模型
        Map<String, Object> dataModel = new HashMap<>();
        dataModel.put("username", "张三");
        //4.处理模板
        try {
            template.process(dataModel, new PrintWriter("output.txt"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

画面 3:
```java
package cn.itcast.freemarker.test;

import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        //4.处理模板
    }
}
```

画面 4:
```java
package cn.itcast.freemarker.test;
import freemarker.template.Configuration;
import org.junit.Test;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        //4.处理模板
    }
}
```

画面 5:
```java
package freemarker.cache;

import ...

public class StringTemplateLoader implements TemplateLoader {
    private final Map templates = new HashMap();

    public StringTemplateLoader() {
    }

    public void putTemplate(String name, String templateSource) {
        this.putTemplate(name, templateSource, System.currentTimeMillis());
    }

    public void putTemplate(String name, String templateSource, long lastModified) {
        this.templates.put(name, new StringTemplateSource(name, templateSource, lastModified));
    }

    public void closeTemplateSource(Object templateSource) {
        this.templates.remove(templateSource);
    }

    public Object findTemplateSource(String name) {
        return this.templates.get(name);
    }

    public long getLastModified(Object templateSource) {
        return ((StringTemplateSource)templateSource).lastModified;
    }
}
```

画面 6:
```java
import freemarker.template.Configuration;
import org.junit.Test;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        //4.处理模板
    }
}
```

画面 7:
```java
import java.io.IOException;
import java.io.StringReader;
import java.io.StringWriter;
import java.util.HashMap;
import java.util.Map;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() throws Exception {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        String templateString = "欢迎您，${username}";
        //4.处理模板
        Template template = new Template("name1", new StringReader(templateString), cfg);
        //5.处理模板
    }
}
```

画面 8:
```java
import freemarker.template.Template;
import org.junit.Test;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        String templateString = "欢迎您，${username}";
        //4.处理模板
        Template template = new Template("name1", new StringReader(templateString), cfg);
        //5.处理模板
    }
}
```

画面 9:
```java
import java.io.IOException;
import java.io.StringReader;
import java.util.HashMap;
import java.util.Map;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() throws Exception {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        String templateString = "欢迎您，${username}";
        //4.处理模板
        Template template = new Template("name1", new StringReader(templateString), cfg);
        //5.处理模板
    }
}
```

画面 10:
```java
import java.util.HashMap;
import java.util.Map;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() throws Exception {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        String templateString = "欢迎您，${username}";
        //4.处理模板
        Template template = new Template("name1", new StringReader(templateString), cfg);
        //5.处理模板
    }
}
```

画面 11:
```java
import java.util.HashMap;
import java.util.Map;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() throws Exception {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //
