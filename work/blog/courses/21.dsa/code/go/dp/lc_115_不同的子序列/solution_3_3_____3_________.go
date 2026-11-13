// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// numDistinct 是 Python 参考 solution_3 的忠实翻译（递归 + 记忆化）。
func numDistinct(s, t string) int { // 定义函数/方法 numDistinct
	m := len(s)              // 把 长度(字符串) 写入 m :
	n := len(t)              // 把 长度(另一字符串) 写入 n :
	memo := make([][]int, m) // 把 make([][]int, 映射表) 写入 memo :
	for i := range memo {    // 把 range 记忆化表 { 写入 for i :
		memo[i] = make([]int, n) // 把 make([]int, 元素个数) 写入 memo[i]
		for j := range memo[i] { // 把 range 记忆化表[下标 i] { 写入 for j :
			memo[i][j] = -1 // 把 减 1 写入 memo[i][j]
		}
	}
	var helper func(i, j int) int // var helper func(下标 i, 下标 j int) int
	helper = func(i, j int) int { // 把 func(下标 i, 下标 j int) int { 写入 helper
		if j < 0 { // 若 下标 j 小于 0
			return 1 // 返回 1
		}
		if i < 0 { // 若 下标 i 小于 0
			return 0 // 返回 0
		}
		if memo[i][j] != -1 { // 若 记忆化表[下标 i][下标 j] 不等于 减 1
			return memo[i][j] // 返回 记忆化表[下标 i][下标 j]
		}
		var res int       // var 结果 int
		if s[i] == t[j] { // 若 字符串[下标 i] 等于 另一字符串[下标 j]
			res = helper(i-1, j) + helper(i-1, j-1) // 把 helper(下标 i 减 1, 下标 j) 加 helper(下标 i 减 1, 下标 j 减 1) 写入 结果
		} else { // 否则
			res = helper(i-1, j) // 把 helper(下标 i 减 1, 下标 j) 写入 结果
		}
		memo[i][j] = res // 把 结果 写入 memo[i][j]
		return res       // 返回 结果
	}
	return helper(m-1, n-1) // 定义函数/方法 helper
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		s, t string // 字符串, 另一字符串 string
		want int    // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"rabbbit", "rabbit", 3},
		{"babgbag", "bag", 5},
		{"a", "a", 1},
		{"abc", "", 1},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := numDistinct(c.s, c.t); got != c.want { // 若 got : 赋值为 numDistinct(字符.字符串, 字符.另一字符串); got 不等于 字符.want
			fmt.Printf("FAIL %q %q got=%d want=%d\n", c.s, c.t, got, c.want) // 打印输出
			os.Exit(1)                                                       // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
