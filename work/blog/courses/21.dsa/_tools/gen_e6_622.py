import os

base = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/java/queue/lc_622_设计循环队列"

classA = '''package com.webfault.dsa;

import java.util.*;

class CqA {
    int capacity;
    int[] data;
    int front;
    int rear;
    int size;

    CqA(int k) {
        capacity = k;
        data = new int[k];
        front = 0;
        rear = 0;
        size = 0;
    }
    boolean enQueue(int v) {
        if (isFull()) return false;
        data[rear] = v;
        rear = (rear + 1) % capacity;
        size++;
        return true;
    }
    boolean deQueue() {
        if (isEmpty()) return false;
        front = (front + 1) % capacity;
        size--;
        return true;
    }
    int Front() { return isEmpty() ? -1 : data[front]; }
    int Rear() { return isEmpty() ? -1 : data[(rear - 1 + capacity) % capacity]; }
    boolean isEmpty() { return size == 0; }
    boolean isFull() { return size == capacity; }

    public static void main(String[] args) {
        CqA q = new CqA(3);
        List<Object> res = new ArrayList<>();
        res.add(q.enQueue(1));
        res.add(q.enQueue(2));
        res.add(q.enQueue(3));
        res.add(q.enQueue(4));
        res.add(q.Rear());
        res.add(q.isFull());
        res.add(q.deQueue());
        res.add(q.enQueue(4));
        res.add(q.Rear());
        List<Object> want = Arrays.asList(true, true, true, false, 3, true, true, true, 4);
        boolean ok = res.equals(want);
        if (!ok) { System.out.println("FAIL got=" + res); throw new RuntimeException("FAILED"); }
        System.out.println("PASS");
    }
}
'''

classB = '''package com.webfault.dsa;

import java.util.*;

class CqB {
    int capacity;
    int[] queue;
    int front;
    int rear;
    int size;

    CqB(int k) {
        capacity = k;
        queue = new int[k];
        front = 0;
        rear = -1;
        size = 0;
    }
    boolean enQueue(int v) {
        if (isFull()) return false;
        rear = (rear + 1) % capacity;
        queue[rear] = v;
        size++;
        return true;
    }
    boolean deQueue() {
        if (isEmpty()) return false;
        front = (front + 1) % capacity;
        size--;
        return true;
    }
    int Front() { return isEmpty() ? -1 : queue[front]; }
    int Rear() { return isEmpty() ? -1 : queue[rear]; }
    boolean isEmpty() { return size == 0; }
    boolean isFull() { return size == capacity; }

    public static void main(String[] args) {
        CqB q = new CqB(3);
        List<Object> res = new ArrayList<>();
        res.add(q.enQueue(1));
        res.add(q.enQueue(2));
        res.add(q.Rear());
        res.add(q.deQueue());
        res.add(q.Front());
        List<Object> want = Arrays.asList(true, true, 2, true, 2);
        boolean ok = res.equals(want);
        if (!ok) { System.out.println("FAIL got=" + res); throw new RuntimeException("FAILED"); }
        System.out.println("PASS");
    }
}
'''

mapping = {
    "solution_1_1_____1______.java": classA,
    "solution_2_2____2_____.java": classA,
    "solution_3_1_____1______.java": classB,
    "solution_4_2____2_____.java": classB,
    "solution_5_1_____1______.java": classB,
    "solution_6_2____2_____.java": classB,
}
for fn, content in mapping.items():
    with open(os.path.join(base, fn), "w") as f:
        f.write(content)
print("wrote 6 java files")
