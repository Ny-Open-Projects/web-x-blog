// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116938
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func sortedSquares(nums []int) []int { // 定义函数/方法 sortedSquares
	n := len(nums)           // 把 长度(数组) 写入 n :
	ans := make([]int, 0, n) // 把 make([]int, 0, 元素个数) 写入 ans :
	negative := -1           // 把 减 1 写入 negative :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		if nums[i] < 0 { // 若 数组[下标 i] 小于 0
			negative = i // 把 下标 i 写入 negative
		}
	}
	i, j := negative, negative+1 // 把 negative, negative 加 1 写入 i, j :
	for i >= 0 || j < n {        // 把 0 或 下标 j 小于 元素个数 { 写入 for i >
		if i < 0 { // 若 下标 i 小于 0
			ans = append(ans, nums[j]*nums[j]) // 把 append(答案, 数组[下标 j] 乘 数组[下标 j]) 写入 答案
			j++                                // 下标 j 加一
		} else if j == n { // 否则，若 下标 j 等于 元素个数
			ans = append(ans, nums[i]*nums[i]) // 把 append(答案, 数组[下标 i] 乘 数组[下标 i]) 写入 答案
			i--                                // 下标 i 减一
		} else if nums[i]*nums[i] < nums[j]*nums[j] { // 否则，若 数组[下标 i] 乘 数组[下标 i] 小于 数组[下标 j] 乘 数组[下标 j]
			ans = append(ans, nums[i]*nums[i]) // 把 append(答案, 数组[下标 i] 乘 数组[下标 i]) 写入 答案
			i--                                // 下标 i 减一
		} else { // 否则
			ans = append(ans, nums[j]*nums[j]) // 把 append(答案, 数组[下标 j] 乘 数组[下标 j]) 写入 答案
			j++                                // 下标 j 加一
		}
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3}, []int{1, 4, 9}},
		{[]int{-4, -1, 0, 3, 10}, []int{0, 1, 9, 16, 100}},
		{[]int{-7, -3, 2, 3, 11}, []int{4, 9, 9, 49, 121}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := sortedSquares(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                           // 把 false 写入 ok
			fmt.Printf("FAIL sortedSquares(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
