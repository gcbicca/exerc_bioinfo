def logestcommonsubsequence(self,text1: str, text2:str):
    # +1 pq precisamos de mais uma coluna para os zeros
    dp = [[0 for j in range(len(text2 +1))] for i in range(len(text1)+1)]
    # Vamos fazer um nested loop e iterar sobre essa grade 2D na ordem inversa
    for i in range(len(text1) -1, -1, -1):
        for j in range(len(text2) -1,-1,-1):
