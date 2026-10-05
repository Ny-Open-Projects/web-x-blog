package com.imooc.dddq.code;

import com.imooc.dddq.common.ListNode;

public class L142 {
    // 哈希表
    public ListNode detectCycle(ListNode head) {
        return null;
    }

    // 快慢指针
    public ListNode detectCycle2(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null) {
            slow = slow.next;
            if (fast.next != null) {
                fast = fast.next.next;
            } else {
                return null;
            }
            // 成环
            if (fast == slow) {
                ListNode ptr = head;
                // a = c + (n-1)(b+c)
                while (ptr != slow) {
                    ptr = ptr.next;
                    slow = slow.next;
                }
                return ptr;
            }
        }
        return null;
    }
}
