// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// mergeSort 递归归并排序（忠实翻译 Python 参考）
func mergeSort(nums []int) []int { // 定义函数/方法 mergeSort
	if len(nums) <= 1 { // 若 长度(数组) 不超过 1
		return nums // 返回 数组
	}
	mid := len(nums) / 2           // 把 长度(数组) 除以 2 写入 mid :
	left := mergeSort(nums[:mid])  // 把 mergeSort(数组[:中点]) 写入 left :
	right := mergeSort(nums[mid:]) // 把 mergeSort(数组[中点:]) 写入 right :
	return merge(left, right)      // 定义函数/方法 merge
}

func merge(left, right []int) []int { // 定义函数/方法 merge
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

func main() { // 程序入口：跑内嵌自测用例
	// 忠实复刻参考：print(mergeSort([1, 2, 3]))
	ref := mergeSort([]int{1, 2, 3})             // 把 mergeSort([]int{1, 2, 3}) 写入 ref :
	if !reflect.DeepEqual(ref, []int{1, 2, 3}) { // 若 取反 reflect.DeepEqual(ref, []int{1, 2, 3}
		fmt.Printf("FAIL ref=%v\n", ref) // 打印输出
		os.Exit(1)                       // os.Exit(1)
	}
	// 正确性校验
	if !reflect.DeepEqual(mergeSort([]int{5, 4, 3, 2, 1}), []int{1, 2, 3, 4, 5}) {
		fmt.Println("FAIL correctness") // 打印输出
		os.Exit(1)                      // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
