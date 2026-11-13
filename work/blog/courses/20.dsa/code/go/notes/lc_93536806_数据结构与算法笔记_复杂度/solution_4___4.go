// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func partition(arr []int, left, right int) int { // 定义函数/方法 partition
	pivot := arr[right]             // 把 数组[右边界] 写入 pivot :
	i := left                       // 把 左边界 写入 i :
	for j := left; j < right; j++ { // 把 左边界; 下标 j 小于 右边界; 下标 j 加一 { 写入 for j :
		if arr[j] < pivot { // 若 数组[下标 j] 小于 pivot
			arr[i], arr[j] = arr[j], arr[i] // 把 数组[下标 j], 数组[下标 i] 写入 arr[i], arr[j]
			i++                             // 下标 i 加一
		}
	}
	arr[i], arr[right] = arr[right], arr[i] // 把 数组[右边界], 数组[下标 i] 写入 arr[i], arr[right]
	return i                                // 返回 下标 i
}

func quickSort(arr []int, left, right int) { // 定义函数/方法 quickSort
	if left < right { // 若 左边界 小于 右边界
		p := partition(arr, left, right) // 把 partition(数组, 左边界, 右边界) 写入 p :
		quickSort(arr, left, p-1)        // quickSort(数组, 左边界, 节点 减 1)
		quickSort(arr, p+1, right)       // quickSort(数组, 节点 加 1, 右边界)
	}
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                                                // 把 true 写入 ok :
	in := []int{3, 1, 4, 1, 5, 9, 2, 6}                       // 把 []int{3, 1, 4, 1, 5, 9, 2, 6} 写入 in :
	q := append([]int{}, in...)                               // 把 append([]int{}, in...) 写入 q :
	quickSort(q, 0, len(q)-1)                                 // quickSort(节点, 0, 长度(节点) 减 1)
	if !reflect.DeepEqual(q, []int{1, 1, 2, 3, 4, 5, 6, 9}) { // 若 取反 reflect.DeepEqual(节点, []int{1, 1, 2, 3, 4, 5, 6, 9}
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL quickSort=%v\n", q) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
