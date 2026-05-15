import re
text = "hello world"
a = re.search("^hello",text)
print(a)

#endswith
import re
text = "hello world"
a = re.search("hello$",text)
print(a)
if a is not None:
    print("match is not found")
else:
    print("match found")

#findall(. any word)
import re
text = "hello world"
a = re.findall("hel..",text)
print(a)

