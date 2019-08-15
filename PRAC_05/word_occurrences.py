counttext = {}
text = input("Text: ")
splitting = text.split()
for a in splitting:
    freq = counttext.get(a, 0)
    counttext[a] = freq + 1

splitting = list(counttext.keys())
splitting.sort()

max_len = max((len(a) for a in splitting))
for a in splitting:
    print("{:{}} : {}". format(a, max_len, counttext[a]))
