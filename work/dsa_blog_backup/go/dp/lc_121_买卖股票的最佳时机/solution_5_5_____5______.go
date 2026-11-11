// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849130
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func maxProfit(prices []int) int { // 定义函数/方法 maxProfit（分治：左半最优、右半最优、跨中点差）
	var solve func(lo, hi int) (int, int) // 返回 [区间min, 区间最优利润]
	solve = func(lo, hi int) (int, int) {
		if hi-lo == 1 { // 单元素
			return prices[lo], 0
		}
		mid := (lo + hi) / 2
		lMin, lBest := solve(lo, mid)
		rMin, rBest := solve(mid, hi)
		rMax := prices[mid]
		for i := mid; i < hi; i++ { // 右半最大卖出价
			if prices[i] > rMax {
				rMax = prices[i]
			}
		}
		cross := rMax - lMin // 跨中点：右半最高卖 - 左半最低买
		if cross < 0 {
			cross = 0
		}
		best := lBest
		if rBest > best {
			best = rBest
		}
		if cross > best {
			best = cross
		}
		mn := lMin
		if rMin < mn {
			mn = rMin
		}
		return mn, best
	}
	_, best := solve(0, len(prices))
	return best // 返回区间最优利润
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
