def normalize(text, casefold, yo2e):
    if yo2e:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")

    if casefold:
        text = text.casefold()

    text = text.replace("\\n", " ")
    text = text.replace("\\t", " ")
    text = text.replace("\\r", " ")

    text_lst = text.split()

    normalize_text = ""
    for i in text_lst:
        normalize_text += i + " "

    return normalize_text.strip()

#print(normalize('ПрИвЕт\\nМИр\\t', True, True))

def tokenize(text):
    base = (
        text.replace(".", " ")
        .replace(",", " ")
        .replace("!", " ")
        .replace(":", " ")
        .replace(";", " ")
        .replace("?", "")
    )
    base = base.split()
    ans = []

    for i in base:
        if i[0].isdigit() == 0 and i[0].isalpha() == 0:
            pass
        else:
            ans.append(i)
    return ans

print(tokenize("emoji 😀 не слово"))

def count_freq(lst):
    ans_items = []
    ans_keys = []
    ans = {}

    for i in lst:
        if i in ans_items:
            pass
        else:
            ans_items.append(i)

    for j in ans_items:
        ans_keys.append(lst.count(j))

    for k in range(len(ans_keys)):
        ans.update({ans_items[k]: ans_keys[k]})

    return ans


def top_n(dict, n=2):
    ans = sorted(list(dict.items()), key=lambda x: (-x[1], x[0]))
    return ans[:n]
