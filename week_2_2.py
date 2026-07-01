# import math
# list = [10, 20, 30, 40, 55]
# print(list[1])
# print(len(list))
# print(math.sqrt(9))
# a = math.floor(6.6)
# print(a)
# name = input("名前\n")
# print("こんにちは")
# print(name)
# age = 16

# if age < 18:
#     print("未成年飲酒です")
#     print("飲酒・喫煙禁止")

# print("処理終了")

# age = 19
# if age < 18:
#     print("あなたは投票権がありません")
# else:
#     print("投票に行けます")

# age = 6
# if age < 6:
#     print("入場は無料です")
# elif age < 13:
#     print("子供料金で入場します")
# elif age < 65:
#     print("大人料金で入場します")
# else:
#     print("シニア料金で入場できます")

# print(10 > 3)
# print(10 < 3)
# print(5 == 5)
# print(5 != 5)

# age = 90
# if age > 60 or age < 20:
#     print("入場料無料です")
# else:
#     print("大人料金です")

# age = int(input("年齢を入力してください"))
# if age <= 12 or age >= 65:
#     print("無料")
# elif age >= 13 and age <=17:
#     print("子供料金")
# else:
    # print("大人料金")


# 演習１
# a = 10 // 4
# print(a)

# a = 10 / 4
# print(a)

# a = 10 % 4
# print(a)

# a = 10 ** 4
# print(a)

# 演習２

# rank = int(input("ランクを入力してください"))
# if rank < 0:
#     print("ランクがありません")
# elif rank > 100:
#     print("上級ランクです")
# elif rank < 10:
#     print("初級ランクです")
# else:
#     print("中級ランクです")

#演習３

# a = int(input())
# if a % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")
# if a % 2 == 0 or a % 3 == 0:
#     print("multiple")
# a = 0
# for i in range(1, 11):
#     a = a + i
#     print("a =", a)


# a = 0
# for i in range(1,11):
#     if i % 2 == 1:
#         a = a + i
#         print("a =", a) 

# for i in range (1,11):
#     if i % 5 == 0:
#         print("a =",i)

# 演習４
# scores = [1,2,3,5,10]
# a = scores.pop()
# print(a)
# print(scores)
# b = scores.append(22)
# print(b)
# print(scores)

#演習5

# names = ["田中", "佐藤", "鈴木", "高橋", "伊藤"]

# for name in names:
#     print(name)

# a = names.remove("伊藤")
# print("消す文字",a)

# b = names.append("山田")
# print("増える文字",b)

# char = ("田")
# for name in names:
#     if char in name:  
#         print(name)

# users = {"年齢1":10, "年齢2":20, "年齢3":30}
# print(users)
# a = users(0) + users(1) + users(2)
# print(a)

# def countdown():
#     print("カウントダウンをします")
#     counter = 5
#     while counter >= 0:
#         print(counter)
#         counter =- 1

# countdown()

# def introduce(name):
#     print("こんにちは")
#     print(f"開発チームの{name}です")
#     print("よろしくお願いします")

# introduce("寺井")


# def judge_winner(team_a,team_b):
#     if team_a > team_b:
#         print("チームAの勝利")
#     elif team_a < team_b:
#         print("チームBの勝利")
#     else:
#         print("引き分け")
    
# judge_winner(5,3)

#演習4

# def repeat_message(message,count):
#      while count >= 1:
#         print(message)
#         count -= 1

# repeat_message("こんにちは", 2)

#演習5

# def average_score(args):
#     return sum(args) / len(args)

# print(average_score([2,100]))

# 演習6

# def user_name(user):
#     if user == "寺井健翔" or user == "admin":
#         print("True")
#     else:
#         print("False")

# user_name("")
# def get_rank(level):
#     if level >= 50:
#         print("プラチナ")
#     elif 50 >= level >= 30:
#         print("ゴールド")
#     elif 30 >= level >=10:
#         print("シルバー")
#     else:
#         print("ブロンズ")

# get_rank(10)

