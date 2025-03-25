import os
import re

# 配置参数
TXT_FOLDER = "书txt"       # 存放TXT文件的文件夹路径
HTML_FILE = "index.html"   # 要更新的HTML文件路径

def generate_button_links():
    """生成所有TXT文件的按钮链接"""
    buttons = []
    for filename in os.listdir(TXT_FOLDER):
        if filename.endswith(".txt"):
            # 生成类似 <a href="书txt/文件名.txt" class="button" target="_blank">文件名.txt</a> 的代码
            button = f'<a href="{TXT_FOLDER}/{filename}" class="button" target="_blank">{filename}</a>'
            buttons.append(button)
    return "\n    ".join(buttons)

def update_html(new_content):
    """更新HTML文件内容"""
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # 使用正则表达式定位需要替换的区域
    pattern = re.compile(
        r'<div class="container">\s*<h1>查看TXT文件</h1>.*?</div>',
        re.DOTALL
    )
    
    # 构建新内容
    replacement = f'''<div class="container">
    <h1>查看TXT文件</h1>
    {new_content}
</div>'''

    new_html = re.sub(pattern, replacement, html)
    
    # 写回文件
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)

if __name__ == "__main__":
    buttons = generate_button_links()
    update_html(buttons)
    print(f"已成功更新 {HTML_FILE}，生成 {buttons.count('</a>')} 个文件按钮")