import os
from random import randrange


def display_board(board):
	print("+-------" * 3, "+", sep="")
	for row in range(3):
		print("|       " * 3, "|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3, "|", sep="")
		print("+-------" * 3, "+", sep="")


def enter_move_user(board):
	ok = False
	while not ok:
		move = input("Ingresa tu movimiento: ")
		if move.lower() == "s":
			print("Salio del juego!")
			os._exit(0)
		ok = len(move) == 1 and move >= "1" and move <= "9"
		if not ok:
			print("Movimiento erróneo, ingrésalo nuevamente")
			continue
		move = int(move) - 1
		row = move // 3
		col = move % 3
		num_sel = board[row][col]
		ok = num_sel not in ['O', 'X']
		if not ok:
			print("¡Cuadro ocupado, ingresa nuevamente!")
			continue
	board[row][col] = "O"


def welcome_title():
	print("\nWelcome to Tic-Tac-Toe!\n")
	print("-------" * 2)
	print("Machine\t: 'X'\nUser\t: 'O'\nSalir\t: 'S'")
	print("-------" * 2)


def main():
	board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
	board[1][1] = "X"


if __name__ == "__main__":
	welcome_title()
	main()
