import pygame
import os
import os.path
from random import *
import pandas as pd
import pickle

# 기본 초기화

pygame.init() #초기화

# 화면크기 설정

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Game")

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path,"images") # images 폴더 위치 반환

fps = 60

# Movement_list
# p2에 넣어줄 게임 플레이 방식
b = []
c = []


# 파일이 있으면 실행
if os.path.isfile(current_path+'\\play_record.csv'):
    # 데이터 가져오기
    df_1 = pd.read_csv(current_path+'\\play_record.csv')

    #fps만 뽑아 비교
    d = df_1['fps']
    d_list = list(d.values)
    max_d = max(d_list)
    
    # fps 1부터 가장 큰 프레임까지 봅기
    for i in range(1, max_d+1):

        # 해당 프레임의 값들 가져오기
        g = df_1[df_1.fps==i]

        # 프레임값들을 리스트로 변환
        g_values = list(g.values)
        
        # 같은 프레임안 플레이들중 렌덤으로 하나 뽑기
        a = randint(0,len(g_values)-1)
        # 렌덤으로 뽑은  플레이 저장
        b.append(list(g_values[a]))
    
    # 플레이 정보중 이긴 플레이만 따로 저장
    for i in b:
        
        b= i[2]
        c.append(eval(b))
    
    print(str(c))

    #피클에 옮기기
    with open(current_path+'\\play_record.txt','wb') as fw:
        pickle.dump(c,fw)

# 파일이 없을때
else : 
    print("파일이 없습니다.")

# Movement_list

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect(). size
stage_width = stage_size[0]
stage_height = stage_size[1]

#케릭터 만들기
p1 = pygame.image.load(os.path.join(image_path, "player1.png"))
p1_size = p1.get_rect().size
p1_width = p1_size[0]
p1_height = p1_size[1]
p1_x_pos = (screen_width/3)-(p1_width/2)
p1_y_pos = screen_height-stage_height - p1_height

p2 = pygame.image.load(os.path.join(image_path, "player2.png"))
p2_size = p2.get_rect().size
p2_width = p2_size[0]
p2_height = p2_size[1]
p2_x_pos = (screen_width/3)*2-(p2_width/2)
p2_y_pos = screen_height-stage_height - p2_height

# 창 만들기
p1_weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
p1_weapon_size = p1_weapon.get_rect().size
p1_weapon_width = p1_weapon_size[0]
p1_weapon_height = p1_weapon_size[1]
p1_weapon_x_pos = p1_x_pos + p1_width/2 -p1_weapon_width/2
p1_weapon_y_pos = p1_y_pos + p1_height/2

p2_weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
p2_weapon_size = p2_weapon.get_rect().size
p2_weapon_width = p2_weapon_size[0]
p2_weapon_height = p2_weapon_size[1]
p2_weapon_x_pos = p2_x_pos + p2_width/2 -p2_weapon_width/2
p2_weapon_y_pos = p2_y_pos + p2_height/2

# 방패 만들기
p1_shield = pygame.image.load(os.path.join(image_path, "shield1.png"))
p1_shield_size = p1_shield.get_rect().size
p1_shield_width = p1_shield_size[0]
p1_shield_height = p1_shield_size[1]
p1_shield_x_pos = p1_x_pos + p1_width/2 -p1_shield_width/2
p1_shield_y_pos = p1_y_pos + p1_height/2

p2_shield = pygame.image.load(os.path.join(image_path, "shield2.png"))
p2_shield_size = p2_shield.get_rect().size
p2_shield_width = p2_shield_size[0]
p2_shield_height = p2_shield_size[1]
p2_shield_x_pos = p2_x_pos + p2_width/2 -p2_shield_width/2
p2_shield_y_pos = p2_y_pos + p2_height/2

# 창 끝 만들기
p1_weapon_1 = pygame.image.load(os.path.join(image_path, "p1_weapon.png"))
p1_weapon_1_size = p1_weapon_1.get_rect().size
p1_weapon_1_width = p1_weapon_1_size[0]
p1_weapon_1_height = p1_weapon_1_size[1]
p1_weapon_1_y_pos = p1_weapon_y_pos

p2_weapon_1 = pygame.image.load(os.path.join(image_path, "p2_weapon.png"))
p2_weapon_1_size = p2_weapon_1.get_rect().size
p2_weapon_1_width = p2_weapon_1_size[0]
p2_weapon_1_height = p2_weapon_1_size[1]
p2_weapon_1_y_pos = p2_weapon_y_pos

# player1 속도
to_x_p1 = 0
to_y_p1 = 0

# player2 속도
to_x_p2 = 0
to_y_p2 = 0


# 무기 속도
p1_weapon_to = 0
p2_weapon_to = 0

# player 방향
to_p1 =0
to_p2 =1

# player 무기 속도
p1_to =0
p2_to =0

# player 무기 공격 시간 조절
i_p1=0
i_p2=0

# player 움직임 허용
move_p1 = True
move_p2 = True

# player 공격 허용
attack_p1 =False
attack_p2 =False

# player 움직임 속도
speed_p1 = 5
speed_p2 = 5

# player 방패 허용
shield_p1 = False
shield_p2 = False

# player SHIFT 허용
SHIFT_p1 = True
SHIFT_p2 = True

# player SPACE 허용
SPACE_p1 = True
SPACE_p2 = True

# 공격 가능
attack_able_p1 = True
attack_able_p2 = True

weapon_speed = 5

weapon_F = 30

# 엔딩 텍스트
ending_txt ="None"
color = (0,0,0)
game_font = pygame.font.SysFont('arial', 40,True,False)

#플레이어 행동
player2_event ={'to_en':False, 'against_en': False, 'jump':False, 'attack': False, 'shield': False}
player1_event ={'to_en':False, 'against_en': False, 'jump':False, 'attack': False, 'shield': False}

# play_record = open(current_path + "\\" + "play_record.txt","a")

# 플레이어 행동 모두 저장
play_p1 = []
play_p2 = []

# 현재 프레임
now_frame = 0

# 게임 기록 저장 리스트
record_list = []

# 게임 기록
record = {'between': 0, 'fps': 0,'winner':{}, 'loser': {}}

# AI가 움직일 행동 정보 리스트
AI_list = []

if os.path.isfile(os.path.join(current_path,'play_record.txt')):
    with open(os.path.join(current_path,'play_record.txt'),"rb") as fr:
        AI_list = pickle.load(fr)

AI_len = len(AI_list)

k=0

# 게임 진행
running = True
while running:

    # 초당 프레임
    dt = clock.tick(fps)

    # player1 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if move_p1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if p1_x_pos -p2_x_pos >= 0:
                        player1_event['against_en']=True
                    elif p1_x_pos -p2_x_pos < 0:
                        player1_event['to_en']=True
                    to_x_p1 += speed_p1
                    to_p1 = 0
                if event.key == pygame.K_LEFT:
                    if p1_x_pos -p2_x_pos < 0:
                        player1_event['against_en']=True
                    elif p1_x_pos -p2_x_pos >= 0:
                        player1_event['to_en']=True
                    to_x_p1 -= speed_p1
                    to_p1 = 1
                if event.key == pygame.K_UP:
                    if p1_y_pos == screen_height - stage_height - p1_height:
                        player1_event['jump']=True
                        to_y_p1 = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    if p1_x_pos -p2_x_pos >= 0:
                        player1_event['against_en']=False
                    elif p1_x_pos -p2_x_pos < 0:
                        player1_event['to_en']=False
                    to_x_p1 = 0
                if event.key == pygame.K_LEFT:
                    if p1_x_pos -p2_x_pos < 0:
                        player1_event['against_en']=False
                    elif p1_x_pos -p2_x_pos >= 0:
                        player1_event['to_en']=False
                    to_x_p1 = 0
        if SPACE_p1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if p1_y_pos == screen_height - stage_height - p1_height:
                        to_x_p1 = 0
                        attack_p1 = True
                        move_p1 = False
                        SHIFT_p1 = False
        if SHIFT_p1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    if p1_y_pos == screen_height - stage_height - p1_height:
                        player1_event['shield']=True
                        to_x_p1 = 0
                        move_p1 = False
                        shield_p1 = True
                        SPACE_p1 =False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    player1_event['shield']=False
                    shield_p1 = False
                    move_p1 = True
                    SPACE_p1 = True
    # player2 AI

    # player2 AI, 움직임 조건

    if k< AI_len:
        player2_event = AI_list[k]



    if k>=AI_len:
        player2_event ={'to_en':False, 'against_en': False, 'jump':False, 'attack': False, 'shield': False}
        movement_p2=randint(0,999)

        if movement_p2%10 <= int(int(2*abs(p1_x_pos -p2_x_pos))/100):
            player2_event['to_en']=True
        elif int(movement_p2/10)%10 >= int(7+int(abs(p1_x_pos -p2_x_pos))/100):
                player2_event['attack']=True
        elif int(movement_p2/10)%10 < int(3+int(abs(p1_x_pos -p2_x_pos))/100):
                player2_event['against_en']=True
        elif int(movement_p2/100) < int(7-int(abs(p1_x_pos -p2_x_pos))/100):
                player2_event['jump']=True
        elif int(movement_p2/100) >= int(7-int(abs(p1_x_pos -p2_x_pos))/100):
                pass
        elif int(movement_p2/10)%10 < int(7+int(abs(p1_x_pos -p2_x_pos))/100):
                player2_event['shield']=True

    # player2 움직임
    for event in player2_event: 
        if move_p2:
                
            if player2_event['to_en']:
                if p1_x_pos -p2_x_pos >= 0:
                    to_x_p2 = speed_p2
                    to_p2 = 0
                elif p1_x_pos -p2_x_pos < 0:
                    to_x_p2 = -speed_p2
                    to_p2 = 1
            if player2_event['against_en']:
                if p1_x_pos -p2_x_pos >= 0:
                    to_x_p2 = -speed_p2
                    to_p2 = 1
                elif p1_x_pos -p2_x_pos < 0:
                    to_x_p2 = speed_p2
                    to_p2 = 0
            if player2_event['jump']:
                if p2_y_pos == screen_height - stage_height - p2_height:
                    to_y_p2 = 10
                    player2_event['jump'] = False
        if SPACE_p2:
            if player2_event['attack']:
                if p2_y_pos == screen_height - stage_height - p2_height:
                    to_x_p2 = 0
                    attack_p2 = True
                    move_p2 = False
                    SHIFT_p2 = False
        if SHIFT_p2:
            if player2_event['shield']:
                if p2_y_pos == screen_height - stage_height - p2_height:
                    to_x_p2 = 0
                    move_p2 = False
                    shield_p2 = True
                    SPACE_p2 =False
            if player2_event['shield'] == False:
                shield_p2 = False
                move_p2 = True
                SPACE_p2 = True
        
        

    # player1의 점프후 하강 및 스테이지 밑으로 내려가지 않게 하기
    p1_y_pos -= to_y_p1
    if p1_y_pos < screen_height - stage_height - p1_height:
        to_y_p1 -= 25/fps
    if p1_y_pos > screen_height - stage_height - p1_height:
        player1_event['jump']=False
        to_y_p1 = 0 
        p1_y_pos = screen_height - stage_height - p1_height
    
    # player2의 점프후 하강 및 스테이지 밑으로 내려가지 않게 하기
    p2_y_pos -= to_y_p2
    if p2_y_pos < screen_height - stage_height - p2_height:
        to_y_p2 -= 25/fps
    if p2_y_pos > screen_height - stage_height - p2_height:
        to_y_p2 = 0 
        p2_y_pos = screen_height - stage_height - p2_height
    
    # player의 x의 이동
    p1_x_pos += to_x_p1
    p2_x_pos += to_x_p2
    
    # player 무기의 이동
    p1_to += p1_weapon_to
    p2_to += p2_weapon_to

    # player1 무기의 위치
    p1_weapon_x_pos = p1_x_pos + p1_width/2 -p1_weapon_width/2 + p1_to
    p1_weapon_y_pos = p1_y_pos + p1_height/2
    p1_weapon_1_y_pos = p1_weapon_y_pos
    
    # player2 무기의 위치
    p2_weapon_x_pos = p2_x_pos + p2_width/2 -p2_weapon_width/2 + p2_to
    p2_weapon_y_pos = p2_y_pos + p2_height/2
    p2_weapon_1_y_pos = p2_weapon_y_pos

    # player2 방패의 위치
    p1_shield_y_pos = p1_y_pos
    p2_shield_y_pos = p2_y_pos

    # 가로 경계
    if p1_x_pos <0:
        p1_x_pos =0
    
    if p1_x_pos > screen_width - p1_width:
        p1_x_pos = screen_width - p1_width
    
    # 가로 경계
    if p2_x_pos <0:
        p2_x_pos =0
    
    if p2_x_pos > screen_width - p2_width:
        p2_x_pos = screen_width - p2_width
    
    if attack_p1 and p1_y_pos == screen_height - stage_height - p1_height:
        player1_event['attack']=True
        
    # player1 무기의 공격 이동
    if attack_p1 and i_p1 < weapon_F / 2 and to_p1 == 0 and p1_y_pos == screen_height - stage_height - p1_height:
        p1_weapon_to = weapon_speed
    elif attack_p1 and i_p1 >=weapon_F / 2 and i_p1 < weapon_F and to_p1 == 0 and p1_y_pos == screen_height - stage_height - p1_height:
        p1_weapon_to = -weapon_speed
    elif attack_p1 and i_p1 < weapon_F / 2 and to_p1 == 1 and p1_y_pos == screen_height - stage_height - p1_height:
        p1_weapon_to = -weapon_speed
    elif attack_p1 and i_p1 >=weapon_F / 2 and i_p1 < weapon_F and to_p1 == 1 and p1_y_pos == screen_height - stage_height - p1_height:
        p1_weapon_to = weapon_speed
    elif i_p1 >= weapon_F:
        p1_weapon_to = 0
        i_p1 =0
        player1_event['attack']=False
        attack_p1 =False
        move_p1 =True
        SHIFT_p1 = True
    if attack_p1:
        i_p1+=1
    p1_weapon_x_pos += p1_weapon_to
    
    # player2 무기의 공격 이동
    if attack_p2 and i_p2 < weapon_F / 2 and to_p2 == 0 and p2_y_pos == screen_height - stage_height - p2_height:
        p2_weapon_to = weapon_speed
    elif attack_p2 and i_p2 >=weapon_F / 2 and i_p2 < weapon_F and to_p2 == 0 and p2_y_pos == screen_height - stage_height - p2_height:
        p2_weapon_to = -weapon_speed
    elif attack_p2 and i_p2 < weapon_F / 2 and to_p2 == 1 and p2_y_pos == screen_height - stage_height - p2_height:
        p2_weapon_to = -weapon_speed
    elif attack_p2 and i_p2 >=weapon_F / 2 and i_p2 < weapon_F and to_p2 == 1 and p2_y_pos == screen_height - stage_height - p2_height:
        p2_weapon_to = weapon_speed
    elif i_p2 >= weapon_F:
        p2_weapon_to = 0
        i_p2 =0 
        attack_p2 =False
        move_p2 =True
        SHIFT_p2 = True
    if attack_p2:
        i_p2+=1
    p2_weapon_x_pos += p2_weapon_to
    
    # player1의 방향 조절
    if to_p1 ==0:
        p1_weapon_1_x_pos = p1_weapon_x_pos + p1_weapon_width -p1_weapon_1_width
        p1_shield_x_pos = p1_x_pos + p1_width + 5
    
    if to_p1 ==1:
        p1_weapon_1_x_pos = p1_weapon_x_pos 
        p1_shield_x_pos = p1_x_pos -p1_shield_width -5
    
    # player2의 방향 조절
    if to_p2 ==0:
        p2_weapon_1_x_pos = p2_weapon_x_pos + p2_weapon_width -p2_weapon_1_width
        p2_shield_x_pos = p2_x_pos + p2_width + 5
    
    if to_p2 ==1:
        p2_weapon_1_x_pos = p2_weapon_x_pos 
        p2_shield_x_pos = p2_x_pos -p2_shield_width -5
    
    # 충돌 처리
    
    p1_weapon_1_rect = p1_weapon_1.get_rect()
    p1_weapon_1_rect.left = p1_weapon_1_x_pos
    p1_weapon_1_rect.top = p1_weapon_1_y_pos
    
    p2_weapon_1_rect = p2_weapon_1.get_rect()
    p2_weapon_1_rect.left = p2_weapon_1_x_pos
    p2_weapon_1_rect.top = p2_weapon_1_y_pos
    
    p1_rect = p1.get_rect()
    p1_rect.left = p1_x_pos
    p1_rect.top = p1_y_pos
    
    p2_rect = p2.get_rect()
    p2_rect.left = p2_x_pos
    p2_rect.top = p2_y_pos
    
    # 방어 가능
    if shield_p2:
        if to_p1 != to_p2:
            attack_able_p1 = False
    else:
            attack_able_p1 = True
    if shield_p1:
        if to_p2 != to_p1:
            attack_able_p2 = False
    else:
            attack_able_p2 = True

    

    # 충돌 처리
    if attack_p1:
        if attack_able_p1:
            if p1_weapon_1_rect.colliderect(p2_rect):
                ending_txt = "Red Win"
                color = (255,0,0)
                running =False

    if attack_p2:
        if attack_able_p2:
            if p2_weapon_1_rect.colliderect(p1_rect):
                ending_txt = "Blue Win"
                color = (0,0,255)
                running = False 
    
    #프레임 진행
    now_frame += 1
    k+=1

    # 거리기록, 프레임 기록
    record['between'] = int(abs(p1_x_pos -p2_x_pos))
    record['fps'] = int(now_frame)

    # 리스트에 저장
    record_list.append(dict(record))

    #각 프레임에 플레이어 행동 저장
    play_p1.append(dict(player1_event))
    play_p2.append(dict(player2_event))



    #화면 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0, 680))
    screen.blit(p1,(p1_x_pos, p1_y_pos))
    screen.blit(p2,(p2_x_pos, p2_y_pos))
    screen.blit(p1_weapon, (p1_weapon_x_pos, p1_weapon_y_pos))
    screen.blit(p1_weapon_1, (p1_weapon_1_x_pos, p1_weapon_1_y_pos))
    screen.blit(p2_weapon, (p2_weapon_x_pos, p2_weapon_y_pos))
    screen.blit(p2_weapon_1, (p2_weapon_1_x_pos, p2_weapon_1_y_pos))
    if shield_p1:
        screen.blit(p1_shield, (p1_shield_x_pos, p1_shield_y_pos))
    if shield_p2:
        screen.blit(p2_shield, (p2_shield_x_pos, p2_shield_y_pos))

    pygame.display.update() # 게임화면 그리기

f=0

if ending_txt == "Red Win":
    for i in record_list:
        i['winner'] = dict(play_p1[f])
        i['loser'] = dict(play_p2[f])
        f+=1
if ending_txt == "Blue Win":
    for i in record_list:
        i['winner'] = dict(play_p2[f])
        i['loser'] = dict(play_p1[f])
        f+=1


record = record_list[0]

df = pd.DataFrame(record_list)
if ending_txt != "None":
    
    if os.path.isfile(os.path.join(current_path+'\\play_record.csv')):
        df_read = pd.read_csv(os.path.join(current_path+'\\play_record.csv'))
        df = df_read.append(df,ignore_index = True)
    df.to_csv(os.path.join(current_path+'\\play_record.csv'),index = False)

# 폰트 조절및 생성
msg = game_font.render(ending_txt, True, color)
msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)

pygame.display.update()

pygame.time.delay(2000)

pygame.quit()
