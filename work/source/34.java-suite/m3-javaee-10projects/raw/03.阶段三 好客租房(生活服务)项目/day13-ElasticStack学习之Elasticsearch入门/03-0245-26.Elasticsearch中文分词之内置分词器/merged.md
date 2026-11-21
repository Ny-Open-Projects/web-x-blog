# 26.Elasticsearch中文分词之内置分词器

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\26.Elasticsearch中文分词之内置分词器【海量资源尽在 ubkz.com】.mp4
- 时长 4分6秒（音频 246s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下ES中的内置的分词器那么它呢提供了有这么几种啊那么我们一个一个来过一下那么首先第一个呢是它的标准分词器它是按照什么的单词做一个切分并且呢会将我们的这个单词会转成一个小写那么这个地方是不是输了一段话对吧那么我们来测试一下那么我们把它打开然后呢把这个拿掉直接就underline就可以了
[00:30] 然后呢做一个发送OK好那么可以看到那么在这个里面呢我们是不是第一个字母是一个大写那么分词的结果是不是已经变成了小写他按照每一个单词去做了这样的一个分词因为比较简单啊标准的分词就是按照我们那个单词去做一个这个分词就可以了这是第一种标准分词那么第二种呢是simple啊这种分词这种分词什么意思呢是是按照
[00:57] 什么呢按照非单词做一个切分并且做一个小写的一个处理那么这个是什么意思呢把它拷贝过来那我们来看一下按照非单词去做一个这个切分然后呢走那么我们可以看到在这个里面呢首先这个衣服已经被是不是做了一个做了一个小写的一个转化然后呢这个是document然后呢这个也注意啊这个地方是不是有一个这个
[01:25] Pierre这个T那么他呢是不是也是按照需要按照这个非单词做一个区分那么这个他不是这个符号啊他不是一个单词对吧所以呢按照他也会做一个分词把这个T后面这个T呢也分割出来了那么前面的我们的一个标准分词呢就会把它认为这是一个词啊这是一个词他们是他们的一个区别那么其他就一样了哎OK这个呢是一个simple的这样的一个分词
[01:53] 然后呢下面还有一个呢这个呢是按照我们的空格去做一个分词那我们再来做一个测试然后把它拷贝过来然后呢发送走那么按照空格去区分注意它并不做大小写的一个转换那么第一个是不是依然还是大写啊那么这个就更为简单了就是按照空格去做一个分词就可以了哎OK那么下面我们接着继续往下面看那么还有一个呢这个呢stop它是按照一个stop分词就是按照我们的一些
[02:24] 语句中的一些这个语气助词去做一些这个分词什么热呢恶呢啊这样的一些这个词做一个分词那么把这个我们也拷贝过来看一下效果就好了然后呢这是一个stop啊然后走那么我们可以看到第一个if和热就直接被去掉了那么这个就是把一些这个助词呢就拿掉了就不需要这样的词那么就认为它因为这个词它本身没有什么意义对吧那么所以说就保留这个document啊等等然后呢
[02:52] 还有我看后面啊后面就全部都保留下来了哎OK好嘞那么这个呢就是一个stop分词OK嗯还有一个呢是keyword分词这个分词就非常有意思了什么意思呢就是不做分词那么就是说你传入什么啊传入什么那就是什么不做分词啊这个其实我们一般啊很少去使用啊你看分词的结果就是你说的这个单话不做分词哎OK
[03:19] 好嘞那么这个就是一个它内置的几种分词其实我们往往我们在我们就是我们去做项目的时候因为我们做的很多是就是我们国内的项目对吧那么我们在做国内项目的时候很少会用到它的一些内置的一些分词为什么呢就前面我们所演示的那个效果对吧比如说听音乐那么他也会把这个音乐这两个这个词也会拆开实际上是不应该拆开的对吧那么所以呢
[03:47] 以上的一些内置的分词对我们去在处理中文的时候显然是都不适用的都不适用的所以内置分词我们做一个基本的了解就可以了那么重点我们是不要来说下面的中文分词OK好那么关于内置分词我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

