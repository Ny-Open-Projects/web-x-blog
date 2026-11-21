"""subTest:循环参数化,失败逐个记录互不阻断。"""
import io
import unittest


def slugify(text):
    """带一个已知瑕疵的实现,供特征对照。"""
    return text.strip().lower().replace(" ", "-")


class SlugifyTest(unittest.TestCase):
    CASES = [
        ("Hello World", "hello-world"),
        ("  Trim  ", "trim"),
        ("Multiple   Spaces", "multiple-spaces"),      # 当前实现会失败
    ]

    def test_cases(self):
        for text, expected in self.CASES:
            with self.subTest(text=text):
                self.assertEqual(slugify(text), expected)


if __name__ == "__main__":
    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=0)
    result = runner.run(unittest.TestLoader().loadTestsFromTestCase(SlugifyTest))
    print("失败数:", len(result.failures), "(失败场景已逐个列出,循环未中断)")
    for _, tb in result.failures:
        print(tb.splitlines()[0])
