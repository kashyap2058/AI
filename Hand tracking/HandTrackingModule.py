import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False,maxHands=2,detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.modelComplexity=modelComplexity
        self.trackCon=trackCon
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,self.modelComplexity,self.detectionCon,self.trackCon)  #params: static image mode(for tracking and detect True xa vane everytime detect garxa making it slow, False xa vane tracks only after reaching a certain confidence value)
        self.mpDraw=mp.solutions.drawing_utils
    def findHands(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB) #camera bata hands lai process garxa
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
        #extracting informaton about single or multiple handmarks
            for handlanmark in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handlanmark,self.mpHands.HAND_CONNECTIONS) #HAND_CONNETIONS draws lines to show hands
        return img

    def findPosition(self,img,handNo=0,draw=True):
        lmlist=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                # print(id,landmark)
                #TO get pixel values:
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),8,(255,0,0),cv2.FILLED)

        return lmlist


def main():
    prev_time=0
    cur_time=0
    cap=cv2.VideoCapture(0)
    detector=handDetector()
    while True:
        sucess,img=cap.read()
        img=detector.findHands(img)
        lmlist=detector.findPosition(img)
        if len(lmlist)!=0:
            print(lmlist[4]) #to print the coordinate of thumb
        # for fps info
        cur_time=time.time()
        fps=1/(cur_time-prev_time)
        prev_time=cur_time
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
        cv2.imshow("Image ",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__=="__main__":
    main()

