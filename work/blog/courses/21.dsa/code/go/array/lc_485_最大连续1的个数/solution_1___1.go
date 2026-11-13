package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func findMaxConsecutiveOnes(nums []int) int { // 定义函数/方法 findMaxConsecutiveOnes
	best := 0                // 把 0 写入 best :
	cur := 0                 // 把 0 写入 cur :
	for _, x := range nums { // 同时取 _ 与 x 遍历
		if x == 1 { // 若 x 等于 1
			cur++           // 当前值 加一
			if cur > best { // 若 当前值 超过 当前最优
				best = cur // 把 当前值 写入 当前最优
			}
		} else { // 否则
			cur = 0 // 把 0 写入 当前值
		}
	}
	return best // 返回 当前最优
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		nums []int // 数组 []int
		want int   // want int
	}{ // }{
		{[]int{1, 1, 0, 1, 1, 1}, 3},
		{[]int{1, 0, 1, 1, 0, 1}, 2},
		{[]int{0}, 0},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := findMaxConsecutiveOnes(c.nums) // 把 findMaxConsecutiveOnes(字符.数组) 写入 got :
		if got != c.want {                    // 若 got 不等于 字符.want
			fmt.Printf("FAIL: got %d expected %d\n", got, c.want) // 打印输出
			os.Exit(1)                                            // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
