from manim import *
MAX_SIZE=10
def square_text_box(number, square_color, text_color):
            square = Square(side_length=0.7)
            square.set_stroke(color=square_color)
            text = MarkupText(number, color=text_color)
            text.scale(0.6)
            squ_text = VGroup()
            squ_text.add(square, text)
            return squ_text


def square_swap(color_name):
            square_fill2 = Square(side_length=0.7)
            square_fill2.set_stroke(color=color_name, width=0)
            square_fill2.set_fill(color=color_name, opacity=0.5)

            return square_fill2
def takeArray():
    print('Enter an array of maximum {} elements : '.format(MAX_SIZE),end="")
    return list(map(int,input().split()))
def takeInt():
    print("Enter an integer : ",end="")
    return int(input())


class bubbleSort(Scene):
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            
            return
        def bubbleSort(arr,l):
            n = len(arr)
        
            for i in range(n):
        
                for j in range(0, n-i-1):

                    bubs_fill_box1 = square_swap(BLUE_D)
                    if(j==0):
                        bubs_fill_box1.shift((n//2-1) * LEFT)
                    else :
                        bubs_fill_box1.next_to(l[j-1], buff=0)
                    
                    bubs_fill_box2 = square_swap(BLUE_D)
                    bubs_fill_box2.next_to(l[j], buff=0)

                    self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
                   
                    
                    if arr[j] > arr[j+1] :
                        arr[j], arr[j+1] = arr[j+1], arr[j]
       
                        
                        self.play(CyclicReplace(l[j+1], l[j]))
                        l[j+1],l[j]=l[j],l[j+1]
                        
                        #self.wait(0.1)
                    self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))
                l[-i-1].set_fill(RED_B,opacity=0.5);
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        
        for x in l:
            self.play(GrowFromCenter(x))
    
        self.wait(1)
        bubbleSort(arr,l)


class selectionSort(Scene):
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")

            return
        def selectionSort(arr,l):
            n = len(arr)
        
            for i in range(n):
                min_idx = i
                
                
                
                for j in range(i+1, n):
                    bubs_fill_box1 = square_swap(BLUE_D)
                    if(min_idx==0):
                        
                        bubs_fill_box1.shift((n//2-1) * LEFT)
                    else :
                        bubs_fill_box1.next_to(l[min_idx-1], buff=0)
                    bubs_fill_box2 = square_swap(BLUE_D)
                    bubs_fill_box2.next_to(l[j-1], buff=0)

                    self.play(FadeIn(bubs_fill_box1), FadeIn(bubs_fill_box2))
                    if arr[min_idx] > arr[j]:
                        min_idx = j
                    self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))
                        
                
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                self.play(CyclicReplace(l[i], l[min_idx]))
                l[i],l[min_idx]=l[min_idx],l[i]


        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        
        for x in l:
            self.play(GrowFromCenter(x))
    
        self.wait(1)
        selectionSort(arr,l)
        
class binarySearch(Scene):
    def construct(self):
        arr=takeArray()
        print("Enter Number to Search - ")
        x=takeInt()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")

            return
        def binarySearch(arr,x,lis):
            low=0;r=len(arr)-1
            while(low<=r):
                m=(low+r)//2
                lis[m].set_fill(BLUE,opacity=0.5)
                self.wait(1.5)
                if(arr[m]==x):
                    lis[m].set_fill(GREEN,opacity=0.6)
                    self.wait(1.5)
                    return
                elif(arr[m]<x):
                    for i in range(low,m+1):
                        lis[i].set_fill(RED,opacity=0.6)
                    low=m+1
                else :
                    for i in range(m,r+1):
                        lis[i].set_fill(RED,opacity=0.6)
                    r=m-1
                self.wait(1.5)

        arr.sort()
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        
        for y in l:
            self.play(GrowFromCenter(y))
    
        self.wait(1)
        binarySearch(arr,x,l)


'''
class insertionSort(Scene):
    
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")

            return
        def insertionSort(arr,l):
            n = len(arr)
            for i in range(1,n):
                key = arr[i]
                j = i-1
                
                if(j>=0 and key < arr[j]):
                    pass
                else:
                    bubs_fill_box1 = square_swap(BLUE_D)
                    if(j==0):
                            
                            bubs_fill_box1.shift((n//2-1) * LEFT)
                    else :
                            bubs_fill_box1.next_to(l[j-1], buff=0)
                    self.play(FadeIn(bubs_fill_box1))
                    self.wait(0.3)
                    self.play(FadeOut(bubs_fill_box1))
                while j >= 0 and key < arr[j] :
                        arr[j + 1] = arr[j]
                        bubs_fill_box1 = square_swap(BLUE_D)
                        if(j==0):
                                
                                bubs_fill_box1.shift((n//2-1) * LEFT)
                        else :
                                bubs_fill_box1.next_to(l[j-1], buff=0)
                        bubs_fill_box2 = square_swap(BLUE_D)
                        bubs_fill_box2.next_to(l[j], buff=0)
                        self.play(FadeIn(bubs_fill_box2))
                        self.play(FadeIn(bubs_fill_box1))
                        
                        self.wait(0.1)
                        self.play(CyclicReplace(l[j], l[j+1]))
                        #self.play(CyclicReplace(bubs_fill_box1, bubs_fill_box2))
                        l[j+1],l[j]=l[j],l[j+1]
                        self.play(FadeOut(bubs_fill_box1))
                        self.play(FadeOut(bubs_fill_box2))
                    

                        j -= 1
                arr[j + 1] = key
                #self.play(FadeOut(bubs_fill_box1))
                #l[j+1]=x
            self.wait(1)
            #7 3 5 9 4 2
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        
        for x in l:
            self.play(GrowFromCenter(x))
    
        self.wait(1)
        insertionSort(arr,l)
'''


class insertionSort(Scene):
    # color krna h blocks ko
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")

            return
        def insertionSort(arr,l):
            n = len(arr)
            for i in range(1,n):
                key = arr[i]
                j = i-1
                x=l[j]
                while j >= 0 and key < arr[j] :
                        arr[j + 1] = arr[j]
                        
                        self.play(CyclicReplace(l[j], l[j+1]))
                        l[j+1],l[j]=l[j],l[j+1]
                        j -= 1
                arr[j + 1] = key
                #l[j+1]=x

        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        
        for x in l:
            self.play(GrowFromCenter(x))
    
        self.wait(1)
        insertionSort(arr,l)
