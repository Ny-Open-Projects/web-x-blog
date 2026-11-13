-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133785568
-- LeetCode 206. 反转链表 — Lua 版（方案4）
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
local function reverse_list(head) -- local function reverse_list(头节点)
	local prev = nil -- 把 nil 写入 local prev
	local cur = head -- 把 头节点 写入 local cur
	while cur do -- while 当前值 do
		local nxt = cur.next -- 把 当前值.下一个 写入 local nxt
		cur.next = prev -- 把 前一个 写入 下一个
		prev = cur -- 把 当前值 存入 前一个
		cur = nxt -- 把 nxt 存入 当前值
	end -- 终点
	return prev -- 返回 前一个
end -- 终点
assert(table.concat(to_vec(reverse_list(build_list({ 1, 2, 3, 4, 5 }))), ",") == "5,4,3,2,1") -- 打印输出
assert(#to_vec(reverse_list(build_list({}))) == 0) -- 断言校验
assert(table.concat(to_vec(reverse_list(build_list({ 1 }))), ",") == "1") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
