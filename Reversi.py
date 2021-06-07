#---<Modules>---#
from pygame import display,init, image, font, event, QUIT, KEYDOWN, K_ESCAPE, K_r, MOUSEBUTTONDOWN, mouse
from os import execv, environ, stat, path
from time import sleep
import sys
#---<Modules>---#

#---------------------<Class: __init__>---------------------#
class Game:
    def __init__ (self):
        self.__PointsBlack = 2
        self.__PointsWhite = 2
        self.__possible_moves = []
        self.__player = 0
        self.__Board = []
        for y in range(8):
            self.__Board.append([])
            for x in range(30,830,100):
                self.__Board[y].append([x,y*100+80,0])
        self.Board()
#---------------------<Class: __init__>---------------------#

    def resource_path(self,relative_path):
        if hasattr(sys, '_MEIPASS'):
            return path.join(sys._MEIPASS, relative_path)
        return path.join(path.abspath('.'), relative_path)

    #--------------------------<Class: Board>--------------------------#
    def Board(self):
        init()
        Res = display.Info()
        environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % ((Res.current_w/2)-425,(Res.current_h/2)-450)
        self.__screen = display.set_mode((850,900))
        Icon = image.load(self.resource_path("./assets/Icon.png"))
        Board = image.load(self.resource_path("./assets/Board.png"))
        self.__White = image.load(self.resource_path("assets/Player_White.png"))
        self.__Black = image.load(self.resource_path("assets/Player_Black.png"))
        self.__Options = image.load(self.resource_path("assets/Player_Possible_move.png"))
        self.__Erase = image.load(self.resource_path("assets/Erase.png"))
        self.__TextEraser = image.load(self.resource_path("assets/TextEraser.png"))
        self.__font = font.Font(self.resource_path('assets/SF-Compact-Rounded-Regular.otf'),24)
        display.set_caption("Reversi")
        display.set_icon(Icon)
        self.__screen.blit(Board,(0,0))
        self.__screen.blit(self.__White,self.__Board[3][3][:2])
        self.__screen.blit(self.__Black,self.__Board[3][4][:2])
        self.__screen.blit(self.__Black,self.__Board[4][3][:2])
        self.__screen.blit(self.__White,self.__Board[4][4][:2])
        self.__Board[3][3][2] = 1
        self.__Board[3][4][2] = 2
        self.__Board[4][3][2] = 2
        self.__Board[4][4][2] = 1
        display.flip()
        self.Options()
        self.listen()
    #--------------------------<Class: Board>--------------------------#

    def Options(self):
        try:
            for i in self.__possible_moves:
                if i != self.__hit:
                    if self.__hit in self.__possible_moves:
                        blit = self.__Board[i[0]][i[1]][:2]
                        self.__screen.blit(self.__Erase,(blit[0]-1,blit[1]-1))
                        display.flip()
        except AttributeError:
            pass
        self.__backup = self.__possible_moves
        self.possible_moves()
        if self.__backup != self.__possible_moves:
            if self.__possible_moves != []:
                for i in self.__possible_moves:
                    self.__screen.blit(self.__Options,self.__Board[i[0]][i[1]][:2])
                    display.flip()

    #----------------------------------------<Class: possible_moves>----------------------------------------#
    def possible_moves(self):
        self.__possible_moves = []
        self.__flip = []

        if self.__player == 1:
            Color = 1
            OppositColor = 2
        if self.__player == 0:
            Color = 2
            OppositColor = 1

        for x in range(8):
            for y in range(8):
                if self.__Board[y][x][2] == Color:
                    if y - 1 >= 0 and x - 1 >= 0 and self.__Board[y - 1][x - 1][2] == OppositColor:
                        List = [y - 1, x - 1]
                        for i in range(2,10):
                            y1 = y - i
                            x1 = x - i
                            if y1 < 0 or x1 < 0:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                    if y - 1 >= 0 and x >= 0 and self.__Board[y - 1][x][2] == OppositColor:
                        List = [y - 1, x]
                        for i in range(2,10):
                            y1 = y - i
                            x1 = x
                            if y1 < 0 or x1 < 0:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                    if y - 1 >= 0 and x + 1 <= 7 and self.__Board[y - 1][x + 1][2] == OppositColor:
                        List = [y - 1, x + 1]
                        for i in range(2,10):
                            y1 = y - i
                            x1 = x + i
                            if y1 < 0 or x1 > 7:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                    if y >= 0 and x - 1 >= 0 and self.__Board[y][x - 1][2] == OppositColor:
                        List = [y, x - 1]
                        for i in range(2,10):
                            y1 = y
                            x1 = x - i
                            if y1 < 0 or x1 < 0:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                    if y >= 0 and x + 1 <= 7 and self.__Board[y][x + 1][2] == OppositColor:
                        List = [y, x + 1]
                        for i in range(2,10):
                            y1 = y
                            x1 = x + i
                            if y1 < 0 or x1 > 7:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                    if y + 1 <= 7 and x - 1 >= 0 and self.__Board[y + 1][x - 1][2] == OppositColor:
                        List = [y + 1, x - 1]
                        for i in range(2,10):
                            y1 = y + i
                            x1 = x - i
                            if y1 > 7 or x1 < 0:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                    if y + 1 <= 7 and x >= 0 and self.__Board[y + 1][x][2] == OppositColor:
                        List = [y + 1,x]
                        for i in range(2,10):
                            y1 = y + i
                            x1 = x
                            if y1 > 7 or x1 < 0:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])
                    if y + 1 <= 7 and x + 1 <= 7 and self.__Board[y + 1][x + 1][2] == OppositColor:
                        List = [y + 1,x + 1]
                        for i in range(2,10):
                            y1 = y + i
                            x1 = x + i
                            if y1 > 7 or x1 > 7:
                                break
                            if self.__Board[y1][x1][2] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Board[y1][x1][2] == Color:
                                break
                            if self.__Board[y1][x1][2] == OppositColor:
                                List.extend([y1,x1])

        if self.__PointsBlack == 2 and self.__PointsWhite == 2 or self.__possible_moves == []:
            self.Points()
    #----------------------------------------<Class: possible_moves>----------------------------------------#


    #-------------------<Class: Points>-------------------#
    def Points(self):
        self.__PointsBlack = 0
        self.__PointsWhite = 0
        for r in range(8):
            for s in range(8):
                if self.__Board[r][s][2] == 1:
                    self.__PointsWhite += 1
                if self.__Board[r][s][2] == 2:
                    self.__PointsBlack += 1

        if self.__PointsWhite >= 2 or self.__PointsBlack >= 2:
            self.__screen.blit(self.__TextEraser,(385,23))
            self.__screen.blit(self.__TextEraser,(435,23))
            display.flip()
        if self.__PointsBlack + self.__PointsWhite != 64 and self.__possible_moves != []:
            text = self.__font.render(str(self.__PointsBlack), True, (255,255,255,255))
            self.__screen.blit(text,(412-text.get_rect()[2],23))
            text = self.__font.render(str(self.__PointsWhite),True,(255,255,255,255))
            self.__screen.blit(text,(438,23))

        if self.__PointsBlack + self.__PointsWhite == 64 or self.__possible_moves == []:
            if self.__PointsBlack > self.__PointsWhite:
                text = self.__font.render("WON",True,(255,255,255,255))
                self.__screen.blit(text,(362,23))
                text = self.__font.render("LOST",True,(255,255,255,255))
                self.__screen.blit(text,(438,23))
            else:
                text = self.__font.render("LOST",True,(255,255,255,255))
                self.__screen.blit(text,(359,23))
                text = self.__font.render("WON",True,(255,255,255,255))
                self.__screen.blit(text,(438,23))
        display.flip()
    #-------------------<Class: Points>-------------------#


    #---------------------------------------<Class: listen>---------------------------------------#
    def listen(self):
        while True:

            if len(self.__possible_moves) == 0:
                File = open("PointStats.txt","a")
                if stat("PointStats.txt").st_size == 0:
                    AIWrite = "AI:" + str(self.__PointsWhite) + " | PLAYER:" + str(self.__PointsBlack)
                else:
                    AIWrite = "\nAI:" + str(self.__PointsWhite) + " | PLAYER:" + str(self.__PointsBlack)
                File.write(AIWrite)
                while True:
                    for playerevent in event.get():
                        if playerevent.type == KEYDOWN and playerevent.key == K_ESCAPE or playerevent.type ==QUIT:
                            sys.exit()
                        if playerevent.type == KEYDOWN and playerevent.key == K_r:
                            execv(sys.executable, ['Reversi.py'] + sys.argv)

            #---------------------------------<AI's Turn>---------------------------------#
            if self.__player == 1 and len(self.__possible_moves) > 0:
                bestMove = 1
                index = 0
                for i in self.__flip:
                    if len(i) > bestMove:
                        bestMove = len(i)
                        index = self.__flip.index(i)

                sleep(0.25)
                first = self.__possible_moves[index][0]
                second = self.__possible_moves[index][1]
                self.__hit = [first,second]

                #self.possible_moves() #Auch hier habe ich beobachten können,dass das gleiche ergebnis auch ohne diese zeile rauskommt
                for i in self.__possible_moves:
                    if i == self.__hit:
                        position = self.__possible_moves.index(self.__hit)
                        loops = int(len(self.__flip[position])/2)
                        if self.__player == 1:
                            position1 = 0
                            position2 = 1
                            for i in range(loops):
                                flip1 = self.__flip[position][position1]
                                flip2 = self.__flip[position][position2]
                                self.__Board[flip1][flip2][2] = 1
                                self.__screen.blit(self.__White,self.__Board[flip1][flip2][:2])
                                position1 += 2
                                position2 += 2
                            self.__screen.blit(self.__White,self.__Board[first][second][:2])
                            self.__Board[first][second][2] = 1
                            display.flip()
                            self.__player = 0
                            self.Points()
                            break
                self.Options()
            #---------------------------------<AI's Turn>---------------------------------#

            if self.__player == 0 and len(self.__possible_moves) > 0:
                for playerevent in event.get():

                    #----------<Quit>-----------#
                    if playerevent.type == KEYDOWN and playerevent.key == K_ESCAPE or playerevent.type ==QUIT:
                        sys.exit()
                    #----------<Quit>-----------#

                    if playerevent.type == KEYDOWN and playerevent.key == K_r:
                        execv(sys.executable, ['Reversi.py'] + sys.argv)

                    #------------------------<Mouseclick>-------------------------#
                    if playerevent.type == MOUSEBUTTONDOWN and playerevent.button == 1:
                        x,y = mouse.get_pos()
                    #------------------------<Mouseclick>-------------------------#


                        #---------<determine Field on X-Coordination>---------#
                        min_number_x = 25
                        max_number_x = 125
                        for i in range(8):
                            if x > min_number_x and x < max_number_x:
                                newx = ((min_number_x + max_number_x)/2)-45
                                break
                            else:
                                min_number_x += 100
                                max_number_x += 100
                        #---------<determine Field on X-Coordination>---------#


                        #---------<determine Field on Y-Coordination>---------#
                        min_number_y = 75
                        max_number_y = 175
                        for i in range(8):
                            if y > min_number_y and y < max_number_y:
                                newy = ((min_number_y + max_number_y)/2)-45
                                break
                            else:
                                min_number_y += 100
                                max_number_y += 100
                        #---------<determine Field on X-Coordination>---------#

                        coordinate = [newx,newy]
                        for m in range(8):
                            for n in range(8):
                                if self.__Board[m][n][:2] == coordinate:
                                    self.__hit = [m,n]
                                    m1 = m
                                    n1 = n
                                    break

                        #self.possible_moves()   #Das hier habe ich erstmal rausgenommen, da bei kurzen ausprobieren das gleiche Ergebnis auch ohne erzielt wurde, es muss jedoch weiter getestet werden
                        for i in self.__possible_moves:
                            if i == self.__hit:
                                position = self.__possible_moves.index(self.__hit)
                                loops = int(len(self.__flip[position])/2)
                                if self.__player == 1:
                                    position1 = 0
                                    position2 = 1
                                    for i in range(loops):
                                        flip1 = self.__flip[position][position1]
                                        flip2 = self.__flip[position][position2]
                                        self.__Board[flip1][flip2][2] = 1
                                        self.__screen.blit(self.__White,self.__Board[flip1][flip2][:2])
                                        position1 += 2
                                        position2 += 2
                                    self.__screen.blit(self.__White,self.__Board[m1][n1][:2])
                                    self.__Board[m1][n1][2] = 1
                                    display.flip()
                                    self.__player = 0
                                    self.Points()
                                    break
                                if self.__player == 0:
                                    position1 = 0
                                    position2 = 1
                                    for i in range(loops):
                                        flip1 = self.__flip[position][position1]
                                        flip2 = self.__flip[position][position2]
                                        self.__Board[flip1][flip2][2] = 2
                                        self.__screen.blit(self.__Black,self.__Board[flip1][flip2][:2])
                                        position1 += 2
                                        position2 += 2
                                    self.__screen.blit(self.__Black,self.__Board[m1][n1][:2])
                                    self.__Board[m1][n1][2] = 2
                                    display.flip()
                                    self.__player = 1
                                    self.Points()
                                    break
                        self.Options()
    #---------------------------------------<Class: listen>---------------------------------------#

#-<Main Program>-#
if __name__ == "__main__":
    Reversi = Game()
#-<Main Program>-#
