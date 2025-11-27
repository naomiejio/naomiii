def enter_word():
    word = input("Enter a word: ")
    return word


def points(word):
     point1 = "E", "A", "I", "O", "N", "R", "T", "L", "S", "U"
     point2 = "D", "G"
     point3 = "B", "C", "M", "P"
     point4 = "F", "H", "V", "W", "Y"
     point5 = "K"
     point8 = "J", "X"
     point10 = "Q", "Z"
     return point1, point2, point3, point4, point5, point8, point10


def calc_points(point1, point2, point3, point4, point5, point8, point10, word):
    pointss = 0
    word = word.upper()
    for each in word:
         print(each, pointss)
         if each in point1:
             pointss = pointss + 1
         elif each in point2:
             pointss = pointss + 2
         elif each in point3:
             pointss = pointss + 3
         elif each in point4:
             pointss = pointss + 4
         elif each in point5:
             pointss = pointss + 5
         elif each in point8:
             pointss = pointss + 8
         else:
             pointss = pointss + 10
    
    return pointss


def main():
    word = enter_word()
    print(word)
    point1, point2, point3, point4, point5, point8, point10 = points(word)
    pointss = calc_points(point1, point2, point3, point4, point5, point8, point10, word)
    print(pointss, "points")


main()
