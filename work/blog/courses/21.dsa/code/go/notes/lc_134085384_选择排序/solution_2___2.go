// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func selectionSort(nums []int) { // 定义函数/方法 selectionSort
	length := len(nums)             // 把 长度(数组) 写入 length :
	for i := 0; i < length-1; i++ { // 让 下标 i 从 0 开始计数
		minIndex := i                     // 把 下标 i 写入 minIndex :
		for j := i + 1; j < length; j++ { // 把 下标 i 加 1; 下标 j 小于 长度; 下标 j 加一 { 写入 for j :
			if nums[j] < nums[minIndex] { // 若 数组[下标 j] 小于 数组[minIndex]
				minIndex = j // 把 下标 j 写入 minIndex
			}
		}
		if i != minIndex { // 若 下标 i 不等于 minIndex
			nums[i], nums[minIndex] = nums[minIndex], nums[i] // 把 数组[minIndex], 数组[下标 i] 写入 nums[i], nums[minIndex]
		}
	}
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{1, 2, 3}, []int{1, 2, 3}},
		{[]int{2, 1}, []int{1, 2}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		in := append([]int{}, c.in...)      // 把 append([]int{}, 字符.in...) 写入 in :
		selectionSort(in)                   // selectionSort(in)
		if !reflect.DeepEqual(in, c.want) { // 若 取反 reflect.DeepEqual(in, 字符.want
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL selectionSort(%v)=%v want %v\n", c.in, in, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
