import time
from fastapi import FastAPI,Request
from fastapi.responses import FileResponse

from ultralytics import YOLO



model = YOLO('yolov8n.pt')
# 각 구역별 타이머 (여기서는 2번만 예시)
box_timers = {1: None, 2: None, 3: None, 4: None}
Tmn = {
    1: "/static/img/human.png",
    2: "/static/img/human.png",
    3: "/static/img/human.png",
    4: "/static/img/human.png"
}
def trail_detect_run():
    print("런닝머신감지기능작동")
    #조건 넣는 구간!!!!
    print(Tmn[1])
    condition = {1: True, 2: False, 3: True, 4: True}



    while True:
    # 카메라에서 프레임 읽기 (예시에서는 비디오 파일 사용)
    # 현제는 테스트용으로 1,3,4번구역 사용중 2번자리 비어있음
    #
    #
    #
        for trmil in range(1, 5):
            if condition[trmil]:
                Tmn[trmil] = "/static/img/onhuman.png"
            else:
                Tmn[trmil] = "/static/img/offhuman.png"

        time.sleep(1)
        print("변경")



       

@app.get('/TMdata')
async def get_tm_data():
    return {
        "Tmn1": Tmn[1],
        "Tmn2": Tmn[2],
        "Tmn3": Tmn[3],
        "Tmn4": Tmn[4]
    }

 