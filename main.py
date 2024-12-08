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
