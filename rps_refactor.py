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
            self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            self.user_score = 0
            self.computer_score = 0
            self.options = ['rock', 'paper', 'scissors', 'nothing']
            self.game_rounds = 0
        
        
    def start_video(self):
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        ret, self.frame = self.cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        cv2.imshow('frame', self.frame)


    def get_predictions(self):
        prediction = self.model.predict(self.data)
        max_index = np.argmax(prediction[0])
        return max_index
        #print(prediction)
        #print(max_index)
        #self.user_choice = " "

    def get_user_choice(self):
        max_index = self.get_predictions()
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
        self.computer_choice = "nothing"

        print(f'computer choice is {computer_choice}')
        return self.computer_choice

    def get_winner(self):
         
        if self.computer_choice == 'Rock' and self.user_choice == 'Scissors':
            self.winner = 'computer'
            self.computer_score += 1
            #self.game_rounds += 1
            print("Computer win!")

        elif self.computer_choice == 'Rock' and self.user_choice == 'Paper':
            self.winner = 'you'
            self.user_score += 1
            #self.game_rounds += 1
            print("You win!")

        elif self.computer_choice == 'Scissors' and self.user_choice == 'Paper':
            self.winner = 'computer'
            self.computer_score += 1
            #self.game_rounds += 1
            print("Computer win!")


        elif self.computer_choice == 'Scissors' and self.user_choice == 'Rock':
            self.winner = 'you'
            self.user_score += 1
            #self.game_rounds += 1
            print("You win!")

        elif self.computer_choice == 'Paper' and self.user_choice == 'Rock':
            self.winner = 'computer'
            self.computer_score += 1
            #self.game_rounds += 1
            print("Computer win!")

        elif self.computer_choice == 'Paper' and self.user_choice == 'Scissors':
            self.winner = 'you'
            self.user_score += 1
            self.game_rounds += 1
            print("You win!")

        elif self.computer_choice == self.user_choice:
            self.winner = 'Tie' 
            #self.game_rounds += 1
            print("it's a tie!")

    def stop_video(self):
        self.cap.release()
        # Destroy all the windows
        if self.game_rounds == 3:
            print(f'Game Over!!!')
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)


def play():
    game = RPS()
    while game.game_rounds < 3:
        print(f'print round {game.game_rounds}')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        game.start_video()
        game.get_user_choice()
        game.get_computer_choice()
        game.get_winner()
        game.game_rounds += 1
        print(f'print round {game.game_rounds}: START!')
    if self.user_score == self.computer_score:
        print("it's a draw")
    elif self.user_score > self.computer_score:
        print('You won the game!')
    else: 
        print('Sorry, You lost!')
        print('Game Over!!!')
    game.stop_video()
    
        
if __name__ == '__main__':
    play()
