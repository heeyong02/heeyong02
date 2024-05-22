class Rectangle:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.__x1 = x1
        self.__y1 = y1 
        self.__x2 = x2
        self.__y2 = y2 

    def show(self):
        print(f'left-top: ({self.__x1},{self.__y1})')
        print(f'right-top: ({self.__x2}, {self.__y2})')
    def getWidth(self):
        self.width = self.__x2-self.__x1
        return self.width
    def getHeight(self):
        self.height = self.__y2-self.__y1
        return self.height
    def getArea(self):
        self.area = (self.__x2-self.__x1)*(self.__y2-self.__y1)
        return self.area
    def getPerimeter(self):
        self.Perimeter = (self.__x2-self.__x1)*2+(self.__y2-self.__y1)*2
        return self.Perimeter
#사용자 정의 함수부

#주 프로그램부
r1 = Rectangle(5,5,20,10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
