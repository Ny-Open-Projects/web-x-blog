// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130514894
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
type ListNode struct {
	Val  int
	Next *ListNode
} // 定义类型
func buildList(vals []int, pos int) *ListNode { // 定义函数/方法 buildList
	if len(vals) == 0 {
		return nil
	} // 若 长度(vals) 等于 0 { return nil }
	nodes := make([]*ListNode, len(vals)) // 把 make([] 乘 ListNode, 长度(vals)) 写入 nodes :
	for i, v := range vals {
		nodes[i] = &ListNode{Val: v}
	} // 同时取 下标 i 与 值 遍历
	for i := 0; i < len(vals)-1; i++ {
		nodes[i].Next = nodes[i+1]
	} // 让 下标 i 从 0 开始计数
	if pos >= 0 && pos < len(vals) {
		nodes[len(vals)-1].Next = nodes[pos]
	}
	return nodes[0] // 返回 nodes[0]
}
func hasCycle(head *ListNode) bool { // 定义函数/方法 hasCycle
	slow := head                          // 把 头节点 写入 slow :
	fast := head                          // 把 头节点 写入 fast :
	for fast != nil && fast.Next != nil { // 把 nil 且 快指针.Next 不等于 nil { 写入 for fast !
		slow = slow.Next      // 把 慢指针.Next 写入 慢指针
		fast = fast.Next.Next // 把 快指针.Next.Next 写入 快指针
		if slow == fast {
			return true
		} // 若 慢指针 等于 快指针 { return true }
	}
	return false // 返回 false
}
func main() { // 程序入口：跑内嵌自测用例
	type tc struct {
		vals []int
		pos  int
		want bool
	} // 定义类型
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{}, -1, false},
		{[]int{3, 2, 0, -4}, 1, true},
		{[]int{1, 2}, 0, true},
		{[]int{1}, -1, false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := hasCycle(buildList(c.vals, c.pos)) // 把 hasCycle(buildList(字符.vals, 字符.pos)) 写入 got :
		if got != c.want {
			ok = false
			fmt.Printf("FAIL vals=%v pos=%d got=%v want=%v\n", c.vals, c.pos, got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
