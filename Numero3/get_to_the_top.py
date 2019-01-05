import time


class Move:
    def __init__(self,start,end,time):
        
        self.start =start
        self.end =end
        self.time =time

class Path_travel:
    def __init__(self,moves,time_total):
        self.moves = moves
        self.time_total = time_total




f = open("mountain.txt", "r")

position_3d =  []
position_2d = []
lines = []


for i in range(0,4):
    lines.append(f.readline())


### J'ai eu des problemes avec le readline avec plus de temps la boucle aurait fonctionner

#for i in range(1,4):
    #for j in range(0,10):
     #   position_2d.append(lines[1].split()[j*10:j*10+10])
    #position_3d.append(position_2d)
    
for j in range(0,10):
    position_2d.append(lines[1].split()[j*10:j*10+10])
position_3d.append(position_2d)

position_2d = []
    
for j in range(0,10):
    position_2d.append(lines[2].split()[j*10:j*10+10])

position_3d.append(position_2d)

position_2d = []
for j in range(0,10):
    position_2d.append(lines[3].split()[j*10:j*10+10])
    
position_3d.append(position_2d)




all_moves = []
depart = []
for i in range(0,3):
    for j in range(0,10):
        for k in range(0,10):
            #depart
            if(position_3d[i][j][k] == "100"):
                depart = [i,j,k]

            #fin
            if(position_3d[i][j][k] == "101"):
                fin = [i,j,k]
            
            #monter
            if(i < 2):
                if(position_3d[i+1][j][k] == "10" or position_3d[i+1][j][k] == "12"):
                    all_moves.append(Move([i,j,k],[i+1,j,k],20))
                    #TODO ajouter monter 2 etage en meme temps
                #deplacement fin
                if(position_3d[i+1][j][k] == "101"):
                    all_moves.append(Move([i,j,k],[i+1,j,k],0))                    
                    
            #descendre
            if(i > 0):
                if(position_3d[i-1][j][k] == "11" or position_3d[i-1][j][k] == "12"):
                    all_moves.append(Move([i,j,k],[i-1,j,k],12))
                #deplacement fin
                if(position_3d[i-1][j][k] == "101"):
                    all_moves.append(Move([i,j,k],[i-1,j,k],0))
                    
            #droite                                                                     
            if(j < 9):
                if(position_3d[i][j+1][k] == "0"):
                    all_moves.append(Move([i,j,k],[i,j+1,k],1.5))
                #fin
                if(position_3d[i][j+1][k] == "101"):
                    all_moves.append(Move([i,j,k],[i,j+1,k],0))
                    
            #gauche                             
            if(j > 0):
                if(position_3d[i][j-1][k] == "0"):
                    all_moves.append(Move([i,j,k],[i,j-1,k],1.5))
                #deplacement fin
                if(position_3d[i][j-1][k] == "101"):
                    all_moves.append(Move([i,j,k],[i,j-1,k],0))

            #avant                                                                     
            if(k < 9):
                if(position_3d[i][j][k+1] == "0"):
                    all_moves.append(Move([i,j,k],[i,j,k+1],1.5))
                #deplacement fin
                if(position_3d[i][j][k+1] == "101"):
                    all_moves.append(Move([i,j,k],[i,j,k+1],0))
                    
            #arriere                             
            if(k > 0):
                if(position_3d[i][j][k-1] == "0"):
                    all_moves.append(Move([i,j,k],[i,j,k-1],1.5))
                #deplacement fin
                if(position_3d[i][j][k-1] == "101"):
                    all_moves.append(Move([i,j,k],[i,j,k-1],0))

def recursive(position_actuel, path):
    print(position_actuel)
    for i in range(0,len(all_moves)):
        if(all_moves[i].start == position_actuel):
            print("oui")
            if(all_moves[i].end == fin):
                print(path)
                return True
            return recursive(all_moves[i].end,path.append(position_actuel))
        else:
            return False
path = [depart]

print(recursive(depart,path)))





                              

        
                                          

                





