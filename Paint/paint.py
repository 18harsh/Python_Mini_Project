import pygame , random
pygame.init()
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Paint")


last_pos = (0,0)
radius = 10
draw_on = False

def roundline(win, color , start, end, radius):
	dx =  end[0] - start[0]
	dy =  end[1] - start[1]

	distance = max(abs(dx),abs(dy))
	for i in range(distance):
		x = int(start[0]+float(i)/distance*dx)
		y = int(start[1]+float(i)/distance*dy)
		pygame.draw.circle(win,color,(x,y),radius)

try:
	while True:
		event = pygame.event.wait()		
		if event.type == pygame.QUIT:
			raise StopIteration
		if event.type == pygame.MOUSEBUTTONDOWN:
			color = (random.randrange(256),random.randrange(256),random.randrange(256))
			pygame.draw.circle(win,color,event.pos,radius)	
			draw_on = True
		if event.type == pygame.MOUSEBUTTONUP:
			draw_on = False
		if event.type == pygame.MOUSEMOTION:
			if draw_on:
				pygame.draw.circle(win,color,event.pos,radius)
				roundline(win, color , event.pos,last_pos , radius)			
			last_pos = event.pos
		pygame.display.flip()
except StopIteration:
	pass

pygame.quit()