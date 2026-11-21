# 画面线理解：day09-14-标的信息检索-ES环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-12 使用ES&logstash实现标的快速检索
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-12 使用ES&logstash实现标的快速检索\day09-14-标的信息检索-ES环境搭建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:36, 02:16, 02:55, 03:19, 03:44, 03:57, 04:27, 05:07, 05:26, 06:00, 06:20, 07:11, 07:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:11:03

1) 这一组画面整体在讲什么（一句话）：
演示如何在本地环境搭建并配置Elasticsearch，使用head插件和Postman创建索引及映射。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示系统架构图，说明项目采用ElasticSearch+Logstash技术实现，交互流程包括前端APP→交易中心→内容检索服务→ES集群。
画面2：展示PPT内容，标题为“4.3.3 搭建ES环境”，子标题“4.3.1 安装和配置”，并展示elasticsearch.yml配置文件内容。
画面3：与画面2内容相同，仅鼠标位置不同。
画面4：展示Elasticsearch安装目录下的bin文件夹，包含多个启动脚本。
画面5：在命令行中执行elasticsearch.bat启动服务，显示启动日志。
画面6：继续展示命令行中Elasticsearch启动日志，显示节点已加入集群。
画面7：展示elasticsearch-head文件夹内容，包含项目相关文件。
画面8：在浏览器中打开Elasticsearch-head界面，地址为http://localhost:9100。
画面9：在Elasticsearch-head界面中，点击“创建索引”按钮，准备创建名为“wanxingp2p_project”的索引。
画面10：展示PPT内容，标题为“4.3.2 创建索引和映射”，说明可通过head插件或Postman创建索引。
画面11：展示创建索引映射的JSON配置内容，包含“investment”、“amount”、“period”等字段。
画面12：在Postman中发送POST请求，创建索引映射，请求地址为http://localhost:9200/wanxingp2p_project/mapping。
画面13：在Elasticsearch-head界面中，显示已创建的索引“wanxingp2p_project”，状态为绿色（3 of 3），并显示索引大小。
画面14：与画面10内容相同，展示PPT中关于创建索引和映射的说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2、3、14：
cluster.name: wanxingp2p
node.name: wanxingp2p_node
network.host: 0.0.0.0
http.port: 9200
transport.tcp.port: 9300
discovery.zen.minimum_master_nodes: 1
bootstrap.memory_lock: true
discovery.type: single-node
http.cors.enabled: true
http.cors.allow-origin: "*"
path.data: C:\Users\apple\Desktop\elasticsearch-7.3.1\data
path.logs: C:\Users\apple\Desktop\elasticsearch-7.3.1\logs

画面11：
{
  "properties": {
    "isassignment": {
      "type": "keyword"
    },
    "amount": {
      "type": "double"
    },
    "period": {
      "type": "integer"
    },
    "paymentway": {
      "type": "keyword"
    },
    "borrowerannualrate": {
      "type": "double"
    },
    "projectstatus": {
      "type": "keyword"
    },
    "projectno": {
      "type": "keyword"
    },
    "commissionannualrate": {
      "type": "keyword"
    },
    "name": {
      "analyzer": "ik_max_word",
      "type": "text"
    },
    "id": {
      "type": "keyword"
    }
  }
}

画面12：
{
  "properties": {
    "investment": {
      "type": "keyword"
    },
    "amount": {
      "type": "double"
    },
    "period": {
      "type": "integer"
    },
    "paymentway": {
      "type": "keyword"
    },
    "borrowerannualrate": {
      "type": "double"
    },
    "projectstatus": {
      "type": "keyword"
    },
    "projectno": {
      "type": "keyword"
    },
    "commissionannualrate": {
      "type": "keyword"
    },
    "name": {
      "analyzer": "ik_max_word",
      "type": "text"
    },
    "id": {
      "type": "keyword"
    }
  }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图，从左到右依次为“前端请求APP”→“交易中心”→“内容检索服务”→“ES集群”，并标注了交互流程步骤。
画面2、3、14：PPT标题“4.3.3 搭建ES环境”，子标题“4.3.1 安装和配置”，并包含elasticsearch.yml配置文件内容。
画面10：PPT标题“4.3.2 创建索引和映射”，内容说明可通过head插件或Postman创建索引。
画面13：Elasticsearch-head界面显示索引“wanxingp2p_project”，状态为绿色（3 of 3），并显示索引大小。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
