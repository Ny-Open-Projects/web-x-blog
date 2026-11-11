// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134633617
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func maxProfit(prices []int) int { // 定义函数/方法 maxProfit
	cash := 0            // 把 0 写入 cash :
	hold := 0            // 把 0 写入 hold :
	if len(prices) > 0 { // 若 长度(价格序列) 超过 0
		hold = -prices[0] // 把 减 价格序列[0] 写入 hold
	}
	for _, price := range prices { // 同时取 _ 与 price 遍历
		newCash := cash        // 把 cash 写入 newCash :
		if hold+price > cash { // 若 hold 加 price 超过 cash
			newCash = hold + price // 把 hold 加 price 写入 newCash
		}
		newHold := hold           // 把 hold 写入 newHold :
		if newCash-price > hold { // 若 newCash 减 price 超过 hold
			newHold = newCash - price // 把 newCash 减 price 写入 newHold
		}
		cash = newCash // 把 newCash 写入 cash
		hold = newHold // 把 newHold 写入 hold
	}
	return cash // 返回 cash
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
