-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
-- LeetCode 133270489. 原型链原理 — Lua 版（方案1：instanceOf 沿原型链判定）
local Proto = {} -- 把 {} 写入 local Proto
Proto.__index = Proto -- 把 Proto 写入 Proto.__index
function Proto.new(name, parent) -- function Proto.new(name, parent)
	return setmetatable({ name = name, props = {}, parent = parent }, Proto)
end -- 终点

local function instance_of(obj, prototype) -- local function instance_of(obj, prototype)
	local p = obj -- 把 obj 写入 local p
	while p ~= nil do -- 把 nil do 写入 while p ~
		if p == prototype then
			return true
		end -- 若 节点 等于 prototype then return true 终点
		p = p.parent -- 把 节点.parent 存入 节点
	end -- 终点
	return false -- 返回 false
end -- 终点

local object_proto = Proto.new("Object.prototype", nil) -- 把 Proto.new(「Object.prototype」, nil) 写入 local object_proto
local function_proto = Proto.new("Function.prototype", object_proto)
local array_proto = Proto.new("Array.prototype", object_proto)
local obj = Proto.new("obj", object_proto) -- 把 Proto.new(「obj」, object_proto) 写入 local obj
local func = Proto.new("func", function_proto) -- 把 Proto.new(「func」, function_proto) 写入 local func
local arr = Proto.new("arr", array_proto) -- 把 Proto.new(「数组」, array_proto) 写入 local arr

local cases = { -- 把 { 写入 local cases
	{ instance_of(obj, object_proto), true },
	{ instance_of(func, function_proto), true },
	{ instance_of(func, object_proto), true },
	{ instance_of(arr, array_proto), true },
	{ instance_of(arr, object_proto), true },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	assert(c[1] == c[2], "case " .. idx .. " failed") -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
