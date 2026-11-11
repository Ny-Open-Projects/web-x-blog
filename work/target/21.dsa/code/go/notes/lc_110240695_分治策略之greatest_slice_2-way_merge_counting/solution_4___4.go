// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// Greatest Slice - 方案4: Linear Scan (Kadane, O(n))
func maxSubArray(arr []int) int { // 定义函数/方法 maxSubArray
	if len(arr) == 0 { // 若 长度(数组) 等于 0
		return 0 // 返回 0
	}
	maxSum := arr[0]                // 把 数组[0] 写入 maxSum :
	currentSum := arr[0]            // 把 数组[0] 写入 currentSum :
	for i := 1; i < len(arr); i++ { // 让 下标 i 从 1 开始计数
		currentSum = max2(arr[i], currentSum+arr[i]) // 把 max2(数组[下标 i], currentSum 加 数组[下标 i]) 写入 currentSum
		maxSum = max2(maxSum, currentSum)            // 把 max2(maxSum, currentSum) 写入 maxSum
	}
	return maxSum // 返回 maxSum
}

func max2(a, b int) int { // 定义函数/方法 max2
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want int   // want int
	}{ // }{
		{[]int{-2, 1, -3, 4, -1, 2, 1}, 6},
		{[]int{-1}, -1},
		{[]int{1}, 1},
		{[]int{-2, -1}, -1},
		{[]int{}, 0},
		{[]int{5, 4, -1, 7, 8}, 23},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := maxSubArray(c.in); got != c.want { // 若 got : 赋值为 maxSubArray(字符.in); got 不等于 字符.want
			ok = false                                                         // 把 false 写入 ok
			fmt.Printf("FAIL maxSubArray(%v)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
