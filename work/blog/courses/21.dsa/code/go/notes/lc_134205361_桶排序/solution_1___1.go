// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sort" // 「sort」
)

func getIndex(arr []int, k int) int { // 定义函数/方法 getIndex
	if len(arr) == 0 { // 若 长度(数组) 等于 0
		return -1 // 返回 减 1
	}
	minVal, maxVal := arr[0], arr[0] // 把 数组[0], 数组[0] 写入 minVal, maxVal :
	for _, num := range arr {        // 同时取 _ 与 num 遍历
		if num < minVal { // 若 num 小于 minVal
			minVal = num // 把 num 写入 minVal
		}
		if num > maxVal { // 若 num 超过 maxVal
			maxVal = num // 把 num 写入 maxVal
		}
	}
	bucketSize := (maxVal-minVal)/len(arr) + 1 // 把 (maxVal 减 minVal) 除以 长度(数组) 加 1 写入 bucketSize :
	if bucketSize < 1 {                        // 若 bucketSize 小于 1
		bucketSize = 1 // 把 1 写入 bucketSize
	}
	bucketCount := (maxVal-minVal)/bucketSize + 1 // 把 (maxVal 减 minVal) 除以 bucketSize 加 1 写入 bucketCount :
	buckets := make([][]int, bucketCount)         // 把 make([][]int, bucketCount) 写入 buckets :
	for _, num := range arr {                     // 同时取 _ 与 num 遍历
		idx := (num - minVal) / bucketSize       // 把 (num 减 minVal) 除以 bucketSize 写入 idx :
		buckets[idx] = append(buckets[idx], num) // 把 append(buckets[idx], num) 写入 buckets[idx]
	}
	for _, bucket := range buckets { // 同时取 _ 与 bucket 遍历
		sort.Ints(bucket) // sort.Ints(bucket)
	}
	for _, bucket := range buckets { // 同时取 _ 与 bucket 遍历
		for _, num := range bucket { // 同时取 _ 与 num 遍历
			k--         // 下标 k 减一
			if k == 0 { // 若 下标 k 等于 0
				return num // 返回 num
			}
		}
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		arr  []int // 数组 []int
		k    int   // 下标 k int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3}, 1, 1},
		{[]int{3, 1, 2}, 2, 2},
		{[]int{5, 4, 3, 2, 1}, 3, 3},
		{[]int{5, 4, 3, 2, 1}, 1, 1},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := getIndex(c.arr, c.k); got != c.want { // 若 got : 赋值为 getIndex(字符.数组, 字符.下标 k); got 不等于 字符.want
			ok = false                                                               // 把 false 写入 ok
			fmt.Printf("FAIL getIndex(%v,%d)=%d want %d\n", c.arr, c.k, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
