# 画面线理解：08.MybatisPlus入门Lombok的使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\08.MybatisPlus入门Lombok的使用【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:40, 03:38, 04:15, 05:09, 05:35, 06:29, 08:13, 09:11, 10:06, 10:54, 11:55, 12:54, 13:36, 14:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:43:15

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中安装 Lombok 插件，并通过 Lombok 注解（@Data、@Builder、@AllArgsConstructor）简化 Java POJO 类的代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 PDF 文档中 Lombok 的介绍和 Maven 依赖配置，标题为“2.7.1、配置安装”，内容包含 Maven 依赖代码。
画面 2：展示在 IntelliJ IDEA 的设置中搜索并安装 Lombok 插件的界面。
画面 3：展示 Lombok 插件安装成功后的状态，显示“Installed”。
画面 4：展示 PDF 文档中 Lombok 的常用注解说明，包括 @Data、@Setter、@Getter 等。
画面 5：展示在 IntelliJ IDEA 中一个名为 Item 的 Java 类，包含手动编写的 get/set 方法。
画面 6：展示在 IntelliJ IDEA 中对 Item 类的结构视图，显示其属性。
画面 7：展示 PDF 文档中关于 @Builder 注解的说明。
画面 8：展示在 IntelliJ IDEA 中为 Item 类添加 @Data 注解，然后使用代码生成器自动生成 getter/setter 等方法。
画面 9：展示运行结果，显示“Process finished with exit code 0”，并标注“测试三：@AllArgsConstructor注解的使用”。
画面 10：展示在 IntelliJ IDEA 中为 Item 类添加 @AllArgsConstructor 注解，然后使用代码生成器自动生成构造方法。
画面 11：展示在 IntelliJ IDEA 中为 Item 类添加 @Builder 注解，然后使用代码生成器自动生成 Builder 模式。
画面 12：展示运行结果，显示“Process finished with exit code 0”，并标注“测试三：@AllArgsConstructor注解的使用”。
画面 13：展示在 IntelliJ IDEA 中对 UserMapperTest 类的测试代码，包含分页查询和更新操作。
画面 14：展示 PDF 文档中 Lombok 的介绍和 Maven 依赖配置，标题为“2.7.1、配置安装”，内容包含 Maven 依赖代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```xml
# 指定全局配置文件
mybatis-plus.config-location = classpath:mybatis-config.xml
# 指定mapper.xml文件
mybatis plus.mapper locations = classpath:mybatis/*.xml
```
画面 1：
```xml
<!--简化代码的工具包-->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
    <version>1.18.4</version>
</dependency>
```
画面 8：
```java
import lombok.Data;
import lombok.extern.slf4j.Slf4j;

@Data
public class Item {
    private Long id;
    private String title;
    private Long price;
}
```
画面 9：
```java
public static void main(String[] args) {
    log.info("实例化Item对象");
    new Item();
}
```
画面 10：
```java
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class Item {
    private Long id;
    private String title;
    private Long price;

    public Item() {
        log.info("写日志。。。。");
    }
}
```
画面 11：
```java
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class Item {
    private Long id;
    private String title;
    private Long price;

    @Builder
    public Item() {
        log.info("写日志。。。。");
    }
}
```
画面 13：
```java
@Test
public void testSelectPage() {
    Page<User> page = new Page<>(current, size);
    user.selectPage(page, queryWrapper);
    System.out.println("总条数-------> " + page.getTotal());
    System.out.println("当前每页显示数-------> " + page.getSize());
    List<User> userList = page.getRecords();
    for (User user : userList) {
        System.out.println(user);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4：PPT 标题为“2.7.2、常用注解”，内容包括：
- @Data：注解在类上，提供所有属性的 getting 和 setting 方法，此外还提供了 equals、canEqual、hashCode、toString 方法。
- @Setter：注解在属性上，为属性提供 setting 方法。
- @Getter：注解在属性上，为属性提供 getting 方法。
- @Slf4j：注解在类上，为类提供一个属性名为 log 的 slf4j 日志对象。
- @NoArgsConstructor：注解在类上，为类提供一个无参的构造方法。
- @AllArgsConstructor：注解在类上，为类提供一个全参的构造方法。
- @Builder：使用 Builder 模式构建对象。

画面 7：PPT 标题为“@Builder：使用Builder模式构建对象”。

画面 13：PPT 标题为“测试三：@AllArgsConstructor注解的使用”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
