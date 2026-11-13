-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
-- 计算思维之下楼梯台阶和象棋跳马问题 — Lua 版（方案3）
local function climb_stairs_variants(n) -- local function climb_stairs_variants(元素个数)
	if n <= 1 then
		return 1
	end -- 若 元素个数 不超过 1 then return 1 终点
	local a, b = 1, 1 -- 把 1, 1 写入 local a, b
	for _ = 2, n do
		a, b = b, a + b
	end -- 让 _ 从 2 走到 元素个数（Lua 1 基）
	return b -- 返回 b
end -- 终点
assert(climb_stairs_variants(10) == 89) -- 断言校验
assert(climb_stairs_variants(1) == 1) -- 断言校验
assert(climb_stairs_variants(2) == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
