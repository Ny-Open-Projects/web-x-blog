// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145083302
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}                        // 定义类型
const NULL = -1000000000 // 把 减 1000000000 存入 NULL
func buildTree(vals []int) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == NULL {
		return nil
	} // 若 长度(vals) 等于 0 或 vals[0] 等于 NULL { return nil }
	root := &TreeNode{Val: vals[0]} // 把 按位与 TreeNode{Val: vals[0]} 写入 root :
	q := []*TreeNode{root}
	i := 1                            // 把 [] 乘 TreeNode{根节点}; 下标 i : 赋值为 1 写入 q :
	for len(q) > 0 && i < len(vals) { // 定义函数/方法 len
		node := q[0]
		q = q[1:] // 把 节点[0]; 节点 赋值为 节点[1:] 写入 node :
		if i < len(vals) && vals[i] != NULL {
			node.Left = &TreeNode{Val: vals[i]}
			q = append(q, node.Left)
		}
		i++
		if i < len(vals) && vals[i] != NULL {
			node.Right = &TreeNode{Val: vals[i]}
			q = append(q, node.Right)
		}
		i++
	}
	return root // 返回 根节点
}
func levelList(root *TreeNode) [][]int { // 定义函数/方法 levelList
	if root == nil {
		return [][]int{}
	} // 若 根节点 等于 nil { return [][]int{} }
	res := [][]int{}
	q := []*TreeNode{root} // 把 [][]int{}; 节点 : 赋值为 [] 乘 TreeNode{根节点} 写入 res :
	for len(q) > 0 {       // for 长度(节点) 超过 0 {
		lvl := []int{}
		n := len(q)              // 把 []int{}; 元素个数 : 赋值为 长度(节点) 写入 lvl :
		for k := 0; k < n; k++ { // 让 下标 k 从 0 开始计数
			node := q[0]
			q = q[1:]                   // 把 节点[0]; 节点 赋值为 节点[1:] 写入 node :
			lvl = append(lvl, node.Val) // 把 append(lvl, 节点.Val) 写入 lvl
			if node.Left != nil {
				q = append(q, node.Left)
			} // 若 节点.Left 不等于 nil { 节点 赋值为 append(节点, 节点.Left) }
			if node.Right != nil {
				q = append(q, node.Right)
			} // 若 节点.Right 不等于 nil { 节点 赋值为 append(节点, 节点.Right) }
		}
		res = append(res, lvl) // 把 append(结果, lvl) 写入 结果
	}
	return res // 返回 结果
}
func sameTree(a, b *TreeNode) bool { // 定义函数/方法 sameTree
	if a == nil && b == nil {
		return true
	} // 若 数组 等于 nil 且 b 等于 nil { return true }
	if a == nil || b == nil {
		return false
	} // 若 数组 等于 nil 或 b 等于 nil { return false }
	if a.Val != b.Val {
		return false
	} // 若 数组.Val 不等于 b.Val { return false }
	return sameTree(a.Left, b.Left) && sameTree(a.Right, b.Right) // 定义函数/方法 sameTree
}
func inorderT(root *TreeNode) []int { // 定义函数/方法 inorderT
	if root == nil {
		return []int{}
	} // 若 根节点 等于 nil { return []int{} }
	return append(append(inorderT(root.Left), root.Val), inorderT(root.Right)...) // 定义函数/方法 append
}
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode { // 定义函数/方法 lowestCommonAncestor
	if root == nil || root == p || root == q {
		return root
	} // 若 根节点 等于 nil 或 根节点 等于 节点 或 根节点 等于 节点 { return 根节点 }
	left := lowestCommonAncestor(root.Left, p, q)   // 把 lowestCommonAncestor(根节点.Left, 节点, 节点) 写入 left :
	right := lowestCommonAncestor(root.Right, p, q) // 把 lowestCommonAncestor(根节点.Right, 节点, 节点) 写入 right :
	if left != nil && right != nil {
		return root
	} // 若 左边界 不等于 nil 且 右边界 不等于 nil { return 根节点 }
	if left != nil {
		return left
	} // 若 左边界 不等于 nil { return 左边界 }
	return right // 返回 右边界
}
func find(root *TreeNode, v int) *TreeNode { // 定义函数/方法 find
	if root == nil {
		return nil
	} // 若 根节点 等于 nil { return nil }
	if root.Val == v {
		return root
	} // 若 根节点.Val 等于 值 { return 根节点 }
	if l := find(root.Left, v); l != nil {
		return l
	} // 若 左指针 : 赋值为 find(根节点.Left, 值); 左指针 不等于 nil { return 左指针 }
	return find(root.Right, v) // 定义函数/方法 find
}
func main() { // 程序入口：跑内嵌自测用例
	root := buildTree([]int{3, 5, 1, 6, 2, 0, 8, NULL, NULL, 7, 4}) // 把 buildTree([]int{3,5,1,6,2,0,8,NULL,NULL,7,4}) 写入 root :
	p := find(root, 5)
	q := find(root, 1) // 把 find(根节点, 5); 节点 : 赋值为 find(根节点, 1) 写入 p :
	if lca := lowestCommonAncestor(root, p, q); lca == nil || lca.Val != 3 {
		fmt.Println("FAIL", lca)
		os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
