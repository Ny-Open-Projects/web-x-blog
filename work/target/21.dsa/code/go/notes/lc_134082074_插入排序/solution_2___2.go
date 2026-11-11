// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func insertionSort(nums []int) []int { // 定义函数/方法 insertionSort
	n := len(nums)           // 把 长度(数组) 写入 n :
	for i := 1; i < n; i++ { // 让 下标 i 从 1 开始计数
		key := nums[i]                // 把 数组[下标 i] 写入 key :
		j := i - 1                    // 把 下标 i 减 1 写入 j :
		for j >= 0 && nums[j] > key { // 把 0 且 数组[下标 j] 超过 key { 写入 for j >
			nums[j+1] = nums[j] // 把 数组[下标 j] 写入 nums[j+1]
			j--                 // 下标 j 减一
		}
		nums[j+1] = key // 把 key 写入 nums[j+1]
	}
	return nums // 返回 数组
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want []int // want []int
	}{ // }{
		{[]int{1, 2, 3}, []int{1, 2, 3}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{3, 1, 4, 1, 5, 9, 2, 6}, []int{1, 1, 2, 3, 4, 5, 6, 9}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := insertionSort(append([]int{}, c.in...)) // 把 insertionSort(append([]int{}, 字符.in...)) 写入 got :
		if len(got) != len(c.want) {
			ok = false
			fmt.Printf("FAIL len %v\n", c.in)
			continue
		}
		for i := range got {
			if got[i] != c.want[i] {
				ok = false
				fmt.Printf("FAIL %v got %v\n", c.in, got)
				break
			}
		} // 打印输出
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
