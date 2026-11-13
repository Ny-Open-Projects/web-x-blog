// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func selectionSort(nums []int) []int { // 定义函数/方法 selectionSort
	for i := 0; i < len(nums); i++ { // 让 下标 i 从 0 开始计数
		minIdx := i                          // 把 下标 i 写入 minIdx :
		for j := i + 1; j < len(nums); j++ { // 把 下标 i 加 1; 下标 j 小于 长度(数组); 下标 j 加一 { 写入 for j :
			if nums[j] < nums[minIdx] { // 若 数组[下标 j] 小于 数组[minIdx]
				minIdx = j // 把 下标 j 写入 minIdx
			}
		}
		nums[i], nums[minIdx] = nums[minIdx], nums[i] // 把 数组[minIdx], 数组[下标 i] 写入 nums[i], nums[minIdx]
	}
	return nums // 返回 数组
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3}, []int{1, 2, 3}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{3, 1, 2}, []int{1, 2, 3}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		in := append([]int{}, c.in...) // 把 append([]int{}, 字符.in...) 写入 in :
		if got := selectionSort(in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                           // 把 false 写入 ok
			fmt.Printf("FAIL selectionSort(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
