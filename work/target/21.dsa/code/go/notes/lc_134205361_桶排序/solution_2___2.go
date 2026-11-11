// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func bucketSort(lst []int, n int) []int { // 定义函数/方法 bucketSort
	if len(lst) < 2 { // 若 长度(lst) 小于 2
		return lst // 返回 lst
	}
	maxVal, minVal := lst[0], lst[0] // 把 lst[0], lst[0] 写入 maxVal, minVal :
	for _, v := range lst {          // 同时取 _ 与 值 遍历
		if v > maxVal { // 若 值 超过 maxVal
			maxVal = v // 把 值 写入 maxVal
		}
		if v < minVal { // 若 值 小于 minVal
			minVal = v // 把 值 写入 minVal
		}
	}
	dist := maxVal - minVal // 把 maxVal 减 minVal 写入 dist :
	if dist == 0 {          // 若 dist 等于 0
		return lst // 返回 lst
	}
	buckets := make([][]int, n) // 把 make([][]int, 元素个数) 写入 buckets :
	width := (dist + 1) / n     // 把 (dist 加 1) 除以 元素个数 写入 width :
	for _, cur := range lst {   // 同时取 _ 与 当前值 遍历
		index := (cur - minVal) / width // 把 (当前值 减 minVal) 除以 width 写入 index :
		if index >= n {                 // 若 index 不低于 元素个数
			index = n - 1 // 把 元素个数 减 1 写入 index
		}
		buckets[index] = append(buckets[index], cur) // 把 append(buckets[index], 当前值) 写入 buckets[index]
	}
	for _, b := range buckets { // 同时取 _ 与 b 遍历
		sort.Ints(b) // sort.Ints(b)
	}
	result := []int{}           // 把 []int{} 写入 result :
	for _, b := range buckets { // 同时取 _ 与 b 遍历
		result = append(result, b...) // 把 append(结果, b...) 写入 结果
	}
	return result // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		n    int   // 元素个数 int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{5, 4, 3, 2, 1}, 5, []int{1, 2, 3, 4, 5}},
		{[]int{5, 4, 3, 2, 1}, 2, []int{1, 2, 3, 4, 5}},
		{[]int{1, 2, 3, 4, 5}, 5, []int{1, 2, 3, 4, 5}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := bucketSort(c.in, c.n); !reflect.DeepEqual(got, c.want) {
			ok = false                                                                // 把 false 写入 ok
			fmt.Printf("FAIL bucketSort(%v,%d)=%v want %v\n", c.in, c.n, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
