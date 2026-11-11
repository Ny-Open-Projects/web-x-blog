// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
	"sort"
) // 引入依赖

func intersect(nums1, nums2 []int) []int { // 定义函数/方法 intersect
	sort.Ints(nums1)                       // sort.Ints(数组1)
	sort.Ints(nums2)                       // sort.Ints(数组2)
	res := []int{}                         // 把 []int{} 写入 res :
	i, j := 0, 0                           // 把 0, 0 写入 i, j :
	for i < len(nums1) && j < len(nums2) { // for 下标 i 小于 长度(数组1) 且 下标 j 小于 长度(数组2) {
		if nums1[i] < nums2[j] { // 若 数组1[下标 i] 小于 数组2[下标 j]
			i++ // 下标 i 加一
		} else if nums1[i] > nums2[j] { // 否则，若 数组1[下标 i] 超过 数组2[下标 j]
			j++ // 下标 j 加一
		} else { // 否则
			res = append(res, nums1[i]) // 把 append(结果, 数组1[下标 i]) 写入 结果
			i++                         // 下标 i 加一
			j++                         // 下标 j 加一
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		a, b []int // 数组, b []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 2, 1}, []int{2, 2}, []int{2, 2}},
		{[]int{3, 1, 2}, []int{1, 1}, []int{1}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := intersect(c.a, c.b); !reflect.DeepEqual(got, c.want) {
			ok = false                                                              // 把 false 写入 ok
			fmt.Printf("FAIL intersect(%v,%v)=%v want %v\n", c.a, c.b, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
