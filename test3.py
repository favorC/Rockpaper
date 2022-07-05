import cv2
from cv2 import FONT_HERSHEY_PLAIN
from keras.models import load_model
import numpy as np
import random
import os
import time

class RPS:
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.possible_actions = ["rock", "paper", "scissors", "Nothing"]
        self.comp_scores = 0
        self.user_scores = 0
        self.game_rounds = 0

    #Start video capture
    def video_capture(self):
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        ret, frame = self.cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        #prediction = self.model.predict(self.data)
        cv2.imshow('frame', frame)
    
    
    def video_capture2(self):
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        #while True: 
        ret, frame = self.cap.read()
        self.crop_image = frame[200:1000, 300:1100]
        
        cv2.imshow('frame', frame)
        
        
    
    def get_predictions(self):
        prediction = self.model.predict(self.data)
        max_index = np.argmax(prediction[0])
        #print(prediction)
        #print(max_index)
        #self.user_choice = " "
        if max_index == 0:
            self.user_choice ="Rock"
            print(self.user_choice)
            return self.user_choice
        elif max_index == 1:
            self.user_choice = "Paper"
            print(self.user_choice)
            return self.user_choice
        elif max_index == 2:
            self.user_choice = "Scissors"
            print(self.user_choice)
            return self.user_choice
        else:
            self.user_choice = "Nothing"
            print(self.user_choice)
            return self.user_choice
       



    def get_computer_choice(self):
        self.possible_actions = ["rock", "paper", "scissors","nothing"]
        #computer_choice = random.choice(self.possible_actions)
        computer_choice = "nothing"

        print(f'computer choice is {computer_choice}')
        return computer_choice

    def get_winner(self):
        comp = self.get_computer_choice()
        user = self.get_predictions()
        while True:
            random_index = random.randint(0,2)
            comp = self.get_computer_choice()
            user = self.get_predictions()
      #while user_choice not in choices:
        #user_choice = input("That is not a valid choice. Please try again: ").lower()
            print()
            print("Your choice:", user)
            print("Computer's choice:", comp)
            print()

            if user == 'rock':
              if comp == 'rock':
                 print("It's a tie!")
            elif comp == 'scissors':
                 print("You win!")
                 self.user_score +=1
            elif comp == 'paper':
                 print("You lose!")
                 self.comp_scores +=1
            elif user == 'paper':
                if comp == 'paper':
                  print("It's a tie!")
            elif comp == 'rock':
                 print("You win!")
                 self.user_scores +=1
            elif comp == 'scissors':
                 print("You lose!")
                 self.comp_scores +=1
            elif user == 'scissors':
                if comp == 'scissors':
                   print("It's a tie!")
            elif comp == 'paper':
                  print("You win!")
                  self.user_scores +=1
            elif comp == 'rock':
                 print("You lose!")
                 self.comp_scores +=1

            print()
            print("You have "+str(self.user_scores)+" wins")
            print("The computer has "+str(self.comp_scores)+" wins")
            print()


        #print(f"user choice is {user}")
        # if comp == user:
        #     print(comp)
        #     print(user)
        #     self.winner = "Tie"

        #     self.game_rounds += 1
        #     print(" It's a tie!")
        #     return self.winner
       
        # elif comp == "Scissors" and  user == "Rock":
        #     self.winner = "user"
        #     self.game_rounds += 1
        #     self.user_scores += 1
        #     print("Rock smashes scissors! You win!")
        #     return self.winner

        # elif comp == "Rock" and user == "Scissors":
        #     self.winner = "comp"
        #     self.game_rounds += 1
        #     self.comp_scores += 1
        #     print("Rock smashes scissors! Computer wins.")
        #     return self.winner
        # #     # #return "computer_choice"
        # elif comp == "Paper" and user == "Rock":
        #     self.winner = "user"
        #     self.game_rounds += 1
        #     self.comp_scores += 1
        #     print("user wins.")
        #     return self.winner
        # #     # #return "computer_choice"
        # # elif comp == "Paper" and user == "Rock":
        # #     self.winner = "comp"
        # #     self.game_rounds += 1
        # #     self.comp_scores += 1
        # #     print("Paper covers rock! You lose.")
        # #     return self.winner
        # #     # #return "computer_choice"
        # elif comp == "Rock" and user == "Paper":
        #     self.winner = "user"
        #     self.game_rounds += 1
        #     self.user_scores += 1
        #     print("Paper covers rock! You win!")
        #     return self.winner
        # #     # #return "user"
        # # elif comp == "Scissors" and user == "Paper":
        # #     self.winner = "comp"
        # #     self.game_rounds += 1
        # #     self.comp_scores += 1
        # #     print("Scissors cuts paper! You lose.")
        # #     return self.winner
        # #     #return "computer_choice"
        # # elif comp == "Paper" and user == "Scissors":
        # #     self.winner = "user"
        # #     self.game_rounds += 1
        # #     self.user_scores += 1
        # #     print("Scissors cuts paper! You win!")
        # #     return self.winner
        # #     #return "prediction"
        
        # # else:
        # #     return self.winner
        # #     #print("You played Nothing,Try Again")

       
    def stop_video(self):
        self.cap.release()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
          

def play():
    game = RPS()
    while True:
        game.video_capture2()
        ret, frame = game.cap.read()
        cv2.imshow("frame", frame)
        cv2.waitKey(30)
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        game.data[0] = normalized_image
        game.get_computer_choice()
        game.get_predictions()
        game.get_winner()
        if game.game_rounds == 3:
           print("Game Over!")
           game.stop_video()
           break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
play()
#game.get_predictions()