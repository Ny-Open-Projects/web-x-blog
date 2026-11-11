// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 忠实翻译 python solution_4：一维 dp 数组 f，f[0]=1，按硬币正序累加
func change(amount int, coins []int) int { // 定义函数/方法 change
	f := make([]int, amount+1) // 把 make([]int, 目标金额 加 1) 写入 f :
	f[0] = 1                   // 把 1 写入 f[0]
	for _, x := range coins {  // 同时取 _ 与 x 遍历
		for c := x; c <= amount; c++ { // 把 x; 字符 不超过 目标金额; 字符 加一 { 写入 for c :
			f[c] += f[c-x] // f[c]累加 f[字符 减 x]
		}
	}
	return f[amount] // 返回 f[目标金额]
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
