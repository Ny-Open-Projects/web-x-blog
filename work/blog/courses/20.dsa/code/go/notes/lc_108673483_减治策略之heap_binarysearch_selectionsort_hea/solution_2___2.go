// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

// quickSelect 快速选择：返回 arr 中第 k 小元素（k 为 0-based 索引），平均 O(n)
func quickSelect(arr []int, k int) int { // 定义函数/方法 quickSelect
	a := make([]int, len(arr))          // 把 make([]int, 长度(数组)) 写入 a :
	copy(a, arr)                        // copy(数组, 数组)
	var selectK func(lo, hi, k int) int // var selectK func(左边界, 右边界, 下标 k int) int
	selectK = func(lo, hi, k int) int { // 把 func(左边界, 右边界, 下标 k int) int { 写入 selectK
		if lo == hi { // 若 左边界 等于 右边界
			return a[lo] // 返回 数组[左边界]
		}
		pivot := a[hi]             // 把 数组[右边界] 写入 pivot :
		i := lo                    // 把 左边界 写入 i :
		for j := lo; j < hi; j++ { // 把 左边界; 下标 j 小于 右边界; 下标 j 加一 { 写入 for j :
			if a[j] <= pivot { // 若 数组[下标 j] 不超过 pivot
				a[i], a[j] = a[j], a[i] // 把 数组[下标 j], 数组[下标 i] 写入 a[i], a[j]
				i++                     // 下标 i 加一
			}
		}
		a[i], a[hi] = a[hi], a[i] // 把 数组[右边界], 数组[下标 i] 写入 a[i], a[hi]
		if i == k {               // 若 下标 i 等于 下标 k
			return a[i] // 返回 数组[下标 i]
		} else if i > k { // 否则，若 下标 i 超过 下标 k
			return selectK(lo, i-1, k) // 定义函数/方法 selectK
		}
		return selectK(i+1, hi, k) // 定义函数/方法 selectK
	}
	return selectK(0, len(a)-1, k) // 定义函数/方法 selectK
}

func main() { // 程序入口：跑内嵌自测用例
	arr := []int{3, 1, 4, 1, 5, 9, 2, 6} // 把 []int{3, 1, 4, 1, 5, 9, 2, 6} 写入 arr :
	if quickSelect(arr, 2) != 2 {        // 若 quickSelect(数组, 2) 不等于 2
		fmt.Println("FAIL quickSelect 2nd") // 打印输出
		os.Exit(1)                          // os.Exit(1)
	}
	if quickSelect(arr, 3) != 3 { // 若 quickSelect(数组, 3) 不等于 3
		fmt.Println("FAIL quickSelect 3rd") // 打印输出
		os.Exit(1)                          // os.Exit(1)
	}
	s := make([]int, len(arr))                                // 把 make([]int, 长度(数组)) 写入 s :
	copy(s, arr)                                              // copy(字符串, 数组)
	sort.Ints(s)                                              // sort.Ints(字符串)
	if !reflect.DeepEqual(s, []int{1, 1, 2, 3, 4, 5, 6, 9}) { // 若 取反 reflect.DeepEqual(字符串, []int{1, 1, 2, 3, 4, 5, 6, 9}
		fmt.Printf("FAIL sorted=%v\n", s) // 打印输出
		os.Exit(1)                        // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
