import cv2
import mediapipe as mp
import time

def findpos(results,img,handNo,draw=True):
    lmlist=[]
    if results.multi_hand_landmarks:
        myHand=results.multi_hand_landmarks[handNo]
        for id,lm in enumerate(myHand.landmark):
                # print(id,landmark)
                #TO get pixel values:
            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            lmlist.append([id,cx,cy])
            if draw:
                   cv2.circle(img,(cx,cy),15,(255,255,0),cv2.FILLED)
    return lmlist

def findhand(img,handno,hands,mpDraw,mpHands,draw=True):
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    if results.multi_hand_landmarks:
        #extracting informaton about single or multiple handmarks
        for handlanmark in results.multi_hand_landmarks:
            for handlanmark in results.multi_hand_landmarks:
                if draw:
                    mpDraw.draw_landmarks(img,handlanmark,mpHands.HAND_CONNECTIONS) #HAND_CONNETIONS draws lines to show hands
    return img,results #HAND_CONNETIONS draws lines to show hands

    # # for fps info
    # cur_time=time.time()
    # fps=1/(cur_time-prev_time)
    # prev_time=cur_time
    # cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
    # cv2.imshow("Image ",img)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
# prev_time=0
# cur_time=0
# cap=cv2.VideoCapture(0)
# mpHands=mp.solutions.hands
# hands=mpHands.Hands()
# mpDraw=mp.solutions.drawing_utils 
# while True:
#     sucess,img=cap.read()
#     img,results=findhand(img,0,hands,mpDraw)
#     lmlist=findpos(results,img,0)
#     if len(lmlist)!=0:
#         print(lmlist[4])
#     cur_time=time.time()
#     fps=1/(cur_time-prev_time)
#     prev_time=cur_time
#     cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
#     cv2.imshow("Image ",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()