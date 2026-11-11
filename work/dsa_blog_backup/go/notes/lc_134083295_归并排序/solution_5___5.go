// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func mergeSort(nums []int) []int { // 定义函数/方法 mergeSort
	var msFn func(arr []int) []int // var msFn func(数组 []int) []int
	msFn = func(arr []int) []int { // 把 func(数组 []int) []int { 写入 msFn
		n := len(arr) // 把 长度(数组) 写入 n :
		if n < 2 {    // 若 元素个数 小于 2
			return arr // 返回 数组
		}
		mid := n / 2                                    // 把 元素个数 除以 2 写入 mid :
		left := append([]int{}, arr[:mid]...)           // 把 append([]int{}, 数组[:中点]...) 写入 left :
		right := append([]int{}, arr[mid:]...)          // 把 append([]int{}, 数组[中点:]...) 写入 right :
		orderLeft := msFn(left)                         // 把 msFn(左边界) 写入 orderLeft :
		orderRight := msFn(right)                       // 把 msFn(右边界) 写入 orderRight :
		res := []int{}                                  // 把 []int{} 写入 res :
		for len(orderLeft) > 0 && len(orderRight) > 0 { // for 长度(orderLeft) 超过 0 且 长度(orderRight) 超过 0 {
			if orderLeft[0] <= orderRight[0] { // 若 orderLeft[0] 不超过 orderRight[0]
				res = append(res, orderLeft[0]) // 把 append(结果, orderLeft[0]) 写入 结果
				orderLeft = orderLeft[1:]       // 把 orderLeft[1:] 写入 orderLeft
			} else { // 否则
				res = append(res, orderRight[0]) // 把 append(结果, orderRight[0]) 写入 结果
				orderRight = orderRight[1:]      // 把 orderRight[1:] 写入 orderRight
			}
		}
		res = append(res, orderLeft...)  // 把 append(结果, orderLeft...) 写入 结果
		res = append(res, orderRight...) // 把 append(结果, orderRight...) 写入 结果
		return res                       // 返回 结果
	}
	return msFn(nums) // 定义函数/方法 msFn
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{1, 2, 3}, []int{1, 2, 3}},
		{[]int{}, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := mergeSort(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL mergeSort(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
