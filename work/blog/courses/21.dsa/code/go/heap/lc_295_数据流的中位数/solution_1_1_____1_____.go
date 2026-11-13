// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344649
package main // 引入依赖
import (
	"fmt"
	"os"
	"sort"
)                                      // 引入依赖
type MedianFinder struct{ nums []int } // 定义类型
func (m *MedianFinder) addNum(num int) { // 定义函数/方法 addNum
	idx := sort.SearchInts(m.nums, num) // 把 sort.SearchInts(映射表.数组, num) 写入 idx :
	m.nums = append(m.nums, 0)          // 把 append(映射表.数组, 0) 写入 数组
	copy(m.nums[idx+1:], m.nums[idx:])  // copy(映射表.数组[idx 加 1:], 映射表.数组[idx:])
	m.nums[idx] = num                   // 把 num 写入 m.nums[idx]
}
func (m *MedianFinder) findMedian() float64 { // 定义函数/方法 findMedian
	n := len(m.nums) // 把 长度(映射表.数组) 写入 n :
	if n == 0 {
		return 0
	} // 若 元素个数 等于 0 { return 0 }
	if n%2 == 1 {
		return float64(m.nums[n/2])
	} // 若 元素个数 对…取模 2 等于 1 { return float64(映射表.数组[元素个数 除以 2]) }
	return float64(m.nums[n/2-1]+m.nums[n/2]) / 2.0 // 返回 float64(映射表.数组[元素个数 除以 2 减 1] 加 映射表.数组[元素个数 除以 2]) 除以 2.0
}
func main() { // 程序入口：跑内嵌自测用例
	type seq struct {
		vals []int
		want float64
	} // 定义类型
	cases := []seq{ // 把 []seq{ 写入 cases :
		{[]int{1, 2, 3, 4, 5}, 3},
		{[]int{1, 2, 3, 4}, 2.5},
		{[]int{42}, 42},
		{[]int{5, 2, 3, 1, 4}, 3},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		mf := &MedianFinder{} // 把 按位与 MedianFinder{} 写入 mf :
		for _, x := range c.vals {
			mf.addNum(x)
		} // 同时取 _ 与 x 遍历
		got := mf.findMedian() // 把 mf.findMedian() 写入 got :
		if got != c.want {
			ok = false
			fmt.Printf("FAIL %v got %v want %v\n", c.vals, got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
