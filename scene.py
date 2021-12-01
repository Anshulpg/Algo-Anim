from manim import *
MAX_SIZE=10
size_sq=0.7
def square_text_box(number, square_color, text_color):
            square = Square(side_length=size_sq)
            square.set_stroke(color=square_color)
            text = MarkupText(number, color=text_color)
            text.scale(0.6)
            squ_text = VGroup()
            squ_text.add(square, text)
            return squ_text


def square_swap(color_name):
            square_fill2 = Square(side_length=size_sq)
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
        if(n==0):
            print("No input given")

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
                    text_a=Text("Maximum till now is "+str(arr[j+1]), font="Arial", color=YELLOW)
                    text_a.shift(DOWN*2)
                    self.play(FadeIn(text_a))
                    self.wait(0.5)
                    self.play(FadeOut(text_a))
                        #self.wait(0.1)
                    self.play(FadeOut(bubs_fill_box1), FadeOut(bubs_fill_box2))
                l[-i-1].set_fill(RED_B,opacity=0.5)
                text_a=Text(str(arr[-i-1])+" is now at its right position.", font="Arial", color=GREEN,size=1.5)
                text_a.shift(DOWN*2)
                self.play(FadeIn(text_a))
                self.wait(0.5)
                self.play(FadeOut(text_a))
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        text_h=Text("Bubble Sort", font="Arial", color=RED, size=2.5)
        text_h.scale(0.5)
        text_h.shift(UP*3)
        self.play(Write(text_h))
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
                    text_a=Text("Minimum till now is "+str(arr[min_idx]), font="Arial", color=YELLOW)
                    text_a.shift(DOWN*2)
                    self.play(FadeIn(text_a))
                    self.wait(0.5)
                    self.play(FadeOut(text_a))
                
                
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                self.play(CyclicReplace(l[i], l[min_idx]))
                
                l[min_idx].set_fill(RED_B,opacity=0.5)
                l[i],l[min_idx]=l[min_idx],l[i]
                text_a=Text(str(arr[i])+" is at its right place.", font="Arial", color=GREEN,size=1.5)
                text_a.shift(DOWN*2)
                self.play(FadeIn(text_a))
                self.wait(0.5)
                self.play(FadeOut(text_a))
                


        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        text_h=Text("Selection Sort", font="Arial", color=RED, size=2.5)
        text_h.scale(0.5)
        text_h.shift(UP*3)
        self.play(Write(text_h))
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
            
            text_a=Text(str(x))
            text_a.scale(0.5)
            text_a.shift(UP*size_sq*3)
            self.add(text_a)
            self.wait(1)
            low=0;r=len(arr)-1
            while(low<=r):
                m=(low+r)//2
                lis[m].set_fill(BLUE,opacity=0.5)
                self.wait(1.5)
                if(arr[m]==x):
                    lis[m].set_fill(GREEN,opacity=0.6)
                    text_a=Text(" SUCCESS.", font="Arial", color=GREEN,size=2)
                    text_a.shift(DOWN*2)
                    self.play(FadeIn(text_a))
                    self.wait(0.5)
                    self.play(FadeOut(text_a))
                    self.wait(1.5)
                    return
                elif(arr[m]<x):
                    text_a=Text(str(arr[m])+" is less than "+str(x)+", hence elements Left to it are of no use.", font="Arial", color=BLUE,size=0.5)
                    text_a.shift(DOWN*2)
                    self.play(FadeIn(text_a))
                    self.wait(0.8)
                    self.play(FadeOut(text_a))
                    for i in range(low,m+1):
                        lis[i].set_fill(RED,opacity=0.6)
                    low=m+1
                else :
                    text_a=Text(str(arr[m])+" is greater than "+str(x)+", hence elements Right to it are of no use.", font="Arial", color=YELLOW,size=0.5)
                    text_a.shift(DOWN*2)
                    self.play(FadeIn(text_a))
                    self.wait(0.8)
                    self.play(FadeOut(text_a))
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
        text_h=Text("Binary Search", font="Arial", color=RED, size=2.5)
        text_h.scale(0.5)
        text_h.shift(UP*3)
        self.play(Write(text_h))
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
                        text_h=Text("We swap "+str(arr[j])+" and "+str(key), font="Courier", color=YELLOW)
                        text_h.scale(1.2)
                        text_h.shift(2*DOWN)
                        self.play(Write(text_h))
                        self.wait(0.5)
                        self.remove(text_h)
                        arr[j + 1] = arr[j]
                        bub1=square_swap(BLUE_D)
                        bub1.shift(l[j].get_center())
                        bub2=square_swap(BLUE_D)
                        bub2.shift(l[j+1].get_center())
                        self.play(FadeIn(bub1),FadeIn(bub2))
                        self.play(CyclicReplace(l[j], l[j+1]))
                        l[j+1],l[j]=l[j],l[j+1]
                        self.play(FadeOut(bub1),FadeOut(bub2))
                        j -= 1
                arr[j + 1] = key
                #l[j+1]=x
                text_h=Text(str(key)+" is inserted", font="Courier", color=GREEN)
                text_h.scale(1.4)
                text_h.shift(2*DOWN)
                self.play(Write(text_h))
                self.wait(0.5)
                self.remove(text_h)
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        text_h=Text("Insertion Sort", font="Arial", color=RED, size=2.5)
        text_h.scale(0.5)
        text_h.shift(UP*3)
        self.play(Write(text_h))
        for x in l:
            self.play(GrowFromCenter(x))
    
        self.wait(1)
        insertionSort(arr,l)








class maxHeap(Scene):
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")

            return
        def maxHeapify(arr,i,lis):
            n = len(arr)
            bubs_fill_box1 = square_swap(BLUE_D)
            bubs_fill_box2=square_swap(GREEN)
            if(i==0):
                        bubs_fill_box1.next_to(lis[0], buff=0)
                        bubs_fill_box1.shift( LEFT*size_sq)
            else :
                        bubs_fill_box1.next_to(lis[i-1], buff=0)
            largest=i
            l=2*i+1
            r=2*i+2
            b3=False
            b4=False
            self.play(FadeIn(bubs_fill_box1))
            if(l<n):
                b3=True
                bubs_fill_box3=square_swap(BLUE_D)
                bubs_fill_box3.next_to(lis[l-1], buff=0)
                self.play(FadeIn(bubs_fill_box3))
            if(r<n):
                b4=True
                bubs_fill_box4=square_swap(BLUE_D)
                bubs_fill_box4.next_to(lis[r-1], buff=0)
                self.play(FadeIn(bubs_fill_box4))

            if(l<n and arr[l]>arr[largest]):
                
                largest=l
            if(r<n and arr[r]>arr[largest]):
               
                largest=r
            if(largest==0):
                        
                        bubs_fill_box2.next_to(lis[0], buff=0)
                        bubs_fill_box2.shift( LEFT*size_sq)
            else :
                        bubs_fill_box2.next_to(lis[largest-1], buff=0)
            self.play(FadeIn(bubs_fill_box2))
            self.wait(0.2)
            if(largest !=i):
                text_h=Text("Largest is "+str(arr[largest])+" , Hence we swap and then heapify "+str(arr[i]), font="Courier", color=YELLOW)
                text_h.scale(0.8)
            else:
                text_h=Text("Largest is "+str(arr[largest])+" , Hence we do not swap", font="Courier", color=BLUE)
            text_h.scale(0.8)
            text_h.shift(2*DOWN)
            self.play(Write(text_h))
            self.wait(0.5)
            self.remove(text_h)
            if(largest!=i):

                arr[i],arr[largest]=arr[largest],arr[i]
                self.play(CyclicReplace(lis[i],lis[largest]))
                lis[i],lis[largest]=lis[largest],lis[i]
                
                self.play(FadeOut(bubs_fill_box1),FadeOut(bubs_fill_box2))
                if(b3):
                    self.play(FadeOut(bubs_fill_box3))
                if(b4):
                    self.play(FadeOut(bubs_fill_box4))
                maxHeapify(arr,largest,lis)
            else:
                self.play(FadeOut(bubs_fill_box1),FadeOut(bubs_fill_box2))
                if(b3):
                    self.play(FadeOut(bubs_fill_box3))
                if(b4):
                    self.play(FadeOut(bubs_fill_box4))


        def maxHeap(arr,l):
            n = len(arr)
            for i in range(n//2-1,-1,-1):
                maxHeapify(arr,i,l)
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        text_h=Text("Max Heap", font="Arial", color=RED, size=2.5)
        text_h.scale(0.5)
        text_h.shift(UP*3)
        self.play(Write(text_h))
        for x in l:
            self.play(GrowFromCenter(x))
        self.wait(1)
      
        maxHeap(arr,l)
        text_h=Text("Max Heap is done now !", font="Arial", color=RED, size=1.7)
        text_h.shift(DOWN*2)
        self.play(Write(text_h))
        self.wait(1.5)
        


class minHeap(Scene):
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")

            return
        def minHeapify(arr,i,lis):
            n = len(arr)
            bubs_fill_box1 = square_swap(BLUE_D)
            bubs_fill_box2=square_swap(GREEN)
            if(i==0):
                        bubs_fill_box1.next_to(lis[0], buff=0)
                        bubs_fill_box1.shift( LEFT*size_sq)
            else :
                        bubs_fill_box1.next_to(lis[i-1], buff=0)
            smallest=i
            l=2*i+1
            r=2*i+2
            b3=False
            b4=False

            

            self.play(FadeIn(bubs_fill_box1))
            if(l<n):
                b3=True
                bubs_fill_box3=square_swap(BLUE_D)
                bubs_fill_box3.next_to(lis[l-1], buff=0)
                self.play(FadeIn(bubs_fill_box3))
            if(r<n):
                b4=True
                bubs_fill_box4=square_swap(BLUE_D)
                bubs_fill_box4.next_to(lis[r-1], buff=0)
                self.play(FadeIn(bubs_fill_box4))
            if(l<n and arr[l]<arr[smallest]):
                smallest=l
            if(r<n and arr[r]<arr[smallest]):
                smallest=r
            if(smallest==0):
                        
                        bubs_fill_box2.next_to(lis[0], buff=0)
                        bubs_fill_box2.shift( LEFT*size_sq)
            else :
                        bubs_fill_box2.next_to(lis[smallest-1], buff=0)
            self.play(FadeIn(bubs_fill_box2))
            self.wait(0.2)
            if(smallest !=i):
                text_h=Text("Smallest is "+str(arr[smallest])+" , Hence we swap and then heapify "+str(arr[i]), font="Courier", color=YELLOW)
                text_h.scale(0.8)
            else:
                text_h=Text("Smallest is "+str(arr[smallest])+" , Hence we do not swap", font="Courier", color=BLUE)
            text_h.scale(0.8)
            text_h.shift(2*DOWN)
            self.play(Write(text_h))
            self.wait(0.5)
            self.remove(text_h)

            if(smallest!=i):

                arr[i],arr[smallest]=arr[smallest],arr[i]
                self.play(CyclicReplace(lis[i],lis[smallest]))
                lis[i],lis[smallest]=lis[smallest],lis[i]
                
                self.play(FadeOut(bubs_fill_box1),FadeOut(bubs_fill_box2))
                if(b3):
                    self.play(FadeOut(bubs_fill_box3))
                if(b4):
                    self.play(FadeOut(bubs_fill_box4))
                minHeapify(arr,smallest,lis)
            else:
                self.play(FadeOut(bubs_fill_box1),FadeOut(bubs_fill_box2))
                if(b3):
                    self.play(FadeOut(bubs_fill_box3))
                if(b4):
                    self.play(FadeOut(bubs_fill_box4))


        def minHeap(arr,l):
            n = len(arr)
            for i in range(n//2-1,-1,-1):
                minHeapify(arr,i,l)
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        text_h=Text("Min Heap", font="Arial", color=RED, size=2.5)
        text_h.scale(0.5)
        text_h.shift(UP*3)
        self.play(Write(text_h))
        for x in l:
            self.play(GrowFromCenter(x))
        self.wait(1)
      
        minHeap(arr,l)
        text_h=Text("Min Heap is done now !", font="Arial", color=RED, size=1.7)
        text_h.shift(DOWN*2)
        self.play(Write(text_h))
        self.wait(1.5)




# heapsort
class heapSort(Scene):
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")

            return
        def heapify(arr,n,i,lis):
           
            bubs_fill_box1 = square_swap(BLUE_D)
            bubs_fill_box2=square_swap(GREEN)
            if(i==0):
                        bubs_fill_box1.next_to(lis[0], buff=0)
                        bubs_fill_box1.shift( LEFT*size_sq)
            else :
                        bubs_fill_box1.next_to(lis[i-1], buff=0)
            largest=i
            l=2*i+1
            r=2*i+2
            b3=False
            b4=False
            self.play(FadeIn(bubs_fill_box1))
            if(l<n):
                b3=True
                bubs_fill_box3=square_swap(BLUE_D)
                bubs_fill_box3.next_to(lis[l-1], buff=0)
                self.play(FadeIn(bubs_fill_box3))
            if(r<n):
                b4=True
                bubs_fill_box4=square_swap(BLUE_D)
                bubs_fill_box4.next_to(lis[r-1], buff=0)
                self.play(FadeIn(bubs_fill_box4))

            if(l<n and arr[l]>arr[largest]):
                
                largest=l
            if(r<n and arr[r]>arr[largest]):
               
                largest=r
            if(largest==0):
                        
                        bubs_fill_box2.next_to(lis[0], buff=0)
                        bubs_fill_box2.shift( LEFT*size_sq)
            else :
                        bubs_fill_box2.next_to(lis[largest-1], buff=0)
            self.play(FadeIn(bubs_fill_box2))
            self.wait(0.2)
            if(largest !=i):
                text_h=Text("Largest is "+str(arr[largest])+" , Hence we swap and then heapify "+str(arr[i]), font="Courier", color=YELLOW)
                text_h.scale(0.8)
            else:
                text_h=Text("Largest is "+str(arr[largest])+" , Hence we do not swap", font="Courier", color=BLUE)
            text_h.scale(0.8)
            text_h.shift(2*DOWN)
            self.play(Write(text_h))
            self.wait(0.5)
            self.remove(text_h)
            if(largest!=i):

                arr[i],arr[largest]=arr[largest],arr[i]
                self.play(CyclicReplace(lis[i],lis[largest]))
                lis[i],lis[largest]=lis[largest],lis[i]
                
                self.play(FadeOut(bubs_fill_box1),FadeOut(bubs_fill_box2))
                if(b3):
                    self.play(FadeOut(bubs_fill_box3))
                if(b4):
                    self.play(FadeOut(bubs_fill_box4))
                heapify(arr,n,largest,lis)
            else:
                self.play(FadeOut(bubs_fill_box1),FadeOut(bubs_fill_box2))
                if(b3):
                    self.play(FadeOut(bubs_fill_box3))
                if(b4):
                    self.play(FadeOut(bubs_fill_box4))

        def heapSort(arr,l):
            n=len(arr)
            for i in range(n//2-1 , -1, -1):
                
                heapify(arr, n, i,l)
            text_h=Text("Base heapify is done now , sorting will start", font="Courier", color=PINK)
            text_h.scale(0.65)
            text_h.shift(2*DOWN)
            self.play(Write(text_h))
            self.wait(0.5)
            self.remove(text_h)
            self.wait(1.5)
           
            for i in range(n-1,0,-1):
                
                arr[0],arr[i]=arr[i],arr[0]
                self.play(CyclicReplace(l[0],l[i])) 
                l[i],l[0]=l[0],l[i]
                l[i].set_fill(color=RED_C, opacity=0.5)
                text_h=Text(str(arr[i]) +" is at right place , now we heapify "+str(arr[0]), font="Courier", color=RED)
                text_h.scale(0.65)
                text_h.shift(2*DOWN)
                self.play(Write(text_h))
                self.wait(0.7)
                self.remove(text_h)
                self.wait(1)
                heapify(arr,i,0,l)

        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        text_h=Text("Heap Sort", font="Arial", color=RED, size=2.5)
        text_h.scale(0.5)
        text_h.shift(UP*3)
        self.play(Write(text_h))

        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        
        for x in l:
            self.play(GrowFromCenter(x))
        self.wait(1)
      
        heapSort(arr,l)
        text_h=Text("Heap Sort is done now !", font="Courier", color=RED)
        text_h.scale(1.4)
        text_h.shift(2*DOWN)
        self.play(Write(text_h))
        self.wait(0.5)
        self.remove(text_h)


class twoPointer(Scene):

    # problem is given 2 arrays and an integer x and you have to find a pair of elements 
    # in the arrays whose sum is equal to x (if exist)
    def construct(self):
        arr=takeArray()
        arr.sort()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")
            return
        print("Enter the value of sum to find in array , ",end=" " )
        x=takeInt()
        def twoPointer(arr,n,l):
            text_a=Text("Sum to find = "+str(x))
            text_a.scale(0.5)
            text_a.shift(UP*size_sq*3)
            self.add(text_a)
            i=0
            j=n-1
            bubs_fill_box1 = square_swap(BLUE_D)
            bubs_fill_box2=square_swap(BLUE_D)
            while(i<n and j>=0 ):
                

                if(i==0):
                        bubs_fill_box1.next_to(l[0], buff=0)
                        bubs_fill_box1.shift( LEFT*size_sq)
                else :
                        bubs_fill_box1.next_to(l[i-1], buff=0)
                if(j==0):
                        bubs_fill_box2.next_to(l[0], buff=0)
                        bubs_fill_box2.shift( LEFT*size_sq)
                else :
                        bubs_fill_box2.next_to(l[j-1], buff=0)
                self.play(FadeIn(bubs_fill_box1),FadeIn(bubs_fill_box2))

                if(arr[i]+arr[j]==x):
                    self.play(FadeOut(bubs_fill_box1),FadeOut(bubs_fill_box2))
                    l[i].set_fill(color=GREEN, opacity=0.5)
                    l[j].set_fill(color=GREEN, opacity=0.5)
                    text_t=Text("Current Sum = "+str(x)+" ,Hence Found", font="Arial", color=GREEN, size=2.5)
                    text_t.scale(0.5)
                    text_t.shift(DOWN*size_sq*3)
                    self.play(Write(text_t))
                    self.wait(2.5)
                    break
                elif(arr[i]+arr[j]<x):
                    
                    text_t=Text("Current Sum = "+str(arr[i]+arr[j])+" is less than "+ str(x) +" ,Hence we increase i", font="Arial", color=YELLOW, size=1.5)
                    text_t.scale(0.5)
                    text_t.shift(DOWN*size_sq*3)
                    self.play(Write(text_t))
                    self.wait(1)
                    self.play(FadeOut(bubs_fill_box1))
                    l[i].set_fill(color=RED, opacity=0.5)
                    self.remove(text_t)
                    self.wait(0.5)
                    i=i+1
                    if(i==j):
                        self.play(FadeOut(bubs_fill_box2))
                        l[i].set_fill(color=RED_C, opacity=0.5)
                        self.wait(2)
                        break
                    
                else:
                    
                    text_t=Text("Current Sum = "+str(arr[i]+arr[j])+" is more than "+ str(x) +" ,Hence we decrease j", font="Arial", color=BLUE, size=1.5)
                    text_t.scale(0.5)
                    text_t.shift(DOWN*size_sq*3)
                    self.play(Write(text_t))
                    self.wait(1)
                    self.play(FadeOut(bubs_fill_box2))
                    l[j].set_fill(color=RED, opacity=0.5)
                    self.remove(text_t)
                    self.wait(0.5)
                    j=j-1
                    if(i==j):
                        self.play(FadeOut(bubs_fill_box1))
                        l[i].set_fill(color=RED_C, opacity=0.5)
                        self.wait(2)
                        break
            
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        text_h=Text("Two Pointer (Two sum)", font="Arial", color=RED, size=2.5)
        text_h.scale(0.5)
        text_h.shift(UP*3)
        self.play(Write(text_h))
        for xa in l:
            self.play(GrowFromCenter(xa))
        self.wait(1)
        twoPointer(arr,n,l)

class linearSearch(Scene):
    
        # problem is given an array and an integer x and you have to find the index of x in the array (if exist)
        def construct(self):
            arr=takeArray()
            
            n=len(arr)
            if(n>MAX_SIZE):
                print("Too Long input!")
                return
            if(n==0):
                print("No input given")
                return
            
            x=takeInt()
            bubs_fill_box1 = square_swap(BLUE_D)
            def linearSearch(arr,n,l):
                text_a=Text(str(x))
                text_a.scale(0.5)
                text_a.shift(UP*size_sq*3)
                self.add(text_a)
                for i in range(n):
                    if(i==0):
                        bubs_fill_box1.next_to(l[0], buff=0)
                        bubs_fill_box1.shift( LEFT*size_sq)
                    else :
                        bubs_fill_box1.next_to(l[i-1], buff=0)
                    self.play(FadeIn(bubs_fill_box1))
                    self.wait(0.5)
                    if(arr[i]==x):
                        text_h=Text("Current element is "+str(arr[i])+" Hence Found ! ", font="Arial", color=GREEN, size=1.2)
                        text_h.scale(0.5)
                        text_h.shift(DOWN*size_sq*3)
                        self.play(Write(text_h))
                        self.wait(1)
                        self.play(FadeOut(text_h))
                        self.play(FadeOut(bubs_fill_box1))
                        l[i].set_fill(color=GREEN, opacity=0.6)
                        self.wait(2.5)
                        break
                    else:
                        text_h=Text("Current element is "+str(arr[i])+" and not equal to "+str(x), font="Arial", color=RED, size=1)
                        text_h.scale(0.5)
                        text_h.shift(DOWN*size_sq*3)
                        self.play(Write(text_h))
                        self.wait(1)
                        self.play(FadeOut(text_h))
                        self.play(FadeOut(bubs_fill_box1))
                        
                        l[i].set_fill(color=RED, opacity=0.5)
                        self.wait(1)
                    
            bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
            bubs.shift((n//2-1) * LEFT)
            l=[]
            l.append(bubs)
            for i in range(1,n):
                bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
                bubs.next_to(l[-1], buff=0)
                l.append(bubs)
            text_h=Text("Linear Search", font="Arial", color=RED, size=2.5)
            text_h.scale(0.5)
            text_h.shift(UP*3)
            self.play(Write(text_h))
            for xa in l:
                self.play(GrowFromCenter(xa))
            self.wait(1)
            linearSearch(arr,n,l)
      


# class mregeSort(Scene):
#     # problem is given an array and you have to sort it using merge sort
#     def construct(self):
#         arr=takeArray()
#         n=len(arr)
#         if(n>MAX_SIZE):
#             print("Too Long input!")
#             return
#         if(n==0):
#             print("No input given")
#             return 
#         def merge(left,right,l):
#             arr=[0]*(len(left)+len(right))
#             i=0
#             j=0
#             k=0
#             while(i<len(left) and j<len(right)):
#                 if(left[i]<right[j]):
#                     arr[k]=left[i]
#                     i=i+1
#                 else:
#                     arr[k]=right[j]
#                     j=j+1
#                 k=k+1
#             while(i<len(left)):
#                 arr[k]=left[i]
#                 i=i+1
#                 k=k+1
#             while(j<len(right)):
#                 arr[k]=right[j]
#                 j=j+1
#                 k=k+1
#             return arr
#         def mergeSort(arr,n,l):
#             if(n==1):
#                 return arr
#             mid=n//2
#             x=[]
#             for i in range(mid) :
#                 bb=square_swap(BLUE_D)
#                 if(i==0):
#                         bb.next_to(l[0], buff=0)
#                         bb.shift( LEFT*size_sq)
#                 else :
#                         bb.next_to(l[i-1], buff=0)
#                 self.play(FadeIn(bb))
#                 x.append(bb)
#             for i in x:
#                 self.play(FadeOut(i))

#             x=[]
#             for i in range(mid,n) :
#                 bb=square_swap(BLUE_D)
#                 if(i==0):
#                         bb.shift((n//2-1) * LEFT)
#                 else :
#                         bb.next_to(l[i-1], buff=0)
#                 self.play(FadeIn(bb))
#                 x.append(bb)
#             for i in x:
#                 self.play(FadeOut(i))
                
#             left=mergeSort(arr[:mid],mid,l)
#             right=mergeSort(arr[mid:],n-mid,l)
#             return merge(left,right,l)
        
#         bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
#         bubs.shift((n//2-1) * LEFT)
#         l=[]
#         l.append(bubs)
#         for i in range(1,n):
#             bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
#             bubs.next_to(l[-1], buff=0)
#             l.append(bubs)
#         for xa in l:
#             self.play(GrowFromCenter(xa))
#         self.wait(1)
#         mergeSort(arr,n,l)
            


class knightTour(Scene):
    
    def construct(self):
        print("Enter the size of the chess board ,which is maximum 8 ",end=" , ")
        n=takeInt()
        if(n>8):
            print("Too Long input!")
            return
        arr=[[0 for i in range(n)] for j in range(n)]
        dx=[2,1,-1,-2,-2,-1,1,2]
        dy=[1,2,2,1,-1,-2,-2,-1]
        def knightTour(arr,n,x,y,count,l):
            if(count==n*n+1):
                return n*n+1
            arr[x][y]=count
            text_c=Text(str(count))
            text_c.scale(0.5)
            if(y==0):
                    text_c.shift((n//2-1) * LEFT)
                    if x<n/2:
                        text_c.shift(UP*size_sq*(n/2-x))
                    elif x==n/2:
                        pass
                    else:
                        text_c.shift(DOWN*size_sq*(x-n/2))
            else:
                    text_c.next_to(l[x][y-1], buff=0.2)
            self.play(FadeIn(text_c))
            self.wait(0.5)
            count=count+1
            l[x][y].set_fill(color=BLUE, opacity=0.7)
            for i in range(8):
                x1=x+dx[i]
                y1=y+dy[i]
                if(x1>=0 and x1<n and y1>=0 and y1<n and arr[x1][y1]==0):
                    count=knightTour(arr,n,x1,y1,count,l)
            l[x][y].set_fill(color=GREEN, opacity=0.7)
            text_h=Text(str(arr[x][y]) +" is processed and we Backtrack ", font="Arial", color=RED, size=1.3)
            text_h.scale(0.8)
            text_h.shift(DOWN*2)
            self.play(Write(text_h))
            self.wait(0.2)
            self.play(FadeOut(text_h))
            self.wait(0.3)
            return count
        l=[]
        for i in range(n):
            lt=[]
            for j in range(n):

                bb=square_text_box("", BLUE_D, GREEN_B)
                if(len(lt)==0):
                    bb.shift((n//2-1) * LEFT)
                    if i<n/2:
                        bb.shift(UP*size_sq*(n/2-i))
                    elif i==n/2:
                        pass
                    else:
                        bb.shift(DOWN*size_sq*(i-n/2))
                else:
                    bb.next_to(lt[-1], buff=0)
                
                lt.append(bb)
                #self.play(FadeIn(bb))
                self.add(bb)
            l.append(lt)
            text_h=Text("Knight's Tour", font="Arial", color=RED, size=2)
            text_h.scale(0.5)
            text_h.shift(UP*3.5)
            self.play(Write(text_h))
        c=knightTour(arr,n,0,0,1,l)
        
                
    