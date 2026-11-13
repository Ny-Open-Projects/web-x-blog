// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091703
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func pi(v int) *int { return &v } // 定义函数/方法 pi

func buildTree(vals []*int) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == nil { // 若 长度(vals) 等于 0 或 vals[0] 等于 nil
		return nil // 返回 nil
	}
	root := &TreeNode{Val: *vals[0]} // 把 按位与 TreeNode{Val: 乘 vals[0]} 写入 root :
	q := []*TreeNode{root}           // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                           // 把 1 写入 i :
	for i < len(vals) {              // for 下标 i 小于 长度(vals) {
		node := q[0]        // 把 节点[0] 写入 node :
		q = q[1:]           // 把 节点[1:] 写入 节点
		if vals[i] != nil { // 若 vals[下标 i] 不等于 nil
			node.Left = &TreeNode{Val: *vals[i]} // 把 按位与 TreeNode{Val: 乘 vals[下标 i]} 写入 node.Left
			q = append(q, node.Left)             // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                // 下标 i 加一
		if i < len(vals) { // 若 下标 i 小于 长度(vals
			if vals[i] != nil { // 若 vals[下标 i] 不等于 nil
				node.Right = &TreeNode{Val: *vals[i]} // 把 按位与 TreeNode{Val: 乘 vals[下标 i]} 写入 node.Right
				q = append(q, node.Right)             // 把 append(节点, 节点.Right) 写入 节点
			}
			i++ // 下标 i 加一
		}
	}
	return root // 返回 根节点
}

func searchBST(root *TreeNode, val int) *TreeNode { // 定义函数/方法 searchBST
	cur := root      // 把 根节点 写入 cur :
	for cur != nil { // 把 nil { 写入 for cur !
		if cur.Val == val { // 若 当前值.Val 等于 值
			return cur // 返回 当前值
		}
		if val < cur.Val { // 若 值 小于 当前值.Val
			cur = cur.Left // 把 当前值.Left 写入 当前值
		} else { // 否则
			cur = cur.Right // 把 当前值.Right 写入 当前值
		}
	}
	return nil // 返回 nil
}

func nodeVal(n *TreeNode) interface{} { // 定义函数/方法 nodeVal
	if n == nil { // 若 元素个数 等于 nil
		return nil // 返回 nil
	}
	return n.Val // 返回 元素个数.Val
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		vals []int       // vals []int
		val  int         // 值 int
		want interface{} // want interface{}
	}{ // }{
		{[]int{4, 2, 7, 1, 3}, 2, 2},
		{[]int{4, 2, 7, 1, 3}, 5, nil},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		pvals := make([]*int, len(c.vals)) // 把 make([] 乘 int, 长度(字符.vals)) 写入 pvals :
		for i, v := range c.vals {         // 同时取 下标 i 与 值 遍历
			pvals[i] = pi(v) // 把 pi(值) 写入 pvals[i]
		}
		got := nodeVal(searchBST(buildTree(pvals), c.val)) // 把 nodeVal(searchBST(buildTree(pvals), 字符.值)) 写入 got :
		if !reflect.DeepEqual(got, c.want) {               // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                                               // 把 false 写入 ok
			fmt.Printf("FAIL searchBST(vals=%v, val=%d) = %v want %v\n", c.vals, c.val, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
