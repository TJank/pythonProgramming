# IN CLASS STUDY SESSION
# QUESTIONS AND HOMEWORK PROBLEM

a_string = "This sentence 12 contains the number twelve 1."

number = ""
for i in range(len(a_string)):
    if "1" == a_string[i] and "2" == a_string[i+1]:
        number += a_string[i] + a_string[i+1]

print(number)

# find <a in a string
html_string = "<p><a "

href = ""
for i in range(len(html_string)):
    if html_string[i] == "<" and html_string[i+1] == "a":
        tail = html_string[i+1:]
        if "href=''" in tail:
            idx = tail.index("href")
            idx += 6
            tail2 = tail[idx:]
            href = tail2[: tail2.index("'")]
        elif "href=\"" in tail:
            idx = tail.index("href")
            idx += 6
            tail2 = tail[idx:]
            href = tail2[: tail2.index('"')]



