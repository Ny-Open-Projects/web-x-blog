// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 方案9: 两个变量滚动迭代（从 0 开始迭代 n 次，返回 a）
func fib(n int) int { // 定义函数/方法 fib
	a, b := 0, 1             // 把 0, 1 写入 a, b :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		a, b = b, a+b // 把 b, 数组 加 b 写入 a, b
	}
	return a // 返回 数组
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   int // in int
		want int // want int
	}{ // }{
		{0, 0},
		{1, 1},
		{2, 1},
		{5, 5},
		{10, 55},
		{20, 6765},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := fib(c.in); got != c.want { // 若 got : 赋值为 fib(字符.in); got 不等于 字符.want
			ok = false                                                 // 把 false 写入 ok
			fmt.Printf("FAIL fib(%d)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
