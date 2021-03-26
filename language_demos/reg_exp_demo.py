import re

# content = "as busy as a bee"

# r = re.compile(r'as')

# starts from the beginning of the content
# print(r.match(content))

# search anywhere in the content, find the first one
# print(r.search(content))

# returns all of the string content matches without span data
# print(r.findall(content))

# returns match objects for all matches in the content
# print(list(r.finditer(content)))

# content = "red|green;blue:yellow"
# # print(content.split("|").split(";").split(":"))
# # r = re.compile(r"\||:|;")
# r = re.compile(r"[|:;]")
# print(r.split(content))
# print(r.sub(",", content))

# content = """apple
# banana
# apple
# banana
# Banana
# apple
# avocado
# """

# # r = re.compile(r"^a[a-z]*", re.MULTILINE)
# r = re.compile(r"[a-z]*a$", re.MULTILINE | re.IGNORECASE)

# print(list(r.finditer(content)))

# content = "<b>content 1</b><span>test</span><b>content 2</b><div>fun</div>"

# # r = re.compile(r"<span>(.*)</span>")
# # r = re.compile(r"<b>(.*?)</b>")
# r = re.compile(r"<.*?>(.*?)</.*?>")

# # m = r.search(content)
# # print(m.groups())

# for m in r.finditer(content):
#     print(m.groups()[0])


# print(list(r.finditer(content)))

r = re.compile(r"^Add: ([0-9]*)", re.MULTILINE)

with open("./report.txt", "r") as report_file:

    report_content = report_file.read()
    add_count_match = r.search(report_content)
    print(add_count_match.groups()[0])
