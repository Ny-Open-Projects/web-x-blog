// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381295
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func onesCount(x int) int { // 定义函数/方法 onesCount
	c := 0      // 把 0 写入 c :
	for x > 0 { // for x 超过 0 {
		c += x % 2 // 字符累加 x 对…取模 2
		x /= 2     // 把 2 写入 x /
	}
	return c // 返回 字符
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true       // 把 true 写入 ok :
	tc := []struct { // 把 []struct { 写入 tc :
		in   int // in int
		want int // want int
	}{ // }{
		{1, 1}, {2, 1}, {3, 2}, {7, 3}, {0, 0},
	}
	for _, c := range tc { // 同时取 _ 与 字符 遍历
		if got := onesCount(c.in); got != c.want { // 若 got : 赋值为 onesCount(字符.in); got 不等于 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL onesCount(%d)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
