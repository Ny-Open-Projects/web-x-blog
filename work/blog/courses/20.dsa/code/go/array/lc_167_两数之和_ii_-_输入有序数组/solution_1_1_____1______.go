// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145115578
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func twoSum(numbers []int, target int) []int { // 定义函数/方法 twoSum
	for i := range numbers { // 把 range numbers { 写入 for i :
		left, right := i+1, len(numbers)-1 // 把 下标 i 加 1, 长度(numbers) 减 1 写入 left, right :
		for left <= right {                // 把 右边界 { 写入 for left <
			mid := (left + right) / 2              // 把 (左边界 加 右边界) 除以 2 写入 mid :
			if numbers[mid] == target-numbers[i] { // 若 numbers[中点] 等于 目标值 减 numbers[下标 i]
				return []int{i + 1, mid + 1} // 返回 []int{下标 i 加 1, 中点 加 1}
			} else if numbers[mid] > target-numbers[i] { // 否则，若 numbers[中点] 超过 目标值 减 numbers[下标 i]
				right = mid - 1 // 把 中点 减 1 写入 右边界
			} else { // 否则
				left = mid + 1 // 把 中点 加 1 写入 左边界
			}
		}
	}
	return []int{-1, -1} // 返回 []int{ 减 1, 减 1}
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums   []int // 数组 []int
		target int   // 目标值 int
		want   []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{2, 7, 11, 15}, 9, []int{1, 2}},
		{[]int{2, 3, 4}, 6, []int{1, 3}},
		{[]int{-1, 0}, -1, []int{1, 2}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := twoSum(c.nums, c.target); !reflect.DeepEqual(got, c.want) {
			ok = false                                                                   // 把 false 写入 ok
			fmt.Printf("FAIL twoSum(%v,%v)=%v want %v\n", c.nums, c.target, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
