// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func mergeSort(nums []int) { // 定义函数/方法 mergeSort
	var msFn func([]int) []int     // var msFn func([]int) []int
	msFn = func(arr []int) []int { // 把 func(数组 []int) []int { 写入 msFn
		if len(arr) < 2 { // 若 长度(数组) 小于 2
			return arr // 返回 数组
		}
		mid := len(arr) / 2                   // 把 长度(数组) 除以 2 写入 mid :
		left := msFn(arr[:mid])               // 把 msFn(数组[:中点]) 写入 left :
		right := msFn(arr[mid:])              // 把 msFn(数组[中点:]) 写入 right :
		res := []int{}                        // 把 []int{} 写入 res :
		i, j := 0, 0                          // 把 0, 0 写入 i, j :
		for i < len(left) && j < len(right) { // for 下标 i 小于 长度(左边界) 且 下标 j 小于 长度(右边界) {
			if left[i] <= right[j] { // 若 左边界[下标 i] 不超过 右边界[下标 j]
				res = append(res, left[i]) // 把 append(结果, 左边界[下标 i]) 写入 结果
				i++                        // 下标 i 加一
			} else { // 否则
				res = append(res, right[j]) // 把 append(结果, 右边界[下标 j]) 写入 结果
				j++                         // 下标 j 加一
			}
		}
		res = append(res, left[i:]...)  // 把 append(结果, 左边界[下标 i:]...) 写入 结果
		res = append(res, right[j:]...) // 把 append(结果, 右边界[下标 j:]...) 写入 结果
		return res                      // 返回 结果
	}
	r := msFn(nums) // 把 msFn(数组) 写入 r :
	copy(nums, r)   // copy(数组, 右指针)
}

func main() { // 程序入口：跑内嵌自测用例
	testList := []int{5, 4, 3, 2, 1}                        // 把 []int{5, 4, 3, 2, 1} 写入 testList :
	mergeSort(testList)                                     // mergeSort(testList)
	if !reflect.DeepEqual(testList, []int{1, 2, 3, 4, 5}) { // 若 取反 reflect.DeepEqual(testList, []int{1, 2, 3, 4, 5}
		fmt.Printf("FAIL=%v\n", testList) // 打印输出
		os.Exit(1)                        // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
