// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 忠实翻译 python solution_1：带记忆化的递归 dfs(i, c)
// i 为当前考虑的硬币下标；i < 0 时若剩余金额为 0 则计 1 种方案，否则 0 种。
func change(amount int, coins []int) int { // 定义函数/方法 change
	n := len(coins)              // 把 长度(硬币面额) 写入 n :
	memo := make(map[[2]int]int) // 把 make(映射表[[2]int]int) 写入 memo :
	var dfs func(i, c int) int   // var dfs func(下标 i, 字符 int) int
	dfs = func(i, c int) int {   // 把 func(下标 i, 字符 int) int { 写入 dfs
		if i < 0 { // 若 下标 i 小于 0
			if c == 0 { // 若 字符 等于 0
				return 1 // 返回 1
			}
			return 0 // 返回 0
		}
		k := [2]int{i, c}         // 把 [2]int{下标 i, 字符} 写入 k :
		if v, ok := memo[k]; ok { // 若 值, ok : 赋值为 记忆化表[下标 k]; ok
			return v // 返回 值
		}
		var r int         // var 右指针 int
		if c < coins[i] { // 若 字符 小于 硬币面额[下标 i]
			r = dfs(i-1, c) // 把 dfs(下标 i 减 1, 字符) 写入 右指针
		} else { // 否则
			r = dfs(i-1, c) + dfs(i, c-coins[i]) // 把 dfs(下标 i 减 1, 字符) 加 dfs(下标 i, 字符 减 硬币面额[下标 i]) 写入 右指针
		}
		memo[k] = r // 把 右指针 写入 memo[k]
		return r    // 返回 右指针
	}
	return dfs(n-1, amount) // 定义函数/方法 dfs
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		amount int   // 目标金额 int
		coins  []int // 硬币面额 []int
		want   int   // want int
	}{ // }{
		{5, []int{1, 2, 5}, 4},
		{11, []int{1, 2, 5}, 11},
		{3, []int{2}, 0},
		{0, []int{1, 2, 5}, 1},
		{7, []int{2, 3}, 1},
		{10, []int{}, 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := change(c.amount, c.coins); got != c.want { // 若 got : 赋值为 change(字符.目标金额, 字符.硬币面额); got 不等于 字符.want
			ok = false                                                                     // 把 false 写入 ok
			fmt.Printf("FAIL change(%d, %v)=%d want %d\n", c.amount, c.coins, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
