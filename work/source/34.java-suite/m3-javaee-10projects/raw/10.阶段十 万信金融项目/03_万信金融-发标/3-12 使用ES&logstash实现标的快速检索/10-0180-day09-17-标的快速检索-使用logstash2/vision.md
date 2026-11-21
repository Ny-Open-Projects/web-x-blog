# 画面线理解：day09-17-标的快速检索-使用logstash2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-12 使用ES&logstash实现标的快速检索
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-12 使用ES&logstash实现标的快速检索\day09-17-标的快速检索-使用logstash2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:18, 00:33, 01:45, 02:01, 02:56, 03:55, 04:41, 07:36, 08:09, 09:00, 09:34, 12:13, 12:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:13:20

1) 这一组画面整体在讲什么（一句话）：
演示如何配置 Logstash 从 MySQL 数据库定时抽取数据并写入 Elasticsearch，包括配置文件结构、SQL 查询语句和测试方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Logstash 配置文件中 `output` 部分的 Elasticsearch 输出配置。
- 代码内容：
  ```
  output {
    elasticsearch {
      hosts => "localhost:9200"
      index => "wanxingzp_project"
      document_id => "%{id}"
      template => "C:/users/apple/desktop/logstash-7.3.1/config/wanxingzp_project_template.json"
      template_name => "wanxingzp_project"
      template_overwrite => true
    }
  }
  ```

画面 2：
- 展示了 Logstash 配置文件中 `input` 部分的 JDBC 输入配置。
- 代码内容：
  ```
  input {
    jdbc {
      jdbc_connection_string => "jdbc:mysql://localhost:3306/pzp_transaction_07"
      useincode=true&characterEncoding=utf-8&useSSL=false
      jdbc_user => "root"
      jdbc_password => "123"
      jdbc_driver_library => "e:/mysql-connector-java-8.0.11.jar"
      jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
      jdbc_paging_enabled => true
      jdbc_page_size => "50000"
      jdbc_default_timezone => "Asia/Shanghai"
      statement_filepath => "e:/wanxingzp-project_0.sql"
      schedule => "*/10 ***"
      record_last_run => true
      last_run_metadata_path => "./logstash_metadata"
    }
  }
  ```

画面 3：
- 展示了 Logstash 配置文件中 `input` 部分的 JDBC 输入配置，与画面 2 内容相同。

画面 4：
- 展示了 Logstash 配置文件中 `input` 部分的 JDBC 输入配置，与画面 2 内容相同。

画面 5：
- 展示了 Logstash 配置文件中 `output` 部分的 Elasticsearch 输出配置，与画面 1 内容相同。

画面 6：
- 展示了 Logstash 配置文件中 `output` 部分的 Elasticsearch 输出配置，与画面 1 内容相同。

画面 7：
- 展示了用于从 MySQL 数据库抽取数据的 SQL 查询语句。
- SQL 语句：
  ```sql
  SELECT
    ID AS id,
    CONSUMER_ID AS consumerId,
    USER_ID AS userId,
    PROJECT_NO AS projectNo,
    NAME AS name,
    DESCRIPTION AS description,
    TYPE AS type,
    PERIOD AS period,
    ANNUAL_RATE AS annualRate,
    BORROWER_ANNUAL_RATE AS borrowAnnualRate,
    COMMISSION_ANNUAL_RATE AS commissionAnnualRate,
    REFUNDMENT_MONEY AS repaymentMoney,
    AMOUNT AS amount,
    PROJECT_STATUS AS projectStatus,
    CREATE_DATE AS createDate,
    MODIFY_DATE AS modifyDate,
    STATUS AS status,
    IS_ASSIGNMENT AS isAssignment
  FROM
    project_0
  WHERE
    MODIFY_DATE >= :sql_last_value
  ```

画面 8：
- 展示了在 Notepad++ 中编辑 SQL 语句，并弹出一个记事本窗口，其中包含关于 Logstash 执行 SQL 查询的说明。
- 记事本内容：
  ```
  把查询到的数据输出到ES中
  如果sql查询语句不带条件，可以吗？不行，如何转换为增量采集？
  sql查询语句一定要带条件，但不希望查询的数据被排除掉
  举例：
  假设logstash上次执行的时间是：10:10，会被记录到logstash metadata文件中
  假设现在10:15修改了表中的ID列
  ```

画面 9：
- 展示了 Logstash 配置文件中 `output` 部分的 Elasticsearch 输出配置，与画面 1 内容相同。

画面 10：
- 展示了在 DBeaver 数据库管理工具中查看 MySQL 数据库 `pzp_transaction_0` 数据库中的 `project_0` 表数据。

画面 11：
- 展示了在 Notepad++ 中编辑 SQL 语句，并弹出一个记事本窗口，其中包含关于 Logstash 执行 SQL 查询的说明。
- 记事本内容：
  ```
  把查询到的数据输出到ES中
  如果sql查询语句不带条件，可以吗？不行，如何转换为增量采集？
  sql查询语句一定要带条件，但不希望查询的数据被排除掉
  举例：
  假设logstash上次执行的时间是：10:10，会被记录到logstash metadata文件中
  假设现在10:15修改了表中的ID列
  ```

画面 12：
- 展示了在 DBeaver 数据库管理工具中查看 MySQL 数据库 `pzp_transaction_0` 数据库中的 `project_0` 表数据。
- 同时，弹出一个记事本窗口，其中包含关于 Logstash 执行 SQL 查询的说明。
- 记事本内容：
  ```
  把查询到的数据输出到ES中
  如果sql查询语句不带条件，可以吗？不行，如何转换为增量采集？
  sql查询语句一定要带条件，但不希望查询的数据被排除掉
  举例：
  假设logstash上次执行的时间是：10:10，会被记录到logstash metadata文件中
  假设现在10:15修改了表中的ID列
  ```

画面 13：
- 展示了 Logstash 配置文件中 `output` 部分的 Elasticsearch 输出配置，与画面 1 内容相同。

画面 14：
- 展示了 Logstash 配置文件中 `output` 部分的 Elasticsearch 输出配置，与画面 1 内容相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上文第 2 点中完整列出）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（无 PPT 标题、架构图或表格数据）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
