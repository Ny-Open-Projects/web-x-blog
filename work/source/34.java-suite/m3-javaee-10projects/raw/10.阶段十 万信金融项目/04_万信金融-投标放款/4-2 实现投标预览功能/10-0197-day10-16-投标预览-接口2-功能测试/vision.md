# 画面线理解：day10-16-投标预览-接口2-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-16-投标预览-接口2-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:23, 00:38, 00:42, 00:49, 00:53, 01:00, 01:06, 01:09, 01:14, 01:23, 01:35, 01:37, 01:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:26:54

1) 这一组画面整体在讲什么（一句话）：
演示通过 Swagger UI 调用交易中心服务的 API，查询特定项目下的投标记录，并展示数据库中的对应数据和后端 Java 代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示系统架构图，包含“调用端/APP”、“交易中心”、“用户服务”、“存管通道服务”和“存管系统”五个模块，以及它们之间的接口调用关系（如 1.1 获取标的的信息、1.5 保存投标人信息等）。
画面 2: 展示 DBeaver 数据库管理工具，连接到 `yq_transaction_1` 数据库，显示 `tender` 表中的数据，其中 `PROJECT_ID` 为 `2139483643803590657`。
画面 3: 展示 Swagger UI 页面，标题为“交易中心服务”，显示 API 文档的入口。
画面 4: 展示 Swagger UI 中的“transaction”控制器下的 API 列表，包括 PUT、POST、GET 等不同类型的接口。
画面 5: 展示 Swagger UI 中的 GET 接口 `/tenders/projects/{id}`，用于根据项目 ID 查询投标记录。
画面 6: 展示 Swagger UI 中的 GET 接口 `/tenders/projects/{id}` 的参数设置界面，其中 `id` 字段为空。
画面 7: 展示 DBeaver 数据库管理工具，显示 `tender` 表中的数据，其中 `PROJECT_ID` 为 `2139483643803590657`。
画面 8: 展示 Swagger UI 中的 GET 接口 `/tenders/projects/{id}` 的参数设置界面，其中 `id` 字段为空。
画面 9: 展示 Swagger UI 中的 GET 接口 `/tenders/projects/{id}` 的参数设置界面，其中 `id` 字段已填写为 `2139483643803590657`，并点击了“Execute”按钮。
画面 10: 展示 Swagger UI 中的 GET 接口 `/tenders/projects/{id}` 的响应结果，包含 JSON 格式的投标记录数据。
画面 11: 展示 DBeaver 数据库管理工具，显示 `tender` 表中的数据，其中 `PROJECT_ID` 为 `2139483643803590657`。
画面 12: 展示 IntelliJ IDEA 中的 Java 代码，位于 `TenderMapper.java` 文件中，包含一个 SQL 查询语句：
```java
Select("SELECT IFNULL(SUM(AMOUNT), 0.0) FROM tender WHERE PROJECT_ID = #{id} AND STATUS = 1")
List<BigDecimal> selectAmountInvestedByProjectId(Long id);
```
画面 13: 展示 Swagger UI 中的 GET 接口 `/tenders/projects/{id}` 的响应结果，包含 JSON 格式的投标记录数据和响应头信息。
画面 14: 展示 Swagger UI 中的 GET 接口 `/tenders/projects/{id}` 的响应结果，包含 JSON 格式的投标记录数据和响应头信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 12 中的代码：
```java
/**
 * 用于操作投标信息的mapper接口
 */
public interface TenderMapper extends BaseMapper<Tender> {

    /**
     * 根据标的的id 获得标的的三拦金额。如果未返回0.0
     * @param id
     * @return
     */
    Select("SELECT IFNULL(SUM(AMOUNT), 0.0) FROM tender WHERE PROJECT_ID = #{id} AND STATUS = 1")
    List<BigDecimal> selectAmountInvestedByProjectId(Long id);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 中的架构图：
- “调用端/APP” → “交易中心”（接口 1.1、1.2、1.3、1.4）
- “交易中心” → “用户服务”（接口 1.5、1.6）
- “用户服务” → “存管通道服务”（接口 2.1）
- “存管通道服务” → “存管系统”（接口 2.2、2.3、2.4、2.5、2.6）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
