// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func fibRecursive(n int) int { // 定义函数/方法 fibRecursive
	if n < 2 { // 若 元素个数 小于 2
		return n // 返回 元素个数
	}
	return fibRecursive(n-1) + fibRecursive(n-2) // 定义函数/方法 fibRecursive
}

func fibIterative(n int) int { // 定义函数/方法 fibIterative
	if n < 2 { // 若 元素个数 小于 2
		return n // 返回 元素个数
	}
	a, b := 0, 1              // 把 0, 1 写入 a, b :
	for i := 2; i <= n; i++ { // 让 下标 i 从 2 开始计数
		a, b = b, a+b // 把 b, 数组 加 b 写入 a, b
	}
	return b // 返回 b
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                          // 把 true 写入 ok :
	if v := fibRecursive(10); v != 55 { // 若 值 : 赋值为 fibRecursive(10); 值 不等于 55
		ok = false                                          // 把 false 写入 ok
		fmt.Printf("FAIL fibRecursive(10)=%d want 55\n", v) // 打印输出
	}
	if v := fibIterative(10); v != 55 { // 若 值 : 赋值为 fibIterative(10); 值 不等于 55
		ok = false                                          // 把 false 写入 ok
		fmt.Printf("FAIL fibIterative(10)=%d want 55\n", v) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
