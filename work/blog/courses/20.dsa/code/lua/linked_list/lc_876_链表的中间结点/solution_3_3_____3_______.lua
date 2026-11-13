-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133867938
-- LeetCode 876. 链表的中间结点 — Lua 版（方案3）
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
local function middle_node(head) -- local function middle_node(头节点)
	local slow, fast = head, head -- 把 头节点, 头节点 写入 local slow, fast
	while fast and fast.next do -- while 快指针 and 快指针.下一个 do
		slow = slow.next -- 把 慢指针.下一个 存入 慢指针
		fast = fast.next.next -- 把 快指针.下一个.下一个 存入 快指针
	end -- 终点
	return slow -- 返回 慢指针
end -- 终点
assert(table.concat(to_vec(middle_node(build_list({ 1, 2, 3, 4, 5 }))), ",") == "3,4,5") -- 打印输出
assert(table.concat(to_vec(middle_node(build_list({ 1, 2, 3, 4, 5, 6 }))), ",") == "4,5,6") -- 打印输出
assert(table.concat(to_vec(middle_node(build_list({ 1 }))), ",") == "1") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
