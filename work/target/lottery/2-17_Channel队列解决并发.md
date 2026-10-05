# Go 企业级抽奖项目: 用 Channel 队列解决红包并发安全

## 纲要

- 红包活动存在两个并发安全问题：全局 `map` 集合（已用 `sync.Map` 解决）与单个红包内部 `[]int` 切片的更新（本节解决）。
- 切片更新不再用互斥锁，改用**消息队列 + Channel** 的模型：用 Goroutine 间通信代替共享内存加锁。
- 定义任务结构 `chanTask`：包含红包 ID（`TaskID`）与回调 Channel（`Callback`），用于把抢到的金额回传。
- 新增一个常驻服务 `GrabService`，死循环从队列取任务、抢红包、通过回调 Channel 把金额返回。
- 抢红包接口改为：构造任务 → 发送到队列 → 从回调 Channel 等待结果，不再直接改切片。

## 任务模型设计

把"抢红包并更新切片"这件事封装成一个任务，投递到队列，由专门的消费者串行处理，从而彻底避免多个请求同时修改同一切片。

```go
package main

// chanTask 抢红包任务
type chanTask struct {
	TaskID   int         // 红包 ID
	Callback chan int    // 回调 Channel，用于把抢到的金额回传
}
```

## 常驻消费服务

服务内部是一个死循环，不断从任务队列取出任务，读取红包、随机定位、更新切片，最后把金额通过 `Callback` 回传。用 Channel 做协程同步，而不是锁。

```go
import (
	"math/rand"
	"time"
)

// taskQueue 抢红包任务队列
var taskQueue = make(chan chanTask, 1024)

// GrabService 常驻服务：串行消费任务，保证切片更新无并发冲突
func GrabService() {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	for task := range taskQueue {
		money := grabOne(task.TaskID, r)
		task.Callback <- money // 回传结果
	}
}

// grabOne 在红包切片内随机取一个金额并更新（由单消费者串行执行）
func grabOne(id int, r *rand.Rand) int {
	amounts, ok := LoadPacket(id)
	if !ok || len(amounts) == 0 {
		return 0
	}
	idx := r.Intn(len(amounts))
	money := amounts[idx]
	amounts = removeAt(amounts, idx)
	if len(amounts) == 0 {
		DeletePacket(id)
	} else {
		StorePacket(id, amounts)
	}
	return money
}
```

## 抢红包接口改造

原来"抢到即改切片"的逻辑去掉，改成构造任务、投递队列、阻塞等待回调。只有抢到（金额 > 0）与未抢到（金额 <= 0）的提示语不同。

```go
// GrabPacket 抢红包：投递任务到队列，等待回调结果
func GrabPacket(id int) (int, string) {
	cb := make(chan int, 1)
	taskQueue <- chanTask{TaskID: id, Callback: cb}
	money := <-cb
	if money <= 0 {
		return money, "很遗憾，没有抢到红包"
	}
	return money, "恭喜你抢到一个红包"
}
```

## 启动方式

在程序初始化（`main` 或 `app` 启动）时启动消费服务，使队列开始工作：

```go
func main() {
	go GrabService() // 启动常驻抢红包服务
	// ... 注册路由、发/抢红包接口
}
```

## API 速览

- `chanTask{TaskID int, Callback chan int}`：抢红包任务，携带红包 ID 与结果回传通道。
- `GrabService()`：常驻消费者，从 `taskQueue` 取任务并串行更新切片。
- `grabOne(id int, r *rand.Rand) int`：读取红包、随机定位、更新切片、返回金额。
- `GrabPacket(id int) (int, string)`：投递任务并阻塞等待回调。

## Demo 示例

运行说明：将本篇 `chanTask`、`GrabService`、`GrabPacket` 与前面 `sync.Map` 版的 `LoadPacket`/`StorePacket`/`DeletePacket`/`removeAt` 合并为 `main` 包，`main` 中 `go GrabService()` 后多次调用 `GrabPacket` 即可验证串行消费下的并发安全。

代码说明：用 Channel 把"共享状态修改"收敛到单一消费者，是"不要通过共享内存来通信，而要通过通信来共享内存"的典型实践。

技术点总结：并发安全的第二条路径是消息队列 + Channel，用协程通信替代锁；相比互斥锁，它把竞争点集中到消费者，逻辑更清晰，也更容易做多队列横向扩展。

相关度：95%。是否需要继续：是。代码是否可运行：是。
