def find_all(a_str, sub, overlap=False):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        if overlap:
            start += 1
            continue
        start += len(sub)


with open('README.md', 'r') as file:
    content = file.read()

_content = ""
_end = -1
ignore = ["#usage"]
base = 'https://github.com/Amith225/NPerlinNoise/tree/master/'
for start, end in zip(find_all(content, '['), find_all(content, ']')):
    _content += content[_end + 1:start]
    end += 1
    alt_text = content[start:end]
    _start, _end = end + 1, content.find(')', end)
    link = content[_start:_end]
    if not link.startswith('http') and link not in ignore: link = base + link
    _content += alt_text + f"({link})"
_content += content[_end + 1:]

with open('README.pypi.md', 'w+') as file:
    file.write(_content)