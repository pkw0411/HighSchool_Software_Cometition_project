
import os
import os.path
from random import *
import pandas as pd
import pickle

# 현 파일위치 반환
current_path = os.path.dirname(__file__)

# p2에 넣어줄 게임 플레이 방식
b = []
c = []

# 파일이 있으면 실행
if os.path.isfile(current_path+'\\play_record.csv'):
    # 데이터 가져오기
    df = pd.read_csv(current_path+'\\play_record.csv')

    #fps만 뽑아 비교
    d = df['fps']
    d_list = list(d.values)
    max_d = max(d_list)
    
    # fps 1부터 가장 큰 프레임까지 봅기
    for i in range(1, max_d+1):

        # 해당 프레임의 값들 가져오기
        g = df[df.fps==i]

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

