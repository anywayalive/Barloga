# Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished For Loop!

def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i+=1
    return res  

# ////////////////////////////////////////////////////////////////////

def create_array(n):
    return list(range(1,int(n)+1))

# //////////////////////////////////////////////////////////////////////
 
def create_array(n):
    return range(1,n+1)