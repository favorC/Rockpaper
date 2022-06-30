import cv2
from cv2 import FONT_HERSHEY_PLAIN
from keras.models import load_model
import numpy as np
import random
import os
import time


def get_computer_choice():
    possible_actions = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_actions)
    print(f'computer choice is {computer_choice}')
    return computer_choice

#user_wins = 0
#computer_wins = 0
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

started = False
next_round = True
count_down = False
counter = 0
elapsed = 0
r_time = 0

message = ''
#t_0 = time.time()
while True:
    ret, frame = cap.read()

    if not started:
        message = 'Press s to start the game'
    if cv2.waitKey(33)== ord('s'):
        if not started:
            counter = time.time()
            started = True
            countdown = True

    if started:
        elapsed = 8 - (time.time() - counter)
        if elapsed <= -3:
            message = 'Press c to continue playing'
            if cv2.waitKey(33) == ord('c'):
                started = False
                elapsed = 0

        #elif elapsed <= 0
        #countdown = False

    cv2.imshow('frame', frame)
    #print(time.time() - t_0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#start = time.time()



# #countdown timer
# def countdown_timer():
#     seconds = int(input("How many seconds to wait?"))
#     for i in range(seconds):
#         print(str(seconds - i) + "remaining")
#         time.sleep(1)
# countdown_timer()




def get_prediction(): 
    start_time = time.time()
    end_time = start_time + 5
    countdown = start_time + 4
    #elapsed = 8 - (time.time() - counter)
    #print(elapsed)
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while time.time() < end_time : 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            print(prediction)
            while time.time() < countdown:
                message = f'Show in .. {int(end_time - time.time())}'
                break
            while countdown < time.time() < end_time:
                message = 'Show your hand'
                break
            cv2.putText(frame, message, (30 , 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
        # while True: 
        #     ret, frame = cap.read()
        #     resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        #     image_np = np.array(resized_frame)
        #     normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        #     data[0] = normalized_image
        #     prediction = model.predict(data)
        #     cv2.imshow('frame', frame)
            #if prediction[0][0] > prediction[0][1] and prediction[0][0] > prediction[0][2]:
            if prediction[0][0] > 0.5:
                #print ('Rock')
                prediction = "Rock"
                
            #elif prediction[0][0] < prediction[0][1] and prediction[0][1] > prediction[0][2]:
            elif prediction[0][1] > 0.5:
                #print('Paper')
                prediction = "Paper"
                
            #elif prediction[0][0] < prediction[0][2] and prediction[0][2] > prediction[0][1]:
            elif prediction[0][2] > 0.5:
                #print('Scissors')
                prediction = "Scissors"
                
            #elif prediction[0][3] > prediction[0][0] and prediction[0][3] > prediction[0][1]:
                ##print('Nothing')
            else: 
                #print('Nothing')
                prediction = "Nothing"
                

            cv2.imshow('frame', frame)
            #print(prediction)
       # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            print(prediction)
            return prediction

get_prediction()

#to determine the winner
def get_winner():
    #user_choice = "rock"
   # computer_choice = "scissors"
    prediction = get_prediction()
    computer_choice = get_computer_choice()
    #winner = ""
    print("success")
    if prediction == computer_choice:
        print(prediction)
        print(f"Both players selected {prediction}. It's a tie!")
        return "Draw"
        
    elif prediction == "rock" and  computer_choice == "scissors":
        print(prediction)
        print("Rock smashes scissors! You win!")
        return "prediction"
    elif prediction == "Rock" and computer_choice == "Paper":
        print(prediction)
        print("Paper covers rock! You lose.")
        return "computer_choice"
    elif prediction == "paper" and computer_choice == "rock":
        print(prediction)
        print("Paper covers rock! You win!")
        return "prediction"
    elif prediction == "Paper" and computer_choice == "Scissors":
        print(prediction)
        print("Scissors cuts paper! You lose.")
        return "computer_choice"
    elif prediction == "scissors" and computer_choice == "paper":
        print(prediction)
        print("Scissors cuts paper! You win!")
        return "prediction"
    elif prediction == "Scissors" and computer_choice == "Rock":
        print(prediction)
        print("Rock smashes scissors! You lose.")
        return "computer_choice"
    
  
        #return winner
get_winner()

# #To detemine script execution time
# end = time.time()
# total_time = end - start
# print("\n Script execution time:" + str(total_time))
    
          
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

