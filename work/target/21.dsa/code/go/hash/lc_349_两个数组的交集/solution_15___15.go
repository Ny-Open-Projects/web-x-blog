// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133279737
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sort" // 「sort」
)

func intersection(nums1, nums2 []int) []int { // 定义函数/方法 intersection
	s1 := make(map[int]bool)  // 把 make(映射表[int]bool) 写入 s1 :
	for _, v := range nums1 { // 同时取 _ 与 值 遍历
		s1[v] = true // 把 true 写入 s1[v]
	}
	var res []int              // var 结果 []int
	seen := make(map[int]bool) // 把 make(映射表[int]bool) 写入 seen :
	for _, v := range nums2 {  // 同时取 _ 与 值 遍历
		if s1[v] && !seen[v] { // 若 s1[值] 且 取反 已见集合[值]
			res = append(res, v) // 把 append(结果, 值) 写入 结果
			seen[v] = true       // 把 true 写入 seen[v]
		}
	}
	return res // 返回 结果
}

func eqIntSlice(a, b []int, sortRes bool) bool { // 定义函数/方法 eqIntSlice
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	if sortRes { // 若 sortRes
		sa := append([]int{}, a...) // 把 append([]int{}, 数组...) 写入 sa :
		sb := append([]int{}, b...) // 把 append([]int{}, b...) 写入 sb :
		sort.Ints(sa)               // sort.Ints(sa)
		sort.Ints(sb)               // sort.Ints(sb)
		a, b = sa, sb               // 把 sa, sb 写入 a, b
	}
	for i := range a { // 把 range 数组 { 写入 for i :
		if a[i] != b[i] { // 若 数组[下标 i] 不等于 b[下标 i]
			return false // 返回 false
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		nums1 []int // 数组1 []int
		nums2 []int // 数组2 []int
		want  []int // want []int
	}{ // }{
		{[]int{1, 2, 2, 1}, []int{2, 2}, []int{2}},
		{[]int{4, 9, 5}, []int{9, 4, 9, 8, 4}, []int{9, 4}},
		{[]int{1, 2}, []int{3, 4}, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := intersection(c.nums1, c.nums2) // 把 intersection(字符.数组1, 字符.数组2) 写入 got :
		if !eqIntSlice(got, c.want, true) {   // 若 取反 eqIntSlice(got, 字符.want, true
			fmt.Printf("FAIL nums1=%v nums2=%v want=%v got=%v\n", c.nums1, c.nums2, c.want, got) // 打印输出
			ok = false                                                                           // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("RESULT: FAIL") // 打印输出
		os.Exit(1)                  // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
