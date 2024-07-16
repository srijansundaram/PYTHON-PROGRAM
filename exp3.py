# EX1
def BayesThm(pA, pB, pBA):
    return pA*pBA/pB
pR=0.2
pC=0.4
pCR=0.85
result=BayesThm(pR,pC,pCR)
print(result)
#EX2
def BayesThm(pI, pP, pPI):
    return pI*pPI/pP
pPI=0.99
pP=0.0198
pI=0.01
result=BayesThm(pI,pP,pPI)
print(result)