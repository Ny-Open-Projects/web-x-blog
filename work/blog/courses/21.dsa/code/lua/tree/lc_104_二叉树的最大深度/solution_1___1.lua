-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
-- LeetCode 104. 二叉树的最大深度 — Lua 版

local TreeNode = {} -- 把 {} 写入 local TreeNode
TreeNode.__index = TreeNode -- 把 TreeNode 写入 TreeNode.__index
function TreeNode.new(val) -- function TreeNode.new(值)
	return setmetatable({ val = val, left = nil, right = nil }, TreeNode)
end -- 终点

-- 层序数组构建二叉树，nil 表示空节点；注意 Lua 中用 "null" 字符串占位
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

-- 主解法：DFS，叶子节点时刷新最大深度（与 blog 方案1一致）
local function max_depth(root) -- local function max_depth(根节点)
	local dep = 0 -- 把 0 写入 local dep
	local function dfs(n, l) -- local function dfs(元素个数, 左指针)
		if not n then
			return
		end -- 若 not 元素个数 then return 终点
		if not n.left and not n.right then -- 若 not 元素个数.左边界 and not 元素个数.右边界 then
			if l > dep then
				dep = l
			end -- 若 左指针 超过 dep then dep 赋值为 左指针 终点
		end -- 终点
		dfs(n.left, l + 1) -- dfs(元素个数.左边界, 左指针 加 1)
		dfs(n.right, l + 1) -- dfs(元素个数.右边界, 左指针 加 1)
	end -- 终点
	dfs(root, 1) -- dfs(根节点, 1)
	return dep -- 返回 dep
end -- 终点

-- 自测：与 LeetCode 官方用例一致
local tests = { -- 把 { 写入 local tests
	{ {}, 0 },
	{ { 1 }, 1 },
	{ { 3, 9, 20, "null", "null", 15, 7 }, 3 },
	{ { 1, "null", 2, "null", 3 }, 3 },
}
for idx, t in ipairs(tests) do -- 遍历取 另一字符串
	local got = max_depth(build_tree(t[1])) -- 把 max_depth(build_tree(另一字符串[1])) 写入 local got
	local want = t[2] -- 把 另一字符串[2] 写入 local want
	assert(got == want, string.format("case %d failed: got %d want %d", idx, got, want)) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
