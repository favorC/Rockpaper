class RPS:

    def __init__(self):
        #self.computer_choice = random.choice(self.choice_list)
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.user_score = 0
        self.computer_score = 0
        

    def start_video(self):
        while True: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            self.prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            self.start_game()
             # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.stop_video()


    def start_game(self):
    
        while self.user_score <3 and self.computer_score <3:
            self.timer()
            #print(self.prediction)
            user_choice = self.get_prediction()
            print(user_choice)
            computer_choice = self.get_computer_choice()
            print(computer_choice)
            self.get_winner(computer_choice,user_choice)
            if self.user_score == 3: 
                print('You have won! What a hero')
                exit()
            elif self.computer_score == 3:
                print('You lost the game! Doofus')
                exit()

    def stop_video(self):
        
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        
    def timer(self):
        countdown_timer = 3
        while countdown_timer>0:
            print(f"Start in {countdown_timer} seconds")
            sleep(1)
            countdown_timer -= 1
        print('START!')
        ret, frame = self.cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        self.prediction = self.model.predict(self.data)
        self.get_prediction()
    

    def get_prediction(self):
        if self.prediction[0][0] > 0.5:
            user_choice = 'rock'
        elif self.prediction[0][1] > 0.5:
            user_choice = 'paper'
        elif self.prediction[0][2] > 0.5:
            user_choice = 'scissors'
        elif self.prediction[0][3] > 0.5:
            user_choice = 'nothing'
        else:
            user_choice = 'No input detected'
        return user_choice

    def get_computer_choice(self):
        possible_actions = ['Rock','Paper','Scissors']
        self.computer_choice = random.choice(possible_actions)
        #print(computer_choice)
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

    
        

    def play():
        
        game = RPS()
        game.start_camera()
       

if __name__ ==  '__main__':
    choice_list = ['Rock','Paper','Scissors','Nothing']
    
    Rock_Paper_Scissors.play()

