-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133886377
-- LeetCode 237. 删除链表中的节点 — Lua 版（方案1）
local ListNode = {} -- 把 {} 写入 local ListNode
ListNode.__index = ListNode -- 把 ListNode 写入 ListNode.__index
function ListNode.new(val, next)
	return setmetatable({ val = val, next = next }, ListNode)
end
local function build_list(vals) -- local function build_list(vals)
	local head, cur = nil, nil -- 把 nil, nil 写入 local head, cur
	for _, v in ipairs(vals) do -- 遍历取 值
		local n = ListNode.new(v) -- 把 ListNode.new(值) 写入 local n
		if not head then
			head, cur = n, n
		else
			cur.next, cur = n, n
		end
	end -- 终点
	return head -- 返回 头节点
end -- 终点
local function to_vec(h) -- local function to_vec(h)
	local out = {} -- 把 {} 写入 local out
	while h do
		out[#out + 1] = h.val
		h = h.next
	end -- 把 h.值; h 赋值为 h.下一个 终点 写入 while h do out[#out + 1]
	return out -- 返回 out
end -- 终点
local function delete_node(node) -- local function delete_node(节点)
	node.val = node.next.val -- 把 节点.下一个.值 写入 值
	node.next = node.next.next -- 把 节点.下一个.下一个 写入 下一个
end -- 终点
local l = build_list({ 4, 5, 1, 9 }) -- 把 build_list({4, 5, 1, 9}) 写入 local l
delete_node(l.next) -- 删除节点 5
assert(table.concat(to_vec(l), ",") == "4,1,9") -- 打印输出
local l2 = build_list({ 1, 2, 3 }) -- 把 build_list({1, 2, 3}) 写入 local l2
delete_node(l2.next) -- 删除节点 2
assert(table.concat(to_vec(l2), ",") == "1,3") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
