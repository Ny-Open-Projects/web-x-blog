/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
 * LeetCode 622. 设计循环队列 — C 版 */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件

/* 方案6：数组 + front/rear/size 循环队列 */
typedef struct {   // typedef struct {
    int capacity;  // int capacity;
    int *data;     // int 乘 data;
    int front;     // int front;
    int rear;      // int rear;
    int size;      // int 大小;
} MyCircularQueue; // } MyCircularQueue;

static MyCircularQueue *cq_new(int k) { // static MyCircularQueue 乘 cq_new(int 下标 k) {
    MyCircularQueue *q = (MyCircularQueue *)malloc(sizeof(MyCircularQueue));
    q->capacity = k; // 把 下标 k; 写入 q->capacity
    q->data = (int *)calloc((size_t)k,
                            sizeof(int)); // 把 (int 乘 )calloc((size_t)下标 k, sizeof(int)); 写入 q->data
    q->front = 0;                         // 把 0; 写入 q->front
    q->rear = 0;                          // 把 0; 写入 q->rear
    q->size = 0;                          // 把 0; 写入 q->size
    return q;                             // 返回 节点
}

static void cq_free(MyCircularQueue *q) { // 定义函数/方法 cq_free
    free(q->data);                        // free(节点 减 超过 data);
    free(q);                              // free(节点);
}

static int cq_is_empty(const MyCircularQueue *q) { return q->size == 0; }
static int cq_is_full(const MyCircularQueue *q) { return q->size == q->capacity; }

static int cq_en_queue(MyCircularQueue *q, int value) { // 定义函数/方法 cq_en_queue
    if (cq_is_full(q))
        return 0;             // 若 cq_is_full(节点)，直接返回 0
    q->data[q->rear] = value; // 把 value; 写入 q->data[q->rear]
    q->rear = (q->rear + 1) %
              q->capacity; // 把 (节点 减 超过 rear 加 1) 对…取模 节点 减 超过 capacity; 写入 q->rear
    q->size += 1; // 把 1; 写入 q->size +
    return 1;     // 返回 1
}

static int cq_de_queue(MyCircularQueue *q) { // 定义函数/方法 cq_de_queue
    if (cq_is_empty(q))
        return 0; // 若 cq_is_empty(节点)，直接返回 0
    q->front = (q->front + 1) %
               q->capacity; // 把 (节点 减 超过 front 加 1) 对…取模 节点 减 超过 capacity; 写入 q->front
    q->size -= 1; // 把 1; 写入 q->size -
    return 1;     // 返回 1
}

static int cq_front(const MyCircularQueue *q) { // 定义函数/方法 cq_front
    if (cq_is_empty(q))
        return -1;            // 若 cq_is_empty(节点)，直接返回 减 1
    return q->data[q->front]; // 返回 节点 减 超过 data[节点 减 超过 front]
}

static int cq_rear(const MyCircularQueue *q) { // 定义函数/方法 cq_rear
    if (cq_is_empty(q))
        return -1; // 若 cq_is_empty(节点)，直接返回 减 1
    return q->data[(q->rear - 1 + q->capacity) % q->capacity];
}

int main(void) { // 程序入口：跑内嵌自测用例
    /* 与 TS 事实源内嵌用例一致：[true,true,true,false,3,true,true,true,4]
     * 布尔结果用 1/0 表示 */
    MyCircularQueue *q = cq_new(3);            // 把 cq_new(3); 写入 MyCircularQueue *q
    int got[9];                                // int got[9];
    got[0] = cq_en_queue(q, 1);                // 把 cq_en_queue(节点, 1); 写入 got[0]
    got[1] = cq_en_queue(q, 2);                // 把 cq_en_queue(节点, 2); 写入 got[1]
    got[2] = cq_en_queue(q, 3);                // 把 cq_en_queue(节点, 3); 写入 got[2]
    got[3] = cq_en_queue(q, 4);                // 把 cq_en_queue(节点, 4); 写入 got[3]
    got[4] = cq_rear(q);                       // 把 cq_rear(节点); 写入 got[4]
    got[5] = cq_is_full(q);                    // 把 cq_is_full(节点); 写入 got[5]
    got[6] = cq_de_queue(q);                   // 把 cq_de_queue(节点); 写入 got[6]
    got[7] = cq_en_queue(q, 4);                // 把 cq_en_queue(节点, 4); 写入 got[7]
    got[8] = cq_rear(q);                       // 把 cq_rear(节点); 写入 got[8]
    cq_free(q);                                // cq_free(节点);
    int want[9] = {1, 1, 1, 0, 3, 1, 1, 1, 4}; // 把 { 1, 1, 1, 0, 3, 1, 1, 1, 4 }; 写入 int want[9]
    for (int i = 0; i < 9; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 9 就继续
        if (got[i] != want[i]) {  // 若 got[下标 i] 不等于 want[下标 i]
            printf("FAIL idx %d got %d want %d\n", i, got[i], want[i]); // 打印输出
            return 1;                                                   // 返回 1
        }
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
