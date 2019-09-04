from programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
c = ProgrammingLanguage("C++", "Static", False, 1983)
java = ProgrammingLanguage("Java", "Static", True, 1995)

print(ruby)
print(python)
print(visual_basic)
print(c)
print(java)

newlist = [ruby, python, visual_basic, c, java]
print("Dynamically typed coding are:")
for languages in newlist:
    if languages.is_dynamic():
        print(languages.coding)