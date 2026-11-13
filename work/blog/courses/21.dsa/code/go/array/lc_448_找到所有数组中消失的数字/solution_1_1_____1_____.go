package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 找到所有数组中消失的数字
// 忠实翻译 Python ref_findDisappearedNumbers: 用集合标记后按顺序收集 1..n 中缺失者
func findDisappearedNumbers(nums []int) []int { // 定义函数/方法 findDisappearedNumbers
	s := make(map[int]bool)  // 把 make(映射表[int]bool) 写入 s :
	for _, v := range nums { // 同时取 _ 与 值 遍历
		s[v] = true // 把 true 写入 s[v]
	}
	res := []int{}                    // 把 []int{} 写入 res :
	for i := 1; i <= len(nums); i++ { // 让 下标 i 从 1 开始计数
		if !s[i] { // 若 取反 字符串[下标 i]
			res = append(res, i) // 把 append(结果, 下标 i) 写入 结果
		}
	}
	return res // 返回 结果
}

func eq(a, b []int) bool { // 定义函数/方法 eq
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	for i := range a { // 把 range 数组 { 写入 for i :
		if a[i] != b[i] { // 若 数组[下标 i] 不等于 b[下标 i]
			return false // 返回 false
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums []int // 数组 []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{4, 3, 2, 7, 8, 2, 3, 1}, []int{5, 6}},
		{[]int{1, 1}, []int{2}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := findDisappearedNumbers(c.nums) // 把 findDisappearedNumbers(字符.数组) 写入 got :
		if !eq(got, c.want) {                 // 若 取反 eq(got, 字符.want
			fmt.Printf("FAIL: findDisappearedNumbers(%v)=%v want %v\n", c.nums, got, c.want) // 打印输出
			ok = false                                                                       // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("FAIL") // 打印输出
		os.Exit(1)          // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
