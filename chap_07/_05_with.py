# with

import pickle

with open("profile.pickle", "rb") as profile_file: # file을 열어서 profile_file이라는 변수에 저장
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())