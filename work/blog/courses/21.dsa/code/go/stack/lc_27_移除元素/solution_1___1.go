// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func removeElement(nums []int, val int) int { // 定义函数/方法 removeElement
	left := 0                                    // 把 0 写入 left :
	for right := 0; right < len(nums); right++ { // 让 右边界 从 0 开始计数
		if nums[right] != val { // 若 数组[右边界] 不等于 值
			nums[left] = nums[right] // 把 数组[右边界] 写入 nums[left]
			left++                   // 左边界 加一
		}
	}
	return left // 返回 左边界
}

func check(nums []int, k int, wantK int, wantSorted []int) bool { // 定义判定函数 check
	if k != wantK { // 若 下标 k 不等于 wantK
		return false // 返回 false
	}
	got := append([]int{}, nums[:k]...)       // 把 append([]int{}, 数组[:下标 k]...) 写入 got :
	sort.Ints(got)                            // sort.Ints(got)
	return reflect.DeepEqual(got, wantSorted) // 返回 reflect.DeepEqual(got, wantSorted)
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true       // 把 true 写入 ok :
	type tc struct { // 定义类型
		in    []int // in []int
		val   int   // 值 int
		wantK int   // wantK int
		want  []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{3, 2, 2, 3}, 3, 2, []int{2, 2}},
		{[]int{0, 1, 2, 2, 3, 0, 4, 2}, 2, 5, []int{0, 0, 1, 3, 4}},
		{[]int{2}, 2, 0, []int{}},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		nums := append([]int{}, c.in...)      // 把 append([]int{}, 字符.in...) 写入 nums :
		k := removeElement(nums, c.val)       // 把 removeElement(数组, 字符.值) 写入 k :
		if !check(nums, k, c.wantK, c.want) { // 若 取反 check(数组, 下标 k, 字符.wantK, 字符.want
			ok = false                                                                                                         // 把 false 写入 ok
			fmt.Printf("FAIL removeElement(%v,%d) k=%d nums[:k]=%v want k=%d %v\n", c.in, c.val, k, nums[:k], c.wantK, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
