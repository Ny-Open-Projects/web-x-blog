-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
-- LeetCode 116. 填充每个节点的下一个右侧节点指针 — Lua 版（方案3）
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

local NNode = {} -- 把 {} 写入 local NNode
NNode.__index = NNode -- 把 NNode 写入 NNode.__index
function NNode.new(v)
	return setmetatable({ val = v, left = nil, right = nil, next = nil }, NNode)
end
local function build_ntree(vals) -- local function build_ntree(vals)
	if #vals == 0 then
		return nil
	end -- 若 #vals 等于 0 then return nil 终点
	local root = NNode.new(vals[1]) -- 把 NNode.new(vals[1]) 写入 local root
	local q = { root } -- 把 {根节点} 写入 local q
	local head, i = 1, 2 -- 把 1, 2 写入 local head, i
	while head <= #q and i <= #vals do -- 把 #节点 and 下标 i 不超过 #vals do 写入 while head <
		local node = q[head] -- 把 节点[头节点] 写入 local node
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		if i <= #vals then
			node.left = NNode.new(vals[i])
			q[#q + 1] = node.left
			i = i + 1
		end
		if i <= #vals then
			node.right = NNode.new(vals[i])
			q[#q + 1] = node.right
			i = i + 1
		end
	end -- 终点
	return root -- 返回 根节点
end -- 终点
local function connect(root) -- local function connect(根节点)
	if not root then
		return nil
	end -- 若 not 根节点 then return nil 终点
	local queue = { root } -- 把 {根节点} 写入 local queue
	while #queue > 0 do -- while #队列 超过 0 do
		local size = #queue -- 把 #队列 写入 local size
		local prev = nil -- 把 nil 写入 local prev
		for _ = 1, size do -- 让 _ 从 1 走到 大小（Lua 1 基）
			local node = table.remove(queue, 1) -- 把 table 弹出 队列, 1) 写入 local node
			if prev then
				prev.next = node
			end -- 若 前一个 then 前一个.下一个 赋值为 节点 终点
			prev = node -- 把 节点 存入 前一个
			if node.left then
				queue[#queue + 1] = node.left
			end -- 若 节点.左边界 then 队列[#队列 加 1] 赋值为 节点.左边界 终点
			if node.right then
				queue[#queue + 1] = node.right
			end -- 若 节点.右边界 then 队列[#队列 加 1] 赋值为 节点.右边界 终点
		end -- 终点
	end -- 终点
	return root -- 返回 根节点
end -- 终点
assert(connect(nil) == nil) -- 断言校验
local root = connect(build_ntree({ 1, 2, 3, 4, 5, 6, 7 })) -- 把 connect(build_ntree({1, 2, 3, 4, 5, 6, 7})) 写入 local root
local levels = {} -- 把 {} 写入 local levels
local cur = root -- 把 根节点 写入 local cur
while cur do -- while 当前值 do
	local vals = {} -- 把 {} 写入 local vals
	local node = cur -- 把 当前值 写入 local node
	while node do -- while 节点 do
		vals[#vals + 1] = node.val -- 把 节点.值 写入 vals[#vals + 1]
		node = node.next -- 把 节点.下一个 存入 节点
	end -- 终点
	levels[#levels + 1] = vals -- 把 vals 写入 levels[#levels + 1]
	cur = cur.left -- 把 当前值.左边界 存入 当前值
end -- 终点
assert(#levels == 3) -- 断言校验
assert(#levels[1] == 1 and levels[1][1] == 1) -- 断言校验
assert(#levels[2] == 2 and levels[2][1] == 2 and levels[2][2] == 3) -- 断言校验
assert(#levels[3] == 4 and levels[3][1] == 4 and levels[3][4] == 7) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
