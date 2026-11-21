# 11-6-mongoDB 查询操作符

继续学 Node.js MongoDB Driver 的操作。上节课查询没有加任何条件，一股脑返回所有结果，这节课学怎么完成条件筛选。之前在 findOne 里已经可以传入条件筛选，但只会用固定对象，比如 name 等于 James，只能查这个固定值。现在介绍 MongoDB 内置的一系列查询条件，称为 query operators，操作符有固定格式，大体分四类：Comparison、Logic、Element、Evaluation。

先学第一类 Comparison 比较操作符，用来比较大小关系。特别注意 Mongo 内置操作符都以美元符号开头，看到 $ 符号就知道用了内置操作符筛选。操作符其实就是英文缩写：大于 $gt（greater than），小于 $lt，大于等于 $gte，小于等于 $lte，等于 $eq，不等于 $neq。格式上，查询条件本身是 object，固定值直接写，比如 age 等于 30；要用比较操作符，就在字段下再包一层 object，里面写操作符和值。

回到代码实验。查 age 大于 30 的数据：results 等于 await userCollection.find({age: {$gt: 30}})，然后 toArray 打印出来，运行后发现返回的条目年龄都大于 30。改成 $lt（less than）再测，出现的都是小于 30 的数据。比较操作符比较好理解，剩下 $eq、$neq 等自己尝试即可。

第二类逻辑操作符 logic operators，用多个条件筛选结果，非常常见。举两个例子：逻辑与有两种写法，直接在对象中添加多个条件，或者用 $and 加一个数组；逻辑或用 $or。写代码实验。先做逻辑与：条件是 age 小于 30 同时 name 等于 AD，运行后 resultArray 里找到两条，两个 AD 都出现了。逻辑或单独写以免看着乱：也是一个 object，$or 等于一个数组，数组里放多个条件。第一个条件 age 大于 30（$gt），第二个条件 name 等于小宝（小宝的年龄小于 30）。运行后大于 30 的数据都拿出来了，name 等于小宝的两条也拿到了，实验成功。

第三类 element operator，非常好理解，只有两个操作符：$exists 判断属性是否存在；$type 判断值的数据类型是 string 还是 number 等。官方文档有完整的 type 列表，可以用 number 表示，也可以用 aliases 字符串判断，我觉得字符串更好理解，比如 double、string、object 等。

代码实验 $exists：数据里有些记录有 hobby 字段，我们要找出有爱好的数据，条件写 {hobby: {$exists: true}}，注意拼写别写错，toArray 后打印。查询出两条记录，都有 hobby，没问题。再测 $type：找 age 的 type 是 number 的记录，条件写 {age: {$type: 'number'}}。这里的 number 代表一个集合，支持 double、32 位整数、64 位整数等各种数值类型。运行后所有 age 是 number 类型的都被查出来。我们现在都是 number 类型，所以其实所有有 age 的记录都出现了，可以自己添加一条 age 不是 number 的记录测试。

最后一类 evaluation operator 属于比较高级的内容，暂时不讲，后面会慢慢涉及。所有操作符的参考我都提供了官方文档地址，四种 operator 里还有很多没讲到的操作符，可以自行了解。

这节课讲完了 MongoDB 的操作符，用它们可以让 MongoDB 非常方便地帮你完成数据筛选。
