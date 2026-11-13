-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874590
-- LeetCode 83. 删除排序链表中的重复元素 — Lua 版（方案6）
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
local function delete_duplicates(head) -- local function delete_duplicates(头节点)
	local cur = head -- 把 头节点 写入 local cur
	while cur and cur.next do -- while 当前值 and 当前值.下一个 do
		if cur.val == cur.next.val then -- 若 当前值.值 等于 当前值.下一个.值 then
			cur.next = cur.next.next -- 把 当前值.下一个.下一个 写入 下一个
		else -- 否则
			cur = cur.next -- 把 当前值.下一个 存入 当前值
		end -- 终点
	end -- 终点
	return head -- 返回 头节点
end -- 终点
assert(table.concat(to_vec(delete_duplicates(build_list({ 1, 1, 2 }))), ",") == "1,2") -- 打印输出
assert(table.concat(to_vec(delete_duplicates(build_list({ 1, 1, 2, 3, 3 }))), ",") == "1,2,3") -- 打印输出
assert(table.concat(to_vec(delete_duplicates(build_list({ 1, 1, 1 }))), ",") == "1") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
