def reverse_list(instr:str):
    return instr.split()[::-1]

def cnsqt(nums:list):
    for i in range(0,len(nums)):
        if(nums[i] == 3 and nums[i+1] == 3):
            return True
    return False

def uniqueString(instr:str):
    resstr = ""
    for i in range(len(instr)):
        if(instr[i] not in resstr):
            resstr = resstr + instr[i]
    
    return resstr

def blackJack(a,b,c):
    if(a,b,c in (range(0,11))):
        if(a+b+c <= 21):
            return a+b+c
        elif(a+b+c > 21 and (a == 11 or b == 11 or c == 11)):
            return a+b+c-10
        else:
            return "BUST"

def spy_game(nums:list):
    code = [0,0,7,"x"]

    for i in nums:
        if i == code[0]:
            code.pop(0)
    
    return len(code) == 1


#print(reverse_list("my name is manohar"))

#print(cnsqt([1,3,2,3,1,2,3,2]))

#print(uniqueString("ddddduuuurrrrgggaaaa"))

#print(blackJack(11,12,3))

print(spy_game([1,2,3,5,6,0,7,1,0]))