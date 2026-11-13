// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 忠实翻译 python solution_3：二维表 f[i][c]，f[0][0]=1
func change(amount int, coins []int) int { // 定义函数/方法 change
	n := len(coins)           // 把 长度(硬币面额) 写入 n :
	f := make([][]int, n+1)   // 把 make([][]int, 元素个数 加 1) 写入 f :
	for i := 0; i <= n; i++ { // 让 下标 i 从 0 开始计数
		f[i] = make([]int, amount+1) // 把 make([]int, 目标金额 加 1) 写入 f[i]
	}
	f[0][0] = 1              // 把 1 写入 f[0][0]
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		for c := 0; c <= amount; c++ { // 让 字符 从 0 开始计数
			if c < coins[i] { // 若 字符 小于 硬币面额[下标 i]
				f[i+1][c] = f[i][c] // 把 f[下标 i][字符] 写入 f[i+1][c]
			} else { // 否则
				f[i+1][c] = f[i][c] + f[i+1][c-coins[i]] // 把 f[下标 i][字符] 加 f[下标 i 加 1][字符 减 硬币面额[下标 i]] 写入 f[i+1][c]
			}
		}
	}
	return f[n][amount] // 返回 f[元素个数][目标金额]
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
