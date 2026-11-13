// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func insertionSort(arr []int) []int { // 定义函数/方法 insertionSort
	for i := 1; i < len(arr); i++ { // 让 下标 i 从 1 开始计数
		key := arr[i]                // 把 数组[下标 i] 写入 key :
		j := i - 1                   // 把 下标 i 减 1 写入 j :
		for j >= 0 && arr[j] > key { // 把 0 且 数组[下标 j] 超过 key { 写入 for j >
			arr[j+1] = arr[j] // 把 数组[下标 j] 写入 arr[j+1]
			j--               // 下标 j 减一
		}
		arr[j+1] = key // 把 key 写入 arr[j+1]
	}
	return arr // 返回 数组
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                          // 把 true 写入 ok :
	in := []int{3, 1, 4, 1, 5, 9, 2, 6} // 把 []int{3, 1, 4, 1, 5, 9, 2, 6} 写入 in :
	if got := insertionSort(append([]int{}, in...)); !reflect.DeepEqual(got, []int{1, 1, 2, 3, 4, 5, 6, 9}) {
		ok = false                                 // 把 false 写入 ok
		fmt.Printf("FAIL insertionSort=%v\n", got) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
