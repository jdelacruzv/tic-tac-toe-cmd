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


def make_list_of_free_fields(board):
	free = []
	for row in range(3):
		for col in range(3):
			if board[row][col] not in ["O", "X"]:
				free.append((row, col))
	return free


def victory_for(board, letter):
	if letter == "X":
		who_won = "machine"
	elif letter == "O":
		who_won = "you"
	else:
		who_won = None
	cross1 = cross2 = True  # para las diagonales
	for rc in range(3):  # rc = row, col
		if board[rc][0] == letter and board[rc][1] == letter and board[rc][2] == letter:  # check row rc
			return who_won
		if board[0][rc] == letter and board[1][rc] == letter and board[2][rc] == letter:  # check column rc
			return who_won
		if board[rc][rc] != letter:  # revisar la primer diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != letter:  # revisar la segunda diagonal
			cross2 = False
	if cross1 or cross2:
		return who_won
	return None


def draw_move_machine(board):
	free = make_list_of_free_fields(board)
	count = len(free)
	if count > 0:
		this = randrange(count)  # devuelve un numero aleatorio
		row, col = free[this]
		board[row][col] = 'X'


def welcome_title():
	print("\nWelcome to Tic-Tac-Toe!\n")
	print("-------" * 2)
	print("Machine\t: 'X'\nUser\t: 'O'\nSalir\t: 'S'")
	print("-------" * 2)


def main():
	board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
	board[1][1] = "X"
	free = make_list_of_free_fields(board)
	user_turn = True


if __name__ == "__main__":
	welcome_title()
	main()
