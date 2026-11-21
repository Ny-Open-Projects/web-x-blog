# 画面线理解：21-Hive的基本操作-自定义函数

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\21-Hive的基本操作-自定义函数【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:08, 02:56, 03:18, 03:48, 04:42, 05:56, 06:54, 07:46, 08:34, 09:09, 09:34, 10:42, 11:26, 12:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:57:01

1) 这一组画面整体在讲如何在Hive中开发自定义函数（UDF），包括创建Maven项目、添加依赖、编写Java代码实现自定义函数。

2) 按时间顺序列出每张画面的要点：
画面1：展示Hive自定义函数（UDF）的分类，包括UDF、UDAF、UDTF，并给出官方文档地址。
画面2：在IDEA中打开Maven项目，展示pom.xml文件的初始结构，包含基本的项目配置。
画面3：在pom.xml中添加Hadoop核心依赖。
画面4：在pom.xml中添加Hive执行依赖。
画面5：在IDEA中打开MyUDF.java文件，展示继承自UDF的类结构。
画面6：在MyUDF.java中编写自定义函数，重写evaluate方法。
画面7：在MyUDF.java中编写evaluate方法的具体实现，判断输入是否为字符串。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
3. 根据用户自定义函数类别分为以下三种：
1. UDF (User-Defined-Function)
2. UDAF (User-Defined Aggregation Function)
   • 聚集函数，多进一出
   • 类似于：count / max / min
3. UDTF (User-Defined Table-Generating Functions)
   • 一进多出
   • 如 lateral view explode()

画面2：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast</groupId>
    <artifactId>day05_hive_udf_demo</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>

画面3：
<dependencies>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-common</artifactId>
        <version>3.1.1</version>
    </dependency>
</dependencies>

画面4：
<dependency>
    <groupId>org.apache.hive</groupId>
    <artifactId>hive-exec</artifactId>
    <version>3.1.1</version>
</dependency>

画面5：
package cn.itcast.udf;
import org.apache.hadoop.hive.ql.exec.UDF;
public class MyUDF extends UDF {
    public boolean equals(Object o) {
        Object
    }
    protected Object clone() {
        Object
    }
    public int hashCode() {
        Object
    }
    protected void finalize() {
        Object
    }
    public String toString() {
        Object
    }
    public String[] getRequiredFiles() {
        UDF
    }
    public String[] getRequiredJars() {
        UDF
    }
    public LDMethodResolver getResolver() {
        UDF
    }
    public void setResolver(LDMethodResolver rslv) {
        UDF
    }
}

画面6：
package cn.itcast.udf;
import org.apache.hadoop.hive.ql.exec.UDF;
public class MyUDF extends UDF {
    evaluate_
}

画面7：
package cn.itcast.udf;
import org.apache.hadoop.hive.ql.exec.UDF;
public class MyUDF extends UDF {
    public Text evaluate(String str) {
        if(str.toString().equals("hello")) {
            return new Text("world");
        }
        return new Text(str);
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3.2. 自定义函数”，内容包括Hive自定义函数的分类和官方文档地址。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
