// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 方案4: 两个变量滚动迭代（start/end + 临时变量）
func fib(n int) int { // 定义函数/方法 fib
	if n == 0 { // 若 元素个数 等于 0
		return 0 // 返回 0
	}
	if n == 1 { // 若 元素个数 等于 1
		return 1 // 返回 1
	}
	start := 0                // 把 0 写入 start :
	end := 1                  // 把 1 写入 end :
	for i := 2; i <= n; i++ { // 让 下标 i 从 2 开始计数
		endTmp := end     // 把 终点 写入 endTmp :
		end = end + start // 把 终点 加 起点 写入 终点
		start = endTmp    // 把 endTmp 写入 起点
	}
	return end // 返回 终点
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
