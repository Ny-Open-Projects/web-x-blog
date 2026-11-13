// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993713
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

type ListNode struct { // 定义类型
	Val  int       // Val int
	Next *ListNode // Next 乘 ListNode
}

func buildList(vals []int) *ListNode { // 定义函数/方法 buildList
	if len(vals) == 0 { // 若 长度(vals) 等于 0
		return nil // 返回 nil
	}
	head := &ListNode{Val: vals[0]} // 把 按位与 ListNode{Val: vals[0]} 写入 head :
	cur := head                     // 把 头节点 写入 cur :
	for _, v := range vals[1:] {    // 同时取 _ 与 值 遍历
		cur.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 cur.Next
		cur = cur.Next               // 把 当前值.Next 写入 当前值
	}
	return head // 返回 头节点
}

func listVals(head *ListNode) []int { // 定义函数/方法 listVals
	res := []int{}    // 把 []int{} 写入 res :
	for head != nil { // 把 nil { 写入 for head !
		res = append(res, head.Val) // 把 append(结果, 头节点.Val) 写入 结果
		head = head.Next            // 把 头节点.Next 写入 头节点
	}
	return res // 返回 结果
}

func inorder(root *TreeNode) []int { // 定义函数/方法 inorder
	if root == nil { // 若 根节点 等于 nil
		return []int{} // 返回 []int{}
	}
	res := []int{}                            // 把 []int{} 写入 res :
	res = append(res, inorder(root.Left)...)  // 把 append(结果, inorder(根节点.Left)...) 写入 结果
	res = append(res, root.Val)               // 把 append(结果, 根节点.Val) 写入 结果
	res = append(res, inorder(root.Right)...) // 把 append(结果, inorder(根节点.Right)...) 写入 结果
	return res                                // 返回 结果
}

func sortedListToBST(head *ListNode) *TreeNode { // 定义函数/方法 sortedListToBST
	var getMedian func(left, right *ListNode) *ListNode // var getMedian func(左边界, 右边界 乘 ListNode) 乘 ListNode
	getMedian = func(left, right *ListNode) *ListNode { // 把 func(左边界, 右边界 乘 ListNode) 乘 ListNode { 写入 getMedian
		fast := left                              // 把 左边界 写入 fast :
		slow := left                              // 把 左边界 写入 slow :
		for fast != right && fast.Next != right { // 把 右边界 且 快指针.Next 不等于 右边界 { 写入 for fast !
			fast = fast.Next.Next // 把 快指针.Next.Next 写入 快指针
			slow = slow.Next      // 把 慢指针.Next 写入 慢指针
		}
		return slow // 返回 慢指针
	}
	var buildTree func(left, right *ListNode) *TreeNode // var buildTree func(左边界, 右边界 乘 ListNode) 乘 TreeNode
	buildTree = func(left, right *ListNode) *TreeNode { // 把 func(左边界, 右边界 乘 ListNode) 乘 TreeNode { 写入 buildTree
		if left == right { // 若 左边界 等于 右边界
			return nil // 返回 nil
		}
		mid := getMedian(left, right)           // 把 getMedian(左边界, 右边界) 写入 mid :
		root := &TreeNode{Val: mid.Val}         // 把 按位与 TreeNode{Val: 中点.Val} 写入 root :
		root.Left = buildTree(left, mid)        // 把 buildTree(左边界, 中点) 写入 root.Left
		root.Right = buildTree(mid.Next, right) // 把 buildTree(中点.Next, 右边界) 写入 root.Right
		return root                             // 返回 根节点
	}
	return buildTree(head, nil) // 定义函数/方法 buildTree
}

type tc struct { // 定义类型
	vals []int // vals []int
	want []int // want []int
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{}, []int{}},
		{[]int{1, 2, 3}, []int{1, 2, 3}},
		{[]int{1, 2, 3, 4, 5, 6, 7}, []int{1, 2, 3, 4, 5, 6, 7}},
	}
	for idx, c := range cases { // 同时取 idx 与 字符 遍历
		head := buildList(c.vals)             // 把 buildList(字符.vals) 写入 head :
		got := inorder(sortedListToBST(head)) // 把 inorder(sortedListToBST(头节点)) 写入 got :
		if !reflect.DeepEqual(got, c.want) {  // 若 取反 reflect.DeepEqual(got, 字符.want
			fmt.Printf("case %d failed: got %v want %v\n", idx, got, c.want) // 打印输出
			os.Exit(1)                                                       // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
