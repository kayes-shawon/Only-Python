import pygame
def draw_board(the_board):
	"""Draw a chess board with queens, from the_board. """
	pygame.init()
	colors = [(255,0,0), (0,0,0)]

	n = len(the_board)
	surface_sz = 480
	sq_sz = surface_sz // n
	surface_sz = n * sq_sz
	surface = pygame.display.set_mode((surface_sz, surface_sz))

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			break;
		# Draw a fresh background (a blank chess board)
	for row in range(n):
	# Draw each row of the board.
		c_indx = row % 2
	# Alternate starting color
		for col in range(n):
	# Run through cols drawing squares
			the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
			surface.fill(colors[c_indx], the_square)
	# Now flip the color index for the next square
			c_indx = (c_indx + 1) % 2

		pygame.display.flip()
	pygame.quit()

if __name__ == '__main__':
	draw_board([0, 5, 3, 1, 6, 4, 2])# 7 x 7 to test window size
	draw_board([6, 4, 2, 0, 5, 7, 1, 3])
	draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1]) # 13 x 13
	draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])