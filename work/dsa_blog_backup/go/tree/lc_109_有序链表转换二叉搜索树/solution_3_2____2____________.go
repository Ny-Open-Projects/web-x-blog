// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993713
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type ListNode struct {
	Val  int
	Next *ListNode
}                      // 定义类型
type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func buildList(vals []int) *ListNode { // 定义函数/方法 buildList
	dummy := &ListNode{}     // 把 按位与 ListNode{} 写入 dummy :
	cur := dummy             // 把 哨兵节点 写入 cur :
	for _, v := range vals { // 同时取 _ 与 值 遍历
		cur.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 cur.Next
		cur = cur.Next               // 把 当前值.Next 写入 当前值
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func treeLevel(root *TreeNode) []interface{} { // 定义函数/方法 treeLevel
	if root == nil { // 若 根节点 等于 nil
		return []interface{}{} // 返回 []interface{}{}
	}
	res := []interface{}{} // 把 []interface{}{} 写入 res :
	q := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 q :
	for len(q) > 0 {       // for 长度(节点) 超过 0 {
		n := q[0]     // 把 节点[0] 写入 n :
		q = q[1:]     // 把 节点[1:] 写入 节点
		if n == nil { // 若 元素个数 等于 nil
			res = append(res, nil) // 把 append(结果, nil) 写入 结果
			continue               // 跳过本轮，进入下一次
		}
		res = append(res, n.Val)       // 把 append(结果, 元素个数.Val) 写入 结果
		q = append(q, n.Left, n.Right) // 把 append(节点, 元素个数.Left, 元素个数.Right) 写入 节点
	}
	for len(res) > 0 { // for 长度(结果) 超过 0 {
		if res[len(res)-1] != nil { // 若 结果[长度(结果) 减 1] 不等于 nil
			break // 跳出循环
		}
		res = res[:len(res)-1] // 把 结果[:长度(结果) 减 1] 写入 结果
	}
	return res // 返回 结果
}

func sortedListToBST(head *ListNode) *TreeNode { // 定义函数/方法 sortedListToBST
	length := 0                           // 把 0 写入 length :
	for p := head; p != nil; p = p.Next { // 把 头节点; 节点 不等于 nil; 节点 赋值为 节点.Next { 写入 for p :
		length++ // 长度 加一
	}
	var build func(int, int) *TreeNode // var build func(int, int) 乘 TreeNode
	build = func(l, r int) *TreeNode { // 把 func(左指针, 右指针 int) 乘 TreeNode { 写入 build
		if l > r { // 若 左指针 超过 右指针
			return nil // 返回 nil
		}
		mid := (l + r + 1) / 2       // 把 (左指针 加 右指针 加 1) 除以 2 写入 mid :
		root := &TreeNode{}          // 把 按位与 TreeNode{} 写入 root :
		root.Left = build(l, mid-1)  // 把 build(左指针, 中点 减 1) 写入 root.Left
		root.Val = head.Val          // 把 头节点.Val 写入 root.Val
		head = head.Next             // 把 头节点.Next 写入 头节点
		root.Right = build(mid+1, r) // 把 build(中点 加 1, 右指针) 写入 root.Right
		return root                  // 返回 根节点
	}
	return build(0, length-1) // 定义函数/方法 build
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		vals []int         // vals []int
		want []interface{} // want []interface{}
	}{ // }{
		{nil, []interface{}{}},
		{[]int{-10, -3, 0, 5, 9}, []interface{}{0, -3, 9, -10, nil, 5}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := treeLevel(sortedListToBST(buildList(c.vals))); !reflect.DeepEqual(g, c.want) {
			ok = false                                            // 把 false 写入 ok
			fmt.Printf("FAIL %v=%v want %v\n", c.vals, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
