// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func heapSort(arr []int) []int { // 定义函数/方法 heapSort
	n := len(arr)                    // 把 长度(数组) 写入 n :
	var heapify func(size, root int) // var heapify func(大小, 根节点 int)
	heapify = func(size, root int) { // 把 func(大小, 根节点 int) { 写入 heapify
		largest := root                              // 把 根节点 写入 largest :
		left := 2*root + 1                           // 把 2 乘 根节点 加 1 写入 left :
		right := 2*root + 2                          // 把 2 乘 根节点 加 2 写入 right :
		if left < size && arr[left] > arr[largest] { // 若 左边界 小于 大小 且 数组[左边界] 超过 数组[largest]
			largest = left // 把 左边界 写入 largest
		}
		if right < size && arr[right] > arr[largest] { // 若 右边界 小于 大小 且 数组[右边界] 超过 数组[largest]
			largest = right // 把 右边界 写入 largest
		}
		if largest != root { // 若 largest 不等于 根节点
			arr[root], arr[largest] = arr[largest], arr[root] // 把 数组[largest], 数组[根节点] 写入 arr[root], arr[largest]
			heapify(size, largest)                            // heapify(大小, largest)
		}
	}
	for i := n/2 - 1; i >= 0; i-- { // 把 元素个数 除以 2 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		heapify(n, i) // heapify(元素个数, 下标 i)
	}
	for i := n - 1; i > 0; i-- { // 把 元素个数 减 1; 下标 i 超过 0; 下标 i 减一 { 写入 for i :
		arr[0], arr[i] = arr[i], arr[0] // 把 数组[下标 i], 数组[0] 写入 arr[0], arr[i]
		heapify(i, 0)                   // heapify(下标 i, 0)
	}
	return arr // 返回 数组
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                          // 把 true 写入 ok :
	in := []int{3, 1, 4, 1, 5, 9, 2, 6} // 把 []int{3, 1, 4, 1, 5, 9, 2, 6} 写入 in :
	if got := heapSort(append([]int{}, in...)); !reflect.DeepEqual(got, []int{1, 1, 2, 3, 4, 5, 6, 9}) {
		ok = false                            // 把 false 写入 ok
		fmt.Printf("FAIL heapSort=%v\n", got) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
