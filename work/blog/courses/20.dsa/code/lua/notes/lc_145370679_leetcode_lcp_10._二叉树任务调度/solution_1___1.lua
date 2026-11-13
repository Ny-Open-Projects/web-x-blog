-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
-- LeetCode LCP 10. 二叉树任务调度 — Lua 版（方案1：深度优先-贪心）

-- 层序数组建树：用 "n" 字符串表示空节点（nil 会把数组截断）
local function new_node(val)
	return { val = val, left = nil, right = nil } -- 二叉树节点：val 为自身执行时间
end

local function build_tree(vals)
	if #vals == 0 then
		return nil
	end
	local root = new_node(vals[1])
	local queue = { root } -- 队列里只放非空节点
	local head, i = 1, 2
	while head <= #queue and i <= #vals do
		local node = queue[head] -- 出队一个父节点
		head = head + 1
		if i <= #vals and vals[i] ~= "n" then -- 左孩子
			node.left = new_node(vals[i])
			queue[#queue + 1] = node.left
		end
		i = i + 1
		if i <= #vals and vals[i] ~= "n" then -- 右孩子
			node.right = new_node(vals[i])
			queue[#queue + 1] = node.right
		end
		i = i + 1
	end
	return root
end

-- dfs 返回 子树总耗时, 两台机器并行可节省的耗时（Lua 多返回值）
local function dfs(root)
	if root == nil then
		return 0.0, 0.0
	end -- 空子树：总耗时 0，节省 0
	local a, b = dfs(root.left) -- a: 左子树总耗时, b: 左子树已节省
	local c, d = dfs(root.right) -- c: 右子树总耗时, d: 右子树已节省
	local saved
	if (c - 2 * d <= a and a <= c) or (a - 2 * b <= c and c <= a) then
		-- 一侧的串行下界落在另一侧的耗时区间内：两台机器互相填空，左右几乎完全并行
		saved = (a + c) / 2.0 -- Lua 的 / 永远是浮点除法：总和为奇数时会出现 0.5
	elseif a - 2 * b > c then
		-- 左子树串行段太长：右子树整体塞进左边空闲的那台机器
		saved = b + c
	else
		-- 右子树占主导：左子树整体塞进右边空闲的那台机器
		saved = a + d
	end
	return a + c + root.val, saved -- 加上当前节点自身的执行时间
end

local function minimal_execution_time(root) -- 答案 = 子树总和 - 并行节省
	local total, saved = dfs(root)
	return total - saved
end

local cases = { -- 三个官方用例
	{ { 47, 74, 31 }, 121.0 },
	{ { 15, 21, "n", 24, "n", 27, 26 }, 87.0 },
	{ { 1, 3, 2, "n", "n", 4, 4 }, 7.5 },
}
local fail = false
for _, case in ipairs(cases) do
	local got = minimal_execution_time(build_tree(case[1]))
	if math.abs(got - case[2]) >= 1e-6 then -- 浮点比较用 1e-6 容差
		print("FAIL got", got, "want", case[2]) -- 失败打印 FAIL
		fail = true
	end
end
if fail then
	os.exit(1)
end -- 非零退出
print("PASS") -- 全部用例通过，输出 PASS
