// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func maximumGap(nums []int) int { // 定义函数/方法 maximumGap
	if len(nums) < 2 {
		return 0
	} // 若 长度(数组) 小于 2 { return 0 }
	minv, maxv := nums[0], nums[0] // 把 数组[0], 数组[0] 写入 minv, maxv :
	for _, v := range nums {
		if v < minv {
			minv = v
		}
		if v > maxv {
			maxv = v
		}
	} // 同时取 _ 与 值 遍历
	if minv == maxv {
		return 0
	} // 若 最小值 等于 最大值 { return 0 }
	n := len(nums) // 把 长度(数组) 写入 n :
	bucketSize := (maxv - minv) / (n - 1)
	if bucketSize < 1 {
		bucketSize = 1
	}
	bucketCount := (maxv-minv)/bucketSize + 1 // 把 (最大值 减 最小值) 除以 bucketSize 加 1 写入 bucketCount :
	bMin := make([]int, bucketCount)
	bMax := make([]int, bucketCount)
	has := make([]bool, bucketCount)
	for _, v := range nums { // 同时取 _ 与 值 遍历
		idx := (v - minv) / bucketSize // 把 (值 减 最小值) 除以 bucketSize 写入 idx :
		if !has[idx] {
			bMin[idx] = v
			bMax[idx] = v
			has[idx] = true
		} else {
			if v < bMin[idx] {
				bMin[idx] = v
			} // 若 值 小于 bMin[idx] { bMin[idx] 赋值为 值 }
			if v > bMax[idx] {
				bMax[idx] = v
			} // 若 值 超过 bMax[idx] { bMax[idx] 赋值为 值 }
		}
	}
	ans, prev := 0, minv               // 把 0, 最小值 写入 ans, prev :
	for i := 0; i < bucketCount; i++ { // 让 下标 i 从 0 开始计数
		if !has[i] {
			continue
		} // 若 取反 has[下标 i] { continue }
		if bMin[i]-prev > ans {
			ans = bMin[i] - prev
		} // 若 bMin[下标 i] 减 前一个 超过 答案 { 答案 赋值为 bMin[下标 i] 减 前一个 }
		prev = bMax[i] // 把 bMax[下标 i] 写入 前一个
	}
	return ans // 返回 答案
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   []int
		want int
	}{ // 把 []struct{ in []int; want int }{ 写入 cases :
		{[]int{3, 6, 9, 1}, 3}, {[]int{10}, 0}, {[]int{1, 10000000}, 9999999},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := maximumGap(c.in); got != c.want {
			ok = false
			fmt.Printf("FAIL=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
