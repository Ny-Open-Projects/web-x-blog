// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 不同路径：二维动态规划
// 忠实于 Python 参考实现 ref_uniquePaths 的 DP 思想
func uniquePaths(m, n int) int { // 定义函数/方法 uniquePaths
	f := make([][]int, m) // 把 make([][]int, 映射表) 写入 f :
	for i := range f {    // 把 range f { 写入 for i :
		f[i] = make([]int, n) // 把 make([]int, 元素个数) 写入 f[i]
	}
	for i := 0; i < m; i++ { // 让 下标 i 从 0 开始计数
		f[i][0] = 1 // 把 1 写入 f[i][0]
	}
	for j := 0; j < n; j++ { // 让 下标 j 从 0 开始计数
		f[0][j] = 1 // 把 1 写入 f[0][j]
	}
	for i := 1; i < m; i++ { // 让 下标 i 从 1 开始计数
		for j := 1; j < n; j++ { // 让 下标 j 从 1 开始计数
			f[i][j] = f[i-1][j] + f[i][j-1] // 把 f[下标 i 减 1][下标 j] 加 f[下标 i][下标 j 减 1] 写入 f[i][j]
		}
	}
	return f[m-1][n-1] // 返回 f[映射表 减 1][元素个数 减 1]
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
