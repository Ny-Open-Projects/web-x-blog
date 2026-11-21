# 画面线理解：26.Elasticsearch中文分词之内置分词器

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\26.Elasticsearch中文分词之内置分词器【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:24, 00:40, 00:51, 01:06, 01:49, 01:53, 02:03, 02:13, 02:16, 02:37, 02:57, 03:08, 03:19, 03:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:40:24

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Postman 发送 HTTP 请求测试 Elasticsearch 中不同分词器（analyzer）对文本的分词效果，并通过 PDF 讲义对照说明。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Postman 中设置请求体，使用 "standard" 分词器分析文本 "A man becomes learned by asking questions."，并显示返回的 tokens 结构。
画面 2: 在 Postman 中切换到 "Preview" 标签页，查看 JSON 格式的分词结果。
画面 3: 展示 PDF 讲义第 34 页，内容为 "4.3.1. Standard" 小节，说明 Standard 分词器按单词切分并转为小写。
画面 4: 在 Postman 中切换到 "Test Results" 标签页，查看分词结果。
画面 5: 在 Postman 中切换到 "Preview" 标签页，查看分词结果。
画面 6: 展示 PDF 讲义第 35 页，内容为 "4.3.4. Stop" 小节，说明 Stop 分词器会去除停用词。
画面 7: 在 Postman 中设置请求体，使用 "whitespace" 分词器分析文本 "If the document doesn't already exist"。
画面 8: 在 Postman 中切换到 "Test Results" 标签页，查看分词结果。
画面 9: 展示 PDF 讲义第 36 页，内容为 "4.3.4. Stop" 小节，展示分词结果。
画面 10: 在 Postman 中设置请求体，使用 "stop" 分词器分析文本 "If the document doesn't already exist"。
画面 11: 展示 PDF 讲义第 37 页，内容为 "4.3.5. Keyword" 小节，说明 Keyword 分词器不进行分词处理。
画面 12: 在 Postman 中切换到 "Test Results" 标签页，查看分词结果。
画面 13: 展示 PDF 讲义第 38 页，内容为 "4.3.5. Keyword" 小节，展示分词结果。
画面 14: 展示 PDF 讲义第 34 页，内容为 "4.3.1. Standard" 小节，展示分词结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```json
{
  "analyzer": "standard",
  "text": "A man becomes learned by asking questions."
}
```
画面 2:
```json
{
  "tokens": [
    {
      "token": "a",
      "start_offset": 0,
      "end_offset": 1,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "man",
      "start_offset": 2,
      "end_offset": 5,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "becomes",
      "start_offset": 6,
      "end_offset": 12,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "learned",
      "start_offset": 13,
      "end_offset": 19,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "by",
      "start_offset": 20,
      "end_offset": 22,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "asking",
      "start_offset": 23,
      "end_offset": 30,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "questions",
      "start_offset": 31,
      "end_offset": 40,
      "type": "<ALPHANUM>",
      "position": 6
    }
  ]
}
```
画面 3:
```json
{
  "tokens": [
    {
      "token": "a",
      "start_offset": 0,
      "end_offset": 1,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "man",
      "start_offset": 2,
      "end_offset": 5,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "becomes",
      "start_offset": 6,
      "end_offset": 12,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "learned",
      "start_offset": 13,
      "end_offset": 19,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "by",
      "start_offset": 20,
      "end_offset": 22,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "asking",
      "start_offset": 23,
      "end_offset": 30,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "questions",
      "start_offset": 31,
      "end_offset": 40,
      "type": "<ALPHANUM>",
      "position": 6
    }
  ]
}
```
画面 4:
```json
{
  "tokens": [
    {
      "token": "a",
      "start_offset": 0,
      "end_offset": 1,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "man",
      "start_offset": 2,
      "end_offset": 5,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "becomes",
      "start_offset": 6,
      "end_offset": 12,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "learned",
      "start_offset": 13,
      "end_offset": 19,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "by",
      "start_offset": 20,
      "end_offset": 22,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "asking",
      "start_offset": 23,
      "end_offset": 30,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "questions",
      "start_offset": 31,
      "end_offset": 40,
      "type": "<ALPHANUM>",
      "position": 6
    }
  ]
}
```
画面 5:
```json
{
  "tokens": [
    {
      "token": "a",
      "start_offset": 0,
      "end_offset": 1,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "man",
      "start_offset": 2,
      "end_offset": 5,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "becomes",
      "start_offset": 6,
      "end_offset": 12,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "learned",
      "start_offset": 13,
      "end_offset": 19,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "by",
      "start_offset": 20,
      "end_offset": 22,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "asking",
      "start_offset": 23,
      "end_offset": 30,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "questions",
      "start_offset": 31,
      "end_offset": 40,
      "type": "<ALPHANUM>",
      "position": 6
    }
  ]
}
```
画面 6:
```json
{
  "tokens": [
    {
      "token": "already",
      "start_offset": 24,
      "end_offset": 31,
      "type": "word",
      "position": 5
    }
  ]
}
```
画面 7:
```json
{
  "analyzer": "whitespace
