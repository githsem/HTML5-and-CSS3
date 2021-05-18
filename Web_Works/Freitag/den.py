word = input()
i=0
j=len(word)-1
dif=0

while i <= len(word)/2 + 1:
    if word[i] != word[j]:
        dif +=1
    i+=1
    j-=1
if dif != 0:
    print("nicht Gleich")
else:
    print("Gleich")            