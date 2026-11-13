// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133322239
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sort" // 「sort」
)

func twoSum(nums []int, target int) []int { // 定义函数/方法 twoSum
	n := len(nums)           // 把 长度(数组) 写入 n :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		for j := i + 1; j < n; j++ { // 把 下标 i 加 1; 下标 j 小于 元素个数; 下标 j 加一 { 写入 for j :
			if nums[i]+nums[j] == target { // 若 数组[下标 i] 加 数组[下标 j] 等于 目标值
				return []int{i, j} // 返回 []int{下标 i, 下标 j}
			}
		}
	}
	return []int{} // 返回 []int{}
}

func eqIntSlice(a, b []int) bool { // 定义函数/方法 eqIntSlice
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	for i := range a { // 把 range 数组 { 写入 for i :
		if a[i] != b[i] { // 若 数组[下标 i] 不等于 b[下标 i]
			return false // 返回 false
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums   []int // 数组 []int
		target int   // 目标值 int
		want   []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
	}
	fail := false             // 把 false 写入 fail :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := twoSum(c.nums, c.target) // 把 twoSum(字符.数组, 字符.目标值) 写入 got :
		g := append([]int{}, got...)    // 把 append([]int{}, got...) 写入 g :
		w := append([]int{}, c.want...) // 把 append([]int{}, 字符.want...) 写入 w :
		sort.Ints(g)                    // sort.Ints(g)
		sort.Ints(w)                    // sort.Ints(权重)
		if !eqIntSlice(g, w) {          // 若 取反 eqIntSlice(g, 权重
			fmt.Printf("FAIL twoSum(%v,%d)=%v want %v\n", c.nums, c.target, got, c.want) // 打印输出
			fail = true                                                                  // 把 true 写入 fail
		}
	}
	if fail { // 若 fail
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
