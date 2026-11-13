// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513247
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
func addTwoNumbers(l1, l2 *ListNode) *ListNode { // 定义函数/方法 addTwoNumbers
	dummy := &ListNode{}
	p := dummy
	carry := 0                                 // 把 按位与 ListNode{}; 节点 : 赋值为 哨兵节点; carry : 赋值为 0 写入 dummy :
	for l1 != nil || l2 != nil || carry != 0 { // 把 nil 或 l2 不等于 nil 或 carry 不等于 0 { 写入 for l1 !
		s := carry // 把 carry 写入 s :
		if l1 != nil {
			s += l1.Val
			l1 = l1.Next
		} // 若 l1 不等于 nil { 字符串 累加 l1.Val; l1 赋值为 l1.Next }
		if l2 != nil {
			s += l2.Val
			l2 = l2.Next
		} // 若 l2 不等于 nil { 字符串 累加 l2.Val; l2 赋值为 l2.Next }
		carry = s / 10 // 把 字符串 除以 10 写入 carry
		p.Next = &ListNode{Val: s % 10}
		p = p.Next // 把 按位与 ListNode{Val: 字符串 对…取模 10}; 节点 赋值为 节点.Next 写入 p.Next
	}
	return dummy.Next // 返回 哨兵节点.Next
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct{ a, b, want []int }{ // 把 []struct{ 数组, b, want []int }{ 写入 cases :
		{[]int{2, 4, 3}, []int{5, 6, 4}, []int{7, 0, 8}},
		{[]int{0}, []int{0}, []int{0}},
		{[]int{9, 9, 9, 9}, []int{9, 9, 9}, []int{8, 9, 9, 0, 1}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := toArr(addTwoNumbers(buildList(c.a), buildList(c.b)))
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
