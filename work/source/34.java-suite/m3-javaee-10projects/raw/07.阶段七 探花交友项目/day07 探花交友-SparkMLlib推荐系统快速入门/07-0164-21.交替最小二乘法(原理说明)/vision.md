# 画面线理解：21.交替最小二乘法（原理说明）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\21.交替最小二乘法（原理说明）_【海量资源尽在 666java.com】.mp4
- 抽帧：7 帧 @ 00:01, 00:05, 00:39, 00:40, 00:41, 01:30, 02:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:45:46

1) 这一组画面整体在讲Spark MLlib中交替最小二乘法（ALS）推荐算法的数学原理和流程。

2) 按时间顺序列出每张画面的要点：
画面1：
- 标题：“7.2、交替最小二乘法”
- 内容：以用户、商品为例说明，用户-商品评分矩阵可分解为用户特征矩阵V和电影特征矩阵U。
- 图表：展示Rating Matrix (N x M)、User Feature Matrix (F x N)、Movie Feature Matrix (F x M)，并用箭头表示分解关系。
- 文字说明：解释目标函数和最小化距离。

画面2：
- 标题：“7.2、交替最小二乘法”
- 内容：与画面1相同，但鼠标指针位置不同。
- 图表：与画面1相同，箭头指向User Feature Matrix和Movie Feature Matrix。

画面3：
- 标题：“7.2、交替最小二乘法”
- 内容：与画面1相同，但鼠标指针位置不同。
- 图表：与画面1相同，箭头指向User Feature Matrix和Movie Feature Matrix。

画面4：
- 标题：“7.2、交替最小二乘法”
- 内容：与画面1相同，但鼠标指针位置不同。
- 图表：与画面1相同，箭头指向User Feature Matrix和Movie Feature Matrix。

画面5：
- 标题：“7.3、ALS算法流程”
- 内容：解释ALS算法中U和V的初始化、交替优化过程。
- 图表：展示User Feature Matrix (F x N)、Movie Feature Matrix (F x M)相乘等于Rating Matrix (N x M)的矩阵运算。

画面6：
- 标题：“7.3、ALS算法流程”
- 内容：与画面5相同，但鼠标指针位置不同。
- 图表：与画面5相同，展示矩阵运算。

画面7：
- 标题：“7.3、ALS算法流程”
- 内容：与画面5相同，但鼠标指针位置不同。
- 图表：与画面5相同，展示矩阵运算。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
- 标题：
  - 画面1、2、3、4：7.2、交替最小二乘法
  - 画面5、6、7：7.3、ALS算法流程
- 架构图/流程图结构：
  - 画面1、2、3、4：Rating Matrix (N x M) → User Feature Matrix (F x N) 和 Movie Feature Matrix (F x M)
  - 画面5、6、7：User Feature Matrix (F x N) × Movie Feature Matrix (F x M) = Rating Matrix (N x M)
- 表格数据：
  - Rating Matrix (N x M)：
    ```
    5  3  5
    4  2  1
    0  3  3
    ```
  - User Feature Matrix (F x N)：
    ```
    f₁  1  -4  1
    f₂  -2  0  -3
    f₃  0  -5  1
    ```
  - Movie Feature Matrix (F x M)：
    ```
    f₁  -1  0  -2
    f₂  4  -4  1
    f₃  0  2  2
    ```

5) 无。
