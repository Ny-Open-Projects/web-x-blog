// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type RecentCounter struct { // 定义类型
	queue []int // 队列 []int
	front int   // front int
}

func NewRecentCounter() *RecentCounter { // 定义函数/方法 NewRecentCounter
	return &RecentCounter{queue: []int{}, front: 0} // 返回 按位与 RecentCounter{队列: []int{}, front: 0}
}

func (this *RecentCounter) Ping(t int) int { // 定义函数/方法 Ping
	this.queue = append(this.queue, t)    // 把 append(this.队列, 另一字符串) 写入 队列
	for this.queue[this.front] < t-3000 { // for this.队列[this.front] 小于 另一字符串 减 3000 {
		this.front++ // this.front 加一
	}
	return len(this.queue) - this.front // 返回 长度(this.队列) 减 this.front
}

func main() { // 程序入口：跑内嵌自测用例
	c := NewRecentCounter() // 把 NewRecentCounter() 写入 c :
	ok := true              // 把 true 写入 ok :
	tc := []struct {        // 把 []struct { 写入 tc :
		t    int // 另一字符串 int
		want int // want int
	}{ // }{
		{1, 1}, {100, 2}, {3001, 3},
	}
	for _, cse := range tc { // 同时取 _ 与 cse 遍历
		if got := c.Ping(cse.t); got != cse.want { // 若 got : 赋值为 字符.Ping(cse.另一字符串); got 不等于 cse.want
			ok = false                                                     // 把 false 写入 ok
			fmt.Printf("FAIL Ping(%d)=%d want %d\n", cse.t, got, cse.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
