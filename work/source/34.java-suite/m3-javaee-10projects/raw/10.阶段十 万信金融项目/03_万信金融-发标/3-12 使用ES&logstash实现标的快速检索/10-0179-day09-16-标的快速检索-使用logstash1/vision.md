# 画面线理解：day09-16-标的快速检索-使用logstash1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-12 使用ES&logstash实现标的快速检索
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-12 使用ES&logstash实现标的快速检索\day09-16-标的快速检索-使用logstash1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 02:56, 03:37, 04:21, 05:05, 06:38, 06:58, 07:44, 09:51, 11:56, 12:44, 14:17, 14:31, 15:17, 15:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:12:37

1) 这一组画面整体在讲如何使用 Logstash 从 MySQL 数据库同步数据到 Elasticsearch，并配置相应的模板文件和连接配置。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了课程文档中“4.4.2 使用Logstash”章节，图示说明 Logstash 从 MySQL 数据库读取数据并写入 ES 索引库，需要两个配置文件：mysql-es.conf 和模板文件。
画面 2: 展示了“4.4.2.1 创建模板文件”部分，显示了模板文件内容，包含字段 "isAssignment"、"amount"、"period" 的类型定义。
画面 3: 展示了“4.4.2.1 创建模板文件”部分，显示了模板文件内容，包含字段 "repaymentway"、"consumerId"、"userName"、"description"、"annualRate" 的类型定义。
画面 4: 展示了“4.4.2.2 配置mysql-es.conf”部分，说明需要执行 SQL 语句在目标表中增加字段，并提到在 Logstash 的 config 目录下创建 mysql-es.conf 配置文件。
画面 5: 展示了 mysql-es.conf 配置文件的 input 部分，包含 jdbc 连接字符串、用户名、密码、驱动库、分页设置、时区等配置。
画面 6: 展示了 mysql-es.conf 配置文件的 output 部分，配置了 Elasticsearch 的 hosts、index、template 等信息。
画面 7: 展示了 mysql-es.conf 配置文件的 input 部分，与画面 5 内容相同。
画面 8: 展示了 mysql-es.conf 配置文件的 input 部分，与画面 5 内容相同。
画面 9: 展示了 IntelliJ IDEA 中的项目结构，项目名为 "wanxing2p_apollo"。
画面 10: 展示了 MySQL Workbench 中的 "p2p_transaction_0" 表数据，包含字段如 PERIOD、ANNUAL_RATE、BORROWER_ANNUAL_RATE、REPAYMENT_WAY、AMOUNT、PROJECT_STATUS、CREATE_DATE、IS_ASSIGNMENT。
画面 11: 展示了 mysql-es.conf 配置文件的 input 部分，与画面 5 内容相同。
画面 12: 展示了 MySQL Workbench 中的 "p2p_transaction_1" 表数据，包含字段如 BORROWER_ANNUAL_RATE、COMMISSION_ANNUAL_RATE、REPAYMENT_WAY、AMOUNT、PROJECT_STATUS、CREATE_DATE、IS_ASSIGNMENT。
画面 13: 展示了 mysql-es.conf 配置文件的 output 部分，配置了 Elasticsearch 的 hosts、index、template 等信息。
画面 14: 展示了 mysql-es.conf 配置文件的 input 部分，与画面 5 内容相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
```
4.4.2 使用Logstash
Logstash的工作是从MySQL中读取数据，然后向ES中写入数据从而创建索引。因此它需要知道数据库相关的表和ES相关的配置文件：
1.mysql-es.conf：配置从哪个数据库和表读取数据，配置把读取到的数据写入到哪个ES索引库中
2.模板文件：索引库的映射配置
```

画面 2:
```
4.4.2.1 创建模板文件
在logstash的config目录中创建wanxing2p_project_template.json作为模板文件，配置索引库映射，内容如下：
{
  "mappings":{
    "properties":{
      "isAssignment":{
        "type":"keyword"
      },
      "amount":{
        "type":"double"
      },
      "period":{
        "type":"integer"
      }
    }
  }
}
```

画面 3:
```
4.4.2.1 创建模板文件
在logstash的config目录中创建wanxing2p_project_template.json作为模板文件，配置索引库映射，内容如下：
{
  "mappings":{
    "properties":{
      "isAssignment":{
        "type":"keyword"
      },
      "amount":{
        "type":"double"
      },
      "period":{
        "type":"integer"
      }
    }
  }
}
```

画面 4:
```
4.4.2.2 配置mysql-es.conf
1. 我们需要执行如下SQL语句，在目标的表中增加一个字段：
ALTER TABLE p2p_transaction_0.`project_0` ADD COLUMN MODIFY_DATE datetime(0)
NULL DEFAULT NULL COMMENT '修改时间' AFTER CREATE_DATE;
ALTER TABLE p2p_transaction_0.`project_1` ADD COLUMN MODIFY_DATE datetime(0)
NULL DEFAULT NULL COMMENT '修改时间' AFTER CREATE_DATE;
ALTER TABLE p2p_transaction_1.`project_0` ADD COLUMN MODIFY_DATE datetime(0)
NULL DEFAULT NULL COMMENT '修改时间' AFTER CREATE_DATE;
ALTER TABLE p2p_transaction_1.`project_1` ADD COLUMN MODIFY_DATE datetime(0)
NULL DEFAULT NULL COMMENT '修改时间' AFTER CREATE_DATE;
2. 在Logstash的config目录下创建mysql-es.conf配置文件，Logstash会根据该配置文件从MySQL中读取数据并同步到ES中。
```

画面 5:
```
input {
  jdbc {
    jdbc_connection_string => "jdbc:mysql://localhost:3306/p2p_transaction_0?"
    useUnicode=true&characterEncoding=utf-8&useSSL=false
    jdbc_user => "root"
    jdbc_password => "123"
    jdbc_driver_library => "e:/mysql-connector-java-8.0.11.jar"
    jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
    jdbc_paging_enabled => true
    jdbc_page_size => "50000"
    jdbc_default_timezone => "Asia/Shanghai"
    #要执行的sql
    statement_filepath => "e:/wanxing2p-project_0.sql"
    #每隔10秒执行一次
    schedule => "*/10 * * * *"
    #是否记录最后一次的运行时间
    record_last_run => true
    #记录最后一次运行时间的位置
    last_run_metadata_path => "./logstash_metadata"
  }
}
```

画面 6:
```
output {
  elasticsearch {
    #es服务地址
    hosts => "localhost:9200"
    #索引库名称
    index => "wanxing2p-project"
    #关联表主键作为文档ID
    document_id => "%{id}"
    #模板文件地址
    template => "C:/Users/apple/Desktop/logstash-7.3.1/config/wanxing2p_project_template.json"
    #模板文件名
    template_name => "wanxing2p_project"
    #覆盖模板
    template_overwrite => true
  }
}
```

画面 7:
```
input {
  jdbc {
    jdbc_connection_string => "jdbc:mysql://localhost:3306/p2p_transaction_0?"
    useUnicode=true&characterEncoding=utf-8&useSSL=false
    jdbc_user => "root"
    jdbc_password => "123"
    jdbc_driver_library => "e:/mysql-connector-java-8.0.11.jar"
    jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
    jdbc_paging_enabled => true
    jdbc_page_size => "50000"
    jdbc_default_timezone => "Asia/Shanghai"
    #要执行的sql
    statement_filepath => "e:/wanxing2p-project_0.sql"
    #每隔10秒执行一次
    schedule => "*/10 * * * *"
    #是否记录最后一次的运行时间
    record_last_run => true
    #记录最后一次运行时间的位置
    last_run_metadata_path => "./logstash_metadata"
  }
}
```

画面 8:
```
input {
  jdbc {
    jdbc_connection_string => "jdbc:mysql://localhost:3306/p2p_transaction_0?"
    useUnicode=true&characterEncoding=utf-8&useSSL=false
    jdbc_user => "root"
    jdbc_password => "123"
    jdbc_driver_library => "e:/mysql-connector-java-8.0.11.jar"
    jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
    jdbc_paging_enabled => true
    jdbc_page_size => "50000"
    jdbc_default_timezone => "Asia/Shanghai"
    #要执行的sql
    statement_filepath => "e:/wanxing2p-project_0.sql"
    #每隔10秒执行一次
    schedule => "*/10 * * * *"
    #是否记录最后一次的运行时间
    record_last_run => true
    #记录最后一次运行时间的位置
    last_run_metadata_path => "./logstash_metadata"
  }
}
```

画面 9:
```
Project: wanxing2p_apollo
├── idea
├── logs
├── wanxing2p-account-service
├── wanxing2p-apl
├── wanxing2p-common
├── wanxing2p-consumer-service
├── wanxing2p-depository-agent-service
├── wanxing2p-discover-server
├── wanxing2p-g
