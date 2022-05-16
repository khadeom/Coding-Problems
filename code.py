#!/bin/python3
# Red Knight's Shortest Path



import math
import os
import random
import re
import sys
from collections import defaultdict 
import queue
'''
class Knight:
    def __init__(self):
        
        graph = defaultdict(list)
        
    def ul(self,t):
        return (t[1]-1,t[1]+1)   
    def ur(self,t):
        return (t[0]+1,t[1]+1)
    def r(self,t):
        return (t[0]+1,t[1])    
    def lr(self,t):
        return (t[0]+1,t[1]-1)
    def ll(self,t):
        return (t[0]-1,t[1]-1)
    def l(self,t):
        return (t[0]-1,t[1])
            
        
    def addgraph(self,t):
        self.graph.append
'''

class Triple:
    def __init__(self,x,y,cnt,move="empty"):
        self.x=x
        self.y=y
        self.cnt=cnt
        self.move=move
    
    

# Complete the printShortestPath function below.
def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    arr=[[0]*n for _ in range(n)]
    moves = [['']*n for _ in range(n)]
    q=queue.Queue()
    
    q.put(Triple(i_start,j_start,0,"empty"))
    cnt=-1
    #for i in list(q):
        #print(i)
    
    while(not q.empty()):
        
        p = q.get()
        #print(p)
            
        x = p.x;
        #print(x)
        y = p.y;
        #print(y)
        c = p.cnt;
       # print(c)
        move = p.move;
        
            
        if(x < 0 or x >= n or y < 0 or y >= n):
            #print("continud  here here")
            continue;
            
        if(arr[x][y] == 1):
            #print("continud 2 here here")
            continue;
            
        arr[x][y] = 1;
        moves[x][y] = move;
            
        if(x == i_end and y == j_end):
            #print("breacked here")
            
            cnt = c;
            break
            
            
        q.put( Triple(x-2,y-1,c+1,"UL"));
        q.put( Triple(x-2,y+1,c+1,"UR"));    
        q.put( Triple(x,y+2,c+1,"R"));
        q.put( Triple(x+2,y+1,c+1,"LR"));
        q.put( Triple(x+2,y-1,c+1,"LL"));
        q.put( Triple(x,y-2,c+1,"L"));
        #print('c is here')
        #print(c)
        #print
    if(cnt != -1):
        
            
            
            
        print(cnt)
            
        st = []
        '''
                print("------")
        print(x)
        print(y)
        print(i_end)
        print(j_end)
        print("_---_")
        '''

            
        x,y = i_end, j_end;
        while(not moves[x][y]=="empty"):
            
            #print("dddjjj")
            st.append(moves[x][y]);
                
            if(moves[x][y]=="UL"):
                
                    #print(type(x))
                    x += 2
                    y +=1
                
            elif(moves[x][y]=="UR"):
                
                    x += 2
                    y -=1
                
            elif(moves[x][y]=="LR"):
                
                
                    x -= 2
                    y -= 1
                
            elif(moves[x][y]=="LL"):
                
                    x -= 2;
                    y +=1
                
            elif(moves[x][y]=="R"):
                
                    y -= 2;
                
            elif(moves[x][y]=="L"):
                
                    y += 2;
                
        while(st):
            
            print(st.pop(),end=" ");
            
        
    else:
        print("Impossible");
    
    
    












    

if __name__ == '__main__':
    n = int(input())

    i_startJ_start = input().split()

    i_start = int(i_startJ_start[0])

    j_start = int(i_startJ_start[1])

    i_end = int(i_startJ_start[2])

    j_end = int(i_startJ_start[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
