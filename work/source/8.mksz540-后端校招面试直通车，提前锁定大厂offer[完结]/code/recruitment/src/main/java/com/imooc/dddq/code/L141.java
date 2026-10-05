package com.imooc.dddq.code;

import com.imooc.dddq.common.ListNode;

import java.util.HashMap;
import java.util.Map;

public class L141 {
    // 哈希表
    public boolean hasCycle(ListNode head) {
        Map<ListNode, Boolean> map = new HashMap<>();
        while (head != null) {
            if (map.containsKey(head)) {
                return true;
            }
            map.put(head, true);
            head = head.next;
        }
        return false;
    }

    // 快慢指针
    public boolean hasCycle2(ListNode head) {
        if(head == null || head.next == null) {
            return false;
        }
        ListNode slow = head;
        ListNode fast = head.next;
        while (slow != fast) {
            if (fast == null || fast.next == null || slow == null) {
                return false;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return true;
    }
}
