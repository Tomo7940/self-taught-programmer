answer = input("what do you like about food?")

with open("answer.txt", "w", encoding="utf-8") as f:
    f.write(answer)