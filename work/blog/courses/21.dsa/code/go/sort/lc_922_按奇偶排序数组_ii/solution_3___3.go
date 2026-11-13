// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func sortArrayByParityII(nums []int) []int { // 定义函数/方法 sortArrayByParityII
	n := len(nums)
	res := make([]int, n)
	e, o := 0, 1             // 把 长度(数组); 结果 : 赋值为 make([]int, 元素个数); e, o : 赋值为 0, 1 写入 n :
	for _, v := range nums { // 同时取 _ 与 值 遍历
		if v%2 == 0 {
			res[e] = v
			e += 2
		} else {
			res[o] = v
			o += 2
		}
	}
	return res // 返回 结果
}
func eqMultiset(a, b []int) bool { // 定义函数/方法 eqMultiset
	if len(a) != len(b) {
		return false
	} // 若 长度(数组) 不等于 长度(b) { return false }
	ca, cb := map[int]int{}, map[int]int{} // 把 映射表[int]int{}, 映射表[int]int{} 写入 ca, cb :
	for _, v := range a {
		ca[v]++
	} // 同时取 _ 与 值 遍历
	for _, v := range b {
		cb[v]++
	} // 同时取 _ 与 值 遍历
	for k, v := range ca {
		if cb[k] != v {
			return false
		}
	} // 同时取 下标 k 与 值 遍历
	return true // 返回 true
}
func validParity(a, src []int) bool { // 定义函数/方法 validParity
	if len(a) != len(src) {
		return false
	} // 若 长度(数组) 不等于 长度(src) { return false }
	if !eqMultiset(a, src) {
		return false
	} // 若 取反 eqMultiset(数组, src) { return false }
	for i, v := range a { // 同时取 下标 i 与 值 遍历
		if i%2 == 0 && v%2 != 0 {
			return false
		} // 若 下标 i 对…取模 2 等于 0 且 值 对…取模 2 不等于 0 { return false }
		if i%2 == 1 && v%2 == 0 {
			return false
		} // 若 下标 i 对…取模 2 等于 1 且 值 对…取模 2 等于 0 { return false }
	}
	return true // 返回 true
}
func main() { // 程序入口：跑内嵌自测用例
	cases := [][]int{{4, 2, 5, 7}, {2, 3}, {1, 2, 3, 4}} // 把 [][]int{{4,2,5,7},{2,3},{1,2,3,4}} 写入 cases :
	ok := true                                           // 把 true 写入 ok :
	for _, c := range cases {                            // 同时取 _ 与 字符 遍历
		if !validParity(sortArrayByParityII(c), c) {
			ok = false
			fmt.Printf("FAIL parity %v\n", c)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
