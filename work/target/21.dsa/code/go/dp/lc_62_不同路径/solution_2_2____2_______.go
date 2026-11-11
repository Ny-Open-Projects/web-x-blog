// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 不同路径：组合优化版（单循环累加）
// 忠实于 Python 参考实现 ref_uniquePaths 的等价数学形式
func uniquePaths(m, n int) int { // 定义函数/方法 uniquePaths
	if m == 1 || n == 1 { // 若 映射表 等于 1 或 元素个数 等于 1
		return 1 // 返回 1
	}
	ans := 1                                   // 把 1 写入 ans :
	for x, y := n, 1; y < m; x, y = x+1, y+1 { // 把 元素个数, 1; y 小于 映射表; x, y 赋值为 x 加 1, y 加 1 { 写入 for x, y :
		ans = ans * x / y // 把 答案 乘 x 除以 y 写入 答案
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct{ m, n, want int }                // 定义类型
	cases := []tc{{3, 7, 28}, {3, 2, 3}, {1, 1, 1}} // 把 []tc{{3, 7, 28}, {3, 2, 3}, {1, 1, 1}} 写入 cases :
	ok := true                                      // 把 true 写入 ok :
	for _, c := range cases {                       // 同时取 _ 与 字符 遍历
		got := uniquePaths(c.m, c.n) // 把 uniquePaths(字符.映射表, 字符.元素个数) 写入 got :
		if got != c.want {           // 若 got 不等于 字符.want
			fmt.Printf("FAIL: uniquePaths(%d,%d)=%d want %d\n", c.m, c.n, got, c.want) // 打印输出
			ok = false                                                                 // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("FAIL") // 打印输出
		os.Exit(1)          // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
