# 11-13-mongoDB 索引管理

上节课介绍了索引的定义，并用示例展示了索引的作用，这节课简单学索引的管理，操作都非常简单。

首先是索引的创建。上节课发现用 name 查询（我们当时用 _id 查的，_id 自带索引）在数据量大时比较耗时，自然想到像 _id 一样，在 name 字段上创建索引。方法也很简单：await userCollection.createIndex()，接受一个 object，key 是你想建立索引的字段名称，这里写 name；值接受两个，和之前 sort 的含义一样：1 代表正序索引，-1 代表倒序索引。我们要正序，写 {name: 1}。运行后返回 name_1，说明建立成功了。

创建完看看集合里目前有哪些索引，也有对应方法：const indexResult = await userCollection.listIndexes()。看方法名就知道是把所有 index 列出来。特别注意 listIndexes 返回的是一个 index cursor，看到 cursor 指针对象就知道它不会直接返回数组，需要循环或者调用 toArray 转成数组再观测。打印出来后数组有两项，简单解读：key 表示在哪个属性上建立了索引，一条在 _id 上，我们新建的这条在 name 上；name 是索引的名称，默认是"字段名加上排序值"中间用杠连接；_id 这条因为它是内置索引，名称很特殊，是 _id_ 这样的形式；后面还有 namespace，代表在哪个 collection 上建立的索引，前面是数据库名 hello，后面是集合名 user，即 hello.user，告诉你索引的位置。

有了索引就可以实验查询效果，看建立索引后是否有提升。直接复用之前的查询：find({name: 'test50000'}) 加 explain，运行后结果和之前相比天翻地覆：之前 executionTimeMillis 是 21，现在直接变成 0；totalKeysExamined 之前是 0（没有任何索引），现在检查了索引并从中选取对应的值；totalDocsExamined 之前要顺序检查所有五万多个文档，现在直接变成 1。在索引的作用下时间大幅减少，说明索引很有用。

验证了结果，当然还可以删除索引，很简单。const dropResult = await userCollection.dropIndex('name_1')，dropIndex 可以 drop 单个，输入索引名称即可，也就是属性名加排序手法：name_1。打印 dropResult，输出 nIndexesWas，之前是两条，删除后应该剩一条。最后用 listIndexes().toArray() 验证一下：只剩一条以 _id 为索引的记录，删除成功。

到这里说了创建、查询、删除三个操作。特别注意我们现在是在 Node.js Driver 中操作，Mongo Shell 里也有一样的操作，而很多情况下索引操作经常在 shell 中进行而不是在代码中。简单看一下：进入 mongo 后 use hello，然后 db.user.createIndex()，和 driver 的 createIndex 一个意思；db.user.getIndexes() 注意是复数，对应 driver 里的 listIndexes，方法名不一样，返回的内容和之前完全一样；它还有个独特的方法 db.user.totalIndexSize()，返回当前索引占用的大小。可见 Node.js SDK 实现了大部分 shell 功能，但一些一般不会在编程语言里用的操作就没有实现，所以 shell 的功能比 Node.js driver 要多一些；最后 db.user.dropIndex() 和 Node.js 中一样。

最后说说索引的优缺点。缺点很简单：索引会增加写操作的代价，除了往集合写数据，还要另外在索引里写数据，可能略微增加写操作的开销。优点不用说，查询效率高，刚才的实验多次体现了：建立索引后查询时间大幅减少。

通过这两节课了解了 MongoDB 索引的简单用法。实际工作中，如果某个操作是在某一字段上查询、且耗时可能比较多，不妨用索引提高查询的响应速度。
