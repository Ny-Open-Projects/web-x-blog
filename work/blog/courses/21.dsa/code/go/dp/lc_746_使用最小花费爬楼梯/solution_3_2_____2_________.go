// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853675
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func minCostClimbingStairs(cost []int) int { // 定义函数/方法 minCostClimbingStairs
	n := len(cost)           // 把 长度(cost) 写入 n :
	prev2 := cost[0]         // 把 cost[0] 写入 prev2 :
	prev1 := cost[1]         // 把 cost[1] 写入 prev1 :
	for i := 2; i < n; i++ { // 让 下标 i 从 2 开始计数
		cur := cost[i]     // 把 cost[下标 i] 写入 cur :
		if prev1 < prev2 { // 若 prev1 小于 prev2
			cur += prev1 // 当前值累加 prev1
		} else { // 否则
			cur += prev2 // 当前值累加 prev2
		}
		prev2 = prev1 // 把 prev1 写入 prev2
		prev1 = cur   // 把 当前值 写入 prev1
	}
	if prev1 < prev2 { // 若 prev1 小于 prev2
		return prev1 // 返回 prev1
	}
	return prev2 // 返回 prev2
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		cost []int // cost []int
		want int   // want int
	}{ // }{
		{[]int{10, 15, 20}, 15},
		{[]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}, 6},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := minCostClimbingStairs(c.cost) // 把 minCostClimbingStairs(字符.cost) 写入 got :
		if got != c.want {                   // 若 got 不等于 字符.want
			fmt.Printf("FAIL: got %d expected %d\n", got, c.want) // 打印输出
			os.Exit(1)                                            // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
