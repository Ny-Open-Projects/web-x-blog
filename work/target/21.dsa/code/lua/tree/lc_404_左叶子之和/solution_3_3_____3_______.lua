-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136391511
-- LeetCode 404. 左叶子之和 — Lua 版（方案3）
local TreeNode = {} -- 把 {} 写入 local TreeNode
TreeNode.__index = TreeNode -- 把 TreeNode 写入 TreeNode.__index
function TreeNode.new(val) -- function TreeNode.new(值)
	return setmetatable({ val = val, left = nil, right = nil }, TreeNode)
end -- 终点

local function build_tree(vals) -- local function build_tree(vals)
	if not vals or #vals == 0 or vals[1] == "null" then
		return nil
	end
	local root = TreeNode.new(vals[1]) -- 把 TreeNode.new(vals[1]) 写入 local root
	local queue = { root } -- 把 {根节点} 写入 local queue
	local head = 1 -- 把 1 写入 local head
	local i = 2 -- 把 2 写入 local i
	while head <= #queue and i <= #vals do -- 把 #队列 and 下标 i 不超过 #vals do 写入 while head <
		local node = queue[head] -- 把 队列[头节点] 写入 local node
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		if i <= #vals then -- 若 下标 i 不超过 #vals then
			if vals[i] ~= "null" then -- 若 vals[下标 i] ~ 赋值为 「null」 then
				node.left = TreeNode.new(vals[i]) -- 把 TreeNode.new(vals[下标 i]) 写入 左边界
				queue[#queue + 1] = node.left -- 把 节点.左边界 写入 queue[#queue + 1]
			end -- 终点
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
		if i <= #vals then -- 若 下标 i 不超过 #vals then
			if vals[i] ~= "null" then -- 若 vals[下标 i] ~ 赋值为 「null」 then
				node.right = TreeNode.new(vals[i]) -- 把 TreeNode.new(vals[下标 i]) 写入 右边界
				queue[#queue + 1] = node.right -- 把 节点.右边界 写入 queue[#queue + 1]
			end -- 终点
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
	end -- 终点
	return root -- 返回 根节点
end -- 终点

local function is_leaf(n) -- local function is_leaf(元素个数)
	return n and not n.left and not n.right -- 返回 元素个数 and not 元素个数.左边界 and not 元素个数.右边界
end -- 终点
local function sum_of_left_leaves(root) -- local function sum_of_left_leaves(根节点)
	if not root then
		return 0
	end -- 若 not 根节点 then return 0 终点
	local total = 0 -- 把 0 写入 local total
	local stack = { root } -- 把 {根节点} 写入 local stack
	while #stack > 0 do -- while #栈 超过 0 do
		local node = table.remove(stack) -- 把 table 弹出 栈) 写入 local node
		if node.left then -- 若 节点.左边界 then
			if is_leaf(node.left) then
				total = total + node.left.val -- 若 is_leaf(节点.左边界) then 总和 赋值为 总和 加 节点.左边界.值
			else
				stack[#stack + 1] = node.left
			end -- 否则
		end -- 终点
		if node.right then
			stack[#stack + 1] = node.right
		end -- 若 节点.右边界 then 栈[#栈 加 1] 赋值为 节点.右边界 终点
	end -- 终点
	return total -- 返回 总和
end -- 终点
assert(sum_of_left_leaves(build_tree({ 3, 9, 20, "null", "null", 15, 7 })) == 24) -- 断言校验
assert(sum_of_left_leaves(nil) == 0) -- 断言校验
assert(sum_of_left_leaves(build_tree({ 1, 2, 3, 4, 5 })) == 4) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
