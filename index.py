def is_empty_LoL(S):
    return S == []

def isEmpty(S):
    return S == []

def jml_elemen_list(S):
    return len(S)

def is_atom(S):
    return not(is_empty_LoL(S)) and jml_elemen_list(S)==1

def is_list(S):
    return not(is_atom(S))

def konso_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return [L]+S
    
def konsi_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return S+[L]
    
def first_List(S):
    if not(is_empty_LoL(S)):
        return S[0]
    
def tail_List(S):
    if not(is_empty_LoL(S)):
        return S[1:]
    
def last_List(S):
    if not(is_empty_LoL(S)):
        return S[-1:]
    
def head_List(S):
    if not(is_empty_LoL(S)):
        return S[:-1]

# Perlu di cek
def IsEqs(S1,S2) :
    if isEmpty(S1) and isEmpty(S2):
        return True
    elif (not isEmpty(S1) and isEmpty(S2)) or (isEmpty(S1) and not isEmpty(S2)):
        return False
    else:
        if is_atom(first_List(S1)) and is_atom(first_List(S2)):
            return first_List(S1) == first_List(S2) and IsEqs(tail_List(S1),tail_List(S2))
        elif is_list(first_List(S1)) and is_list(first_List(S2)):
            return IsEqs(first_List(S1),first_List(S2)) and IsEqs(tail_List(S1), tail_List(S2))
        else:
            return False
        
def IsMemberS(A, S):
    if isEmpty(S):
        return False
    else:
        if is_atom(S):
            return A == first_List(S)
        elif is_list(S):
            return IsMemberS(A, first_List(S)) or IsMemberS(A, tail_List(S))
            
def isMemberLS(L, S):
    print(L, S)
    if isEmpty(L) and isEmpty(S):
        return True
    elif (not isEmpty(L) and isEmpty(S)) or (isEmpty(L) and not isEmpty(S)):
        return False
    else:
        if is_atom(first_List(S)):
            return isMemberLS(L, tail_List(S))
        elif is_list(first_List(S)):
            if IsEqs(L, first_List(S)):
                return True
            else:
                return isMemberLS(L, tail_List(S))
        
def Rember(a, S):
    if isEmpty(S):
        return S
    elif is_list(first_List(S)):
        return konso_LoL(Rember(a, first_List(S)), Rember(a, tail_List(S)))
    else:
        if first_List(S) == a:
            return Rember(a, tail_List(S))
        else:
            return konso_LoL(first_List(S), Rember(a, tail_List(S)))
        
def Max2(a,b):
    if a >= b:
        return a
    else:
        b
        
def Max(S):
    if is_atom(first_List(S)):
        return Max2(first_List(S), Max(tail_List(S)))
    else:
        return Max2(Max(first_List(S)), Max(tail_List(S)))
        

# L1=[]
# L2=[[]]
# L3=[['s',2,3],2,[5,'b']]
# print(is_empty_LoL(L1))
# print(is_empty_LoL(L2))
# print(is_empty_LoL(L3))

# L1=['a']
# L2=['b',5]
# L3=[['s',2,3],2,[5,'b']]
# print(is_atom(L1))
# print(is_atom(L2))
# print(is_atom(L3))
# print(is_list(L1))
# print(is_list(L2))
# print(is_list(L3))

# L=[1,2,3] 
# S=[3,5,[3,8]]
# print(konso_LoL(L, S))
# print(konsi_LoL(L, S))

# L3=[['s',2,3],2,[5,'b']]
# print(first_List(L3))

# X=['a',['b','c','e']] 
# X=[['a','b'],'e']  
# X=[['a','b'],'e', ['d','c']]  
# print(tail_List(X))
# print(last_List(X))
# print(head_List(X))

# S1 = [[2, 3]]
# S2 = [[2, 3]] 
# print(IsEqs(S1, S2))
# print(len([1,2]))

# A = 'd'
# S = ['s', 'a', 'd'] 
# print(IsMemberS(A, S))

# A = 'd'
# S = ['s', 'a', 'd'] 
# print(IsMemberS(A, S))

L = ['a', 'd', 'c']
S = ['b', ['a', 'd', 'c']] 
print(isMemberLS(L, S))
    