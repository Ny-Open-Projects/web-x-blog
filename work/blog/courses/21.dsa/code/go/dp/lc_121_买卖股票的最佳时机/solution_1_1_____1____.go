// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849130
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func maxProfit(prices []int) int { // 定义函数/方法 maxProfit（O(n)：遍历中追踪历史最低价）
	minPrice := int(^uint(0) >> 1) // 历史最低价（初值取最大 int）
	maxprofit := 0                 // 最大利润
	for _, p := range prices {     // 单趟扫描
		if p < minPrice { // 先更新最低价
			minPrice = p
		} else if p-minPrice > maxprofit { // 若今天卖出更优
			maxprofit = p - minPrice
		}
	}
	return maxprofit // 返回 maxprofit
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		prices []int // 价格序列 []int
		want   int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{7, 1, 5, 3, 6, 4}, 5},
		{[]int{7, 6, 4, 3, 1}, 0},
		{[]int{1, 2, 3}, 2},
	}
	fail := false             // 把 false 写入 fail :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := maxProfit(c.prices) // 把 maxProfit(字符.价格序列) 写入 got :
		if got != c.want {         // 若 got 不等于 字符.want
			fmt.Printf("FAIL maxProfit(%v)=%d want %d\n", c.prices, got, c.want) // 打印输出
			fail = true                                                          // 把 true 写入 fail
		}
	}
	if fail { // 若 fail
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
