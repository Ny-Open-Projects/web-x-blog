// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 不同路径：排列组合 C(m+n-2, m-1)
// 忠实于 Python 参考实现 ref_uniquePaths 的等价数学形式
func uniquePaths(m, n int) int { // 定义函数/方法 uniquePaths
	if m == 1 || n == 1 { // 若 映射表 等于 1 或 元素个数 等于 1
		return 1 // 返回 1
	}
	k := m - 1   // 把 映射表 减 1 写入 k :
	if n-1 < k { // 若 元素个数 减 1 小于 下标 k
		k = n - 1 // 把 元素个数 减 1 写入 下标 k
	}
	total := m + n - 2       // 把 映射表 加 元素个数 减 2 写入 total :
	num := 1                 // 把 1 写入 num :
	for i := 0; i < k; i++ { // 让 下标 i 从 0 开始计数
		num *= (total - i) // 把 (总和 减 下标 i) 写入 num *
	}
	den := 1                  // 把 1 写入 den :
	for i := 1; i <= k; i++ { // 让 下标 i 从 1 开始计数
		den *= i // 把 下标 i 写入 den *
	}
	return num / den // 返回 num 除以 den
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
