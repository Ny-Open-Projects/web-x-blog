// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 方案2: 带记忆化的递归
func fib(n int) int { // 定义函数/方法 fib
	memo := map[int]int{} // 把 映射表[int]int{} 写入 memo :
	var f func(int) int   // var f func(int) int
	f = func(k int) int { // 把 func(下标 k int) int { 写入 f
		if k <= 1 { // 若 下标 k 不超过 1
			return k // 返回 下标 k
		}
		if v, ok := memo[k]; ok { // 若 值, ok : 赋值为 记忆化表[下标 k]; ok
			return v // 返回 值
		}
		memo[k] = f(k-1) + f(k-2) // 把 f(下标 k 减 1) 加 f(下标 k 减 2) 写入 memo[k]
		return memo[k]            // 返回 记忆化表[下标 k]
	}
	return f(n) // 定义函数/方法 f
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
