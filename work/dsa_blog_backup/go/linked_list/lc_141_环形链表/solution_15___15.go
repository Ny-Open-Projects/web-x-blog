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
func buildList(vals []int) *ListNode { // 定义函数/方法 buildList
	dummy := &ListNode{}
	p := dummy // 把 按位与 ListNode{}; 节点 : 赋值为 哨兵节点 写入 dummy :
	for _, v := range vals {
		p.Next = &ListNode{Val: v}
		p = p.Next
	} // 同时取 _ 与 值 遍历
	return dummy.Next // 返回 哨兵节点.Next
}
func toArr(head *ListNode) []int { // 定义函数/方法 toArr
	res := []int{} // 把 []int{} 写入 res :
	for head != nil {
		res = append(res, head.Val)
		head = head.Next
	}
	return res // 返回 结果
}
func hasCycle(head *ListNode) bool { // 定义函数/方法 hasCycle
	slow, fast := head, head // 把 头节点, 头节点 写入 slow, fast :
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			return true
		}
	}
	return false // 返回 false
}
func main() { // 程序入口：跑内嵌自测用例
	// acyclic
	a := buildList([]int{1, 2, 3})
	if hasCycle(a) {
		fmt.Println("FAIL acyclic")
		os.Exit(1)
	} // 打印输出
	// cycle: tail -> head
	b := buildList([]int{1, 2, 3})
	p := b
	for p.Next != nil {
		p = p.Next
	}
	p.Next = b
	if !hasCycle(b) {
		fmt.Println("FAIL cycle")
		os.Exit(1)
	} // 若 取反 hasCycle(b) { fmt.Println(「FAIL cycle」); os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
