#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
runref.py — 运行博客 python 参考实现，针对给定输入计算 expected 输出。
用法:
  python3 runref.py <pyfile> '<json list of calls>' [--sig]
每个 call 是一个参数列表(位置参数), 元素为 JSON 可序列化值。
对于树/链表的输入用 LeetCode 风格 list 表示, 本脚本内部 build_tree/build_listnode 还原。
输出: JSON 数组, 与输入一一对应。
特殊: 若某 call 第一个元素是字符串 "__build_tree__", 则其后的 list 被 build 为 TreeNode 再传入。
      若第一个元素是 "__build_listnode__", 其后 list 被 build 为 ListNode。
      若第一个元素是 "__raw__", 则后面的参数保持 JSON 原样 (不 build)。
默认: 若函数名暗示 (tree/listnode) 或参数看起来是 list-of-scalars 且函数名含 tree/list, 自动 build。
为简单: 统一约定 —— 调用方显式用 "__build_tree__"/"__build_listnode__" 包裹需要还原的参数。
"""
import sys, ast, json, os

HELPERS = {"print", "build_list", "print_list", "build_tree", "to_list",
           "list_to_arr", "demo", "helper", "main", "TreeNode", "ListNode",
           "ListNode", "Node"}

def find_func(src, ns):
    try:
        tree = ast.parse(src)
    except Exception:
        return None
    main_block = None
    for node in tree.body:
        if isinstance(node, ast.If):
            main_block = node.body; break
    for node in (main_block or []):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            f = node.value.func
            if isinstance(f, ast.Name) and f.id not in HELPERS:
                return f.id
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name not in HELPERS:
            return node.name
    return None

# ---- 结构 build / serialize ----
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val; self.left=left; self.right=right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val; self.next=next

def build_tree(vals):
    if not vals: return None
    root = TreeNode(vals[0])
    q=[root]; i=1
    while q and i < len(vals):
        n=q.pop(0)
        if vals[i] is not None:
            n.left=TreeNode(vals[i]); q.append(n.left)
        i+=1
        if i < len(vals) and vals[i] is not None:
            n.right=TreeNode(vals[i]); q.append(n.right)
        i+=1
    return root

def tree_to_list(root):
    if root is None: return []
    res=[]; q=[root]
    while q:
        n=q.pop(0)
        if n is None:
            res.append(None); continue
        res.append(n.val)
        q.append(n.left); q.append(n.right)
    while res and res[-1] is None: res.pop()
    return res

def build_listnode(vals):
    if not vals: return None
    head=ListNode(vals[0]); p=head
    for v in vals[1:]:
        p.next=ListNode(v); p=p.next
    return head

def listnode_to_list(head):
    res=[]; p=head
    while p:
        res.append(p.val); p=p.next
    return res

def to_jsonable(x):
    if x is None or isinstance(x,(int,float,str,bool)): return x
    if isinstance(x,(list,tuple)): return [to_jsonable(v) for v in x]
    if isinstance(x,set): return sorted(to_jsonable(v) for v in x)
    if isinstance(x,dict): return {str(k):to_jsonable(v) for k,v in x.items()}
    if isinstance(x,TreeNode): return tree_to_list(x)
    if isinstance(x,ListNode): return listnode_to_list(x)
    # duck typing for classes defined inside the executed source
    if hasattr(x,"left") and hasattr(x,"right"): return tree_to_list(x)
    if hasattr(x,"next") and hasattr(x,"val"): return listnode_to_list(x)
    return repr(x)

def main():
    pyfile=sys.argv[1]
    calls=json.loads(sys.argv[2])
    src=open(pyfile,encoding='utf-8').read()
    ns={"__name__":"_ref_","TreeNode":TreeNode,"ListNode":ListNode}
    exec(compile(src,pyfile,"exec"),ns)
    fname=find_func(src,ns)
    if not fname or fname not in ns:
        sys.stderr.write("FUNC_NOT_FOUND\n"); sys.exit(2)
    fnc=ns[fname]
    out=[]
    for call in calls:
        args=[]
        for a in call:
            if isinstance(a,dict) and a.get("__t")=="tree":
                args.append(build_tree(a["v"]))
            elif isinstance(a,dict) and a.get("__t")=="list":
                args.append(build_listnode(a["v"]))
            elif isinstance(a,dict) and a.get("__t")=="listoflist":
                args.append([build_listnode(x) for x in a["v"]])
            else:
                args.append(a)
        try:
            res=fnc(*args)
        except Exception as e:
            out.append({"__exc__":str(e)})
            continue
        out.append(to_jsonable(res))
    print(json.dumps(out,ensure_ascii=False))

if __name__=="__main__":
    main()
