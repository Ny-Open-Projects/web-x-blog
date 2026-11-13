// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145588341
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func sortArrayByParity(nums []int) []int { // 定义函数/方法 sortArrayByParity
	left, right := 0, len(nums)-1 // 把 0, 长度(数组) 减 1 写入 left, right :
	for left < right {            // for 左边界 小于 右边界 {
		for left < right && nums[left]%2 == 0 { // 把 赋值为 0 { 写入 for left < right && nums[left]%2
			left++ // 左边界 加一
		}
		for left < right && nums[right]%2 == 1 { // 把 赋值为 1 { 写入 for left < right && nums[right]%2
			right-- // 右边界 减一
		}
		if left < right { // 若 左边界 小于 右边界
			nums[left], nums[right] = nums[right], nums[left] // 把 数组[右边界], 数组[左边界] 写入 nums[left], nums[right]
			left++                                            // 左边界 加一
			right--                                           // 右边界 减一
		}
	}
	return nums // 返回 数组
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3}, []int{2, 1, 3}},
		{[]int{3, 1, 2, 4}, []int{4, 2, 1, 3}},
		{[]int{}, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		in := append([]int{}, c.in...) // 把 append([]int{}, 字符.in...) 写入 in :
		if got := sortArrayByParity(in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                               // 把 false 写入 ok
			fmt.Printf("FAIL sortArrayByParity(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
