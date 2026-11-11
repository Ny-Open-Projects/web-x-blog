// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func mergeSort(arr []int) []int { // 定义函数/方法 mergeSort
	if len(arr) <= 1 { // 若 长度(数组) 不超过 1
		return arr // 返回 数组
	}
	mid := len(arr) / 2           // 把 长度(数组) 除以 2 写入 mid :
	left := mergeSort(arr[:mid])  // 把 mergeSort(数组[:中点]) 写入 left :
	right := mergeSort(arr[mid:]) // 把 mergeSort(数组[中点:]) 写入 right :
	return merge(left, right)     // 定义函数/方法 merge
}

func merge(left, right []int) []int { // 定义函数/方法 merge
	result := []int{}                     // 把 []int{} 写入 result :
	i, j := 0, 0                          // 把 0, 0 写入 i, j :
	for i < len(left) && j < len(right) { // for 下标 i 小于 长度(左边界) 且 下标 j 小于 长度(右边界) {
		if left[i] <= right[j] { // 若 左边界[下标 i] 不超过 右边界[下标 j]
			result = append(result, left[i]) // 把 append(结果, 左边界[下标 i]) 写入 结果
			i++                              // 下标 i 加一
		} else { // 否则
			result = append(result, right[j]) // 把 append(结果, 右边界[下标 j]) 写入 结果
			j++                               // 下标 j 加一
		}
	}
	result = append(result, left[i:]...)  // 把 append(结果, 左边界[下标 i:]...) 写入 结果
	result = append(result, right[j:]...) // 把 append(结果, 右边界[下标 j:]...) 写入 结果
	return result                         // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                          // 把 true 写入 ok :
	in := []int{3, 1, 4, 1, 5, 9, 2, 6} // 把 []int{3, 1, 4, 1, 5, 9, 2, 6} 写入 in :
	if got := mergeSort(append([]int{}, in...)); !reflect.DeepEqual(got, []int{1, 1, 2, 3, 4, 5, 6, 9}) {
		ok = false                             // 把 false 写入 ok
		fmt.Printf("FAIL mergeSort=%v\n", got) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
