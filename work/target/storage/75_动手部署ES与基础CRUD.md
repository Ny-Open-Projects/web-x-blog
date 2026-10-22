# 75. 六大数据库存储实战: 动手部署 Elasticsearch 与基础索引 CRUD

## 纲要

- 用 Docker 拉起 ES 7.1.0 单节点：`discovery.type=single-node` 绕开默认的集群三节点要求
- 映射双端口：9200 为 HTTP / 监控端口，9300 为 Java 客户端（Transport）端口
- 开启跨域配置（HTTP CORS），否则本地页面与 Java 客户端跨域访问被拒
- 安装 IK 中文分词器并置于 plugins 目录，注意 `chmod` 赋予读取执行权限
- 用 `analyze` API 验证 IK 分词效果
- 基础语法：建索引（settings 指定分片/副本 + mappings 指定字段类型与 analyzer）、插入文档、match 搜索

## 📎 代码说明

本讲代码以**内联片段**形式呈现在正文中。课程课件仅发布第 2/3/4 章（MySQL 核心能力）的完整工程源码，本讲所属章节未随课件发布独立源码文件，故不做外部文件关联，请以正文片段为准。

## Docker 部署单节点 ES

课程使用 ES 7.1.0。默认情况下 ES 以集群方式启动、要求至少三个节点，学习阶段我们只用单节点接入，因此用 `discovery.type=single-node` 关闭集群约束。

```bash
# 拉取镜像（首次较慢）
docker pull elasticsearch:7.1.0

# 以单节点方式启动
docker run -d --name elasticsearch \
  -e discovery.type=single-node \
  -p 9200:9200 \
  -p 9300:9300 \
  elasticsearch:7.1.0
```

- `9200`：HTTP 层，浏览器、Postman、插件都走这个端口做查询与监控
- `9300`：Java 客户端（Transport 层）连接端口

启动后用浏览器访问 `http://localhost:9200`，能看到 `cluster_name`、`node.name`、`cluster_uuid` 和版本信息，即代表部署成功。

## 安装 IK 中文分词器

ES 容器基于极简 Linux 镜像（类似 CentOS），默认连 `vim` 都没有，改配置通常用 `docker cp` 把配置文件拷出、改完再拷回。进入容器：

```bash
docker exec -it elasticsearch bash
# 默认工作目录：/usr/share/elasticsearch
# 配置目录：/usr/share/elasticsearch/config
```

### 开启跨域

编辑 `config/elasticsearch.yml`，新增两行：

```yaml
http.cors.enabled: true
http.cors.allow-origin: "*"
```

本地页面（localhost:9200）访问 ES 的 HTTP 服务端，而请求方是 Java 程序，属于跨域；不配置这两行，跨域请求会被拒绝。保存后**重启容器**生效。

### 部署 IK 插件

IK 分词器下载较慢，讲师已提前下载好对应 7.1.0 的版本并拷贝进容器：

```bash
# 进入容器后，把 IK 分词器拷贝到 plugins 目录并改名
docker cp <本地下载的 IK 目录> elasticsearch:/usr/share/elasticsearch/plugins/ik

# 关键：必须 chmod 赋予读取与执行权限，否则 ES 进程读不到插件而启动失败
chmod -R 755 /usr/share/elasticsearch/plugins/ik
```

IK 目录内部是一些 jar 包，其 `config` 下有多个 `.dic` 字典文件：

- `main.dic`：主扩展词库，可在里面追加行业专有中文词（如"龙岩大悦城"即可被正确切出）
- `stopword.dic`：停用词库，收录"的、了、在"等常见中文停用词

改完字典后重启生效。

### 用 analyze API 验证分词

重启后用 Postman 发 POST 请求到 `http://localhost:9200/_analyze`，验证 IK 是否生效：

```json
{
  "analyzer": "ik_smart",
  "text": "中华人民共和国国歌"
}
```

返回按 IK 智能切分：`中华人民共和国`、`国歌`。再试 `ik_max_word` 会切得更细（连"国"字都会拆出），与前面章节讲的"索引时用 `ik_max_word`、搜索时用 `ik_smart`"方案一致。

## 基础索引与文档 CRUD

### 建索引（库）并指定结构

传统数据库先建库，ES 先建索引（index）。建索引时通过 `settings` 指定分片与副本数，通过 `mappings` 定义字段（相当于表结构）：

```bash
curl -X PUT "http://localhost:9200/test" -H 'Content-Type: application/json' -d '{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "id":   { "type": "long" },
      "name": {
        "type": "text",
        "analyzer": "ik_max_word",
        "search_analyzer": "ik_smart"
      }
    }
  }
}'
```

- `number_of_shards`：主分片数
- `number_of_replicas`：副本数
- `name` 字段 `type=text`，默认可被分词索引
- `analyzer`：建索引时使用的分析器（`ik_max_word` 切得细，召回全）
- `search_analyzer`：外部搜索时使用的分析器（`ik_smart` 切得粗，精度高）

### 插入文档

```bash
# _doc 是索引里默认的 type（类似库的默认表），指定 id=1
curl -X PUT "http://localhost:9200/test/_doc/1" -H 'Content-Type: application/json' -d '{
  "id": 1,
  "name": "iphoneXS"
}'
# 返回 "result": "created"
```

### 搜索文档

```bash
# match 搜索 name 字段包含 iphone 的文档
curl -X POST "http://localhost:9200/test/_search" -H 'Content-Type: application/json' -d '{
  "query": {
    "match": { "name": "iphone" }
  }
}'
```

返回里 `hits` 中的 `_score` 是经 TF-IDF 加归一化算法算出的排序分值。搜 `iphone` 能命中 `iphoneXS`；若把文档改成 `iphone1` 则无命中。

再插入一条 `情人节玫瑰花` 后用 `match` 搜 `情人`：

```bash
curl -X PUT "http://localhost:9200/test/_doc/2" -H 'Content-Type: application/json' -d '{
  "id": 2,
  "name": "情人节玫瑰花"
}'

curl -X POST "http://localhost:9200/test/_search" -H 'Content-Type: application/json' -d '{
  "query": { "match": { "name": "情人" } }
}'
```

用 `情人 玫瑰`（空格切词）搜索时，空格被忽略，两个词分别命中，评分从零点几分升到一分，仍能搜出。这些就是 ES 最基础的创建、插入与搜索语法。

## 技术点总结

- 学习阶段用 `discovery.type=single-node` 跑单节点，9200 走 HTTP、9300 走 Java 客户端
- 不做跨域配置，本地与 Java 客户端的访问会被拒绝
- IK 分词器放 `plugins` 后务必 `chmod`，否则进程读不到插件
- 建索引时在 `settings` 定分片/副本，在 `mappings` 定字段类型与索引/搜索分析器
- 索引用 `ik_max_word`、搜索用 `ik_smart` 是兼顾召回与精度的标准组合


