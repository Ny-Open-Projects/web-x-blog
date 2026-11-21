# 画面线理解：12.RDD、DataSet、Dataframe区别及转化

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\12.RDD、DataSet、Dataframe区别及转化_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 03:12, 03:56, 05:18, 05:47, 06:13, 07:26, 08:02, 08:40, 09:32, 10:08, 10:33, 11:35, 12:09, 12:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:41:15

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写 Spark MLlib 代码，通过 RDD 转化为 DataFrame，并展示数据操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程大纲，当前章节为“1.3. RDD、DataSet、DataFrame区别及转化”，并显示 Student 类的 Java 代码。
画面 2: 在 IntelliJ IDEA 中打开项目，显示 Student 类的完整代码，包含 id、name、age 字段及 getter/setter 方法。
画面 3: 展示 TestMLib.java 文件中关于两个矩阵相加的代码，包含 System.out.println 输出语句。
画面 4: 在 TestMLib.java 中，光标位于 SparkSession.builder().appName().getOrCreate() 代码行，显示 SparkSession 的可用方法。
画面 5: 展示 TestMLib.java 中的 JavaRDD<Vector> rdd1 和 JavaRDD<IndexedRow> rdd2 的创建代码。
画面 6: 展示 TestMLib.java 中的 SparkSession.read().textFile("F:\\code\\files\\users.txt") 代码，用于读取文本文件。
画面 7: 展示 TestMLib.java 中的 JavaRDD<String> rdd1.map(...) 代码，用于将字符串按空格分割。
画面 8: 展示 TestMLib.java 中的 SparkSession.builder().appName("test").getOrCreate() 代码，用于创建 SparkSession。
画面 9: 展示 TestMLib.java 中的 JavaRDD<String> rdd1.map(...) 代码，用于将字符串按空格分割。
画面 10: 展示 TestMLib.java 中的 sparkSession.createDataFrame(...) 代码，用于将 RDD 转化为 DataFrame。
画面 11: 展示 TestMLib.java 中的 dataset.show() 代码，用于显示 DataFrame 数据。
画面 12: 展示 TestMLib.java 中的 dataset.select(col("id"), col("name")).orderBy(dataset.col("id")).show() 代码，用于选择并排序数据。
画面 13: 展示课程大纲，当前章节为“1.3. RDD、DataSet、DataFrame区别及转化”，并显示 Student 类的 Java 代码。
画面 14: 展示课程大纲，当前章节为“1.3. RDD、DataSet、DataFrame区别及转化”，并显示 Student 类的 Java 代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
import java.io.Serializable;
public class Student implements Serializable {
    private Long id;
    private String name;
    private Integer age;
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Integer getAge() {
        return age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }
}

画面 2:
import java.io.Serializable;
public class Student implements Serializable {
    private Long id;
    private String name;
    private Integer age;
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Integer getAge() { return age; }
    public void setAge(Integer age) { this.age = age; }
}

画面 3:
BlockMatrix addBlockMatrix = blockMatrix.add(blockMatrix);
System.out.println(addBlockMatrix.numCols());
System.out.println(addBlockMatrix.numRows());
List<Tuple2<Tuple2<Object, Object>, Matrix>> collect = addBlockMatrix.block
.collect().forEach(tuple2MatrixTuple2 -> System.out.println(tuple2MatrixTuple2));

画面 4:
SparkSession sparkSession = SparkSession.builder()
    .appName("test")
    .getOrCreate();

画面 5:
JavaRDD<Vector> rdd1 = fileRDD.map(v -> {
    String[] ss = v.split(" ");
    double[] da = new double[ss.length];
    for (int i = 0; i < ss.length; i++) {
        da[i] = Double.valueOf(ss[i]);
    }
    return Vectors.dense(da);
});
JavaRDD<IndexedRow> rdd2 = rdd1.map(v -> new IndexedRow(v.size(), v));

画面 6:
sparkSession.read().textFile("F:\\code\\files\\users.txt");

画面 7:
JavaRDD<String> rdd1 = sparkSession.read().textFile("F:\\code\\files\\users.txt").javaRDD();
JavaRDD<String> rdd1 = rdd1.map(v -> {
    String[] ss = v.split(" ");
    return ss[0];
});

画面 8:
SparkSession sparkSession = SparkSession.builder()
    .appName("test")
    .getOrCreate();

画面 9:
JavaRDD<String> rdd1 = sparkSession.read().textFile("F:\\code\\files\\users.txt").javaRDD();
JavaRDD<String> rdd1 = rdd1.map(v -> {
    String[] ss = v.split(" ");
    return ss[0];
});

画面 10:
Dataset<Row> dataSet = sparkSession.createDataFrame(rdd2, Student.class);

画面 11:
dataset.show();

画面 12:
dataset.select(col("id"), col("name")).orderBy(dataset.col("id")).show();

画面 13:
import java.io.Serializable;
public class Student implements Serializable {
    private Long id;
    private String name;
    private Integer age;
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Integer getAge() {
        return age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }
}

画面 14:
import java.io.Serializable;
public class Student implements Serializable {
    private Long id;
    private String name;
    private Integer age;
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Integer getAge() {
        return age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
