import cv2
from keras.models import load_model
import numpy as np
import random
import os
import time

user_wins = 0
computer_wins = 0


start = time.time()

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#countdown timer
def countdown_timer():
    seconds = int(input("How many seconds to wait?"))
    for i in range(seconds):
        print(str(seconds - i) + "remaining")
        time.sleep(1)
countdown_timer()

def get_computer_choice():
    possible_actions = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_actions)
    return computer_choice


def get_prediction(): 
    
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
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
        return prediction

#get_prediction()

#to determine the winner
def get_winner():
    #user_choice = "rock"
   # computer_choice = "scissors"
    user_choice = get_prediction()
    computer_choice = get_computer_choice()

    if user_choice == computer_choice:
        print(user_choice)
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock" and  computer_choice == "scissors":
        print(user_choice)
        print("Rock smashes scissors! You win!")
    elif user_choice == "Rock" and computer_choice == "Paper":
        print(user_choice)
        print("Paper covers rock! You lose.")
    elif user_choice == "paper" and computer_choice == "rock":
        print(user_choice)
        print("Paper covers rock! You win!")
    elif user_choice == "Paper" and computer_choice == "Scissors":
        print(user_choice)
        print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors" and computer_choice == "paper":
        print(user_choice)
        print("Scissors cuts paper! You win!")
    elif user_choice == "Scissors" and computer_choice == "Rock":
        print(user_choice)
        print("Rock smashes scissors! You lose.")

get_winner()

#To detemine script execution time
end = time.time()
total_time = end - start
print("\n Script execution time:" + str(total_time))
    
          
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

