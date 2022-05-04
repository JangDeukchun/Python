import pygame

pygame.init() # 초기화 작업

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("황기운 게임") # 게임 이름 설정

# FPS
clock = pygame.time.Clock()
#########################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트)

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\rlaej\\Desktop\\python\\pygame\\background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\rlaej\\Desktop\\python\\pygame\\charcter.png")
character_size = character.get_rect().size # 캐릭터의 가로세로 크기 가져옴
character_width = character_size[0] # 가로크기
character_height = character_size[1] # 세로크기
character_x_pos = screen_width /2 - character_width/2 # 가로 크기 절반에 위치함
character_y_pos = screen_height - character_height # 화면 세로 크기에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.4

# 적 캐릭터 만들기
enemy = pygame.image.load("C:\\Users\\rlaej\\Desktop\\python\\pygame\\enemy.png")
enemy_size = enemy.get_rect().size # 캐릭터의 가로세로 크기 가져옴
enemy_width = enemy_size[0] # 가로크기
enemy_height =enemy_size[1] # 세로크기
enemy_x_pos = screen_width /2 -enemy_width/2 # 가로 크기 절반에 위치함
enemy_y_pos = screen_height/2 - enemy_height/2 # 화면 세로 크기에 해당하는 곳에 위치


# 폰트 정의
game_font = pygame.font.Font(None,40)

# 게임 시간
total_time = 10

# 시간 계산
start_time = pygame.time.get_ticks() # 시작 시간을 받아옴



# 이벤트 루프 실행(이게 있어야 창이 꺼지지 않음)
running = True # 게임이 진행중인가 ?
while running:
    dt = clock.tick(30)  # 게임 화면의 초당 프레임 수는 30 이다
    print("fps : " + str(clock.get_fps()))

    # 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get(): # 프로그램이 종료되지 않도록 대기하며 동작을 체크함
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아니다

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 키를 왼쪽으로     
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP: # 방향키 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # 3. 캐릭터 위치 정의
    character_x_pos += to_x  * dt
    character_y_pos += to_y  * dt

    # 캐릭터가 화면에서 벗어나지 않게 하기 가로 값
    if character_x_pos < 0:
        character_x_pos = 0 
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width = character_width

    # 세로값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height = character_height

    # 4. 충돌처리
    character_rect = character.get_rect()  # 캐릭터가 가지는 좌표 정보를 가져옴
    character_rect.left = character_x_pos # 잘 이해안됨
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했따")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경화면이 나올 좌표 설정

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) # 적 캐릭터 그리기


    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 # 밀리세컨드이기 떄문에 나누어 준다

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    screen.blit(timer, (10,10))

    # 시간이 음수로 향하면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() # 화면을 그려준다 


# 종료 되기 전 대기 하는 코드
pygame.time.delay(5000)


# pygame 종료
pygame.quit()