// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853482
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func maxProfit(prices []int, fee int) int { // 定义函数/方法 maxProfit
	n := len(prices) // 把 长度(价格序列) 写入 n :
	if n == 0 {      // 若 元素个数 等于 0
		return 0 // 返回 0
	}
	cash := 0                // 把 0 写入 cash :
	hold := -prices[0]       // 把 减 价格序列[0] 写入 hold :
	for i := 1; i < n; i++ { // 让 下标 i 从 1 开始计数
		newCash := cash                // 把 cash 写入 newCash :
		if hold+prices[i]-fee > cash { // 若 hold 加 价格序列[下标 i] 减 fee 超过 cash
			newCash = hold + prices[i] - fee // 把 hold 加 价格序列[下标 i] 减 fee 写入 newCash
		}
		newHold := hold               // 把 hold 写入 newHold :
		if newCash-prices[i] > hold { // 若 newCash 减 价格序列[下标 i] 超过 hold
			newHold = newCash - prices[i] // 把 newCash 减 价格序列[下标 i] 写入 newHold
		}
		cash = newCash // 把 newCash 写入 cash
		hold = newHold // 把 newHold 写入 hold
	}
	return cash // 返回 cash
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		prices []int // 价格序列 []int
		fee    int   // fee int
		want   int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 3, 2, 8, 4, 9}, 2, 8},
		{[]int{1, 3, 7, 5}, 1, 5},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := maxProfit(c.prices, c.fee); got != c.want { // 若 got : 赋值为 maxProfit(字符.价格序列, 字符.fee); got 不等于 字符.want
			ok = false                                                                     // 把 false 写入 ok
			fmt.Printf("FAIL maxProfit(%v,%d)=%v want %v\n", c.prices, c.fee, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
