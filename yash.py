from manim import *
from collections import defaultdict
import math
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



class Tree:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
    
class Tree_inorder(Scene):
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")
            return

        # leng=math.ceil(math.log(2,n+1))
        
        def order(i, j,arr): 
            indx=2*i+j
            if indx>len(arr) or arr[indx-1]==-1:
                return None
            curr=Tree(arr[indx-1])
            curr.left=order(indx,0,arr)
            curr.right=order(indx,1,arr)
            return curr

        def construct_Tree(arr, n):
            if(n == 0):
                return None
            length=2**math.ceil(math.log(2,n+1))
            while len(arr)<length:
                arr.append(-1)
            root = Tree(arr[0])
            root.left=order(1,0,arr)
            root.right=order(1,1,arr)
            return root

        def visualise_Tree(root):
            if root==None:
                return None
            curr=Tree(square_text_box(str(root.val),BLUE_D, GREEN_B))
            curr.left=visualise_Tree(root.left)
            curr.right=visualise_Tree(root.right)
            return curr
        


        def show_Tree(root,x,y,k,par):
            if root==None:
                return 
            root.val.shift(((x) * RIGHT) +(y*UP))
            self.play(GrowFromCenter(root.val))
            if par!=None:
                li=Line(root.val.get_center()+[0,0.35,0],par.val.get_center()+[0,-0.35,0])
                li.z_index-=1
                self.play(GrowFromCenter(li))
            if k==0:
                k=(n)/2.2
            k/=2
            show_Tree(root.left,x-k,y-1,k,root)
            show_Tree(root.right,x+k,y-1,k,root)

        def show_Inorder(root):    
            if root:
                root.val.set_fill(BLUE,opacity=0.8)
                self.wait(1)
                show_Inorder(root.left)
                root.val.set_fill(GREEN,opacity=0.6)
                self.wait(1.5)
                show_Inorder(root.right)

        num_root=construct_Tree(arr,n)
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        text_a=Text("    In \n   Order \n Traversal" ,font="Arial",size=0.9,color=RED)
        text_a.to_edge(UP)
        text_a.shift(RIGHT*4)
        self.play(Write(text_a))
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        
        anime_root=visualise_Tree(num_root)
        show_Tree(anime_root,0,3,0,None)
        show_Inorder(anime_root)


class Tree_preorder(Scene):
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")
            return

        leng=math.ceil(math.log(2,n+1))
        
        def order(i, j,arr): 
            indx=2*i+j
            if indx>len(arr) or arr[indx-1]==-1:
                return None
            curr=Tree(arr[indx-1])
            curr.left=order(indx,0,arr)
            curr.right=order(indx,1,arr)
            return curr
      

        def construct_Tree(arr, n):
            if(n == 0):
                return None
            length=2**math.ceil(math.log(2,n+1))
            while len(arr)<length:
                arr.append(-1)
            root = Tree(arr[0])
            root.left=order(1,0,arr)
            root.right=order(1,1,arr)
            return root

        def visualise_Tree(root):
            if root==None:
                return None
            curr=Tree(square_text_box(str(root.val),BLUE_D, GREEN_B))
            curr.left=visualise_Tree(root.left)
            curr.right=visualise_Tree(root.right)
            return curr
        
        def show_Tree(root,x,y,k,par):
            if root==None:
                return 
            root.val.shift(((x) * RIGHT) +(y*UP))
            self.play(GrowFromCenter(root.val))
            if par!=None:
                li=Line(root.val.get_center()+[0,0.35,0],par.val.get_center()+[0,-0.35,0])
                li.z_index-=1
                self.play(GrowFromCenter(li))
            if k==0:
                k=(n)/2.2
            k/=2
            show_Tree(root.left,x-k,y-1,k,root)
            show_Tree(root.right,x+k,y-1,k,root)

        def show_preorder(root):    
            if root:
                root.val.set_fill(BLUE,opacity=0.8)
                self.wait(1)
                root.val.set_fill(GREEN,opacity=0.6)
                self.wait(1.5)
                show_preorder(root.left)
                show_preorder(root.right)

        num_root=construct_Tree(arr,n)
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        text_a=Text("    Pre \n   Order \n Traversal" ,font="Arial",size=0.9,color=RED)
        text_a.to_edge(UP)
        text_a.shift(RIGHT*4)
        self.play(Write(text_a))
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        
        anime_root=visualise_Tree(num_root)
        show_Tree(anime_root,0,3,0,None)
        show_preorder(anime_root)
        

class Tree_postorder(Scene):
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")
            return

        leng=math.ceil(math.log(2,n+1))
        
        def order(i, j,arr): 
            indx=2*i+j
            if indx>len(arr) or arr[indx-1]==-1:
                return None
            curr=Tree(arr[indx-1])
            curr.left=order(indx,0,arr)
            curr.right=order(indx,1,arr)
            return curr
      

        def construct_Tree(arr, n):
            if(n == 0):
                return None
            length=2**math.ceil(math.log(2,n+1))
            while len(arr)<length:
                arr.append(-1)
            root = Tree(arr[0])
            root.left=order(1,0,arr)
            root.right=order(1,1,arr)
            return root

        def visualise_Tree(root):
            if root==None:
                return None
            curr=Tree(square_text_box(str(root.val),BLUE_D, GREEN_B))
            curr.left=visualise_Tree(root.left)
            curr.right=visualise_Tree(root.right)
            return curr
        
        def show_Tree(root,x,y,k,par):
            if root==None:
                return 
            root.val.shift(((x) * RIGHT) +(y*UP))
            self.play(GrowFromCenter(root.val))
            if par!=None:
                li=Line(root.val.get_center()+[0,0.35,0],par.val.get_center()+[0,-0.35,0])
                li.z_index-=1
                self.play(GrowFromCenter(li))
            if k==0:
                k=(n)/2.2
            k/=2
            show_Tree(root.left,x-k,y-1,k,root)
            show_Tree(root.right,x+k,y-1,k,root)

        def show_postorder(root):    
            if root:
                root.val.set_fill(BLUE_C,opacity=0.8)
                self.wait(1)
                show_postorder(root.left)
                show_postorder(root.right)
                
                root.val.set_fill(GREEN,opacity=0.6)
                self.wait(1.5)

        num_root=construct_Tree(arr,n)
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        text_a=Text("    Post \n   Order \n Traversal" ,font="Arial",size=0.9,color=RED)
        text_a.to_edge(UP)
        text_a.shift(RIGHT*4)
        self.play(Write(text_a))
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        
        anime_root=visualise_Tree(num_root)
        show_Tree(anime_root,0,3,0,None)
        show_postorder(anime_root)




class Tree_levelorder(Scene):
    def construct(self):
        arr=takeArray()
        n=len(arr)
        if(n>MAX_SIZE*2):
            print("Too Long input!")
            return
        if(n==0):
            print("No input given")
            return

        # leng=math.ceil(math.log(2,n+1))
        
        def order(i, j,arr): 
            indx=2*i+j
            if indx>len(arr) or arr[indx-1]==-1:
                return None
            curr=Tree(arr[indx-1])
            curr.left=order(indx,0,arr)
            curr.right=order(indx,1,arr)
            return curr
      

        def construct_Tree(arr, n):
            if(n == 0):
                return None
            length=2**math.ceil(math.log(2,n+1))
            while len(arr)<length:
                arr.append(-1)
            root = Tree(arr[0])
            root.left=order(1,0,arr)
            root.right=order(1,1,arr)
            return root

        def visualise_Tree(root):
            if root==None:
                return None
            curr=Tree(square_text_box(str(root.val),BLUE_D, GREEN_B))
            curr.left=visualise_Tree(root.left)
            curr.right=visualise_Tree(root.right)
            return curr
        
        def show_Tree(root,x,y,k,par):
            if root==None:
                return 
            root.val.shift(((x) * RIGHT) +(y*UP))
            self.play(GrowFromCenter(root.val))
            if par!=None:
                li=Line(root.val.get_center()+[0,0.35,0],par.val.get_center()+[0,-0.35,0])
                li.z_index-=1
                self.play(GrowFromCenter(li))
            if k==0:
                k=(n)/2.2
            k/=2
            show_Tree(root.left,x-k,y-1,k,root)
            show_Tree(root.right,x+k,y-1,k,root)

        def show_levelorder(root,num_root):    
            if root:
                q=[]
                q1=[]
                q.append(root)
                q1.append(num_root)

                text_c=Text("   "+str(num_root.val )+" \n  gets in \n  queue",color=BLUE,size=0.6)
                text_c.to_edge(UP)
                text_c.shift(4.5*LEFT+DOWN)
                self.play(Write(text_c))
                self.wait(0.4)
                self.play(FadeOut(text_c))

                root.val.set_fill(BLUE_C,opacity=0.8)
                self.wait(1)
                while(len(q)!=0):
                    p=q.pop(0)
                    p1=q1.pop(0)

                    text_c=Text("   "+str(p1.val)+" \n  gets  \n  visited",color=GREEN,size=0.6)
                    text_c.to_edge(UP)
                    text_c.shift(4.5*LEFT+DOWN)
                    self.play(Write(text_c))
                    self.wait(0.4)
                    self.play(FadeOut(text_c))

                    p.val.set_fill(GREEN,opacity=0.6)
                    self.wait(1.5)
                    if p.left:
                        p.left.val.set_fill(BLUE_C,opacity=0.8)
                        text_c=Text("   "+str(p1.left.val )+" \n  gets in \n  queue",color=BLUE,size=0.6)
                        text_c.to_edge(UP)
                        text_c.shift(4.5*LEFT+DOWN)
                        self.play(Write(text_c))
                        self.wait(0.4)
                        self.play(FadeOut(text_c))
                        self.wait(1)
                        q.append(p.left)
                        q1.append(p1.left)
                    if p.right:
                        p.right.val.set_fill(BLUE_C,opacity=0.8)
                        text_c=Text("   "+str(p1.right.val )+" \n  gets in \n  queue",color=BLUE,size=0.6)
                        text_c.to_edge(UP)
                        text_c.shift(4.5*LEFT+DOWN)
                        self.play(Write(text_c))
                        self.wait(0.4)
                        self.play(FadeOut(text_c)) 
                        self.wait(1)
                        q.append(p.right)
                        q1.append(p1.right)

                    
        text_a=Text("   Level \n   Order \n Traversal" ,font="Arial",size=0.9,color=RED)
        text_a.to_edge(UP)
        text_a.shift(RIGHT*4)
        self.play(Write(text_a))
        num_root=construct_Tree(arr,n)
        bubs = square_text_box(str(arr[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        l=[]
        l.append(bubs)
        
        for i in range(1,n):
            bubs = square_text_box(str(arr[i]), BLUE_D, GREEN_B)
            bubs.next_to(l[-1], buff=0)
            l.append(bubs)
        
        anime_root=visualise_Tree(num_root)
        show_Tree(anime_root,0,3,0,None)
        show_levelorder(anime_root,num_root)

class BST(Scene):
    def construct(self):
        print("Enter number of operations  that is ,", end=" ")
        n = takeInt()
        print("For Search : 0 input_number")
        print("For Insert : 1 input_number")    
        l=[]
        arr=[]
        for i in range(n):
            arr.append(list(map(int,input("Enter operation : ").split())))
        def search(root,obj_root,key):
            if root is None: 
                return root
            elif root.val == key:
                s=square_swap(GREEN)
                s.shift(obj_root.val.get_center())
                text_c=Text("Found",color=GREEN)
                text_c.to_edge(UP)
                text_c.shift(4*RIGHT+DOWN)
                self.play(Write(text_c))
                self.play(FadeIn(s))
                self.wait(0.4)
                self.play(FadeOut(s))
                self.play(FadeOut(text_c))
                return root
            if root.val < key:
                s=square_swap(BLUE)
                s.shift(obj_root.val.get_center())
                self.play(FadeIn(s))
                text_c=Text("  we will \n  search right \n  as key is \n  bigger",color=BLUE,size=0.6)
                text_c.to_edge(UP)
                text_c.shift(4*RIGHT+DOWN)
                self.play(Write(text_c))
                
                self.wait(0.4)
                self.play(FadeOut(s))
                self.play(FadeOut(text_c))
                return search(root.right,obj_root.right,key)
            s=square_swap(PINK)
            s.shift(obj_root.val.get_center())
            self.play(FadeIn(s))
            text_c=Text("we will \n search left \n as key is \nsmaller",color=PINK,size=0.6)
            text_c.to_edge(UP)
            text_c.shift(3.5*RIGHT+DOWN)
            self.play(Write(text_c))
            self.wait(0.4)
            self.play(FadeOut(s))
            self.play(FadeOut(text_c))
            return search(root.left,obj_root.left,key)
         
        def insert(root,obj_root, key,par,x,y,k):
            if root is None:
                text_c=Text("  Inserting \n  here ",color=GREEN,size=0.6)
                text_c.to_edge(UP)
                text_c.shift(4*RIGHT+DOWN)
                self.play(Write(text_c))
                self.wait(0.4)
                self.play(FadeOut(text_c))
                y1=square_text_box(str(key),BLUE_D, GREEN_B)
                y1.shift(((x) * RIGHT) +(y*UP))
                if par!=None:
                    li=Line(y1.get_center()+[0,0.35,0],par.val.get_center()+[0,-0.35,0])
                    li.z_index-=1
                    self.play(GrowFromCenter(li))
                self.play(GrowFromCenter(y1))
                return [Tree(key),Tree(y1)]
            else:
                if k==0:
                    k=(n)/2.2
                k/=2
                if root.val == key:
                    return [root,obj_root]
                elif root.val < key:
                    s=square_swap(BLUE)
                    s.shift(obj_root.val.get_center())
                    self.play(FadeIn(s))
                    self.wait(0.4)
                    text_c=Text("  we will \n  go right \n  as key is \n  bigger",color=BLUE,size=0.6)
                    text_c.to_edge(UP)
                    text_c.shift(4*RIGHT+DOWN)
                    self.play(Write(text_c))
                    self.wait(0.4)
                    self.play(FadeOut(text_c))
                    temp=insert(root.right,obj_root.right, key,obj_root,x+k,y-1,k)
                    root.right = temp[0]
                    obj_root.right=temp[1]  
                    self.play(FadeOut(s))      
                else:
                    s=square_swap(YELLOW)
                    s.shift(obj_root.val.get_center())
                    self.play(FadeIn(s))
                    self.wait(0.4)
                    text_c=Text("  we will \n  go left \n  as key is \n  smaller",color=YELLOW,size=0.6)
                    text_c.to_edge(UP)
                    text_c.shift(4*RIGHT+DOWN)
                    self.play(Write(text_c))
                    self.wait(0.4)
                    self.play(FadeOut(text_c))
                    t=insert(root.left,obj_root.left, key,obj_root,x-k,y-1,k)
                    root.left = t[0]
                    obj_root.left=t[1]
                    self.play(FadeOut(s))  
            return [root,obj_root]
         
        
        def inorder(root):
            if root:
                inorder(root.left)
                print(root.val)
                inorder(root.right)
        root=None
        obj_root=None
        text_a=Text("BST",font="Arial",size=1.2,color=RED)
        text_a.to_edge(UP)
        text_a.shift(RIGHT*4)
        self.play(Write(text_a))

        for _ in arr:

            if _[0]==1:
                text_h=Text("Operation : \nInserting "+str(_[1]))
                text_h.set_color(BLUE_D)
                text_h.to_edge(UP)
                text_h.shift(LEFT*4.5)
                text_h.scale(0.8)
                self.play(Write(text_h))
                self.wait(0.5)
                
                root,obj_root=insert(root,obj_root,_[1],None,0,3,0)
                self.play(FadeOut(text_h))
            else:
                text_h=Text("Operation : \nSearching "+str(_[1]))
                text_h.set_color(YELLOW)
                text_h.to_edge(UP)
                text_h.shift(LEFT*4.5)
                text_h.scale(0.8)
                self.play(Write(text_h))
                self.wait(0.5)
                
                t=search(root,obj_root,_[1])
                self.play(FadeOut(text_h))
        
                
        
 
    



    