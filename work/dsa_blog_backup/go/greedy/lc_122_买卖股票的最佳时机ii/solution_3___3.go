// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134633617
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func maxProfit(prices []int) int { // 定义函数/方法 maxProfit
	n := len(prices) // 把 长度(价格序列) 写入 n :
	if n < 2 {       // 若 元素个数 小于 2
		return 0 // 返回 0
	}
	i := 0        // 把 0 写入 i :
	profit := 0   // 把 0 写入 profit :
	for i < n-1 { // for 下标 i 小于 元素个数 减 1 {
		for i < n-1 && prices[i] >= prices[i+1] { // 把 价格序列[下标 i 加 1] { 写入 for i < n-1 && prices[i] >
			i++ // 下标 i 加一
		}
		valley := prices[i]                       // 把 价格序列[下标 i] 写入 valley :
		for i < n-1 && prices[i] <= prices[i+1] { // 把 价格序列[下标 i 加 1] { 写入 for i < n-1 && prices[i] <
			i++ // 下标 i 加一
		}
		peak := prices[i]       // 把 价格序列[下标 i] 写入 peak :
		profit += peak - valley // profit累加 peak 减 valley
	}
	return profit // 返回 profit
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{7, 1, 5, 3, 6, 4}, 7},
		{[]int{1, 2, 3}, 2},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := maxProfit(c.in); got != c.want { // 若 got : 赋值为 maxProfit(字符.in); got 不等于 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL maxProfit(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
