#--<Modules>--#
import pygame
import os
import sys
from time import*
#--<Modules>--#


#---------------------<Class: __init__>---------------------#
class Game:
    def __init__ (self):
        self.__PointsBlack = 2
        self.__PointsWhite = 2
        self.__possible_moves = []
        self.__player = 0
        self.__Check = []
        self.__Board = []
        self.__x = 30
        self.__y = 80
        for x in range(8):
            self.__Check.append([])
            self.__Board.append([])
            for y in range(8):
                self.__Check[x].append(0)
                self.__Board[x].append((self.__x,self.__y))
                self.__x += 100
            self.__y += 100
            self.__x = 30
        self.Board()
#---------------------<Class: __init__>---------------------#

    #--------------------------<Class: Board>--------------------------#
    def Board(self):
        pygame.init()
        Res = pygame.display.Info()
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % ((Res.current_w/2)-425,(Res.current_h/2)-450)
        self.__screen = pygame.display.set_mode((850,900))
        Icon = pygame.image.load("Assets/Icon.png")
        Board = pygame.image.load("Assets/Board.png")
        self.__White = pygame.image.load("Assets/Player_White.png")
        self.__Black = pygame.image.load("Assets/Player_Black.png")
        self.__Options = pygame.image.load("Assets/Player_Possible_move.png")
        self.__Erase = pygame.image.load("Assets/Erase.png")
        self.__TextEraser = pygame.image.load("Assets/TextEraser.png")
        self.__font = pygame.font.Font('Assets/SF-Compact-Rounded-Regular.otf', 24)
        pygame.display.set_caption("Reversi")
        pygame.display.set_icon(Icon)
        self.__screen.blit(Board,(0,0))
        self.__screen.blit(self.__White,self.__Board[3][3])
        self.__screen.blit(self.__Black,self.__Board[3][4])
        self.__screen.blit(self.__Black,self.__Board[4][3])
        self.__screen.blit(self.__White,self.__Board[4][4])
        self.__Check[3][3] = 1
        self.__Check[3][4] = 2
        self.__Check[4][3] = 2
        self.__Check[4][4] = 1
        pygame.display.flip()
        self.Options()
    #--------------------------<Class: Board>--------------------------#

    def Options(self):
        try:
            for i in self.__possible_moves:
                if i != self.__hit:
                    if self.__hit in self.__possible_moves:
                        blit = self.__Board[i[0]][i[1]]
                        self.__screen.blit(self.__Erase,(blit[0]-1,blit[1]-1))
                        pygame.display.flip()
        except AttributeError:
            pass
        self.__backup = self.__possible_moves
        self.possible_moves()
        if self.__backup != self.__possible_moves:
            if self.__possible_moves != []:
                for i in self.__possible_moves:
                    self.__screen.blit(self.__Options,self.__Board[i[0]][i[1]])
                    pygame.display.flip()

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
                if self.__Check[y][x] == Color:
                    Direction = 2
                    if y - 1 >= 0 and x - 1 >= 0 and self.__Check[y - 1][x - 1] == OppositColor:
                        List = [y - 1, x - 1]
                        while True:
                            y1 = y - Direction
                            x1 = x - Direction
                            if y1 < 0 or x1 < 0:
                                break
                            if self.__Check[y1][x1] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Check[y1][x1] == Color:
                                break
                            if self.__Check[y1][x1] == OppositColor:
                                List.extend([y1,x1])
                                Direction += 1
                    Direction = 2
                    if y - 1 >= 0 and x >= 0 and self.__Check[y - 1][x] == OppositColor:
                        List = [y - 1, x]
                        while True:
                            y1 = y - Direction
                            x1 = x
                            if y1 < 0 or x1 < 0:
                                break
                            if self.__Check[y1][x1] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Check[y1][x1] == Color:
                                break
                            if self.__Check[y1][x1] == OppositColor:
                                List.extend([y1,x1])
                                Direction += 1
                    Direction = 2
                    if y - 1 >= 0 and x + 1 <= 7 and self.__Check[y - 1][x + 1] == OppositColor:
                        List = [y - 1, x + 1]
                        while True:
                            y1 = y - Direction
                            x1 = x + Direction
                            if y1 < 0 or x1 > 7:
                                break
                            if self.__Check[y1][x1] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Check[y1][x1] == Color:
                                break
                            if self.__Check[y1][x1] == OppositColor:
                                List.extend([y1,x1])
                                Direction += 1
                    Direction = 2
                    if y >= 0 and x - 1 >= 0 and self.__Check[y][x - 1] == OppositColor:
                        List = [y, x - 1]
                        while True:
                            y1 = y
                            x1 = x - Direction
                            if y1 < 0 or x1 < 0:
                                break
                            if self.__Check[y1][x1] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Check[y1][x1] == Color:
                                break
                            if self.__Check[y1][x1] == OppositColor:
                                List.extend([y1,x1])
                                Direction += 1
                    Direction = 2
                    if y >= 0 and x + 1 <= 7 and self.__Check[y][x + 1] == OppositColor:
                        List = [y, x + 1]
                        while True:
                            y1 = y
                            x1 = x + Direction
                            if y1 < 0 or x1 > 7:
                                break
                            if self.__Check[y1][x1] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Check[y1][x1] == Color:
                                break
                            if self.__Check[y1][x1] == OppositColor:
                                List.extend([y1,x1])
                                Direction += 1
                    Direction = 2
                    if y + 1 <= 7 and x - 1 >= 0 and self.__Check[y + 1][x - 1] == OppositColor:
                        List = [y + 1, x - 1]
                        while True:
                            y1 = y + Direction
                            x1 = x - Direction
                            if y1 > 7 or x1 < 0:
                                break
                            if self.__Check[y1][x1] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Check[y1][x1] == Color:
                                break
                            if self.__Check[y1][x1] == OppositColor:
                                List.extend([y1,x1])
                                Direction += 1
                    Direction = 2
                    if y + 1 <= 7 and x >= 0 and self.__Check[y + 1][x] == OppositColor:
                        List = [y + 1,x]
                        while True:
                            y1 = y + Direction
                            x1 = x
                            if y1 > 7 or x1 < 0:
                                break
                            if self.__Check[y1][x1] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Check[y1][x1] == Color:
                                break
                            if self.__Check[y1][x1] == OppositColor:
                                List.extend([y1,x1])
                                Direction += 1
                    Direction = 2
                    if y + 1 <= 7 and x + 1 <= 7 and self.__Check[y + 1][x + 1] == OppositColor:
                        List = [y + 1,x + 1]
                        while True:
                            y1 = y + Direction
                            x1 = x + Direction
                            if y1 > 7 or x1 > 7:
                                break
                            if self.__Check[y1][x1] == 0:
                                if [y1,x1] in self.__possible_moves:
                                    pos = self.__possible_moves.index([y1,x1])
                                    self.__flip[pos].extend(List)
                                    break
                                if [y1,x1] not in self.__possible_moves:
                                    self.__possible_moves.append([y1,x1])
                                    self.__flip.append(List)
                                    break
                            if self.__Check[y1][x1] == Color:
                                break
                            if self.__Check[y1][x1] == OppositColor:
                                List.extend([y1,x1])
                                Direction += 1

        if self.__PointsBlack == 2 and self.__PointsWhite == 2 or self.__possible_moves == []:
            self.Points()
    #----------------------------------------<Class: possible_moves>----------------------------------------#


    #-------------------<Class: Points>-------------------#
    def Points(self):
        self.__PointsBlack = 0
        self.__PointsWhite = 0
        for r in range(8):
            for s in range(8):
                if self.__Check[r][s] == 1:
                    self.__PointsWhite += 1
                if self.__Check[r][s] == 2:
                    self.__PointsBlack += 1

        if self.__PointsWhite >= 2 or self.__PointsBlack >= 2:
            self.__screen.blit(self.__TextEraser,(385,23))
            self.__screen.blit(self.__TextEraser,(435,23))
            pygame.display.flip()
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
        pygame.display.flip()
    #-------------------<Class: Points>-------------------#


    #---------------------------------------<Class: listen>---------------------------------------#
    def listen(self):
        Run = True
        while Run:

            if len(self.__possible_moves) == 0:
                File = open("PointStats.txt","a")
                if os.stat("PointStats.txt").st_size == 0:
                    AIWrite = "AI:" + str(self.__PointsWhite) + " | PLAYER:" + str(self.__PointsBlack)
                else:
                    AIWrite = "\nAI:" + str(self.__PointsWhite) + " | PLAYER:" + str(self.__PointsBlack)
                File.write(AIWrite)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            sys.exit(0)
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                            os.execv(sys.executable, ['Reversi.py'] + sys.argv)

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

                self.possible_moves()
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
                                self.__Check[flip1][flip2] = 1
                                self.__screen.blit(self.__White,self.__Board[flip1][flip2])
                                position1 += 2
                                position2 += 2
                            self.__screen.blit(self.__White,self.__Board[first][second])
                            self.__Check[first][second] = 1
                            pygame.display.flip()
                            self.__player = 0
                            self.Points()
                            break
                self.Options()
            #---------------------------------<AI's Turn>---------------------------------#

            if self.__player == 0 and len(self.__possible_moves) > 0:
                for event in pygame.event.get():

                    #----------<Quit>-----------#
                    if event.type == pygame.QUIT:
                        Run = False
                    #----------<Quit>-----------#

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        sys.exit(0)

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        os.execv(sys.executable, ['Reversi.py'] + sys.argv)

                    #------------------------<Mouseclick>-------------------------#
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        x,y = pygame.mouse.get_pos()
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

                        coordinate = (newx,newy)
                        for m in range(8):
                            for n in range(8):
                                if self.__Board[m][n] == coordinate:
                                    self.__hit = [m,n]
                                    m1 = m
                                    n1 = n
                                    break

                        self.possible_moves()
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
                                        self.__Check[flip1][flip2] = 1
                                        self.__screen.blit(self.__White,self.__Board[flip1][flip2])
                                        position1 += 2
                                        position2 += 2
                                    self.__screen.blit(self.__White,self.__Board[m1][n1])
                                    self.__Check[m1][n1] = 1
                                    pygame.display.flip()
                                    self.__player = 0
                                    self.Points()
                                    break
                                if self.__player == 0:
                                    position1 = 0
                                    position2 = 1
                                    for i in range(loops):
                                        flip1 = self.__flip[position][position1]
                                        flip2 = self.__flip[position][position2]
                                        self.__Check[flip1][flip2] = 2
                                        self.__screen.blit(self.__Black,self.__Board[flip1][flip2])
                                        position1 += 2
                                        position2 += 2
                                    self.__screen.blit(self.__Black,self.__Board[m1][n1])
                                    self.__Check[m1][n1] = 2
                                    pygame.display.flip()
                                    self.__player = 1
                                    self.Points()
                                    break
                        Reversi.Options()
    #---------------------------------------<Class: listen>---------------------------------------#


#-<Main Program>-#
Reversi = Game()
Reversi.listen()
#-<Main Program>-#
