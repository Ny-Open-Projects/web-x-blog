// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
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
func sortList(head *ListNode) *ListNode { // 定义函数/方法 sortList
	if head == nil || head.Next == nil {
		return head
	} // 若 头节点 等于 nil 或 头节点.Next 等于 nil { return 头节点 }
	slow, fast := head, head // 把 头节点, 头节点 写入 slow, fast :
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	mid := slow.Next
	slow.Next = nil // 把 慢指针.Next; 慢指针.Next 赋值为 nil 写入 mid :
	left := sortList(head)
	right := sortList(mid) // 把 sortList(头节点); 右边界 : 赋值为 sortList(中点) 写入 left :
	dummy := &ListNode{}
	p := dummy                        // 把 按位与 ListNode{}; 节点 : 赋值为 哨兵节点 写入 dummy :
	for left != nil && right != nil { // 把 nil 且 右边界 不等于 nil { 写入 for left !
		if left.Val <= right.Val {
			p.Next = left
			left = left.Next
		} else {
			p.Next = right
			right = right.Next
		}
		p = p.Next // 把 节点.Next 写入 节点
	}
	if left != nil {
		p.Next = left
	} else {
		p.Next = right
	} // 若 左边界 不等于 nil { 节点.Next 赋值为 左边界 } else { 节点.Next 赋值为 右边界 }
	return dummy.Next // 返回 哨兵节点.Next
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct{ in, want []int }{ // 把 []struct{ in, want []int }{ 写入 cases :
		{[]int{4, 2, 1, 3}, []int{1, 2, 3, 4}},
		{[]int{}, []int{}},
		{[]int{-1, 5, 3, 4, 0}, []int{-1, 0, 3, 4, 5}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := toArr(sortList(buildList(c.in))) // 把 toArr(sortList(buildList(字符.in))) 写入 got :
		if !reflect.DeepEqual(got, c.want) {
			ok = false
			fmt.Printf("FAIL %v\n", got)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
