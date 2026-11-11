// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func mergeSort(nums []int) { // 定义函数/方法 mergeSort
	var msFn func([]int, int, int)            // var msFn func([]int, int, int)
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

func merge(arr []int, left, mid, right int) { // 定义函数/方法 merge
	temp := []int{}              // 把 []int{} 写入 temp :
	i, j := left, mid+1          // 把 左边界, 中点 加 1 写入 i, j :
	for i <= mid && j <= right { // 把 中点 且 下标 j 不超过 右边界 { 写入 for i <
		if arr[i] <= arr[j] { // 若 数组[下标 i] 不超过 数组[下标 j]
			temp = append(temp, arr[i]) // 把 append(临时变量, 数组[下标 i]) 写入 临时变量
			i++                         // 下标 i 加一
		} else { // 否则
			temp = append(temp, arr[j]) // 把 append(临时变量, 数组[下标 j]) 写入 临时变量
			j++                         // 下标 j 加一
		}
	}
	temp = append(temp, arr[i:mid+1]...)   // 把 append(临时变量, 数组[下标 i:中点 加 1]...) 写入 临时变量
	temp = append(temp, arr[j:right+1]...) // 把 append(临时变量, 数组[下标 j:右边界 加 1]...) 写入 临时变量
	for k := 0; k < len(temp); k++ {       // 让 下标 k 从 0 开始计数
		arr[left+k] = temp[k] // 把 临时变量[下标 k] 写入 arr[left+k]
	}
}

func main() { // 程序入口：跑内嵌自测用例
	nums := []int{5, 4, 3, 2, 1}                        // 把 []int{5, 4, 3, 2, 1} 写入 nums :
	mergeSort(nums)                                     // mergeSort(数组)
	if !reflect.DeepEqual(nums, []int{1, 2, 3, 4, 5}) { // 若 取反 reflect.DeepEqual(数组, []int{1, 2, 3, 4, 5}
		fmt.Printf("FAIL=%v\n", nums) // 打印输出
		os.Exit(1)                    // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
