import os
import os.path


# 현 파일위치 반환
current_path = os.path.dirname(__file__)

print(type(current_path))
print(current_path)

path_list = []
for i in range(0,len(current_path)-1):

    p=current_path[len(current_path)-1-i:]
    print(p)
    k=p.find('\\')
    print(k)
    if k==0:
        path_list.append(p)

current_path = current_path.replace(path_list[0],'\\play_record.csv')
    


print(current_path)