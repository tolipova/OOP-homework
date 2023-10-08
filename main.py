#N1
class Oson1:
    a = 5
    def output_a(cls):
        print(cls.a)
Oson1.output_a(Oson1)        

#N2
class Oson2:
    a = 4
    b = 5

    def summa(cls):
        print(cls.a+cls.b)
Oson2.summa(Oson2)        

#N3
class Oson3:
    a = int(input("Son kiriting: "))

    def plus_minus(cls):
        if cls.a >= 0 :
            print("Musbat son")
        else:
            print("Manfiy son")    
Oson3.plus_minus(Oson3)

#N4            
class Oson5:
    a = int(input("Son kiriting: "))
    b = int(input(f"{a} ning darajasi uchun son kiriting: "))
    
    def daraja(cls):
        print(cls.a**cls.b)
Oson5.daraja(Oson5)        

class MyClass6:
    words = []

    def add_word(cls):
        word = input("enter the word: ")
        cls.words.append(word)
        if word == 'word':
            cls.words.remove('word')

MyClass6.add_word(MyClass6)    #??     

#N5
class MyClass7:
    numbers = [1,2,3,4,5]      
    new_list = [5,6,7] 

    
    def compare_lists(cls):
        total = 0
        for num in cls.numbers:
            total += num
            # print(f"{cls.numbers} shu listdagi sonlar yig'indisi: {total}")
        a = 0    
        for son in cls.new_list:
            a += son
            # print(f"{cls.new_list} shu listdagi sonlar yig'indisi: {a}")
        if total > a:
            print(f"{cls.numbers} > {cls.new_list}")
        else:
            print(f"{cls.new_list} > {cls.numbers}")    



MyClass7.compare_lists(MyClass7)                

                

            