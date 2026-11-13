// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829143
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func findNumberOfLIS(nums []int) int { // 定义函数/方法 findNumberOfLIS
	d := [][]int{}           // 把 [][]int{} 写入 d :
	cnt := [][]int{}         // 把 [][]int{} 写入 cnt :
	for _, x := range nums { // 同时取 _ 与 x 遍历
		i := 0              // 把 0 写入 i :
		lo, hi := 0, len(d) // 把 0, 长度(d) 写入 lo, hi :
		for lo < hi {       // for 左边界 小于 右边界 {
			mid := (lo + hi) / 2 // 把 (左边界 加 右边界) 除以 2 写入 mid :
			if d[mid][0] < x {   // 若 d[中点][0] 小于 x
				lo = mid + 1 // 把 中点 加 1 写入 左边界
			} else { // 否则
				hi = mid // 把 中点 写入 右边界
			}
		}
		i = lo     // 把 左边界 写入 下标 i
		c := 1     // 把 1 写入 c :
		if i > 0 { // 若 下标 i 超过 0
			lo2, hi2 := 0, len(d[i-1]) // 把 0, 长度(d[下标 i 减 1]) 写入 lo2, hi2 :
			for lo2 < hi2 {            // for lo2 小于 hi2 {
				mid2 := (lo2 + hi2) / 2 // 把 (lo2 加 hi2) 除以 2 写入 mid2 :
				if d[i-1][mid2] < x {   // 若 d[下标 i 减 1][mid2] 小于 x
					lo2 = mid2 + 1 // 把 mid2 加 1 写入 lo2
				} else { // 否则
					hi2 = mid2 // 把 mid2 写入 hi2
				}
			}
			c = cnt[i-1][lo2] // 把 计数[下标 i 减 1][lo2] 写入 字符
		}
		if i == len(d) { // 若 下标 i 等于 长度(d
			d = append(d, []int{x})        // 把 append(d, []int{x}) 写入 d
			cnt = append(cnt, []int{0, c}) // 把 append(计数, []int{0, 字符}) 写入 计数
		} else { // 否则
			d[i] = append(d[i], x) // 把 append(d[下标 i], x) 写入 d[i]
			cnt[i] = append(cnt[i], cnt[i][len(cnt[i])-1]+c)
		}
	}
	if len(cnt) == 0 { // 若 长度(计数) 等于 0
		return 0 // 返回 0
	}
	last := cnt[len(cnt)-1]  // 把 计数[长度(计数) 减 1] 写入 last :
	return last[len(last)-1] // 返回 last[长度(last) 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 3, 5, 4, 7}, 2},
		{[]int{2, 2, 2, 2, 2}, 5},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := findNumberOfLIS(c.in); got != c.want { // 若 got : 赋值为 findNumberOfLIS(字符.in); got 不等于 字符.want
			ok = false                                                             // 把 false 写入 ok
			fmt.Printf("FAIL findNumberOfLIS(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
