def isAnagram(s: str, t: str):
        result = False
        a = []
        b = []
        count1 = 0
        count2 = 0
        if(len(s) == len(t)):
            for i in range(0,len(s)):
                if(s[i] not in a):
                    a.append(s[i])
                else:
                    count1 = count1 + 1 
                    print(i,count1)
                if(t[i] not in b):
                    b.append(t[i])
                else:
                    count2 = count2 + 1
                    print(i,count2)
            if(len(a) == len(b) and (count1 == count2)):
                for j in range(0,len(a)):
                    if(a[j] in b):
                        result = True
                    else:
                        result =  False
            else:
                result = False
        else:
            result = False

        return result

print(isAnagram("bbcc","cbcc"))