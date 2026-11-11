// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095015
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
func getIntersectionNode(headA, headB *ListNode) int { // 定义函数/方法 getIntersectionNode
	a, b := headA, headB // 把 链表 A, 链表 B 写入 a, b :
	for a != b {         // 把 b { 写入 for a !
		if a == nil {
			a = headB
		} else {
			a = a.Next
		} // 若 数组 等于 nil { 数组 赋值为 链表 B } else { 数组 赋值为 数组.Next }
		if b == nil {
			b = headA
		} else {
			b = b.Next
		} // 若 b 等于 nil { b 赋值为 链表 A } else { b 赋值为 b.Next }
	}
	if a == nil {
		return -1
	} // 若 数组 等于 nil { return 减 1 }
	return a.Val // 返回 数组.Val
}
func main() { // 程序入口：跑内嵌自测用例
	// intersect at value 3
	common := buildList([]int{3, 4}) // 把 buildList([]int{3,4}) 写入 common :
	a := &ListNode{Val: 1}
	a.Next = &ListNode{Val: 2}
	a.Next.Next = common
	b := &ListNode{Val: 9}
	b.Next = common // 把 按位与 ListNode{Val:9}; b.Next 赋值为 common 写入 b :
	if got := getIntersectionNode(a, b); got != 3 {
		fmt.Println("FAIL", got)
		os.Exit(1)
	}
	// disjoint
	d1 := buildList([]int{1, 2})
	d2 := buildList([]int{3, 4})
	if got := getIntersectionNode(d1, d2); got != -1 {
		fmt.Println("FAIL", got)
		os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
