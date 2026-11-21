# 画面线理解：9-MapReduce-流量统计求和-排序-Mapper和Reducer编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\9-MapReduce-流量统计求和-排序-Mapper和Reducer编写【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:22, 00:45, 01:31, 02:37, 02:56, 03:09, 03:21, 04:04, 04:20, 04:45, 05:37, 05:59, 06:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:36:16

1) 这一组画面整体在讲如何使用 MapReduce 编写一个对流量数据进行分组和排序的程序，重点是自定义的 FlowBean 类和 Mapper/Reducer 的实现。

2) 按时间顺序列出每张画面的要点：
画面1: 在项目中右键点击 "day04_mapeuduce_combiner" 目录，选择 "Delete" 选项，准备删除该模块。
画面2: 编辑 FlowCountSortMapper.java 文件，定义了 Mapper 类，继承自 Mapper<LongWritable, Text, FlowBean, Text>，并导入了必要的包。
画面3: 在 Mapper 类的泛型中，将输出的 Value 类型从 Text 改为 FlowBean。
画面4: 显示了一个 Excel 文件，内容是原始的流量数据，包含手机号、流量、上下行等字段。
画面5: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面6: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面7: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面8: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面9: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面10: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面11: 编辑 FlowCountSortReducer.java 文件，定义了 Reducer 类，继承自 Reducer<FlowBean, Text, FlowBean, Text>。
画面12: 在 FlowCountSortReducer.java 中，将 Reducer 的泛型从 Reducer<FlowBean, Text, FlowBean, Text> 改为 Reducer<FlowBean, Text, FlowBean, Text>。
画面13: 在 FlowCountSortReducer.java 中，为 Reducer 类添加了 import 语句。
画面14: 在 FlowCountSortReducer.java 中，为 Reducer 类添加了 import 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面2:
```java
package cn.itcast.mapeuduce_sort;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mrpackage.Mapper;

public class FlowCountSortMapper extends Mapper<LongWritable, Text, FlowBean, Text> {
}
```

画面3:
```java
package cn.itcast.mapeuduce_sort;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mrpackage.Mapper;

public class FlowCountSortMapper extends Mapper<LongWritable, Text, FlowBean, Text> {
}
```

画面5:
```java
import org.apache.hadoop.mrpackage.FlowBean;
```

画面6:
```java
import org.apache.hadoop.mrpackage.FlowBean;
```

画面7:
```java
import org.apache.hadoop.mrpackage.FlowBean;
```

画面8:
```java
import org.apache.hadoop.mrpackage.FlowBean;
```

画面9:
```java
import org.apache.hadoop.mrpackage.FlowBean;
```

画面10:
```java
import org.apache.hadoop.mrpackage.FlowBean;
```

画面11:
```java
package cn.itcast.mapeuduce_sort;
import org.apache.hadoop.mrpackage.Reducer;
public class FlowCountSortReducer extends Reducer<FlowBean, Text, FlowBean, Text> {
}
```

画面12:
```java
package cn.itcast.mapeuduce_sort;
import org.apache.hadoop.mrpackage.Reducer;
public class FlowCountSortReducer extends Reducer<FlowBean, Text, FlowBean, Text> {
}
```

画面13:
```java
import java.io.IOException;
```

画面14:
```java
import java.io.IOException;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
