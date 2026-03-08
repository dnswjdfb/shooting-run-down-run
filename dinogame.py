import pygame
import re
import random

pygame.init()
pygame.font.init()

info = pygame.display.Info()
WINDOW_X = 1200 # 창 x
WINDOW_Y = 675 # 창 y
GAME_SCREEN_RESOLUTION = (WINDOW_X, WINDOW_Y)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 80 # 프레임
DINO_X_POS = 100 # 공룡 기본 x
DINO_Y_POS = 360 # 공룡 기본 y
OBJ_X_POS = WINDOW_X + 48 # 장애물 초기화시 x
OBJ_Y_POS = 360 # 장애물 y

PLAYER_RUNNING_IMAGE = [pygame.image.load('img/player/RUNNING1.png'),  # 달리는 이미지
                      pygame.image.load('img/player/RUNNING2.png'),
                      pygame.image.load('img/player/RUNNING3.png'),
                      pygame.image.load('img/player/RUNNING4.png'),
                      pygame.image.load('img/player/RUNNING5.png'),
                      pygame.image.load('img/player/RUNNING6.png'),
                      pygame.image.load('img/player/RUNNING7.png'),
                      pygame.image.load('img/player/RUNNING8.png')]
DINO_SLIDING_IMAGE = [pygame.transform.scale(pygame.image.load('img/player/SLIDING1.png'), (64, 32)),  # 슬리이딩 이미지
                      pygame.transform.scale(pygame.image.load('img/player/SLIDING2.png'), (64, 32)),
                      pygame.transform.scale(pygame.image.load("img/player/SLIDING3.png"), (64, 32))]
OBSTACLES = [pygame.transform.scale(pygame.image.load("img/obj/RUSTY_COPPER_BOX.png"), (64, 64)), # 장애물 이미지
             pygame.transform.scale(pygame.image.load('img/obj/RUSTY_COPPER_BOX.png'), (64, 128)),
             pygame.transform.scale(pygame.image.load('img/obj/ON_RUSTY_COPPER_BOX.png'), (64, 192)),
             pygame.transform.scale(pygame.image.load('img/obj/IRON_BOX.png'), (80, 80)),
             pygame.transform.scale(pygame.image.load('img/obj/CANDYBOX.png'), (64, 64)),
             pygame.transform.scale(pygame.image.load('img/obj/LOW_LONG_FISH_TANK.png'), (96, 64)),
             pygame.transform.scale(pygame.image.load('img/obj/TREE_SKY_BOX.png'), (80, 80))]
MAGIC_CIRCLE = pygame.transform.scale((pygame.image.load('img/maigc/MAGIC_CIRCLE.png')), (64, 64)) # 마법진 이미지
MAGIC_ICON = [pygame.transform.scale((pygame.image.load('img/maigc/MAGIC_ICON_ALLOW.png')), (128, 128)),
              pygame.transform.scale((pygame.image.load('img/maigc/MAGIC_ICON_FALSE.png')), (128, 128)),
              pygame.transform.scale((pygame.image.load('img/maigc/MAGIC_ICON_OVERCHARGE.png')), (128, 128))]
START_BUTTON = [pygame.transform.scale((pygame.image.load('img/main/OFF_START.png')), (240, 80)),
                pygame.transform.scale((pygame.image.load('img/main/ON_START.png')), (240, 80))]
SETTING_BUTTON = [pygame.transform.scale((pygame.image.load('img/main/OFF_SETTING.png')), (240, 80)),
                  pygame.transform.scale((pygame.image.load('img/main/ON_SETTING.png')), (240, 80))]
BACK_BUTTON = [pygame.transform.scale((pygame.image.load('img/main/OFF_BACK.png')), (240, 80)),
               pygame.transform.scale((pygame.image.load('img/main/ON_BACK.png')), (240, 80))]
AGAIN_BUTTON = [pygame.transform.scale(pygame.image.load('img/playing/OFF_AGAIN.png'), (240, 80)),
                pygame.transform.scale(pygame.image.load('img/playing/ON_AGAIN.png'), (240, 80)), ]
GOMAIN_BUTTON = [pygame.transform.scale(pygame.image.load('img/playing/OFF_GOMAIN.png'), (240, 80)),
                 pygame.transform.scale(pygame.image.load('img/playing/ON_GOMAIN.png'), (240, 80)), ]
SIGNUPBUTTON = [pygame.transform.scale((pygame.image.load('img/main/OFF_SIGNUP.png')), (240, 80)),
               pygame.transform.scale((pygame.image.load('img/main/ON_SIGNUP.png')), (240, 80))]
LOGINBUTTON = [pygame.transform.scale((pygame.image.load('img/main/OFF_LOGIN.png')), (240, 80)),
               pygame.transform.scale((pygame.image.load('img/main/ON_LOGIN.png')), (240, 80))]
LOGOUTBUTTON = [pygame.transform.scale((pygame.image.load('img/main/OFF_LOGOUT.png')), (240, 80)),
                pygame.transform.scale((pygame.image.load('img/main/ON_LOGOUT.png')), (240, 80))]
CREATEBUTTON = [pygame.transform.scale((pygame.image.load('img/join/OFF_CREATE.png')), (240, 80)),
                pygame.transform.scale((pygame.image.load('img/join/ON_CREATE.png')), (240, 80))]
DEATH_SCREEN = pygame.transform.scale((pygame.image.load('img/playing/DEATHSCREEN.png')), (420, 500))
GAMEOVER = pygame.transform.scale((pygame.image.load('img/playing/GAMEOVER.png')), (280, 120))
DOWNRUN_MARK = pygame.transform.scale((pygame.image.load('img/main/DOWNRUN_MARK.png')), (420, 180))

IDINPUT = [pygame.transform.scale((pygame.image.load('img/join/OFF_INPUT.png')), (240, 80)),
           pygame.transform.scale((pygame.image.load('img/join/ON_INPUT.png')), (240, 80))]

PASSINPUT = [pygame.transform.scale((pygame.image.load('img/join/OFF_INPUT.png')), (240, 80)),
           pygame.transform.scale((pygame.image.load('img/join/ON_INPUT.png')), (240, 80))]

ID = [pygame.transform.scale((pygame.image.load('img/join/OFF_ID.png')), (120, 80)),
      pygame.transform.scale((pygame.image.load('img/join/ON_ID.png')), (120, 80))]
PASS = [pygame.transform.scale((pygame.image.load('img/join/OFF_PASS.png')), (160, 80)),
        pygame.transform.scale((pygame.image.load('img/join/ON_PASS.png')), (160, 80))]

class PLAYER:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    RAZER_BEAM = pygame.transform.scale((pygame.image.load('img/maigc/MAGIC_BEAM.png')), (1, 128))  # 레이저 빔 이미지
    player_rect = PLAYER_RUNNING_IMAGE[0].get_rect()
    magic_circle_rect = MAGIC_CIRCLE.get_rect()
    magic_beam_rect = RAZER_BEAM.get_rect()
    magic_icon_rect = MAGIC_ICON[0].get_rect()
    ROTATE_MAGIC_CIRCLE =pygame.transform.rotate(MAGIC_CIRCLE, 0)
    JUMPING = False # 점프 유무
    SLIDING = False # 슬라이딩 유무
    ON_GROUND = True  # 땅에 붙어 있는지 확인

    Accelerating_VELOCITY = 0 # 가속화된 속도
    Y_GRAVITY = 0.75 # 중력
    JUMP_HEIGHT = 15 # 최대 점프 높이
    Y_VELOCITY = JUMP_HEIGHT # 올라갔다 내려가는 속도
    stepR = 0 # 달리는 이미지 변환 변수
    stepS = 0 # 업드린 이미지 변환 변수
    stepC = 0 # 마법 캐스팅 이미지 변환 변수
    stepL = 0 # 마법 발사 이미지 변화 변수
    stepR_LIMIT = 4 # 뛰는 이미지 바뀌는 속도
    stepS_LIMIT = 5 # 업드리는 이미지 바뀌는 속도
    stepL_LIMIT = 3 # 레이저 이미지 바뀌는 속도
    stepC_S = 0 # 마법진 크기 변환 변수
    masic_max = info.current_w #마법 최대 길이
    masic_length = 0 # 마법 길이
    Cooldown = 240 # 마법 쿨타임
    NOT_ON_GROUND_IF_SLIDING = False # 바닥이 아닌 곳에서 아래 방향키를 눌렀는지의 유무
    DOUBLE_JUMP_PREVENTION = False # 더블 점프 방지
    CASTING_MAGIC = False # 마법 준비
    MAGIC_DURATION = 0 # 마법 지속 시간

    K_DOWN = pygame.K_DOWN
    K_UP = pygame.K_UP
    K_SPACE = pygame.K_SPACE
    K_c = pygame.K_c

    def action(self):
        KEY = pygame.key.get_pressed()  # 무슨 키를 눌렀는지 입력 받기

        if KEY[self.K_DOWN] and not self.ON_GROUND:  # 바닥이 아닌 곳에서 아래 방향키를 눌렀는가
            self.SLIDING = True
            self.NOT_ON_GROUND_IF_SLIDING = True
        elif KEY[self.K_DOWN] and self.ON_GROUND:  # 바닥에서 아래 방향키를 눌렀는가
            self.SLIDING = True
        else:  # 아래 방향키를 누르지 않았는가
            self.SLIDING = False
            self.NOT_ON_GROUND_IF_SLIDING = False

        if (KEY[self.K_SPACE] or KEY[self.K_UP]) and self.ON_GROUND and self.SLIDING == False:  # 바닥에서 점프를 했는가 단 아래 방향키가 먼저 눌러져 있으면 점프가 되면 안됨
            self.JUMPING = True
            self.ON_GROUND = False
            self.y -= self.Y_VELOCITY + 20
        elif (KEY[self.K_SPACE] or KEY[self.K_UP]) and not self.DOUBLE_JUMP_PREVENTION and self.JUMPING:  # 이후에도 점프키를 누르고 있는가
            self.Y_VELOCITY -= self.Y_GRAVITY
            self.y -= self.Y_VELOCITY
            if self.Y_VELOCITY <= 0 or self.SLIDING:  # 만약 올라갈수 있는 최고 높이 달성시
                self.Y_VELOCITY = 0
                self.DOUBLE_JUMP_PREVENTION = True
        else:
            if not self.DOUBLE_JUMP_PREVENTION:  # 점프 키를 최고 높이에 올라가지 않고 중간에 점프를 누르지 않았을때 내려오게 하기 위해서
                self.Y_VELOCITY = 0
                self.DOUBLE_JUMP_PREVENTION = True
            if self.NOT_ON_GROUND_IF_SLIDING:  # 내려 오는 도중 아래 키를 누르면 빨리 내려오게 하기
                self.Y_VELOCITY -= self.Y_GRAVITY
                self.Accelerating_VELOCITY = self.Y_VELOCITY * 4
                self.y -= self.Accelerating_VELOCITY
            elif not self.NOT_ON_GROUND_IF_SLIDING:  # 그냥 공중에 있을때 바닥에 떨어지기
                self.Y_VELOCITY -= self.Y_GRAVITY
                self.y -= self.Y_VELOCITY

        if self.y >= DINO_Y_POS:  # 만약 공룡의 높이가 기준값보다 같거나 더 밑으로 가면 기준값으로 설정 및 다른 설정 초기화
            self.y = DINO_Y_POS
            self.ON_GROUND = True
            self.JUMPING = False
            self.Y_VELOCITY = self.JUMP_HEIGHT
            self.DOUBLE_JUMP_PREVENTION = False

    def break_obj(self):
        KEY = pygame.key.get_pressed()

        if self.Cooldown < 240:
            self.Cooldown += 1
        if KEY[self.K_c] and self.ON_GROUND: # 땅에 있을때만 마법 실행 가능
            if self.Cooldown >= 120:
                self.Cooldown -= 210
                self.CASTING_MAGIC = True
        if self.CASTING_MAGIC:# 마법
            self.stepC += 5 # 마법진 돌아가는것
            if self.stepC >= 360:
                self.stepC = 0
            if self.masic_max > self.masic_length:
                self.masic_length += 30
            self.RAZER_BEAM = pygame.transform.scale((pygame.image.load('img/maigc/MAGIC_BEAM.png')), (self.masic_length, 128))  # 레이저 빔 이미지
            self.MAGIC_DURATION += 1
            if self.MAGIC_DURATION >= 90: # 마법 유지 시간
                self.MAGIC_DURATION = 0
                self.masic_length = 0
                self.CASTING_MAGIC = False

    def game_over(self):
        self.MAGIC_DURATION = 0
        self.stepL = 0
        self.stepC_S = 0
        self.CASTING_MAGIC = False
        self.y = DINO_Y_POS
        self.ON_GROUND = True
        self.JUMPING = False
        self.Y_VELOCITY = self.JUMP_HEIGHT
        self.DOUBLE_JUMP_PREVENTION = False
        self.MAGIC_DURATION = 0
        self.masic_length = 0
        self.Cooldown = 240
        self.CASTING_MAGIC = False

    def draw(self):
        if self.JUMPING: # 점프
            self.player_rect = PLAYER_RUNNING_IMAGE[self.stepR // self.stepR_LIMIT].get_rect(midbottom=(self.x, self.y))
            GAME_SCREEN.blit(PLAYER_RUNNING_IMAGE[self.stepR // self.stepR_LIMIT], self.player_rect)
        elif self.SLIDING: #슬라이딩
            self.stepS += 1
            if self.stepS >= self.stepS_LIMIT*len(DINO_SLIDING_IMAGE):
                self.stepS = 0
            self.player_rect = DINO_SLIDING_IMAGE[self.stepS // self.stepS_LIMIT].get_rect(midbottom=(self.x, self.y))
            GAME_SCREEN.blit(DINO_SLIDING_IMAGE[self.stepS // self.stepS_LIMIT], self.player_rect)
        else: #런
            self.stepR += 1
            if self.stepR >= self.stepR_LIMIT * len(PLAYER_RUNNING_IMAGE):
                self.stepR = 0
            self.player_rect = PLAYER_RUNNING_IMAGE[self.stepR // self.stepR_LIMIT].get_rect(midbottom=(self.x, self.y))
            GAME_SCREEN.blit(PLAYER_RUNNING_IMAGE[self.stepR // self.stepR_LIMIT], self.player_rect)

        if self.CASTING_MAGIC:
            self.ROTATE_MAGIC_CIRCLE = pygame.transform.rotate(MAGIC_CIRCLE,self.stepC)
            self.magic_circle_rect = self.ROTATE_MAGIC_CIRCLE.get_rect(center=(DINO_X_POS + 48, DINO_Y_POS - 128))
            GAME_SCREEN.blit(self.ROTATE_MAGIC_CIRCLE, self.magic_circle_rect)
            self.magic_beam_rect = self.RAZER_BEAM.get_rect(midleft=(DINO_X_POS + 48, DINO_Y_POS - 128))
            GAME_SCREEN.blit(self.RAZER_BEAM, self.magic_beam_rect)
        if self.Cooldown == 240:
            self.magic_icon_rect = MAGIC_ICON[2].get_rect(center=(128, WINDOW_Y - 128))
            GAME_SCREEN.blit(MAGIC_ICON[2], self.magic_icon_rect)
        elif self.Cooldown >= 120:
            self.magic_icon_rect = MAGIC_ICON[0].get_rect(center=(128, WINDOW_Y - 128))
            GAME_SCREEN.blit(MAGIC_ICON[0], self.magic_icon_rect)
        else:
            self.magic_icon_rect = MAGIC_ICON[1].get_rect(center=(128, WINDOW_Y - 128))
            GAME_SCREEN.blit(MAGIC_ICON[1], self.magic_icon_rect)

class OBJ: # 장애물
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r_x = x
        self.r_y = y
        self.obj_num = random.randint(0, len(OBSTACLES)-1) #장애물의 종류 결정

    obj_rect = OBSTACLES[0].get_rect()
    X_SPEED = 10 # 장애물 속도
    MAX_SPEED = 16 # 장애물 최고 속도
    START_FLAG = True # 달리기 시작했는지 유무
    RESET_FLAG = False
    DISTANCE = 750
    MIN_DISTANCE = 500
    MAX_DISTANCE = 800

    def move(self):
        if self.x <= -48:
            self.reset()
        if self.START_FLAG:
            self.x -= self.X_SPEED
            self.draw()

    def draw(self):
        self.obj_rect = OBSTACLES[self.obj_num].get_rect(midbottom=(self.x, self.y))
        GAME_SCREEN.blit(OBSTACLES[self.obj_num], self.obj_rect)

    def reset(self):
        self.RESET_FLAG = True
        self.START_FLAG = False
        self.x = OBJ_X_POS
        self.obj_num = random.randint(0, len(OBSTACLES)-1)
        if self.obj_num == 1:
            self.y = OBJ_Y_POS-48
        else:
            self.y = OBJ_Y_POS
        self.DISTANCE = random.randint(self.MIN_DISTANCE, self.MAX_DISTANCE)

    def game_over(self):
        self.START_FLAG = True
        self.RESET_FLAG = False
        self.x = self.r_x
        self.y = self.r_y
        self.obj_rect = OBSTACLES[self.obj_num].get_rect(midbottom=(self.x, self.y))
        GAME_SCREEN.blit(OBSTACLES[self.obj_num], self.obj_rect)

class GAMEMANAGEMENT:
    def __init__(self, player, objs):
        self.player = player
        self.objs = objs

    system_font = pygame.font.Font('font/PixelEnglishFont.ttf', 25)
    score_font = system_font.render('score : 0', True, WHITE)
    score_font_rect = score_font.get_rect()
    max_score_font = system_font.render('max score : 0', True, WHITE)
    max_score_font_rect = max_score_font.get_rect()
    score = 0 # 점수
    max_score = 0
    stepS = 0
    stepL_LIMIT = 5

    def signup(self, inputid, inputpass):
        id_pattern = r"^[a-zA-Z0-9_]+$"
        id_regexp = False # 정규표현식을 통과하였는가?
        if re.fullmatch(id_pattern, inputid): # id 정규표현식
            id_regexp = True

        # id 중복 check
        id_Checked = False  # 아이디 중복을 통과하였는가?

        # pass 정규표현식
        pass_pattern = r"^[a-zA-Z0-9!@#]+$"
        pass_regexp = False
        if re.fullmatch(pass_pattern, inputpass):
            pass_regexp = True
        if id_regexp and pass_regexp : # and id_Checked
            return True
        else:
            return False


    def login(self, inputid, inputpass):
        pattern = r"^[a-zA-Z0-9_]+$"
        regexp = False  # 정규표현식을 통과하였는가?
        if re.fullmatch(pattern, inputid):
            regexp = True
        # id 찾기 및 찾은 id랑 pass 맞는 지 확인후


        if regexp:
            return True
        else:
            return False

    def score_up(self):
        self.stepS += 1
        if self.stepS >= self.stepL_LIMIT:
            self.stepS = 0
            self.score += 1
        self.score_font = self.system_font.render('score : '+str(self.score), True, WHITE)
        self.score_font_rect.center = (WINDOW_X - 250, 30)
        if self.max_score < self.score:
            self.max_score = self.score
        self.max_score_font = self.system_font.render('max score : '+str(self.max_score), True, WHITE)
        self.max_score_font_rect.center = (WINDOW_X - 250, 80)
        GAME_SCREEN.blit(self.score_font, self.score_font_rect)
        GAME_SCREEN.blit(self.max_score_font, self.max_score_font_rect)

    def dino_obj_control(self):
        for i in range(len(self.objs)):
            self.objs[i].move()
            if self.player.player_rect.colliderect(self.objs[i].obj_rect): #충돌 시 감지
                self.player.game_over()
                for j in range(len(self.objs)):
                    self.objs[j].game_over()
                    self.score = 0
                return True
            if self.player.CASTING_MAGIC:
                if self.objs[i].obj_num == 2:
                    if self.player.magic_beam_rect.colliderect(self.objs[i].obj_rect):
                        self.objs[i].obj_num = 0
                if self.objs[i].obj_num == 1:
                    if self.player.magic_beam_rect.colliderect(self.objs[i].obj_rect):
                        self.player.masic_length = self.objs[i].x - 160
                        if self.player.masic_length < 0:
                            self.player.masic_length = 0
            if self.objs[i].RESET_FLAG:
                if self.objs[i].x - self.objs[i-1].x >= self.objs[i].DISTANCE:
                    self.objs[i].RESET_FLAG = False
                    self.objs[i].START_FLAG = True
        return False


def main():
    global WINDOW_X, WINDOW_Y, GAME_SCREEN, RAZER_BEAM
    GAME_SCREEN = pygame.display.set_mode(GAME_SCREEN_RESOLUTION)  # 창 크기  세팅
    # Background = pygame.image.load('img/Background.png')  # 배경화면
    pygame.display.set_caption('Down Run')  # 타이틀
    player = PLAYER(DINO_X_POS, DINO_Y_POS)
    objs = [OBJ(OBJ_X_POS, OBJ_Y_POS), OBJ(-48, OBJ_Y_POS), OBJ(-48, OBJ_Y_POS), OBJ(-48, OBJ_Y_POS)]
    gm = GAMEMANAGEMENT(player, objs)
    start_button_rect = START_BUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 4)
    setting_button_rect = SETTING_BUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2)
    again_button_rect = AGAIN_BUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2)
    gomain_button_rect = GOMAIN_BUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2)
    id_input_rect = IDINPUT[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 200)
    pass_input_rect = PASSINPUT[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 75)
    back_rect = BACK_BUTTON[0].get_rect(centerx=WINDOW_X -150, centery=WINDOW_Y - 80)
    signup_rect = SIGNUPBUTTON[0].get_rect(centerx=450, centery=WINDOW_Y - 80)
    login_rect = LOGINBUTTON[0].get_rect(centerx=150, centery=WINDOW_Y - 80)
    logout_rect = LOGOUTBUTTON[0].get_rect(centerx=150, centery=WINDOW_Y - 80)
    death_screen_rect = DEATH_SCREEN.get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2)
    gameover_rect = GAMEOVER.get_rect(centerx=WINDOW_X // 2, centery=death_screen_rect.top)
    downrun_mark_rect = DOWNRUN_MARK.get_rect(centerx=WINDOW_X // 2, centery=140)
    create_rect = CREATEBUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y - 80)

    death_screen = False # play 도중 죽었는가
    play = True # 게임이 실행중인가
    start_main = True # 메인 화면인 돌아가는 중인가
    start_set = False # 설정 화면이 돌아가는 중인가
    login = False # 로그인이 되었는가
    signup = False # 회원가입
    pressed_button = False # 현재 버튼을 눌렀는가
    playing = False # 게임을 플레이 중인가
    id_click = False
    pass_click = False
    loginscreen = False
    inputid = ''
    inputpass = ''
    success = False

    inputfont = pygame.font.Font('font/PixelEnglishFont.ttf', 20)
    id_font = inputfont.render(inputid, True, BLACK)
    id_font_rect = id_font.get_rect()
    pass_font = inputfont.render(inputpass, True, BLACK)
    pass_font_rect = pass_font.get_rect()
    enter = True

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

            if id_click:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        id_click = False
                        pass_click = True
                        enter = True
                    elif event.key == pygame.K_BACKSPACE:
                        inputid = inputid[:-1]
                    else:
                        if len(inputid) < 10:
                            inputid += event.unicode
            if pass_click:
                if not enter:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:

                            id_click = False
                            pass_click = False
                            success = True
                            if loginscreen:
                                success = gm.login(inputid, inputpass)
                            if signup:
                                success = gm.signup(inputid, inputpass)
                            print(success)
                        elif event.key == pygame.K_BACKSPACE:
                            inputpass = inputpass[:-1]
                        else:
                            if len(inputpass) < 12:
                                inputpass += event.unicode

        mousePos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            pressed_button = False
        if event.type == pygame.KEYDOWN:
            enter = False


        if signup:
            GAME_SCREEN.fill(WHITE)
            if id_input_rect.collidepoint(mousePos) or id_click:

                if event.type == pygame.MOUSEBUTTONDOWN:
                    id_click = True
                    pass_click = False

                id_input_rect = IDINPUT[1].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 200)
                GAME_SCREEN.blit(IDINPUT[1], id_input_rect)
                id_rect = ID[1].get_rect(midright=id_input_rect.midleft)
                GAME_SCREEN.blit(ID[1], id_rect)
            else:
                id_input_rect = IDINPUT[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 200)
                GAME_SCREEN.blit(IDINPUT[0], id_input_rect)
                id_rect = ID[0].get_rect(midright=id_input_rect.midleft)
                GAME_SCREEN.blit(ID[0], id_rect)

            id_font = inputfont.render(inputid, True, BLACK)
            id_font_rect.center = (WINDOW_X // 2 - 80, WINDOW_Y // 2 - 200)
            GAME_SCREEN.blit(id_font, id_font_rect)

            if pass_input_rect.collidepoint(mousePos) or pass_click:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    id_click = False
                    pass_click = True
                pass_input_rect = PASSINPUT[1].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 75)
                GAME_SCREEN.blit(PASSINPUT[1], pass_input_rect)
                pass_rect = PASS[1].get_rect(midright=pass_input_rect.midleft)
                GAME_SCREEN.blit(PASS[1], pass_rect)
            else:
                pass_input_rect = PASSINPUT[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 75)
                GAME_SCREEN.blit(PASSINPUT[0], pass_input_rect)
                pass_rect = PASS[0].get_rect(midright=pass_input_rect.midleft)
                GAME_SCREEN.blit(PASS[0], pass_rect)

            if len(inputpass) > 0 and pass_click:
                pass_font = inputfont.render(((len(inputpass)-1)*'*')+inputpass[-1], True, BLACK)
            elif len(inputpass) > 0:
                pass_font = inputfont.render((len(inputpass) * '*'), True, BLACK)
            else:
                pass_font = inputfont.render(inputpass, True, BLACK)
            pass_font_rect.center = (WINDOW_X // 2 - 80, WINDOW_Y // 2 - 75)
            GAME_SCREEN.blit(pass_font, pass_font_rect)

            if create_rect.collidepoint(mousePos):
                if not pressed_button:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pressed_button = True
                        success = True
                        success = gm.signup(inputid, inputpass)
                        print(success)
                create_rect = CREATEBUTTON[1].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y - 80)
                GAME_SCREEN.blit(CREATEBUTTON[1], create_rect)

            else:
                create_rect = CREATEBUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y - 80)
                GAME_SCREEN.blit(CREATEBUTTON[0], create_rect)

            if back_rect.collidepoint(mousePos):
                if not pressed_button:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        start_main = True
                        signup = False
                        id_click = False
                        pass_click = False
                        pressed_button = True
                        inputpass = ''
                        inputid = ''
                back_rect = BACK_BUTTON[1].get_rect(centerx=WINDOW_X - 150, centery=WINDOW_Y - 80)
                GAME_SCREEN.blit(BACK_BUTTON[1], back_rect)

            else:
                back_rect = BACK_BUTTON[0].get_rect(centerx=WINDOW_X - 150, centery=WINDOW_Y - 80)
                GAME_SCREEN.blit(BACK_BUTTON[0], back_rect)

        if loginscreen:
            GAME_SCREEN.fill(WHITE)
            if id_input_rect.collidepoint(mousePos) or id_click:

                if event.type == pygame.MOUSEBUTTONDOWN:
                    id_click = True
                    pass_click = False

                id_input_rect = IDINPUT[1].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 200)
                GAME_SCREEN.blit(IDINPUT[1], id_input_rect)
                id_rect = ID[1].get_rect(midright=id_input_rect.midleft)
                GAME_SCREEN.blit(ID[1], id_rect)
            else:
                id_input_rect = IDINPUT[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 200)
                GAME_SCREEN.blit(IDINPUT[0], id_input_rect)
                id_rect = ID[0].get_rect(midright=id_input_rect.midleft)
                GAME_SCREEN.blit(ID[0], id_rect)

            id_font = inputfont.render(inputid, True, BLACK)
            id_font_rect.center = (WINDOW_X // 2 - 80, WINDOW_Y // 2 - 200)
            GAME_SCREEN.blit(id_font, id_font_rect)

            if pass_input_rect.collidepoint(mousePos) or pass_click:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    id_click = False
                    pass_click = True
                pass_input_rect = PASSINPUT[1].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 75)
                GAME_SCREEN.blit(PASSINPUT[1], pass_input_rect)
                pass_rect = PASS[1].get_rect(midright=pass_input_rect.midleft)
                GAME_SCREEN.blit(PASS[1], pass_rect)
            else:
                pass_input_rect = PASSINPUT[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 75)
                GAME_SCREEN.blit(PASSINPUT[0], pass_input_rect)
                pass_rect = PASS[0].get_rect(midright=pass_input_rect.midleft)
                GAME_SCREEN.blit(PASS[0], pass_rect)

            if len(inputpass) > 0 and pass_click:
                pass_font = inputfont.render(((len(inputpass) - 1) * '*') + inputpass[-1], True, BLACK)
            elif len(inputpass) > 0:
                pass_font = inputfont.render((len(inputpass) * '*'), True, BLACK)
            else:
                pass_font = inputfont.render(inputpass, True, BLACK)
            pass_font_rect.center = (WINDOW_X // 2 - 80, WINDOW_Y // 2 - 75)
            GAME_SCREEN.blit(pass_font, pass_font_rect)

            if login_rect.collidepoint(mousePos):
                if not pressed_button:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        gm.login(inputid, inputpass)
                        pressed_button = True
                login_rect = LOGINBUTTON[1].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y - 80)
                GAME_SCREEN.blit(LOGINBUTTON[1], login_rect)

            else:
                login_rect = LOGINBUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y - 80)
                GAME_SCREEN.blit(LOGINBUTTON[0], login_rect)


            if back_rect.collidepoint(mousePos):
                if not pressed_button:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        start_main = True
                        loginscreen = False
                        id_click = False
                        pass_click = False
                        pressed_button = True
                        inputpass = ''
                        inputid = ''
                back_rect = BACK_BUTTON[1].get_rect(centerx=WINDOW_X - 150, centery=WINDOW_Y - 80)
                GAME_SCREEN.blit(BACK_BUTTON[1], back_rect)

            else:
                back_rect = BACK_BUTTON[0].get_rect(centerx=WINDOW_X - 150, centery=WINDOW_Y - 80)
                GAME_SCREEN.blit(BACK_BUTTON[0], back_rect)

        if start_main:  # 메인 화면
            GAME_SCREEN.fill(WHITE)
            GAME_SCREEN.blit(DOWNRUN_MARK, downrun_mark_rect)
            if start_button_rect.collidepoint(mousePos):
                if not pressed_button:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        start_main = False
                        playing = True
                        pressed_button = True
                start_button_rect = START_BUTTON[1].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 65)
                GAME_SCREEN.blit(START_BUTTON[1], start_button_rect)
            else:
                start_button_rect = START_BUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 - 65)
                GAME_SCREEN.blit(START_BUTTON[0], start_button_rect)
            if setting_button_rect.collidepoint(mousePos):
                if not pressed_button:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        start_main = False
                        start_set = True
                        pressed_button = True
                setting_button_rect = SETTING_BUTTON[1].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 + 65)
                GAME_SCREEN.blit(SETTING_BUTTON[1], setting_button_rect)
            else:
                setting_button_rect = SETTING_BUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 + 65)
                GAME_SCREEN.blit(SETTING_BUTTON[0], setting_button_rect)
            if not login:
                if login_rect.collidepoint(mousePos):
                    if not pressed_button:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            loginscreen = True
                            start_main = False
                            pressed_button = True
                    login_rect = LOGINBUTTON[1].get_rect(centerx=150, centery=WINDOW_Y - 80)
                    GAME_SCREEN.blit(LOGINBUTTON[1], login_rect)

                else:
                    login_rect = LOGINBUTTON[0].get_rect(centerx=150, centery=WINDOW_Y - 80)
                    GAME_SCREEN.blit(LOGINBUTTON[0], login_rect)

                if signup_rect.collidepoint(mousePos):
                    if not pressed_button:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            signup = True
                            start_main = False
                            pressed_button = True
                    signup_rect = SIGNUPBUTTON[1].get_rect(centerx=450, centery=WINDOW_Y - 80)
                    GAME_SCREEN.blit(SIGNUPBUTTON[1], signup_rect)
                else:
                    signup_rect = SIGNUPBUTTON[0].get_rect(centerx=450, centery=WINDOW_Y - 80)
                    GAME_SCREEN.blit(SIGNUPBUTTON[0], signup_rect)

            elif login:
                if logout_rect.collidepoint(mousePos):
                    if not pressed_button:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            login = False
                            pressed_button = True
                    logout_rect = LOGOUTBUTTON[1].get_rect(centerx=150, centery=WINDOW_Y - 80)
                    GAME_SCREEN.blit(LOGOUTBUTTON[1], logout_rect)

                else:
                    logout_rect = LOGOUTBUTTON[0].get_rect(centerx=150, centery=WINDOW_Y - 80)
                    GAME_SCREEN.blit(LOGOUTBUTTON[0], logout_rect)

        elif start_set:  # 설정 화면
            GAME_SCREEN.fill(WHITE)

            if back_rect.collidepoint(mousePos):
                if not pressed_button:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        start_main = True
                        start_set = False
                        pressed_button = True
                back_rect = BACK_BUTTON[1].get_rect(centerx=WINDOW_X - 150, centery=WINDOW_Y - 80)
                GAME_SCREEN.blit(BACK_BUTTON[1], back_rect)

            else:
                back_rect = BACK_BUTTON[0].get_rect(centerx=WINDOW_X - 150, centery=WINDOW_Y - 80)
                GAME_SCREEN.blit(BACK_BUTTON[0], back_rect)
        elif playing:  # play 화면
            if not death_screen:
                GAME_SCREEN.fill(BLACK)
                player.action()
                player.break_obj()
                player.draw()
                gm.score_up()
                death_screen = gm.dino_obj_control()
            else:
                GAME_SCREEN.blit(DEATH_SCREEN, death_screen_rect)
                GAME_SCREEN.blit(GAMEOVER, gameover_rect)
                if again_button_rect.collidepoint(mousePos):
                    if not pressed_button:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            death_screen = False
                            pressed_button = True
                    again_button_rect = AGAIN_BUTTON[1].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 + 50)
                    GAME_SCREEN.blit(AGAIN_BUTTON[1], again_button_rect)

                else:
                    again_button_rect = AGAIN_BUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 + 50)
                    GAME_SCREEN.blit(AGAIN_BUTTON[0], again_button_rect)
                if gomain_button_rect.collidepoint(mousePos):
                    if not pressed_button:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            death_screen = False
                            start_main = True
                            playing = False
                            pressed_button = True
                    gomain_button_rect = GOMAIN_BUTTON[1].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 + 150)
                    GAME_SCREEN.blit(GOMAIN_BUTTON[1], gomain_button_rect)
                else:
                    gomain_button_rect = GOMAIN_BUTTON[0].get_rect(centerx=WINDOW_X // 2, centery=WINDOW_Y // 2 + 150)
                    GAME_SCREEN.blit(GOMAIN_BUTTON[0], gomain_button_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

main()