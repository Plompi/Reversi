from pygame import display,init, image, font, event, QUIT, KEYDOWN, K_ESCAPE, K_r,K_p, MOUSEBUTTONDOWN, mouse, time, draw, Rect
from os import execv, stat, path #,environ
import sys

class Game:
    def __init__ (self):
        self.__PointsBlack,self.__PointsWhite = 2,2
        self.__possible_moves,self.__Board = [],[]
        self.__player = "black"
        for y in range(8):
            self.__Board.append([])
            for x in range(30,830,100):
                self.__Board[y].append([x,y*100+80,0])
        self.Board()

    def resource_path(self,relative_path):
        if hasattr(sys, '_MEIPASS'):
            return path.join(sys._MEIPASS, relative_path)
        return path.join(path.abspath('.'), relative_path)
    
    def Board(self):
        init()
        print("test")
        #Res = display.Info()
        #environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % ((Res.current_w/2)-425,(Res.current_h/2)-450) #The window is already in the middle of the screen (need to test this further)
        self.__screen = display.set_mode((850,900))
        self.__Icon = image.load(self.resource_path("assets/Icon.ico"))
        self.__Reversiboard = image.load(self.resource_path("assets/Board.png"))
        self.__White = image.load(self.resource_path("assets/Player_White.png"))
        self.__Black = image.load(self.resource_path("assets/Player_Black.png"))
        self.__Options = image.load(self.resource_path("assets/Player_Possible_move.png"))
        self.__font = font.Font(self.resource_path('assets/SF-Compact-Rounded-Regular.otf'),24)
        self.__won = self.__font.render("WON",True,(255,255,255,255))
        self.__lost = self.__font.render("LOST",True,(255,255,255,255))
        display.set_caption("Reversi")
        display.set_icon(self.__Icon)
        self.__screen.blits([(self.__Reversiboard,(0,0)),(self.__White,self.__Board[3][3][:2]),(self.__Black,self.__Board[3][4][:2]),(self.__Black,self.__Board[4][3][:2]),(self.__White,self.__Board[4][4][:2])])
        self.__Board[3][3][2],self.__Board[3][4][2],self.__Board[4][3][2],self.__Board[4][4][2]= 1,2,2,1
        self.Options()
        self.listen()

    def Options(self):
        self.__backup = self.__possible_moves
        self.possible_moves()
        if self.__backup != self.__possible_moves and self.__possible_moves != []:
            for i in self.__backup:
                if i != self.__hit and self.__hit in self.__backup:
                    blit = self.__Board[i[0]][i[1]][:2]
                    draw.rect(self.__screen, (41,104,33), Rect(blit[0]-1, blit[1]-1, 92, 92))
            for i in self.__possible_moves:
                self.__screen.blit(self.__Options,self.__Board[i[0]][i[1]][:2])
        display.flip()

    def possible_moves(self):
        self.__possible_moves, self.__flip = [],[]
        if self.__player == "white":
            Color, OppositColor = 1,2
        if self.__player == "black":
            Color, OppositColor = 2,1

        for x in range(8):
            for y in range(8):
                if self.__Board[y][x][2] == Color:
                    if y - 1 >= 0 and x - 1 >= 0 and self.__Board[y - 1][x - 1][2] == OppositColor:
                        List = [y - 1, x - 1]
                        for i in range(2,10):
                            y1,x1 = y - i, x - i
                            if y1 < 0 or x1 < 0 or self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    self.__flip[self.__possible_moves.index([y1,x1])].extend(List)
                                else:
                                    self.__possible_moves.append([y1,x1]),self.__flip.append(List)
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                    if y - 1 >= 0 and x >= 0 and self.__Board[y - 1][x][2] == OppositColor:
                        List = [y - 1, x]
                        for i in range(2,10):
                            y1 = y - i
                            if y1 < 0 or x < 0 or self.__Board[y1][x][2] == Color:
                                break
                            if self.__Board[y1][x][2] == 0:
                                if [y1,x] in self.__possible_moves:
                                    self.__flip[self.__possible_moves.index([y1,x])].extend(List)
                                else:
                                    self.__possible_moves.append([y1,x]),self.__flip.append(List)
                                break
                            if self.__Board[y1][x][2] == OppositColor:
                                List.extend([y1,x])
                    if y - 1 >= 0 and x + 1 <= 7 and self.__Board[y - 1][x + 1][2] == OppositColor:
                        List = [y - 1, x + 1]
                        for i in range(2,10):
                            y1,x1 = y - i, x + i
                            if y1 < 0 or x1 > 7 or self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    self.__flip[self.__possible_moves.index([y1,x1])].extend(List)
                                else:
                                    self.__possible_moves.append([y1,x1]),self.__flip.append(List)
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                    if y >= 0 and x - 1 >= 0 and self.__Board[y][x - 1][2] == OppositColor:
                        List = [y, x - 1]
                        for i in range(2,10):
                            x1 = x - i
                            if y < 0 or x1 < 0 or self.__Board[y][x1][2] == Color:
                                break
                            if self.__Board[y][x1][2] == 0:
                                if [y,x1] in self.__possible_moves:
                                    self.__flip[self.__possible_moves.index([y,x1])].extend(List)
                                else:
                                    self.__possible_moves.append([y,x1]),self.__flip.append(List)
                                break
                            if self.__Board[y][x1][2] == OppositColor:
                                List.extend([y,x1])
                    if y >= 0 and x + 1 <= 7 and self.__Board[y][x + 1][2] == OppositColor:
                        List = [y, x + 1]
                        for i in range(2,10):
                            x1 = x + i
                            if y < 0 or x1 > 7 or self.__Board[y][x1][2] == Color:
                                break
                            if self.__Board[y][x1][2] == 0:
                                if [y,x1] in self.__possible_moves:
                                    self.__flip[self.__possible_moves.index([y,x1])].extend(List)
                                else:
                                    self.__possible_moves.append([y,x1]),self.__flip.append(List)
                                break
                            if self.__Board[y][x1][2] == OppositColor:
                                List.extend([y,x1])
                    if y + 1 <= 7 and x - 1 >= 0 and self.__Board[y + 1][x - 1][2] == OppositColor:
                        List = [y + 1, x - 1]
                        for i in range(2,10):
                            y1,x1 = y + i, x - i
                            if y1 > 7 or x1 < 0 or self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    self.__flip[self.__possible_moves.index([y1,x1])].extend(List)
                                else:
                                    self.__possible_moves.append([y1,x1]),self.__flip.append(List)
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                    if y + 1 <= 7 and x >= 0 and self.__Board[y + 1][x][2] == OppositColor:
                        List = [y + 1,x]
                        for i in range(2,10):
                            y1 = y + i
                            if y1 > 7 or x < 0 or self.__Board[y1][x][2] == Color:
                                break
                            if self.__Board[y1][x][2] == 0:
                                if [y1,x] in self.__possible_moves:
                                    self.__flip[self.__possible_moves.index([y1,x])].extend(List)
                                else:
                                    self.__possible_moves.append([y1,x]),self.__flip.append(List)
                                break
                            if self.__Board[y1][x][2] == OppositColor:
                                List.extend([y1,x])
                    if y + 1 <= 7 and x + 1 <= 7 and self.__Board[y + 1][x + 1][2] == OppositColor:
                        List = [y + 1,x + 1]
                        for i in range(2,10):
                            y1,x1 = y + i, x + i
                            if y1 > 7 or x1 > 7 or self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    self.__flip[self.__possible_moves.index([y1,x1])].extend(List)
                                else:
                                    self.__possible_moves.append([y1,x1]),self.__flip.append(List)
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                                
        if self.__PointsBlack == 2 and self.__PointsWhite == 2 or self.__possible_moves == []:
            self.Points()

    def Points(self):
        self.__PointsBlack,self.__PointsWhite = 0,0
        for y in self.__Board:
            for x in y:
                if x[2] == 1:
                    self.__PointsWhite += 1
                if x[2] == 2:
                    self.__PointsBlack += 1

        draw.rect(self.__screen, (32,32,32), Rect(385, 23, 30, 30)), draw.rect(self.__screen, (32,32,32), Rect(435, 23, 30, 30))
        if self.__PointsBlack + self.__PointsWhite != 64 and self.__possible_moves != []:
            textPointsBlack = self.__font.render(str(self.__PointsBlack), True, (255,255,255,255))
            textPointsWhite = self.__font.render(str(self.__PointsWhite),True,(255,255,255,255))
            self.__screen.blits([(textPointsBlack,(412-textPointsBlack.get_rect()[2],23)),(textPointsWhite,(438,23))])

        if self.__PointsBlack + self.__PointsWhite == 64 or self.__possible_moves == []:
            if self.__PointsBlack > self.__PointsWhite:
                self.__screen.blits([(self.__won,(362,23)),(self.__lost,(438,23))])
            else:
                self.__screen.blits([(self.__lost,(359,23)),(self.__won,(438,23))])
        display.flip()

    def listen(self):
        while True:

            if len(self.__possible_moves) == 0:
                while True:
                    for playerevent in event.get():
                        if playerevent.type == KEYDOWN and playerevent.key == K_ESCAPE or playerevent.type ==QUIT:
                            sys.exit()
                        if playerevent.type == KEYDOWN and playerevent.key == K_r:
                            execv(sys.executable, ['Reversi.py'] + sys.argv)
                        if playerevent.type == KEYDOWN and playerevent.key == K_p:
                            File = open("PointStats.txt","a")
                            if stat("PointStats.txt").st_size == 0:
                                File.write("AI:" + str(self.__PointsWhite) + " | PLAYER:" + str(self.__PointsBlack))
                            else:
                                File.write("\nAI:" + str(self.__PointsWhite) + " | PLAYER:" + str(self.__PointsBlack))
                            File.close()

            #---------------------------------<AI's Turn>---------------------------------#
            if self.__player == "white" and len(self.__possible_moves) > 0:
                bestMove = 1
                for i in self.__flip:
                    if len(i) > bestMove:
                        bestMove,index = len(i),self.__flip.index(i)

<<<<<<< HEAD
                time.wait(500)
=======
                time.wait(400)
>>>>>>> 4aa8a8e0cb094b9f69d788f537c9fb564140241b
                self.__hit = [self.__possible_moves[index][0],self.__possible_moves[index][1]]
                if self.__hit in self.__possible_moves:
                    position = self.__possible_moves.index(self.__hit)
                    for z in range(0,len(self.__flip[position]),2):
                        flip1,flip2 = self.__flip[position][z],self.__flip[position][z+1]
                        self.__Board[flip1][flip2][2] = 1
                        self.__screen.blit(self.__White,self.__Board[flip1][flip2][:2])
                    self.__screen.blit(self.__White,self.__Board[self.__hit[0]][self.__hit[1]][:2])
                    self.__Board[self.__hit[0]][self.__hit[1]][2],self.__player = 1,"black"
                    self.Points()
                self.Options()
            #---------------------------------<AI's Turn>---------------------------------#

            if self.__player == "black" and len(self.__possible_moves) > 0:
                for playerevent in event.get():
                    if playerevent.type == KEYDOWN and playerevent.key == K_ESCAPE or playerevent.type ==QUIT:
                        sys.exit()
                    if playerevent.type == KEYDOWN and playerevent.key == K_r:
                        execv(sys.executable, ['Reversi.py'] + sys.argv)
                    if playerevent.type == MOUSEBUTTONDOWN and playerevent.button == 1:
                        x,y = mouse.get_pos()
                        self.__newx, self.__newy = None,None
                        
                        for xs in range(25,825,100):
                            if x > xs and x < xs+100:
                                self.__newx = xs //100
                                break

                        for ys in range(75,875,100):
                            if y > ys and y < ys+100:
                                self.__newy = ys //100
                                break

                        if self.__newx == None or self.__newy == None:
                            break

                        self.__hit = [self.__newy,self.__newx]
                        if self.__hit in self.__possible_moves:
                            position = self.__possible_moves.index(self.__hit)
                            for z in range(0,len(self.__flip[position]),2):
                                flip1,flip2 = self.__flip[position][z],self.__flip[position][z+1]
                                self.__Board[flip1][flip2][2] = 2
                                self.__screen.blit(self.__Black,self.__Board[flip1][flip2][:2])
                            self.__screen.blit(self.__Black,self.__Board[self.__hit[0]][self.__hit[1]][:2])
                            self.__Board[self.__hit[0]][self.__hit[1]][2],self.__player = 2,"white"
                            self.Points()
                        self.Options()

if __name__ == "__main__":
<<<<<<< HEAD
    Reversi = Game()
=======
    Reversi = Game()
#-<Main Program>-#
>>>>>>> 4aa8a8e0cb094b9f69d788f537c9fb564140241b
