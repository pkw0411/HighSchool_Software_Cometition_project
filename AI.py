
import os
import os.path
from random import *
import pandas as pd
import pickle

# 현 파일위치 반환
current_path = os.path.dirname(__file__)

# p2에 넣어줄 게임 플레이 방식
Action_list = []
Fixed_Action_list = []

# 파일이 있으면 실행
if os.path.isfile(current_path+'\\play_record.csv'):
    # 데이터 가져오기
    DataFrame = pd.read_csv(current_path+'\\play_record.csv')

    #fps만 뽑아 비교
    DF_fps = DataFrame['fps']
    DF_fps_list = list(DF_fps.values)
    max_DF_fps = max(DF_fps_list)
    
    # fps 1부터 가장 큰 프레임까지 봅기
    for i in range(1, max_DF_fps+1):

        # 해당 프레임의 값들 가져오기
        DF_SelectedByFrame = DataFrame[DataFrame.fps==i]

        # 프레임값들을 리스트로 변환
        DFSF_values = list(DF_SelectedByFrame.values)
        
        # 같은 프레임안 플레이들중 렌덤으로 하나 뽑기
        Rnd_Num = randint(0,len(DFSF_values)-1)
        # 렌덤으로 뽑은  플레이 저장
        Action_list.append(list(DFSF_values[Rnd_Num]))
    
    # 플레이 정보중 이긴 플레이만 따로 저장
    for i in Action_list:
        
        Action_list= i[2]
        Fixed_Action_list.append(eval(Action_list))
    
    print(str(Fixed_Action_list))

    #피클에 옮기기
    with open(current_path+'\\play_record.txt','wb') as fw:
        pickle.dump(Fixed_Action_list,fw)

# 파일이 없을때
else : 
    print("파일이 없습니다.")

