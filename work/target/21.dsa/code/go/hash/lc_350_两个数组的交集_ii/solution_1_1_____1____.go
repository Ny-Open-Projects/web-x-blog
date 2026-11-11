// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

func intersect(nums1, nums2 []int) []int { // 定义函数/方法 intersect
	if len(nums1) > len(nums2) { // 定义函数/方法 len
		return intersect(nums2, nums1) // 定义函数/方法 intersect
	}
	mp := map[int]int{}         // 把 映射表[int]int{} 写入 mp :
	for _, num := range nums1 { // 同时取 _ 与 num 遍历
		mp[num]++ // mp[num] 加一
	}
	res := []int{}              // 把 []int{} 写入 res :
	for _, num := range nums2 { // 同时取 _ 与 num 遍历
		if cnt, ok := mp[num]; ok && cnt > 0 { // 若 计数, ok : 赋值为 mp[num]; ok 且 计数 超过 0
			res = append(res, num) // 把 append(结果, num) 写入 结果
			mp[num]--              // mp[num] 减一
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
