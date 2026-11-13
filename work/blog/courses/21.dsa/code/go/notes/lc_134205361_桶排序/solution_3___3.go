// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"math" // 「math」
	"os"   // 「os」
)

func bucketSort(arr []float64) { // 定义函数/方法 bucketSort
	n := len(arr) // 把 长度(数组) 写入 n :
	if n == 0 {   // 若 元素个数 等于 0
		return // return
	}
	minVal, maxVal := arr[0], arr[0] // 把 数组[0], 数组[0] 写入 minVal, maxVal :
	for _, v := range arr {          // 同时取 _ 与 值 遍历
		if v < minVal { // 若 值 小于 minVal
			minVal = v // 把 值 写入 minVal
		}
		if v > maxVal { // 若 值 超过 maxVal
			maxVal = v // 把 值 写入 maxVal
		}
	}
	if minVal == maxVal { // 若 minVal 等于 maxVal
		return // return
	}
	bucketCount := n                          // 把 元素个数 写入 bucketCount :
	buckets := make([][]float64, bucketCount) // 把 make([][]float64, bucketCount) 写入 buckets :
	for _, v := range arr {                   // 同时取 _ 与 值 遍历
		idx := int(math.Floor(float64(bucketCount-1) * (v - minVal) / (maxVal - minVal)))
		buckets[idx] = append(buckets[idx], v) // 把 append(buckets[idx], 值) 写入 buckets[idx]
	}
	pos := 0                           // 把 0 写入 pos :
	for i := 0; i < bucketCount; i++ { // 让 下标 i 从 0 开始计数
		b := buckets[i]               // 把 buckets[下标 i] 写入 b :
		for a := 1; a < len(b); a++ { // 让 数组 从 1 开始计数
			key := b[a]                // 把 b[数组] 写入 key :
			j := a - 1                 // 把 数组 减 1 写入 j :
			for j >= 0 && b[j] > key { // 把 0 且 b[下标 j] 超过 key { 写入 for j >
				b[j+1] = b[j] // 把 b[下标 j] 写入 b[j+1]
				j--           // 下标 j 减一
			}
			b[j+1] = key // 把 key 写入 b[j+1]
		}
		for _, v := range b { // 同时取 _ 与 值 遍历
			arr[pos] = v // 把 值 写入 arr[pos]
			pos++        // pos 加一
		}
	}
}

func main() { // 程序入口：跑内嵌自测用例
	want := []float64{0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52}
	arr := []float64{0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51}
	bucketSort(arr)            // bucketSort(数组)
	ok := true                 // 把 true 写入 ok :
	if len(arr) != len(want) { // 定义函数/方法 len
		ok = false                 // 把 false 写入 ok
		fmt.Println("FAIL length") // 打印输出
	}
	for i := range want { // 把 range want { 写入 for i :
		if i >= len(arr) || math.Abs(arr[i]-want[i]) > 1e-9 {
			ok = false                                            // 把 false 写入 ok
			fmt.Printf("FAIL bucketSort=%v want %v\n", arr, want) // 打印输出
			break                                                 // 跳出循环
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
