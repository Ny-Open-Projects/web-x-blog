// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func shellSort(nums []int) []int { // 定义函数/方法 shellSort
	n := len(nums) // 把 长度(数组) 写入 n :
	gap := n / 2   // 把 元素个数 除以 2 写入 gap :
	for gap > 0 {  // for gap 超过 0 {
		for i := gap; i < n; i++ { // 把 gap; 下标 i 小于 元素个数; 下标 i 加一 { 写入 for i :
			temp := nums[i]                      // 把 数组[下标 i] 写入 temp :
			j := i                               // 把 下标 i 写入 j :
			for j >= gap && nums[j-gap] > temp { // 把 gap 且 数组[下标 j 减 gap] 超过 临时变量 { 写入 for j >
				nums[j] = nums[j-gap] // 把 数组[下标 j 减 gap] 写入 nums[j]
				j -= gap              // 下标 j累减 gap
			}
			nums[j] = temp // 把 临时变量 写入 nums[j]
		}
		gap /= 2 // 把 2 写入 gap /
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
		in := append([]int{}, c.in...)                             // 把 append([]int{}, 字符.in...) 写入 in :
		if got := shellSort(in); !reflect.DeepEqual(got, c.want) { // 若 got : 赋值为 shellSort(in); 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL shellSort(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
