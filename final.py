import cv2
from keras.models import load_model
import numpy as np
import random
import time
class RPS:
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.game_rounds = 1
        self.options = ['rock', 'paper', 'scissors', 'nothing']
        self.user_score = 0
        self.computer_score = 0
        self.started = False
        self.countdown_flag = False
        self.video_error = False
        self.start_time = time.time()
        self.end_time = time.time() + 5

    def play_video(self):
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        ret, self.frame = self.cap.read()
        resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        cv2.imshow('frame', self.frame)
        
    def start_game(self):
        if cv2.waitKey(33) & 0xFF == ord('s'):
            self.started = True
            self.countdown_flag = True

    def game_control(self):
        if self.started == False:
            if self.game_rounds == 1:
                self.start_game()
            elif self.game_rounds == 3:
                self.end_game()
            elif self.video_error == True:
                print('no image captured by camera, please show an image')
                self.start_game()
            elif self.game_rounds > 1:
                print(f"Press 's' to start round")
                self.start_game()

    def get_user_choice(self):
        if self.started == True:
            self.time_interval = self.end_time - self.start_time
            if self.countdown_flag:
                print(f'Show your hand after the count of 3...')
                print()
                print(1)
                print()
                print(2)
                print()
                print(3)
            if self.time_interval > 0:
                self.countdown_flag = False
                self.computer_choice = random.choice(self.options[:3])
                index = self.get_prediction()
                if index == 3:
                    self.camera_error = True
                else:
                    self.user_choice = self.options[index]
                    print(f'User chose {self.user_choice}.')
                    print(f'Computer chose {self.computer_choice}.')
                    self.get_winner()

    def get_prediction(self):
        prediction = self.model.predict(self.data)
        index = np.argmax(prediction[0])
        return index
    def get_winner(self):
        if self.user_choice == self.computer_choice:
            print('it is a Tie!!')
            self.game_rounds += 1
        elif (self.user_choice == 'scissors' and self.computer_choice == 'paper') \
            or (self.user_choice == 'paper' and self.computer_choice == 'rock') \
            or (self.user_choice == 'rock' and self.computer_choice == 'scissors'):
            self.user_score += 1
            self.game_rounds += 1
            print('You won this round!')
        else:
            self.computer_score += 1
            self.game_rounds += 1
            print('Computer won this round!')

    def end_game(self):
        self.get_winner()
        if self.user_score == self.computer_score:
            print('The game is a draw.')
        elif self.user_score > self.computer_score:
            print('You won the game! Well done!')
        else:
            print('You lost. Try Again!')
            exit()

    def close_window(self):
        self.cap.release()
        cv2.waitKey(1000)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
def play_game():
    game = RPS()
    while game.game_rounds < 3:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        game.play_video()
        game.game_control()
        game.get_user_choice()
    game.close_window()
if __name__ == '__main__':
    play_game() 