import os
import pickle

class StudentScoreManager:
    def __init__(self, filename='score.bin'):
        self.filename = filename
        self.scores = []
        self.load_scores()

    def add_score(self, name, score):
        self.scores.append((name, score))

    def display_scores(self):
        if not self.scores:
            print("저장된 점수가 없습니다.")
        else:
            for name, score in self.scores:
                print(f'이름: {name}, 점수: {score}')

    def save_scores(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.scores, file)

    def load_scores(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                self.scores = pickle.load(file)
                self.display_scores()

def main():
    manager = StudentScoreManager()

    if not manager.scores:  # 파일에서 읽어온 점수가 없을 때만 입력을 받음
        while True:
            name = input("학생의 이름을 입력하세요 (종료: 'exit'): ")
            if name.lower() == 'exit':
                break
            score = input("학생의 점수를 입력하세요: ")
            try:
                score = int(score)
 
