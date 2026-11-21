# 14-4-Node.js Cluster 压力测试对比结果

上节课介绍了 cluster 模式是什么，这节课说说它的实际优势。空口无凭，最好拿出实实在在的数据来，这样不用解释自然明了。我们的任务是创建两个脚本，分别构建两种模式来对比。

## 构建慢接口（no-cluster 版）

第一个脚本是不用 cluster 的版本。为了创建路由，安装了 Express 简单使用一下。接口设计成 `/api/slow`，故意让它慢一些：

```ts
console.time('slow API');
const baseNumber = 7;
let result = 0;
for (let i = Math.pow(baseNumber, 7); i >= 0; i--) {
  result += Math.tan(i) * Math.atan(i);
}
console.timeEnd('slow API');
console.log(`process id: ${process.pid}`);
res.send(`result: ${result}`);
```

思路是模拟一个相对缓慢的计算：从 7 的 7 次方开始往下循环，循环体内再做 tan 和 atan 两个三角函数运算并相乘累加。三角函数的意义可能都淡忘了，没关系，我们知道它比较耗时就行。想更耗时的话，可以加大 baseNumber 的数值或乘方次数。计算结束后用 `timeEnd` 记录耗时（与开头的命名相同，都叫 slow API），并输出 process.pid 和结果。

先运行一下看效果：访问 `/api/slow`，能看到 slow API 的耗时记录，单次请求其实还挺快。

## Cluster 版

第二个脚本叫 cluster-express，和上节课的代码几乎完全一样：先用 `cluster.isPrimary` 判断 master，再根据 CPU 核数 fork 出一系列子进程，把 worker 的 HTTP 服务逻辑原样搬过来。运行后可以看到 master 在某个 PID 上，CPU 四核，四个 worker 都启动了，并且监听同一个端口。

现在刷新页面，单次请求下两者的时间几乎差不多，而且每次只发送一个 request，差别不够大。要看差距，需要做压力测试。

## 压力测试：loadtest

用了 cluster 之后，应用架构变成：request 先到 master process，由 master 按自己的策略分配给对应的 worker。master 有点像 load balancer，把工作尽量平均分给每个 worker，避免一个 worker 活太重、其他进程没活干。这个分配是自动的，不需要任何操作。

测试工具选 loadtest，Node.js 生态非常流行的压测工具，使用也很简单：

```bash
npm install loadtest --save-dev
```

需要了解的参数有三个：`--n` 后面接数字，代表总共发送多少个请求；`--c` 是 concurrency，即同时有几个客户端在发请求；`--rps` 是 requests per second，每秒发送多少个请求。最后跟上目标 URL。

在 package.json 里加一个脚本：

```json
"cluster": "npx loadtest --n 400 --c 50 http://localhost:3000/api/slow"
```

因为安装在本地，所以用 npx 来运行。计划总共发 400 个请求，并发 50。

## 对比结果

先启动 no-cluster 版本，再运行压测脚本。测试结束后关注几个关键数据：由于没用 cluster，只有一个进程在处理（PID 固定不变），结果：

- total time：约 13 秒
- mean latency（平均延迟）：约 1599ms（1600ms 左右）

关掉它，改跑 cluster 版本，重新执行同样的压测。这次观察 process id 会发现每次处理的进程不一样，说明 master 在做分配。结果：

- total time：约 7.6 秒
- mean latency：约 895ms（900ms 左右）

从 1600ms 降到 900ms 左右，性能提升非常显著。

所以两节课下来：我们介绍了 cluster 的概念，并用数据对比出了它的优点。生产环境中一般都会用 cluster 来运行应用。下节课说说框架针对 Cluster 做的特殊优化。
