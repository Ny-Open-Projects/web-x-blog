// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// fibonacci 带记忆化 (Memoization)
func fibonacci(n int) int { // 定义函数/方法 fibonacci
	memo := map[int]int{}   // 把 映射表[int]int{} 写入 memo :
	var fib func(int) int   // var fib func(int) int
	fib = func(n int) int { // 把 func(元素个数 int) int { 写入 fib
		if n <= 1 { // 若 元素个数 不超过 1
			return n // 返回 元素个数
		}
		if v, ok := memo[n]; ok { // 若 值, ok : 赋值为 记忆化表[元素个数]; ok
			return v // 返回 值
		}
		memo[n] = fib(n-1) + fib(n-2) // 把 fib(元素个数 减 1) 加 fib(元素个数 减 2) 写入 memo[n]
		return memo[n]                // 返回 记忆化表[元素个数]
	}
	return fib(n) // 定义函数/方法 fib
}

func main() { // 程序入口：跑内嵌自测用例
	if fibonacci(10) != 55 { // 若 fibonacci(10) 不等于 55
		fmt.Println("FAIL fibonacci(10)") // 打印输出
		os.Exit(1)                        // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
