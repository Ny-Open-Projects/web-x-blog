-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
-- LeetCode 133270489. 原型链原理 — Lua 版（方案4：null/undefined 边界：instanceOf 均返回 false）
local function instance_of(a, b) -- local function instance_of(数组, b)
	local p = a -- 把 数组 写入 local p
	while p ~= nil do -- 把 nil do 写入 while p ~
		if p == b.prototype then
			return true
		end -- 若 节点 等于 b.prototype then return true 终点
		p = p.__proto__ -- 把 节点.__proto__ 存入 节点
	end -- 终点
	return false -- 返回 false
end -- 终点

local ctor = { prototype = nil } -- 把 { prototype 赋值为 nil } 写入 local ctor
assert(instance_of(nil, ctor) == false, "null case failed") -- 断言校验
assert(instance_of(nil, ctor) == false, "undefined case failed") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
