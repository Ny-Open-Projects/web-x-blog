# 实际项目应 from myproj.core import xxx,这里演示 src 布局的 import 纪律
def import_check():
    # 平铺布局下 pytest 根目录可直接 import myproj
    # src 布局下必须先 pip install -e . 否则 ImportError —— 这正是保护
    return "installed or editable install required"

def test_layout_discipline():
    assert "install" in import_check()
