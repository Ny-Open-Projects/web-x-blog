// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660487
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func climbStairs(n int) int { // 定义函数/方法 climbStairs
	if n <= 1 { // 若 元素个数 不超过 1
		return 1 // 返回 1
	}
	prev, cur := 1, 1         // 把 1, 1 写入 prev, cur :
	for k := 2; k <= n; k++ { // 让 下标 k 从 2 开始计数
		prev, cur = cur, prev+cur // 把 当前值, 前一个 加 当前值 写入 prev, cur
	}
	return cur // 返回 当前值
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		n    int // 元素个数 int
		want int // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{2, 2},
		{3, 3},
		{10, 89},
	}
	fail := false             // 把 false 写入 fail :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := climbStairs(c.n) // 把 climbStairs(字符.元素个数) 写入 got :
		if got != c.want {      // 若 got 不等于 字符.want
			fmt.Printf("FAIL climbStairs(%d)=%d want %d\n", c.n, got, c.want) // 打印输出
			fail = true                                                       // 把 true 写入 fail
		}
	}
	if fail { // 若 fail
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
