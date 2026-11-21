# 13.GraphQL入门之什么是GraphQL？

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\13.GraphQL入门之什么是GraphQL？【海量资源尽在 ubkz.com】.mp4
- 时长 8分46秒（音频 526s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么前面呢我们讲了一些我们这个关于房源的一些功能的实现啊包括像新增房源呢房源列表啊做了一些功能的实现那么我们呢对于这功能实现呢我们就先到这儿然后呢接下来呢我们继续去往后面去走那么下面呢我们要去做什么内容呢其实我们要去整合我们的一些前端的系统啊
[00:23] 那么我们现在其实意在做后段我们并没有去整合前端那么我们其实接下来要做的是我们前端系统但是呢在我们讲前端系统之前呢我们先要给大家去讲一个东西啊叫这个GraphQL那么它是什么东西啊它呢其实它和我们的rest4啊其实有点类似或者说有点相像或者说它们是
[00:47] 相同的一种这个相同作用的这样的一种技术其实都是做我们的这种接口的做这种接口的那么我们为什么去讲它呢其实现在目前的这个GraphQL它是一个
[01:01] 比较流行或者说它是有一个很好的一个流行趋势的这样的一门这个技术那么也希望呢我们在我们的前端的这个系统中能够去跟我们的后端的这种接口做这种交互的时候我们采用这个GraphQL的这种这种标准或者这种规范或者这种技术来做一个实现所以呢我们希望在这个位置呢去给大家把这个GraphQL呢去讲一下到底
[01:30] 他是怎么去玩怎么去用包括他的一些规范啊到底是什么需要希望呢把这个给大家讲明白呃他呢其实要比RESTful啊其实这个思想呢更先进啊但是呢他呢呃也比RESTful
[01:46] 要学习起来这个难度稍大一点并且呢需要你去很好的去理解他才能够理解他了解到他的一个作者这样的一个意图啊OK好那么废话就不多说了那么我们就去来首先我们先去看一下什么是GraphQL那么GraphQL呢他呢是Facebook啊这个公司其实呢大家呢在学习一些新技术的时候会发现
[02:15] 目前呢由Facebook去主导的去或者说去引领的一个技术的一个方向啊还是有挺多的啊还是有挺多的所以Facebook也是一个比较伟大的这样的一个公司啊那么尤其在这个技术这个领域啊也是非常棒的一个公司啊他呢去创造了这样的一个查询的语言叫做GypheQ
[02:38] 是用于描述复杂的一种数据模型的一种查询语言其实在这呢我们把它定义为是个查询语言其实也是在GraphQL它最初的一个这样的一个用途或者说它的一个这样的一个这样的一个想法吧去做这样的一个查询其实到后面它也支持一些这个修改数据啊或者说我们去变更数据啊但是呢我们可能用的更多的是它的一个查询哎OK
[03:07] 那么你可以看到后面是不是也说了并不是指常规意义上的一个类似于搜索语言的查询言而是用于前后端数据查询方式的一个规范那么下面的这个是他的官网这个是他的官网那么比较友好的是这个官网还做了一个中文版的这样的一个网站所以当我们去学习GrabQR的时候其实我们还是有一定优色的就是去可以读中文的文档这个也是他官方的一个文档
[03:37] 那么关于它的规范的地址呢是在这啊ok好那么接下来呢我们就来打开这个官方的这个网站我们来看一下来看一下那么要注意的是这个网站啊这个网站那么它有些时候啊可能会打不开就是有些人可能会被强调啊这个大家注意一下就好了这个它的一个网站啊其实做的还是比较炫酷的这样的一个网站那么这个是它的一个logo啊大家可以去
[04:03] 大概的去记一下以后见到这个logo就认识了那么他呢大概有这么几个内容啊就说你看通过我们去描述你的一个数据然后呢我们去请求你想要的一个数据就可以得到你这样的一个结果那么其实就是刚刚我们所说的就是什么呢就是我们前后端啊去数据查询这样的一个方式啊好
[04:29] okok那么下面可以看到那么有很多的一些内容大家可以看一下一种用于API查询的语言等等那么这个就不做太多的一个
[04:41] 讲解了对吧或者说我们去读这个内容大家可以自行去阅读一下那么像他下面呢提供了一些说了他的一些这个卖点对吧比较优秀的一些点就说请求的数据不多不少怎么怎么样啊然后呢这个后面我们一会详细再说啊我们简单简单带大家呢来看一下他的一些这个官方的一些这个描述啊然后呢像这个呢是不是就描述了一些这个获取多个资源只需要一个请求这个是什么意思那么后面我们也会提到
[05:10] 包括有这样的一些内容大家都可以去观去查看一下官网的一些信息包括说现在有谁在用GraphQL大了你可以看到排在第一的是不是Facebook对吧还有推特给他哈巴都在使用OK好那么其中不在我们国内有这样的一种流行的趋势那么逐渐的可能会去流行使用GraphQL可能会逐步的去取代Restful
[05:36] 打了rest4它也是一个比较优秀的这样的一个API的一个规范OK 打了后面我们也会讲到rest4它本身的也会存在一些问题那么这个里面有些内容包括像这种学习有比较完善的一个文档它都是中文版的还是比较友好的然后还有一个代码可以看到在这个里面有很多语言的一种实现很多语言的一种实现但是它并不是官方的一些实现
[06:05] 到这个到我们后面的时候我们再聊这个话题然后呢我们继续往下面看还有些什么社区啊还有他的一些这个我们把这个简单说一下吧这个社区社区呢你可以到这个stackofflow中去查看一些问题还有Facebook然后Twitter上面去查看那么他下面呢还有一些这个链接我觉得还是都是一些比较好的一些这个帮助我们去学习GolfQR的一些文章还有视频啊大家都可以去看一下啊
[06:34] 这个是博客是一些这个文章然后呢还有些这个视频啊视频的也是不错的包括像这个什么30分钟从零开始这GraphQL当然了他都是一些英文版的一些视频啊大家可能需要一些英文的一些基础去查看这样的一些视频都是一些也是非常优秀的啊哎OK好嘞这个是他的一些这个社区那么其实我们要说的一个点呢是他的一个规范啊这个呢我们重新刷新一下好来看一下
[07:02] 那么这样的话呢它呢是关于GraphQL呢去做了一个非常完善的这样的一个规范的一个说明这个里面有好多一些内容啊那么大家大概可以去看一下有很多一些内容那么通过这个目录其实就能够
[07:20] 发现看出他有很多的规范包括他的一些这个语言对吧然后呢他的一些什么查询的文档啊操作的文档啊等等还有一些这个类型对吧还有一些什么叫内审然后呢一些基本原则啊等等等等这个就不做一个太多的一个这个讲解了对吧有非常多的这种规范啊非常多的规范那么要注意的是那么我们现在
[07:48] 或者说我们接下来要给大家讲的内容呢其实都是更多的是偏向于理论那么更偏向于这个规范那么我们当我们把这规范我们搞清楚之后或者说我们已经了解清楚GrabQ它到底想做什么事情之后那么我们再去动手去实现或者说去使用它的规范的具体的实现去做一些我们的一些接口
[08:14] 做我们那些接口的调用是这样的一个学习的一个过程所以接下来我们要学的就是它这个规范这么多的一些内容当然了我们不可能说一个一个去做一个学习我们会挑一些比较重要的一些内容去做一些这样的一个讲解OK好那么关于第一个这个小的话题就是什么是GraphQL我们就讲到这里下面我们就来分析一下什么REST4的一些它所存在的一些问题OK
[08:42] 好那么关于GraphQL是什么我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
介绍 GraphQL 的基本概念、优势、使用场景及其社区资源。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 课程 PPT 标题为“6. GraphQL入门”，子标题“6.1. 什么是GraphQL?”。
- 内容：GraphQL 是由 Facebook 创造的用于描述复杂数据模型的一种查询语言，不是常规 SQL，而是一种用于前后端数据查询方式的规范。
- 提供了官网地址：https://GraphQL.cn/ 和规范地址：http://spec.GraphQL.cn/。
- 展示了 GraphQL 的核心理念图：描述你的数据 → 请求你所要的数据 → 得到可预测的结果。

画面 2:
- 展示了 GraphQL 官网首页，核心理念图：描述你的数据 → 请求你所要的数据 → 得到可预测的结果。
- 网站标语：“一种用于 API 的查询语言”。
- 提供了“马上开始”和“了解更多”按钮。

画面 3:
- 展示了 GraphQL 的核心优势：提供一套易于理解的完整描述，客户端能准确获得所需数据，没有冗余，API 易于演进，便于构建强大开发者工具。
- 展示了 GraphQL 查询示例：
  ```GraphQL
  {
    hero {
      name
      height
    }
  }
  ```
  和对应的响应：
  ```json
  {
    "hero": {
      "name": "Luke Skywalker",
      "height": 1.72
    }
  }
  ```

画面 4:
- 标题：“获取多个资源 只用一个请求”。
- 内容：GraphQL 查询不仅能获取资源属性，还能沿着资源间引用进一步查询。与 REST API 需要多个 URL 请求不同，GraphQL 一次请求即可获取所有数据，即使在慢速网络下也能表现迅速。
- 展示了数据结构示意图：一个手机屏幕显示了多个角色数据（如 Luke Skywalker、Obi-Wan Kenobi 等）。

画面 5:
- 标题：“谁在使用 GraphQL?”。
- 内容：Facebook 的移动应用从 2012 年开始使用 GraphQL，GraphQL 规范于 2015 年开放，现已被多种环境下使用，并被各种体量的团队所使用。
- 展示了使用 GraphQL 的公司 Logo：Facebook、Twitter、GitHub、Pinterest、Airbnb、Intuit。

画面 6:
- 继续展示“谁在使用 GraphQL?”页面。
- 展示了更多公司 Logo：Coursera、Shopify。
- 底部有“更多 GraphQL 使用者”按钮。

画面 7:
- 标题：“GraphQL 入门”。
- 内容：介绍 GraphQL 是一种用于 API 的查询语言，基于类型系统运行，不绑定特定数据库或存储。
- 展示了 GraphQL 服务创建示例：
  ```GraphQL
  type Query {
    me: User
  }
  type User {
    id: ID
    name: String
  }
  ```
- 右侧导航栏列出了学习内容：入门、Schema 架构图、类型系统、语言、指令、变量、执行、响应等。

画面 8:
- 标题：“IRC”。
- 内容：在 freenode 服务器上的 #GraphQL 频道与 GraphQL 开发者聊天。
- 标题：“Slack & Discord #”。
- 内容：许多 GraphQL 开发者会在 Discord 和 Slack 聊天室中实时交流和快速解决问题。
- 提供了加入 Discord 的链接：在 ReactFlux Discord 上加入 #GraphQL。
- Slack 社区链接：
  - #general on GraphQL (在这里获得邀请！)
  - Apollo Slack
  - Reindex Slack

画面 9:
- 标题：“要探索其他有关 GraphQL 的社区开发的资源和内容，请查看以下网站：”。
- 列表：
  - How to GraphQL : GraphQL 的全线教程
  - Building Apollo
  - Learn GraphQL
  - awesome-GraphQL : 一个奇妙的社区，维护了库、资源等的合集。
  - GraphQL-apis : 公开 GraphQL API 的集合列表。
  - Graphcool Blog
  - Learn Apollo : Apollo GraphQL Client 的动手教程（适用于 React、ReactNative、Exponent、Angular、Vue 和 iOS）。
  - Learn Relay : 对 Relay 的全面介绍（包含视频教程）。
  - Scaphold Community : 一些帮助您将使用 GraphQL 的 app 发布到生产环境的资源。
  - GraphQL World : GraphQL 开发者和活动的全球社区。
  - GraphQL Talks : 找到并观看最好的 GraphQL 演讲。
  - Basically, Full-stack GraphQL : 使用简单英文的一个基于代码的介绍在客户端使用服务端使用 GraphQL。

画面 10:
- 标题：“spec.GraphQL.cn”。
- 内容：显示了 GraphQL 规范的版权声明和使用条款。
- 内容：THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
- 内容：Contents 部分显示了目录结构：
  - 1 Overview/概述
  - 2 Language/语言
    - 2.1 Source Text/源文本
      - 2.1.1 Unicode/统一码
      - 2.1.2 White Space/空白符
      - 2.1.3 Line Terminators/行终止符
      - 2.1.4 Comments/注释
    - 2.2 Query Document/查询文档
    - 2.3 Operations/操作
    - 2.4 Selection Sets/选择集合
    - 2.5 Fields/字段
    - 2.6 Arguments/参数
    - 2.7 Field Alias/字段别名
    - 2.8 Fragments/片段
    - 2.9 Input Value/输入值
      - 2.9.1 Int Value/整数值
      - 2.9.2 Float Value/浮点值
      - 2.9.3 Boolean Value/布尔值
      - 2.9.4 String Value/字符串值
      - 2.9.5 Null Value/空值
      - 2.9.6 Enum Value/枚举值
      - 2.9.7 List Value/列表值
      - 2.9.8 Input Object Values/输入对象值
    - 2.10 Variables/变量
    - 2.11 Input Types/输入类型
    - 2.12 Directives/指令
    - 3 Type System/类型系统
      - 3.1.1 Scalars/标量
        - 3.1.1.1 Int/整数型
        - 3.1.1.2 Float/浮点型
        - 3.1.1.3 String/字符串型
        - 3.1.1.4 Boolean/布尔型
        - 3.1.1.5 ID/标识符型
        - 3.1.1.6 Enum/枚举型
        - 3.1.1.7 List/列表型
        - 3.1.1.8 Non-Null/非空型
      - 3.1.2 Type System/类型系统
        - 3.1.2.1 Object/对象型
        - 3.1.2.2 Interface/接口型
        - 3.1.2.3 Union/联合型
        - 3.1.2.4 Scalar/标量型
        - 3.1.2.5 Enum/枚举型
        - 3.1.2.6 Input Object/输入对象型
        - 3.1.2.7 List/列表型
        - 3.1.2.8 Non-Null/非空型
      - 3.1.3 Type System/类型系统
        - 3.1.3.1 Object/对象型
        - 3.1.3.2 Interface/接口型
        - 3.1.3.3 Union/联合型
        - 3.1.3.4 Scalar/标量型
        - 3.1.3.5 Enum/枚举型
        - 3.1.3.6 Input Object/输入对象型
        - 3.1.3.7 List/列表型
        - 3.1.3.8 Non-Null/非空型

画面 11:
- 标题：“spec.GraphQL.cn”。
- 内容：显示了 GraphQL 规范的目录结构。
- 内容：右侧导航栏

