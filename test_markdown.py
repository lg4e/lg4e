from markdown import markdown
from markdown_katex import KatexExtension

test_markdown = """
示例:
$${a, b} = {b, a}$$
$${a, a, b} = {a, b}$$
"""

# 移除无效参数
html_content = markdown(
    test_markdown,
    extensions=[KatexExtension(strict="ignore", throwOnError=False)]
)

print(html_content)

