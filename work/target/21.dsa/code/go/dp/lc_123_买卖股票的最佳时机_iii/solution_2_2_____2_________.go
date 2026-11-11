// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849793
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func max(a, b int) int { // 定义函数/方法 max
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

func maxProfit(prices []int) int { // 定义函数/方法 maxProfit
	if len(prices) == 0 { // 若 长度(价格序列) 等于 0
		return 0 // 返回 0
	}
	buy1 := -prices[0]             // 把 减 价格序列[0] 写入 buy1 :
	sell1 := 0                     // 把 0 写入 sell1 :
	buy2 := -prices[0]             // 把 减 价格序列[0] 写入 buy2 :
	sell2 := 0                     // 把 0 写入 sell2 :
	for _, p := range prices[1:] { // 同时取 _ 与 节点 遍历
		buy1 = max(buy1, -p)       // 把 取较大值 buy1, 减 节点) 写入 buy1
		sell1 = max(sell1, buy1+p) // 把 取较大值 sell1, buy1 加 节点) 写入 sell1
		buy2 = max(buy2, sell1-p)  // 把 取较大值 buy2, sell1 减 节点) 写入 buy2
		sell2 = max(sell2, buy2+p) // 把 取较大值 sell2, buy2 加 节点) 写入 sell2
	}
	return sell2 // 返回 sell2
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true          // 把 true 写入 ok :
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want int   // want int
	}{ // }{
		{[]int{3, 3, 5, 0, 0, 3, 1, 4}, 6},
		{[]int{1, 2, 3}, 2},
		{[]int{1}, 0},
		{[]int{}, 0},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := maxProfit(c.in); got != c.want { // 若 got : 赋值为 maxProfit(字符.in); got 不等于 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL maxProfit(%v)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
