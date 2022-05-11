import html
# s = "&#8231;"
# s = "&#x00B7;"
s = "O&#770;&#770;"
reg = "(&#?\\w{2,7};)"
print(html.unescape(s))
