class pattern:
    def right_num_same(self,n):
        for i in range(n+1):
            for j in range(i):
                print(i,end="")
            print(" ")
    def right_num_diff(self,n):
        for i in range(1,n+2):
            for j in range(1,i):
                print(j,end="")
            print(" ")
    def invr_num_same(self,n):
        for i in range(1,n+2):
            for j in range(n,i,-1):
                print(i,end="")
            print(" ")
    def invr_same_num(self,n):
        for i in range(n):
            for j in range(n,i,-1):
                print("5",end="")
            print(" ")
    def half_invr_num(self,n):
        for i in range(n,0,-1):
            for j in range(0,i+1):
                print(j,end="")
            print(" ")
    def odd_num_tri(self,n):
        for i in range(1,n):
            if(i%2!=0):
                for j in range(i):
                    print(i,end="")
                print("")
    def rev_num_same(self,n):
        for i in range(n,0,-1):
            for j in range(i):
                print(i,end="")
            print(" ")
    def rev_num_diff(self,n):
        for i in range(n):
            for j in range(i,0,-1):
                print(j,end="")
            print(" ")
    def rev_num_rev_tri(self,n):
        for i in range(n,0,-1):
            for j in range(i,0,-1):
                print(j,end="")
            print(" ")
    def cnsqt_prmd(self,n):
        sum = 0
        for i in range(n):
            for j in range(i):
                sum = sum +1
                print(sum,end="")
            print("")
    def right_tri(self,n):
        for i in range(1,n):
            for j in range(n,0,-1):
                if j > i:
                    print(" ",end = " ")
                else:
                    print(j,end=" ")
            print(" ")
    def square_nums(self,n):
        for i in range(1,n):
            for j in range(1,n):
                if(j <= i):
                    print(i,end=" ")
                else:
                    print(j,end=" ")
            print(" ")
    def mul_table_pattern(self,n):
        for i in range(1,n):
            for j in range(1,i+1):
                #print(i,j)
                print(i*j,end=" ")
            print(" ")
    def star_tri1(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print('*',end=" ")
            print(" ")
    def star_tri2(self,n):
        for i in range(1,n+1):
            for j in range(n,0,-1):
                if j > i:
                    print(" ",end=" ")
                else:
                    print("*",end=" ")
            print(" ")
    def star_tri3(self,n):
        for i in range(n,0,-1):
            for j in range(i):
                print("*",end=" ")
            print(" ")
    def pyrmd_star(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for k in range(i+1):
                print("*",end=" ")
            print("")
    def pyrmd_star1(self,n):
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for k in range(n-i):
                print("*",end=" ")
            print("")
    def rd_star(self,n):
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for k in range(n-i):
                print("*",end="")
            print("")
    def pyrmd_two(self,n):
        for i in range(n+1):
            for j in range(i):
                print("*",end="")
            print("")
        for i in range(n,-1,-1):
            for j in range(i):
                print("*",end="")
            print("")
    def pyrmd_left(self,n):
        for i in range(n):
            for j in range(n-i):
                print(" ",end="")
            for k in range(i):
                print("*",end="")
            print("")
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for k in range(n-i):
                print("*",end="")
            print("")
    def rev_diamond(self,n):
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for k in range(n-i):
                print("* ",end="")
            print("")
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for k in range(i+1):
                print("* ",end="")
            print("")
    def diamond_star(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for k in range(i+1):
                print("* ",end="")
            print("")
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for k in range(n-i):
                print("* ",end="")
            print("")





    



    
    




pat = pattern()

#pat.right_num_same(5)

#pat.right_num_diff(5)

#pat.invr_num_same(6)

#pat.invr_same_num(10)

#pat.half_invr_num(5)

#pat.odd_num_tri(10)

#pat.rev_num_same(5)

#pat.rev_num_diff(6)

#pat.rev_num_rev_tri(5)

#pat.cnsqt_prmd(5)

#pat.right_tri(5)

#pat.square_nums(5)

#pat.mul_table_pattern(10)

#pat.star_tri1(5)

#pat.star_tri2(5)

#pat.star_tri3(5)

#pat.pyrmd_star(5)

#pat.pyrmd_star1(5)

#pat.rd_star(5)

#pat.pyrmd_two(5)

#pat.pyrmd_left(5)

#pat.rev_diamond(5)

pat.diamond_star(5)