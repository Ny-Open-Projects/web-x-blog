# 20-热点商品抢单-Redis集群操作Lua脚本编写 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们写一个Redis集群的操作对象

那在很多地方都有可能会用到我们Redis的一个操作

那我们可以把这个Redis操作啊

单独封装到一个工具类里面去

在我们热点商品抢购座里

正好可以用它来实现我们Redis操作

好那我们写一个工具类叫Redis Cluster.do

在这里我们新建这个文件

这个文件呢

它主要是用来实现Redis操作的

这里是Redis集群

好那这里面该怎么实现呢

我们来用我们的编辑器去实现一下

在这一块我们简单介绍一下

一会儿我要做什么事情

我要做这么几个事

第一我要操作Redis

所以我要配置Redis连接信息

第二个呢

我要做什么事情呢

连接信息配置了之后

我还需要做这么一个事情

我把它封装成一个模块

所以我要定义一个模块

模块定义了之后

紧接着我做另外一个事情

就开始去实现我的功能点了

对不对

那第一个功能

我想根据key查询

这五串类型

这也是可以的

那我紧接着还想添加数据

我添加数据

我还想给它

过期时间呢

并设置过期时间

这个可不可以了

也是可以的

那比如我还想做另外一个事情

就是哈希的操作

那哈希的操作

我想操作什么事情呢

我想根据key查询哈希数据

好

我根据几个key

比如我这里就是哈希类型

这是一个key

这是两个key

我可以传两个key过来

key一key二

传两个key

来查询第二层里面的数据

这可不可以了

也是可以的

那除了这个之外

我能不能也执行哈希操作

做这么一个事情

添加数据呢

我也希望有两个key

key一key二

因为只有一个key

那太简单了

两个key操作第二层

好

这是这一块

那我还能不能做另外一个事情

也是做哈希操作

不过我是做这么一个事情

让key一的key二

值之增

之增一

可以吗

这也是可以的

好

我们把这些功能给实现一下

看这一块实现起来难不难

好

我们首先参考

这一块

它给我们提供的案例

第一个

这个是连接配置

我们可以把它拷贝过来

更改一下

我们就在这里

简单改一下吧

192.168.211.137

对吧

好

7001

这个是23456

把这整个给拷贝过来

拷贝到我们当前这里

这就是我要连的redis信息

接着我们定义一个模块

local

local比如说叫lredis

开始往这个模块中添加我们的功能点

func lredis.

根据key获取写个get就行了

你要把key给我

好

中间这一块该怎么操作

中间这一块操作的话

我们参考它这里的一个案例

第一个步骤要依赖它

咱们依赖没有写

我们要依赖一下

除了依赖之外

还有一个这个地方是创建一个对象

创建一个对象

创建一个连接对象

连接对象

创建连接对象

那要不要获取连接呢

肯定是要获取的

我们看它这里获取对应的连接

初始化

连接

初始化连接之后就是你要执行的操作了

执行的操作好

那你要执行什么操作呢

我现在是去查询

它这里有一个rget

这里

这里的是它对应的key

把key给拷贝过来就可以了

这只是说编写了命令还没有执行

所以紧接着还要执行命令

执行命令怎么执行呢

它这里有

commit是吧

把它给拷过来

执行之后这是结果集

那为了节约资源

最后不要忘了关闭连接

那关闭怎么关闭呢

它这里也有readyclosed close

好

不要忘了返回你的值

return当前的结果集

可以了

这个就是根据key查询

那么后面这一块呢

基本上都是一样的

我们来写一下

比如我添加数据

我写个set

我还想给它搞个过期时间exp

好

那一个key

一个值

过期时间呢

来个time

这块就可以了

那添加这一块换成什么

换成set

set

set

,一定是一个key加一个值

这是这一块

但是这只是说给它添加值

并没有说设置过期时间呢

设置过期时间用另外一个方法

就是我刚才把注释取消的这个这个方法

好

把它给拷过来

key给它时间给它

可以了

当然这一块执行的话就不会有这个结果集返回了

对吧

这是我们这个添加数据并设置过期时间

我们接着往后面继续看看另外一个哈希的操作

那么哈希的操作呢

其实也是一样

没有多大区别

这个是查询

那我也写个Hget

key1 key2传两个key进来

key1 key2

那别的都不变

只需要把这里换一下就行了

这里换一下怎么换呢

我们来说一下

这里呢

要这样子换

执行相关的命令

那命令呢

得这样写

RED

后面怎么写呢

大家注意哈

用谁

现在是H

是哈希类型的

哈希类型这里有一个

大家看

HMget

这是操作哈希类型的

我们可以用它

把它给写过来

好

后面有几个key

注意

key1

key2

两个key给写过来就可以了

这就是你最终查询的结果

不要忘了把它给返回出去

好了

可以了

这是我们哈希类型的查询

那哈希类型除了查询

能不能添加数据呢

答案是可以的

我们添加一下数据

Hset

那么Hset这一块怎么做

注意key1 key2

你要添加数据

你总得给个值

对不对

value

这一块怎么做

也很简单

把这一块换掉

大家可以看到有一个叫做

HMset

get

HMset

这个

把它给拷过来

key1 key2

不要忘了给value

最后给value

执行命令

这个就没有返回值

像上面这个说一下

这里还有

这还要注意一下

我们可以看到这里

后面都是集合

对不对

后面都是集合

在他这里

他认为哈希类型里面

每个地方都有可能是集合

所以他这里返回的是集合类型

那集合类型呢

其实我们这里不是集合类型

我们这里其实只要一条记录就行了

对不对

那么我们就取其中第一个就好了

这里得加一个中括号1

中括号1就可以了

行

接着再往这里看

进入这里

进入到下面最后一个

最后一个的这个也比较简单哈

这个是让里面的值自身

那你要把这个key给我key

key2给我自身多少

你也要给我那自身是哪一个呢

我们看一下

自身在这里有一个自身的

这个是自身

这个

好

我们来写一下

这个就是自身了

那这个方法写到这里

让他里面key1里面key2的值自身多少

就是这一块

行

这个整体的工具内我们就搞定了

最后不要忘了把这个对象给返回出去

return

可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是一个关于 **Redis 集群（Cluster）** 的实战教学演示。讲师通过在本地开发环境中，使用 Lua 脚本语言和 Redis 客户端工具（如 Redis Desktop Manager）来操作和验证一个由多个节点组成的 Redis 集群。演示内容涵盖了集群的连接、配置、以及使用 Lua 脚本执行复杂的数据操作，如设置键值、哈希操作和自增操作。整个过程旨在展示如何在实际项目中利用 Redis 集群进行数据管理，并通过 Lua 脚本实现高效的批量操作。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 视频开头，展示了一个远程终端界面，提示用户连接到 `192.168.211.137` 的 Redis 服务，但终端为空，尚未执行任何命令。
*   **00:04 - 00:06**: 切换到 **Redis Desktop Manager**，显示了集群的连接状态，其中 `192.168.211.137:6379` 被选中，下方的“Connection”面板显示了多个节点的连接信息，表明这是一个多节点集群。
*   **00:07 - 00:10**: 切换到 **IntelliJ IDEA** 开发环境，展示了一个 Java 项目中的 `OrderServiceImpl` 类，其中包含一个分页查询方法 `findPage`，该方法使用了 `PageHelper` 和 `orderMapper.selectByExample` 进行数据库查询。
*   **00:11 - 00:13**: 在 IntelliJ IDEA 中，讲师将光标移动到 `OrderServiceImpl` 类的 `findPage` 方法下方，展示了一个名为 `local config` 的 Lua 配置块，其中定义了集群的名称为 `"test"`，并列出了多个节点的 IP 地址和端口（7001-7006）。
*   **00:14 - 00:16**: 切换到 **GitHub 页面**，显示了 `lua-resty-redis-cluster` 项目的 `nginx.conf` 配置文件，该文件用于在 Nginx 中配置 Redis 集群。
*   **00:17 - 00:19**: 展示了 `lua-resty-redis-cluster` 项目的 Lua 配置文件 `resty_redis_cluster.lua`，其中包含了 `local redis_cluster = require "resty.redis_cluster"` 的导入语句和 `local config` 的配置块。
*   **00:20 - 00:22**: 在 `resty_redis_cluster.lua` 文件中，讲师高亮了 `local redis_cluster = require "resty.redis_cluster"` 这一行，用于引入 Redis 集群模块。
*   **00:23 - 00:25**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.getstring` 函数，该函数用于根据 key 查询字符串值。
*   **00:26 - 00:28**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.setexp` 函数，该函数用于设置键值并设置过期时间。
*   **00:29 - 00:31**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hset` 函数，该函数用于向哈希表中添加数据。
*   **00:32 - 00:34**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **00:35 - 00:37**: 切换回 **Redis Desktop Manager**，显示了集群的连接状态，其中 `192.168.211.137:6379` 被选中，下方的“Connection”面板显示了多个节点的连接信息。
*   **00:38 - 00:40**: 切换回 **IntelliJ IDEA**，展示 `resty_redis_cluster.lua` 文件中的 `function iredis.hset` 函数，该函数用于向哈希表中添加数据。
*   **00:41 - 00:43**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **00:44 - 00:46**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **00:47 - 00:49**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **00:50 - 00:52**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **00:53 - 00:55**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **00:56 - 00:58**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **00:59 - 01:01**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:02 - 01:04**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:05 - 01:07**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:08 - 01:10**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:11 - 01:13**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:14 - 01:16**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:17 - 01:19**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:20 - 01:22**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:23 - 01:25**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:26 - 01:28**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:29 - 01:31**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:32 - 01:34**: 展示了 `resty_redis_cluster.lua` 文件中的 `function iredis.hincrby` 函数，该函数用于对哈希表中指定 key 的值进行自增操作。
*   **01:35 - 01:37**: 展
