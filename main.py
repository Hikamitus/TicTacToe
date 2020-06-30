

class TicTacToe:
    def __init__(self):
        self.board =\
        	[None,
          1, 2, 3,
          4, 5, 6,
          7, 8, 9
        	 ];
        

    def print_board(self):
        print(f"""
         {self.board[1]}  |   {self.board[2]}   |  {self.board[3]}
        ____ _______ ____

         {self.board[4]}  |   {self.board[5]}   |  {self.board[6]}
        ____ _______ ____

         {self.board[7]}  |   {self.board[8]}   |  {self.board[9]}
        	""".center(32))
    
    def verify(self):
        win = lambda x: f'''{self.board[x]} Win!''';
        if self.board[1] == self.board[2] == self.board[3]: return win(3)
        if self.board[4] == self.board[5] == self.board[6]: return (6)
        if self.board[7] == self.board[8] == self.board[9]: return win(9)
            
        if self.board[1] == self.board[4] == self.board[7]: return win(7)
        if self.board[2] == self.board[5] == self.board[8]: return win(8)
        if self.board[3] == self.board[6] == self.board[9]: return win(9)
            
        if self.board[1] == self.board[5] == self.board[9]: return win(9)
        if self.board[3] == self.board[5] == self.board[7]: return win(7)
        
        boardin = self.board[1:];
        if all(type(l)==str for l in boardin) == True:
            return f'{self.print_board}\nDeu Empate!';
        
    def botchoice(self):
        local = randint(1, 9)
        
        while True:
            if type(self.board[local]) == int:
                self.board[local] = self.botsymbol;
                break;
            else:
                local = randint(1, 9);
                continue;
 
    def choice(self):
        print('Onde colocar o %s? '%(self.symbol));
        while True:
            try:
                local = int(input('Local: '));
                while local < 1 or local > 9:
                    local = int(input('Local: '));
                    
            except:
                continue
            else:
                try:
                    if type(self.board[local]) == int:
                        self.board[local] = self.symbol;
                        press()
                        break
                    else:
                        print('O local já foi escolhido!');
                        local = int(input('Local: '));
                except:
                    continue
        
    def play(self):
        while True:
            self.symbol = input('X ou O: ').upper();
            if self.symbol == 'X':
                self.botsymbol = 'O';
                break
            elif self.symbol == 'O':
                self.botsymbol = 'X';
                break
        
        while True:
            head('Tic Tac Toe')
            self.print_board();              
            self.choice()
            if self.verify():
                head('Tic Tac Toe')
                self.print_board();
                head(self.verify());
                press(); break;
                
            self.botchoice()
            if self.verify():
                head('Tic Tac Toe')
                self.print_board();
                head(self.verify());
                press(); break;
    def reset(self):
        self.__init__()

def head(text, symbol = '~', amount = 33):
    print(symbol*amount)
    print(text.center(amount))
    print(symbol*amount)

         
def press():
    input('Aperte Enter para continuar...');
    system('clear')

from os import system
from random import randint

game = TicTacToe()
while True:
    game.play();
    game.reset();
