// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

type ListNode struct { // 定义类型
	Val  int       // Val int
	Next *ListNode // Next 乘 ListNode
}

func sortList(head *ListNode) *ListNode { // 定义函数/方法 sortList
	if head == nil { // 若 头节点 等于 nil
		return nil // 返回 nil
	}
	nodes := []*ListNode{}                        // 把 [] 乘 ListNode{} 写入 nodes :
	for cur := head; cur != nil; cur = cur.Next { // 把 头节点; 当前值 不等于 nil; 当前值 赋值为 当前值.Next { 写入 for cur :
		nodes = append(nodes, cur) // 把 append(nodes, 当前值) 写入 nodes
	}
	sort.Slice(nodes, func(i, j int) bool { // sort.Slice(nodes, func(下标 i, 下标 j int) bool {
		return nodes[i].Val < nodes[j].Val // 返回 nodes[下标 i].Val 小于 nodes[下标 j].Val
	}) // })
	for i := 0; i < len(nodes)-1; i++ { // 让 下标 i 从 0 开始计数
		nodes[i].Next = nodes[i+1] // 把 nodes[下标 i 加 1] 写入 nodes[i].Next
	}
	nodes[len(nodes)-1].Next = nil // 把 nil 写入 nodes[len(nodes)-1].Next
	if len(nodes) > 0 {            // 若 长度(nodes) 超过 0
		return nodes[0] // 返回 nodes[0]
	}
	return nil // 返回 nil
}

func buildList(vals []int) *ListNode { // 定义函数/方法 buildList
	dummy := &ListNode{}     // 把 按位与 ListNode{} 写入 dummy :
	curr := dummy            // 把 哨兵节点 写入 curr :
	for _, v := range vals { // 同时取 _ 与 值 遍历
		curr.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 curr.Next
		curr = curr.Next              // 把 当前值.Next 写入 当前值
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func toList(head *ListNode) []int { // 定义函数/方法 toList
	res := []int{}    // 把 []int{} 写入 res :
	for head != nil { // 把 nil { 写入 for head !
		res = append(res, head.Val) // 把 append(结果, 头节点.Val) 写入 结果
		head = head.Next            // 把 头节点.Next 写入 头节点
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{4, 2, 1, 3}, []int{1, 2, 3, 4}},
		{nil, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := toList(sortList(buildList(c.in))) // 把 toList(sortList(buildList(字符.in))) 写入 got :
		if !reflect.DeepEqual(got, c.want) {     // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                       // 把 false 写入 ok
			fmt.Printf("FAIL got=%v want=%v\n", got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		panic("FAILED") // panic(「FAILED」)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
