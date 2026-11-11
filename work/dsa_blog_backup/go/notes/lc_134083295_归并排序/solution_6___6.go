// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func mergeSortInPlace(nums []int) { // 定义函数/方法 mergeSortInPlace
	var msFn func(arr []int, left, right int)       // var msFn func(数组 []int, 左边界, 右边界 int)
	var merge func(arr []int, left, mid, right int) // var merge func(数组 []int, 左边界, 中点, 右边界 int)
	merge = func(arr []int, left, mid, right int) { // 把 func(数组 []int, 左边界, 中点, 右边界 int) { 写入 merge
		temp := make([]int, right-left+1) // 把 make([]int, 右边界 减 左边界 加 1) 写入 temp :
		i, j, k := left, mid+1, 0         // 把 左边界, 中点 加 1, 0 写入 i, j, k :
		for i <= mid && j <= right {      // 把 中点 且 下标 j 不超过 右边界 { 写入 for i <
			if arr[i] <= arr[j] { // 若 数组[下标 i] 不超过 数组[下标 j]
				temp[k] = arr[i] // 把 数组[下标 i] 写入 temp[k]
				i++              // 下标 i 加一
			} else { // 否则
				temp[k] = arr[j] // 把 数组[下标 j] 写入 temp[k]
				j++              // 下标 j 加一
			}
			k++ // 下标 k 加一
		}
		for i <= mid { // 把 中点 { 写入 for i <
			temp[k] = arr[i] // 把 数组[下标 i] 写入 temp[k]
			i++              // 下标 i 加一
			k++              // 下标 k 加一
		}
		for j <= right { // 把 右边界 { 写入 for j <
			temp[k] = arr[j] // 把 数组[下标 j] 写入 temp[k]
			j++              // 下标 j 加一
			k++              // 下标 k 加一
		}
		for idx := 0; idx < len(temp); idx++ { // 让 idx 从 0 开始计数
			arr[left+idx] = temp[idx] // 把 临时变量[idx] 写入 arr[left+idx]
		}
	}
	msFn = func(arr []int, left, right int) { // 把 func(数组 []int, 左边界, 右边界 int) { 写入 msFn
		if left >= right { // 若 左边界 不低于 右边界
			return // return
		}
		mid := (left + right) / 2    // 把 (左边界 加 右边界) 除以 2 写入 mid :
		msFn(arr, left, mid)         // msFn(数组, 左边界, 中点)
		msFn(arr, mid+1, right)      // msFn(数组, 中点 加 1, 右边界)
		merge(arr, left, mid, right) // merge(数组, 左边界, 中点, 右边界)
	}
	msFn(nums, 0, len(nums)-1) // msFn(数组, 0, 长度(数组) 减 1)
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{1, 2, 3}, []int{1, 2, 3}},
		{[]int{3}, []int{3}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		in := append([]int{}, c.in...)      // 把 append([]int{}, 字符.in...) 写入 in :
		mergeSortInPlace(in)                // mergeSortInPlace(in)
		if !reflect.DeepEqual(in, c.want) { // 若 取反 reflect.DeepEqual(in, 字符.want
			ok = false                                                             // 把 false 写入 ok
			fmt.Printf("FAIL mergeSortInPlace(%v)=%v want %v\n", c.in, in, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
