// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095646
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type ListNode struct { // 定义类型
	val  int       // 值 int
	next *ListNode // 下一个 乘 ListNode
}

func buildList(vals []int) *ListNode { // 定义函数/方法 buildList
	dummy := &ListNode{}     // 把 按位与 ListNode{} 写入 dummy :
	cur := dummy             // 把 哨兵节点 写入 cur :
	for _, v := range vals { // 同时取 _ 与 值 遍历
		cur.next = &ListNode{val: v} // 把 按位与 ListNode{值: 值} 写入 下一个
		cur = cur.next               // 把 当前值.下一个 写入 当前值
	}
	return dummy.next // 返回 哨兵节点.下一个
}

func toSlice(head *ListNode) []int { // 定义函数/方法 toSlice
	res := []int{}    // 把 []int{} 写入 res :
	for head != nil { // 把 nil { 写入 for head !
		res = append(res, head.val) // 把 append(结果, 头节点.值) 写入 结果
		head = head.next            // 把 头节点.下一个 写入 头节点
	}
	return res // 返回 结果
}

func removeElements(head *ListNode, val int) *ListNode { // 定义函数/方法 removeElements
	if head == nil { // 若 头节点 等于 nil
		return nil // 返回 nil
	}
	head.next = removeElements(head.next, val) // 把 removeElements(头节点.下一个, 值) 写入 下一个
	if head.val == val {                       // 若 头节点.值 等于 值
		return head.next // 返回 头节点.下一个
	}
	return head // 返回 头节点
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true          // 把 true 写入 ok :
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		val  int   // 值 int
		want []int // want []int
	}{ // }{
		{[]int{1, 2, 6, 3, 4, 5, 6}, 6, []int{1, 2, 3, 4, 5}},
		{[]int{}, 6, []int{}},
		{[]int{6, 6, 6}, 6, []int{}},
		{[]int{1, 2, 3}, 4, []int{1, 2, 3}},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := toSlice(removeElements(buildList(c.in), c.val)) // 把 toSlice(removeElements(buildList(字符.in), 字符.值)) 写入 got :
		if !reflect.DeepEqual(got, c.want) {                   // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL removeElements(%v,%d)=%v want %v\n", c.in, c.val, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
