// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 方案7: 记忆化搜索（等价于 python lru_cache 的内部 dfs）
func fib(n int) int { // 定义函数/方法 fib
	memo := map[int]int{}   // 把 映射表[int]int{} 写入 memo :
	var dfs func(int) int   // var dfs func(int) int
	dfs = func(x int) int { // 把 func(x int) int { 写入 dfs
		if x == 0 { // 若 x 等于 0
			return 0 // 返回 0
		}
		if x == 1 { // 若 x 等于 1
			return 1 // 返回 1
		}
		if v, ok := memo[x]; ok { // 若 值, ok : 赋值为 记忆化表[x]; ok
			return v // 返回 值
		}
		memo[x] = dfs(x-1) + dfs(x-2) // 把 dfs(x 减 1) 加 dfs(x 减 2) 写入 memo[x]
		return memo[x]                // 返回 记忆化表[x]
	}
	return dfs(n) // 定义函数/方法 dfs
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
