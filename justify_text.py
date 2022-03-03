import pygame

''' Example to show fps with pygame 12.01.2022 - python 3.10 '''

def text_on_screen(content, font, w, h):
	''' Renders content with font '''
	fps_surface = font.render(content, 1, pygame.Color("white"))
	text_width = fps_surface.get_width()
	if w + text_width > screen.get_width():
		start = 0
		for word in content.split():
			wr = font.render(word + " ", 1, pygame.Color("white"))
			if w + start + wr.get_width() < screen.get_width():
				screen.blit(wr, (w + start, h))
				start += wr.get_width()
			else:
				start = 0
				h = h + 20
				screen.blit(wr, (w + start, h))
				start += wr.get_width()
	else:
		screen.blit(fps_surface, (w, h))


timer = 0 #                                             counter increase each frame
def show_timer(max_frame_rate):
	global timer

	fps = f"Fps: {int(clock.get_fps())}" #               FPS
	fps += f" Timer: {timer//max_frame_rate}" #                      TIMER
	text_on_screen(fps, fps_font, 0, 0) #                       call to blit fps
	timer += 1 #                                        UPDATE COUNTER

def mainloop(max_frame_rate=60):
	''' loop where thing happens every frame '''

	while True:
		screen.fill(0) # clear the screen with black
		show_timer(max_frame_rate)
		text_on_screen("Showing frame rate and timer with pygame and now we are going out of the screen to see if this goes to the next line when it is too long and goes out of the screen", fps_font, 100, 100)
		for event in pygame.event.get(): #                   USER EVENTS HANDLER
			if event.type == pygame.QUIT:
				pygame.quit()
		clock.tick(max_frame_rate) #                         MAX FRAME RATE (60 is default)
		pygame.display.update() #                            UPDATE DISPLAY


# the engine initialization
pygame.init()
screen = pygame.display.set_mode((600, 400)) #             the screen surface
size = 20
fps_font = pygame.font.SysFont("Arial", size) #                font
clock = pygame.time.Clock() #                                FRAME RATE OBJECT
mainloop()