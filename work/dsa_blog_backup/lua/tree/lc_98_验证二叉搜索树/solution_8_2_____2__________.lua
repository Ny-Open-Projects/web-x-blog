-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135314196
-- LeetCode 98. 验证二叉搜索树 — Lua 版（方案8）
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

local function is_valid_bst(root) -- local function is_valid_bst(根节点)
	if not root then
		return true
	end -- 若 not 根节点 then return true 终点
	local stack = { { root, nil, nil } } -- 把 {{根节点, nil, nil}} 写入 local stack
	while #stack > 0 do -- while #栈 超过 0 do
		local node, low, high = table.unpack(table.remove(stack)) -- 把 table.unpack(table 弹出 栈)) 写入 local node, low, high
		if low and node.val <= low then
			return false
		end -- 若 low and 节点.值 不超过 low then return false 终点
		if high and node.val >= high then
			return false
		end -- 若 high and 节点.值 不低于 high then return false 终点
		if node.right then
			stack[#stack + 1] = { node.right, node.val, high }
		end -- 若 节点.右边界 then 栈[#栈 加 1] 赋值为 {节点.右边界, 节点.值, high} 终点
		if node.left then
			stack[#stack + 1] = { node.left, low, node.val }
		end -- 若 节点.左边界 then 栈[#栈 加 1] 赋值为 {节点.左边界, low, 节点.值} 终点
	end -- 终点
	return true -- 返回 true
end -- 终点
assert(is_valid_bst(build_tree({ 2, 1, 3 })) == true) -- 断言校验
assert(is_valid_bst(build_tree({ 5, 1, 4, "null", "null", 3, 6 })) == false) -- 断言校验
assert(is_valid_bst(nil) == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
