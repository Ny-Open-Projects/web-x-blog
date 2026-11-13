import os

base = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/go/linked_list/lc_203_移除链表元素"

go203 = '''package main

import ("fmt"; "os"; "reflect")

type ListNode struct {
    val  int
    next *ListNode
}

func buildList(vals []int) *ListNode {
    dummy := &ListNode{}
    cur := dummy
    for _, v := range vals {
        cur.next = &ListNode{val: v}
        cur = cur.next
    }
    return dummy.next
}

func toSlice(head *ListNode) []int {
    var res []int
    for head != nil {
        res = append(res, head.val)
        head = head.next
    }
    return res
}

func removeElements(head *ListNode, val int) *ListNode {
    dummy := &ListNode{next: head}
    temp := dummy
    for temp.next != nil {
        if temp.next.val == val {
            temp.next = temp.next.next
        } else {
            temp = temp.next
        }
    }
    return dummy.next
}

func main() {
    ok := true
    cases := []struct {
        in   []int
        val  int
        want []int
    }{
        {[]int{1, 2, 6, 3, 4, 5, 6}, 6, []int{1, 2, 3, 4, 5}},
        {[]int{}, 6, []int{}},
        {[]int{6, 6, 6}, 6, []int{}},
        {[]int{1, 2, 3}, 4, []int{1, 2, 3}},
    }
    for _, c := range cases {
        got := toSlice(removeElements(buildList(c.in), c.val))
        if !reflect.DeepEqual(got, c.want) {
            ok = false
            fmt.Printf("FAIL removeElements(%v,%d)=%v want %v\\n", c.in, c.val, got, c.want)
        }
    }
    if !ok {
        os.Exit(1)
    }
    fmt.Println("PASS")
}
'''

go203_rec = '''package main

import ("fmt"; "os"; "reflect")

type ListNode struct {
    val  int
    next *ListNode
}

func buildList(vals []int) *ListNode {
    dummy := &ListNode{}
    cur := dummy
    for _, v := range vals {
        cur.next = &ListNode{val: v}
        cur = cur.next
    }
    return dummy.next
}

func toSlice(head *ListNode) []int {
    var res []int
    for head != nil {
        res = append(res, head.val)
        head = head.next
    }
    return res
}

func removeElements(head *ListNode, val int) *ListNode {
    if head == nil {
        return nil
    }
    head.next = removeElements(head.next, val)
    if head.val == val {
        return head.next
    }
    return head
}

func main() {
    ok := true
    cases := []struct {
        in   []int
        val  int
        want []int
    }{
        {[]int{1, 2, 6, 3, 4, 5, 6}, 6, []int{1, 2, 3, 4, 5}},
        {[]int{}, 6, []int{}},
        {[]int{6, 6, 6}, 6, []int{}},
        {[]int{1, 2, 3}, 4, []int{1, 2, 3}},
    }
    for _, c := range cases {
        got := toSlice(removeElements(buildList(c.in), c.val))
        if !reflect.DeepEqual(got, c.want) {
            ok = false
            fmt.Printf("FAIL removeElements(%v,%d)=%v want %v\\n", c.in, c.val, got, c.want)
        }
    }
    if !ok {
        os.Exit(1)
    }
    fmt.Println("PASS")
}
'''

with open(os.path.join(base, "solution_1_1_____1____.go"), "w") as f:
    f.write(go203_rec)
with open(os.path.join(base, "solution_2_2_____2____.go"), "w") as f:
    f.write(go203)
print("wrote 2 go files")
