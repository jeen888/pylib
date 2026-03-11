import textwrap

text = "This is a long text that needs to be wrapped."
text2 = "이것은 아주 긴 이야기이고, 약 2천년의 시간을 거슬러 올라간다."

# Wrap the text to a specified width
wrapped_text = textwrap.fill(text, width=20)
print(wrapped_text)
short_text = textwrap.shorten(text2, width=20, placeholder="...")
print(short_text)