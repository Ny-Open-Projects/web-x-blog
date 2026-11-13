// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type RecentCounter struct { // 定义类型
	q []int // 节点 []int
}

func Constructor() *RecentCounter { // 定义函数/方法 Constructor
	return &RecentCounter{q: []int{}} // 返回 按位与 RecentCounter{节点: []int{}}
}

func (this *RecentCounter) Ping(t int) int { // 定义函数/方法 Ping
	this.q = append(this.q, t) // 把 append(this.节点, 另一字符串) 写入 节点
	for this.q[0] < t-3000 {   // for this.节点[0] 小于 另一字符串 减 3000 {
		this.q = this.q[1:] // 把 this.节点[1:] 写入 节点
	}
	return len(this.q) // 定义函数/方法 len
}

func main() { // 程序入口：跑内嵌自测用例
	c := Constructor() // 把 Constructor() 写入 c :
	ok := true         // 把 true 写入 ok :
	tc := []struct {   // 把 []struct { 写入 tc :
		t    int // 另一字符串 int
		want int // want int
	}{ // }{
		{1, 1}, {100, 2}, {3001, 3}, {3002, 3},
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
