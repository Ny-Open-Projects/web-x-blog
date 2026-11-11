/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135533027 */
/* LeetCode 208. 实现 Trie (前缀树) — C 版（方案2） */
#include <stdio.h>  // 引入头文件
#include <stdlib.h> // 引入头文件
#include <string.h> // 引入头文件
typedef struct TrieNode {
    struct TrieNode *children[26];
    int is_end;
} TrieNode;
static TrieNode *tn_new() { return calloc(1, sizeof(TrieNode)); }
static void tn_free(TrieNode *n) { // 定义函数/方法 tn_free
    if (!n)
        return; // 若 取反 元素个数) return;
    for (int i = 0; i < 26; i++)
        tn_free(n->children[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 26 就继续
    free(n);                     // free(元素个数);
}
static void trie_insert(TrieNode *root, const char *word) { // 定义函数/方法 trie_insert
    TrieNode *node = root;                                  // 把 根节点; 写入 TrieNode *node
    for (const char *p = word; *p; p++) { // 把 单词; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        int idx = *p - 'a';               // 把 乘 节点 减 '数组' 存入 idx
        if (!node->children[idx])
            node->children[idx] = tn_new();
        node = node->children[idx]; // 把 节点 减 超过 children[idx]; 写入 节点
    }
    node->is_end = 1; // 把 1; 写入 node->is_end
}
static TrieNode *trie_walk(TrieNode *root, const char *s) {
    TrieNode *node = root;             // 把 根节点; 写入 TrieNode *node
    for (const char *p = s; *p; p++) { // 把 字符串; 乘 节点; 节点 加一 ) { 写入 for (const char *p
        int idx = *p - 'a';            // 把 乘 节点 减 '数组' 存入 idx
        if (idx < 0 || idx >= 26)
            return NULL; // 若 idx 小于 0 或 idx 不低于 26，直接返回 NULL
        if (!node->children[idx])
            return NULL;            // 若 取反 节点 减 超过 children[idx]，直接返回 NULL
        node = node->children[idx]; // 把 节点 减 超过 children[idx]; 写入 节点
    }
    return node; // 返回 节点
}
static int trie_search(TrieNode *root, const char *word) { // 定义函数/方法 trie_search
    TrieNode *n = trie_walk(root, word); // 把 trie_walk(根节点, 单词); 写入 TrieNode *n
    return n && n->is_end;               // 返回 元素个数 且 元素个数 减 超过 is_end
}
static int trie_starts(TrieNode *root, const char *prefix) { return trie_walk(root, prefix) != NULL; }
int main(void) {             // 程序入口：跑内嵌自测用例
    TrieNode *t = tn_new();  // 把 tn_new(); 写入 TrieNode *t
    trie_insert(t, "apple"); // trie_insert(另一字符串, 「apple」);
    if (!trie_search(t, "apple")) {
        printf("FAIL 1\n");
        return 1;
    } // 若 取反 trie_search(另一字符串, 「apple」)) { 输出「apple」); return 1; }
    if (trie_search(t, "app")) {
        printf("FAIL 2\n");
        return 1;
    } // 若 trie_search(另一字符串, 「app」)) { 输出「app」); return 1; }
    if (!trie_starts(t, "app")) {
        printf("FAIL 3\n");
        return 1;
    } // 若 取反 trie_starts(另一字符串, 「app」)) { 输出「app」); return 1; }
    if (trie_search(t, "appl")) {
        printf("FAIL 4\n");
        return 1;
    }                 // 若 trie_search(另一字符串, 「appl」)) { 输出「appl」); return 1; }
    tn_free(t);       // tn_free(另一字符串);
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
