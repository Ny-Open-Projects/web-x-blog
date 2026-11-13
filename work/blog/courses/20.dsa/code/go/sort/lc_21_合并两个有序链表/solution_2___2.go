// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134358253
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
func mergeTwoLists(l1, l2 *ListNode) *ListNode { // 定义函数/方法 mergeTwoLists
	dummy := &ListNode{}
	p := dummy                   // 把 按位与 ListNode{}; 节点 : 赋值为 哨兵节点 写入 dummy :
	for l1 != nil && l2 != nil { // 把 nil 且 l2 不等于 nil { 写入 for l1 !
		if l1.Val <= l2.Val {
			p.Next = l1
			l1 = l1.Next
		} else {
			p.Next = l2
			l2 = l2.Next
		}
		p = p.Next // 把 节点.Next 写入 节点
	}
	if l1 != nil {
		p.Next = l1
	} else {
		p.Next = l2
	} // 若 l1 不等于 nil { 节点.Next 赋值为 l1 } else { 节点.Next 赋值为 l2 }
	return dummy.Next // 返回 哨兵节点.Next
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct{ a, b, want []int }{ // 把 []struct{ 数组, b, want []int }{ 写入 cases :
		{[]int{1, 2, 4}, []int{1, 3, 4}, []int{1, 1, 2, 3, 4, 4}},
		{[]int{}, []int{}, []int{}},
		{[]int{1}, []int{}, []int{1}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := toArr(mergeTwoLists(buildList(c.a), buildList(c.b)))
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
