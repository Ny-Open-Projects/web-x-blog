// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func bubbleSort(arr []int) []int { // 定义函数/方法 bubbleSort
	n := len(arr)            // 把 长度(数组) 写入 n :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		for j := 0; j < n-i-1; j++ { // 让 下标 j 从 0 开始计数
			if arr[j] > arr[j+1] { // 若 数组[下标 j] 超过 数组[下标 j 加 1]
				arr[j], arr[j+1] = arr[j+1], arr[j] // 把 数组[下标 j 加 1], 数组[下标 j] 写入 arr[j], arr[j+1]
			}
		}
	}
	return arr // 返回 数组
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                          // 把 true 写入 ok :
	in := []int{3, 1, 4, 1, 5, 9, 2, 6} // 把 []int{3, 1, 4, 1, 5, 9, 2, 6} 写入 in :
	if got := bubbleSort(append([]int{}, in...)); !reflect.DeepEqual(got, []int{1, 1, 2, 3, 4, 5, 6, 9}) {
		ok = false                              // 把 false 写入 ok
		fmt.Printf("FAIL bubbleSort=%v\n", got) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
