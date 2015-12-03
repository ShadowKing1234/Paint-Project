#Rahul Jayachandiran
#A paint program allows the user to draw, erase and do a variety of things. It should be easy to use, have many features and have certain tools.
from pygame import*
from random import*
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename




#----------------Setup-------------------------------------#
screen=display.set_mode((1024,768))
draw_col=(0,0,0) #The current colour. Starting colour is black.

tool="None" #Doesn't start off with a tool or stamp
stamp="None"
screen.fill((0,0,0))
outline=(255,0,0)

#Flags
drawing=False
click=True


#Used to change what is displayed in the side panel.
page1="tools"
page2="stamps"
page3="stamps2"
page4="music"
page0="opening screen"
page=page0#Starting page
width=1 #For spraypaint
init() #For font

root = Tk() 
root.withdraw()
                            


#---------------------Images/songs-------------------------------#
tools_pic=image.load("Pictures/tools.png")
stamps_pic=image.load("Pictures/stamps.png")
music_pic=image.load("Pictures/music.png")
pencil_pic=image.load("Pictures/pen-icon.png")
eraser_pic=image.load("Pictures/eraser-icon.png")
bg_pic=image.load("Pictures/Bg.png")
colour_palette=image.load("Pictures/palette.png")
trash_pic=image.load("Pictures/trash.png")
white_pic=image.load("Pictures/white.png")
ellipse_pic=image.load("Pictures/ellipse.png")
rectangle_pic=image.load("Pictures/rectangle.png")
fellipse_pic=image.load("Pictures/filled ellipse.png")
frectangle_pic=image.load("Pictures/filled rectangle.png")
line_pic=image.load("Pictures/line.png")
spraypaint_pic=image.load("Pictures/spraypaint.png")
polygon_pic=image.load("Pictures/polygon.png")
fill_pic=image.load("Pictures/fill.png")
eyedrop_pic=image.load("Pictures/eyedrop.png")
brush_pic=image.load("Pictures/brush.png")
narutosage_pic=image.load("Pictures/NarutoSage.png")
leaf_pic=image.load("Pictures/Leaf.png")
sand_pic=image.load("Pictures/Sand.png")
stone_pic=image.load("Pictures/Stone.png")
mist_pic=image.load("Pictures/Mist.png")
lightning_pic=image.load("Pictures/Lightning.png")
kakashi_pic=image.load("Pictures/kakashi.png")
naruto_pic=image.load("Pictures/naruto.png")
sakura_pic=image.load("Pictures/sakura.png")
sasuke_pic=image.load("Pictures/sasuke.png")
sharingan_pic=image.load("Stamps/sharingan.png")
headband_pic=image.load("Stamps/headband.png")
rinnegan_pic=image.load("Stamps/rinnegan.png")
kunai_pic=image.load("Stamps/kunai.png")
byakugan_pic=image.load("Stamps/byakugan.png")
shuriken_pic=image.load("Stamps/shuriken.png")
rasengan_pic=image.load("Stamps/rasengan.png")
chidori_pic=image.load("Stamps/chidori.png")
leftarrow=image.load("Pictures/left arrow.png")
rightarrow=image.load("Pictures/right arrow.png")
akatsuki_pic=image.load("Pictures/akatsuki.png")
fox_pic=image.load("Pictures/fox.png")
jinchuuriki_pic=image.load("Pictures/jinchuuriki.png")
shippuden_pic=image.load("Pictures/shippuden.png")
orochimaru_pic=image.load("Pictures/orochimaru.png")
toad_pic=image.load("Stamps/toad.png")
snake_pic=image.load("Stamps/snake.png")
slug_pic=image.load("Stamps/slug.png")
gamakichi_pic=image.load("Stamps/Gamakichi.png")
kyuubi_pic=image.load("Stamps/kyuubi.png")
leaf_bg=image.load("Pictures/leaf_bg.png")
sand_bg=image.load("Pictures/sand_bg.png")
stone_bg=image.load("Pictures/stone_bg.png")
mist_bg=image.load("Pictures/mist_bg.png")
lightning_bg=image.load("Pictures/lightning_bg.png")
file_pic=image.load("Pictures/file.png")
save_pic=image.load("Pictures/save.png")
undo_pic=image.load("Pictures/undo.png")
redo_pic=image.load("Pictures//redo.png")
left_pic=image.load("Pictures/left arrow2.png")
right_pic=image.load("Pictures/right arrow2.png")
yellow_bg=image.load("Pictures/yellow.png")
naruto_bg=image.load("Pictures/naruto bg.png")
squares_pic=image.load("Pictures/squares.png")




#------------------------Rects---------------------#

pencil_rect=Rect((10,150),(50,50))
eraser_rect =Rect((80,150),(50,50))
spraypaint_rect=Rect((10,220),(50,50))
brush_rect=Rect((80,220),(50,50))
rectangle_rect=Rect((10,290),(50,50))
ellipse_rect=Rect((80,290),(50,50))
frectangle_rect=Rect((10,360),(50,50))
fellipse_rect=Rect((80,360),(50,50))
eyedrop_rect=Rect((10,430),(50,50))
line_rect=Rect((80,430),(50,50))

fill_rect=Rect((10,500),(50,50))
trash_rect=Rect((80,500),(50,50))





headband_rect=Rect((10,150),(55,65))
sharingan_rect=Rect((75,150),(55,65))
kunai_rect=Rect((10,225),(55,65))
rinnegan_rect=Rect((75,225),(55,65))
shuriken_rect=Rect((10,300),(55,65))
byakugan_rect=Rect((75,300),(55,65))
rasengan_rect=Rect((10,375),(55,65))
chidori_rect=Rect((75,375),(55,65))
rarrow_rect=Rect((60,470),(40,25))

black_rect=Rect((10,145),(120,355))
toad_rect=Rect((20,150),(100,60))
snake_rect=Rect((20,220),(100,60))
slug_rect=Rect((20,290),(100,60))
gamakichi_rect=Rect((20,360),(100,60))
kyuubi_rect=Rect((20,430),(100,60))
larrow_rect=Rect((53,505),(35,25))

akatsuki_rect=Rect((10,150),(120,50))
fox_rect=Rect((10,215),(120,50))
jinchuuriki_rect=Rect((10,280),(120,50))
theme_rect=Rect((10,345),(120,50))
orochimaru_rect=Rect((10,410),(120,50))

leaf_rect=Rect((444,20),(100,80))
sand_rect=Rect((564,20),(100,80))
stone_rect=Rect((684,20),(100,80))
mist_rect=Rect((804,20),(100,80))
lightning_rect=Rect((924,20),(100,80))


music_rect=Rect((45,28),(50,50))
tools_rect=Rect((15,88),(50,50))
stamps_rect=Rect((75,88),(50,50))

file_rect=Rect((0,0),(35,25))
save_rect=Rect((35,0),(35,25))
undo_rect=Rect((70,0),(35,25))
redo_rect=Rect((105,0),(35,25))


box_rect=Rect(290,620,50,50)
orange_rect=Rect((0,78),(140,472))
palette_rect=Rect((160,580),(130,120))
canvas_rect=Rect(370,200,650,500)

pos_rect=Rect(650,120,130,60)
text_rect=Rect(150,0,200,200)


left_rect=Rect(850,125,30,40)
right_rect=Rect(985,125,30,40)

button_rect=Rect(600,600,200,100)
page_rect=Rect((0,0),(1024,768))

description_rect=Rect((160,140),(200,65))
blue_rect=Rect((160,120),(200,20))

dark_rect=Rect((5,145),(130,305))

#Lists
tools=[spraypaint_rect,pencil_rect,eraser_rect,brush_rect,rectangle_rect,trash_rect,fill_rect,line_rect,ellipse_rect,eyedrop_rect,fellipse_rect,frectangle_rect]

coords=[] #For fill tool
music=[akatsuki_rect,fox_rect,jinchuuriki_rect,theme_rect,orochimaru_rect]











#---------------Text-----------------------------#
font.init()
romanfont=font.SysFont("Times New Roman",35)
posfont=font.SysFont("Arial",25)
posfont2=font.SysFont("Arial",20)
cover=screen.subsurface(pos_rect).copy()

cover3=screen.subsurface(description_rect).copy()
cover4=screen.subsurface(blue_rect).copy()
cover5=screen.subsurface(text_rect).copy()
descriptionfont=font.SysFont("Arial",15)









#---------------Placing images and shapes-------------
screen.blit(bg_pic,(150,0))
draw.rect(screen,(255,128,64),((0,0),(140,767)))
draw.rect(screen,(0,0,0),((140,0),(10,768)))
draw.rect(screen,(0,0,0),leaf_rect)
draw.rect(screen,(0,0,0),sand_rect)
draw.rect(screen,(0,0,0),stone_rect)
draw.rect(screen,(0,0,0),mist_rect)
draw.rect(screen,(0,0,0),lightning_rect)
draw.rect(screen,(255,255,255),music_rect)                  
draw.rect(screen,(255,255,255),tools_rect)
draw.rect(screen,(255,255,255),stamps_rect)
draw.rect(screen,(73,243,226),file_rect)
draw.rect(screen,(73,243,226),save_rect)
draw.rect(screen,(73,243,226),undo_rect)
draw.rect(screen,(73,243,226),redo_rect)
draw.rect(screen,(draw_col),palette_rect)
draw.rect(screen,(255,0,0),pos_rect)


draw.rect(screen,(255,0,0),description_rect)
draw.rect(screen,(0,0,255),blue_rect)


canvas=draw.rect(screen,(255,255,255),canvas_rect)
draw.line(screen,(0,0,0),(35,0),(35,25))
draw.line(screen,(0,0,0),(70,0),(70,25))
draw.line(screen,(0,0,0),(105,0),(105,25))



screen.blit(leaf_pic,(444,20))
screen.blit(sand_pic,(564,20))
screen.blit(stone_pic,(684,20))
screen.blit(mist_pic,(804,20))
screen.blit(lightning_pic,(924,20))


screen.blit(naruto_pic,(-20,-5))
screen.blit(sakura_pic,(300,-10))
screen.blit(sasuke_pic,(650,-20))

screen.blit(music_pic,(45,28))
screen.blit(stamps_pic,(75,88))
screen.blit(tools_pic,(20,95))

screen.blit(file_pic,(-240,-245))
screen.blit(save_pic,(-165,-210))
screen.blit(undo_pic,(-35,-115))
screen.blit(redo_pic,(0,-115))

screen.blit(kakashi_pic,(-400,330))
screen.blit(narutosage_pic,(-110,140))

screen.blit(colour_palette,(160,580))


#Things for undo/redo
undo=[]
redo=[]
firstcopy=screen.subsurface(canvas_rect).copy()
undo.append(firstcopy)


#Sizes
size=1000
size1=1000
size2=1
size3=10


#Mouse coordinates
sx,sy=0,0
bx,by=mouse.get_pos()


running=True
while running:
    clickDown = False
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            

            if e.button==1:
                clickDown = True
                screencopy=screen.copy() 
                sx,sy=mouse.get_pos() #For tools
                
                if len(undo)>1 and clickDown and undo_rect.collidepoint(mx,my):
                    screen.set_clip(canvas)
                    tool="undo"
                    redo.append(undo[-1])#Adds the last thing in the undo list to the redo list.
                    screen.blit(undo[-2],(370,200)) #Blits the 2nd last thing in the undo list.
                    del undo[-1] #Deletes the last thing in the undo list.
                    

                if len(redo)>0 and clickDown and redo_rect.collidepoint(mx,my):
                    screen.set_clip(canvas)
                    tool="redo"
                    undo.append(redo[-1]) #Adds the last thing in the redo list to the undo list.
                    screen.blit(redo[-1],(370,200)) #Blits the last thing in the redo list.
                    del redo[-1] #Deletes the last thing in the redo list.
                    

                

                                                        

                
                
                    
                
                

            if e.button==4:#Scroll up
                if stamp=="toad" or stamp=="snake" or stamp=="slug" or stamp=="gamakichi" or stamp=="kyuubi":
                    size+=50
                    if size==3950:
                        size=3950
               
                    size1+=50
                    if size1==3950:
                        size1=1950
                #if one of these stamps are selected you can increase the size of the stamp.

                if tool=="rectangle" or tool=="line":
                    size2+=1
                    if size2==20:
                        size2=19
                #If one of these tools are selected it increases the thickness of the the line and rectangle.


                if tool=="brush" or tool=="eraser":
                    size3+=1
                    if size3==25:
                        size3=24
                #If one of these tools are selected it increases the size of the tool.

                if tool=="spraypaint":
                    width+=1
                    if width==16:
                        width=15
                #If this tool is selected the spraypaint gets a larger radius.
            

            if e.button==5:#Scroll down
                if stamp=="toad" or stamp=="snake" or stamp=="slug" or stamp=="gamakichi" or stamp=="kyuubi":
                    
                    size-=50
                    if size==950:
                        size=1000
               
               
                    size1-=50
                    if size1==950:
                        size1=1000
                #if one of these stamps are selected you can decrease the size of the stamp by scrolling down.

                if tool=="rectangle" or tool=="line":
                    size2-=1
                    if size2==0:
                        size2=1
                #If one of these tools are selected it decreases the thickness of the the line and rectangle.


                if tool=="brush" or tool=="eraser":
                    size3-=1
                    if size3==10:
                        size3=11
                #If one of these tools are selected it decreases the size of the tool.

                if tool=="spraypaint":
                    width-=1
                    if width==0:
                        width=1
                #If this tool is selected the spraypaint gets a smaller radius.
                
           




        if e.type==MOUSEBUTTONUP:

            if e.button==1:
                clickDown=True
                if clickDown and canvas_rect.collidepoint(mx,my):
                    copy=screen.subsurface(canvas_rect).copy()
                    undo.append(copy)
         
    #For mouse
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

        
        

    #Always displays the position inside the screen.
    if mx<=1024 and my<=768:
        screen.set_clip(pos_rect)
        x_txt=posfont.render("X =",True,(0,0,255)) #Makes mx a string
        y_txt=posfont.render("Y=",True,(0,0,255)) #Makes my a string
        pos_txt=posfont.render(str((mx)),True,(0,0,255))
        post_txt2=posfont.render(str((my)),True,(0,0,255))
        #Redraws the position box.
        draw.rect(screen,(255,0,0),pos_rect)
        draw.rect(screen,(0,0,255),pos_rect,7)
        #Blitting all the text.
        screen.blit(x_txt,(680,120))
        screen.blit(y_txt,(680,150))
        screen.blit(pos_txt,(720,120))
        screen.blit(post_txt2,(720,150))

 
               


   
    #Is always displaying this text because this flag isn't changing.   
    if click:
        screen.set_clip(text_rect)
        txtpic=romanfont.render("Choose",True,(255,255,0))
        txtpic2=romanfont.render("Your",True,(255,255,0))
        txtpic3=romanfont.render("Village",True,(255,255,0))
        screen.blit(txtpic,(230,0))
        screen.blit(txtpic2,(240,40))
        screen.blit(txtpic3,(225,80)) 
        
        

    if tools_rect.collidepoint(mx,my) and mb[0]==1:
    #this page displays all the tools in this paint program.
        page=page1
        if page==page1:
            screen.set_clip(orange_rect)
            draw.rect(screen,(255,128,64),orange_rect)                  

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)

            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
            #Must redraw and blit this because the tools and stamps icons are not visible because of the orange_rect.

            draw.line(screen,(0,0,0),(15,138),(65,138),7)
            #Indicates that this is the tool page.

            #Blits the background for the tools.
            screen.blit(squares_pic,(10,150))
            screen.blit(squares_pic,(80,150))
            screen.blit(squares_pic,(10,220))
            screen.blit(squares_pic,(80,220))
            screen.blit(squares_pic,(10,290))
            screen.blit(squares_pic,(80,290))
            screen.blit(squares_pic,(10,360))
            screen.blit(squares_pic,(80,360))
            screen.blit(squares_pic,(10,430))
            screen.blit(squares_pic,(80,430))
            screen.blit(squares_pic,(10,500))
            screen.blit(squares_pic,(80,500))
            screen.blit(squares_pic,(10,570))
            screen.blit(squares_pic,(80,570))

            #Blits the pictures of the tools.
            screen.blit(pencil_pic,(-95,40))
            screen.blit(eraser_pic,(-45,28))
            screen.blit(spraypaint_pic,(10,220))
            screen.blit(brush_pic,(80,220))
            screen.blit(line_pic,(80,430))
            screen.blit(trash_pic,(35,465))
            screen.blit(fill_pic,(10,500))
            screen.blit(eyedrop_pic,(10,430))
            screen.blit(ellipse_pic,(-20,195))
            screen.blit(fellipse_pic,(-535,-243))
            screen.blit(rectangle_pic,(15,295))
            screen.blit(frectangle_pic,(-85,265))
            
   
        


    #Depending on the page selected the orange rectangle displays something different.

    elif stamps_rect.collidepoint(mx,my) and mb[0]==1 or larrow_rect.collidepoint(mx,my) and mb[0]==1 and page==page3:
        #This is the first page where the user can use stamps.   
        page=page2
        if page==page2:
            screen.set_clip(orange_rect)
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),((5,145),(130,305)))
            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))

            
            draw.line(screen,(0,0,0),(75,138),(125,138),7)
            #Indicates that this is the stamp page
            
            #Draws the rectangles for all the stamps.
            draw.rect(screen,(255,255,255),sharingan_rect)
            draw.rect(screen,(255,255,255),headband_rect)
            draw.rect(screen,(255,255,255),rinnegan_rect)
            draw.rect(screen,(255,255,255),kunai_rect)
            draw.rect(screen,(255,255,255),byakugan_rect)
            draw.rect(screen,(255,255,255),shuriken_rect)
            draw.rect(screen,(255,255,255),rasengan_rect)
            draw.rect(screen,(255,255,255),chidori_rect)
            
            
            
            #Blits the pictures of the stamps to the rectangles.
            screen.blit(sharingan_pic,(-410,-330))
            screen.blit(headband_pic,(-115,70))
            screen.blit(rinnegan_pic,(0,155))
            screen.blit(kunai_pic,(-212,24))
            screen.blit(byakugan_pic,(-48,182))
            screen.blit(shuriken_pic,(-40,260))
            screen.blit(rasengan_pic,(-213,153))
            screen.blit(chidori_pic,(-20,289))
            screen.blit(rightarrow,(0,400))
        

    elif page==page2 and rarrow_rect.collidepoint(mx,my) and mb[0]==1:
        #This is the other page where users can use stamps.
        page=page3
        if page==page3:
            screen.set_clip(orange_rect)
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)

            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))

            draw.line(screen,(0,0,0),(75,138),(125,138),7)
            #Indicates that this is still a stamp page.

            #Draws the rectangles for these stamps.
            draw.rect(screen,(0,0,0),black_rect)
            draw.rect(screen,(255,255,255),toad_rect)
            draw.rect(screen,(255,255,255),snake_rect)
            draw.rect(screen,(255,255,255),slug_rect)
            draw.rect(screen,(255,255,255),gamakichi_rect)
            draw.rect(screen,(255,255,255),kyuubi_rect)
            
            
            #Blits the pictures of the stamps to the rectangles.
            screen.blit(toad_pic,(-340,-305))
            screen.blit(snake_pic,(-380,30))
            screen.blit(slug_pic,(-250,80))
            screen.blit(gamakichi_pic,(-185,180))
            screen.blit(kyuubi_pic,(-130,255))
            screen.blit(leftarrow,(-10,445))
            

           

    elif music_rect.collidepoint(mx,my) and mb[0]==1:
        page=page4
        if page==page4:
            screen.set_clip(orange_rect)
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            draw.rect(screen,(255,255,255),music_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
            screen.blit(music_pic,(45,28))
            draw.line(screen,(0,0,0),(45,78),(95,78),7)
            
                      

            draw.rect(screen,(255,255,255),akatsuki_rect)
            draw.rect(screen,(255,255,255),fox_rect)
            draw.rect(screen,(255,255,255),jinchuuriki_rect)
            draw.rect(screen,(255,255,255),theme_rect)
            draw.rect(screen,(255,255,255),orochimaru_rect)
            

            screen.blit(akatsuki_pic,(10,150))
            screen.blit(fox_pic,(10,215))
            screen.blit(jinchuuriki_pic,(10,280))
            screen.blit(shippuden_pic,(10,345))
            screen.blit(orochimaru_pic,(10,410))
            
            
         

        
    

    if palette_rect.collidepoint(mx,my) and mb[0]==1 and clickDown:
        draw_col=screen.get_at((mx,my))#Changes the current colour.
        screen.set_clip(box_rect)
        draw.rect(screen,(draw_col),box_rect)#Displays the current colour.


    #Changing backgrounds.
    if leaf_rect.collidepoint(mx,my) and clickDown:
        screen.set_clip(canvas)
        screen.blit(leaf_bg,(370,200))
    elif sand_rect.collidepoint(mx,my) and clickDown:
        screen.set_clip(canvas)
        screen.blit(sand_bg,(370,200))
    elif stone_rect.collidepoint(mx,my) and clickDown:
        screen.set_clip(canvas)
        screen.blit(stone_bg,(370,200))
    elif mist_rect.collidepoint(mx,my) and clickDown:
        screen.set_clip(canvas)
        screen.blit(mist_bg,(370,200))
    elif lightning_rect.collidepoint(mx,my) and clickDown:
        screen.set_clip(canvas)
        screen.blit(lightning_bg,(370,200))

    #Loads an image from your files.
    if file_rect.collidepoint(mx,my) and clickDown:
        screen.set_clip(canvas)
        fileName = askopenfilename(parent=root,title="Open Image:") #Gets the file name
        print(fileName)
        loadpic=image.load(fileName) #Loads the image.
        screen.blit(loadpic,(370,200)) #Blits the image.
        screen.set_clip(None)


    #Save an image to your files.
    if save_rect.collidepoint(mx,my) and clickDown:
        back=screen.subsurface(canvas_rect)
        fileName = asksaveasfilename(parent=root,title="Save the image as...") #Gets the name of what the file will be saved as
        print(fileName)
        image.save(back,fileName+".png") #Saves the picture.

    
       
                
    
    if page==page1:
        #Selecting tools
        if pencil_rect.collidepoint(mx,my) and clickDown: #ClickDown allows you to select the tools
            screen.set_clip(orange_rect)
            tool="pencil"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5) #Draws an orange rectangle to blend in with background.
            draw.rect(screen,(0,0,0),pencil_rect,5)#Draws rectangle to show which tools is selected.
            
            

        elif eraser_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect)
            tool="eraser"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),eraser_rect,5)

        elif spraypaint_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect)
            tool="spraypaint"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),spraypaint_rect,5)

        elif brush_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect)
            tool="brush"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),brush_rect,5)

        elif rectangle_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect)
            tool="rectangle"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),rectangle_rect,5)

        elif ellipse_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect)
            tool="ellipse"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),ellipse_rect,5)

        elif frectangle_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect)
            tool="filled rectangle"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),frectangle_rect,5)
        elif fellipse_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect)
            tool="filled ellipse"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),fellipse_rect,5)  
        elif eyedrop_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect)
            tool="eyedrop"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),eyedrop_rect,5)
        elif line_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect) 
            tool="line"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),line_rect,5)
        elif fill_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect)
            tool="fill"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),fill_rect,5)
        elif trash_rect.collidepoint(mx,my) and clickDown:
            screen.set_clip(orange_rect)
            tool="trash"
            for i in tools:
                draw.rect(screen,(255,128,64),i,5)
            draw.rect(screen,(0,0,0),trash_rect,5)
            screen.blit(white_pic,(370,200))

        if tool=="trash":
            screen.set_clip(canvas)
            screen.blit(white_pic,(370,200))

        
        
            
        if canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            drawing=True

            if tool=="pencil" and mb[0]==1:
                draw.circle(screen,draw_col,(mx,my),1)
                draw.line(screen,draw_col,(bx,by),(mx,my),5) #Draws line connecting the circles.
                

            elif tool=="eraser" and mb[0]==1:
                draw.circle(screen,(255,255,255),(mx,my),size3)
                draw.line(screen,(255,255,255),(bx,by),(mx,my),size3*2+5) #Line that connects the white circles
      
            elif tool=="spraypaint" and mb[0]==1:
                for i in range(width): #When the width increases the radius of the circles does as well.
                    x=randint(mx-width,mx+width)    
                    y=randint(my-width,my+width)
                    if ((mx-x)**2+(my-y)**2)**.5 <= 10: #Distance formula
                        draw.circle(screen,draw_col,(x,y),0)

                
            elif tool=="brush" and mb[0]==1: #Larger version of the pencil. 
                draw.circle(screen,draw_col,(mx,my),size3)
                draw.line(screen,draw_col,(bx,by),(mx,my),size3*2+5)

            elif tool=="rectangle" and mb[0]==1:
                screen.blit(screencopy,(0,0)) #Shows the rectangle when you are making it.
                draw.rect(screen,draw_col,(sx,sy,mx-sx,my-sy),size2) #Lets you drag the rectangle

            elif tool=="ellipse" and mb[0]==1:
                screen.blit(screencopy,(0,0)) #Shows the rectangle when you are making it.
                #Allows you to drag the elipse in all 4 directions.
                if (mx-sx)>2 and (my-sy)>2:
                    draw.ellipse(screen,draw_col,(sx,sy,mx-sx,my-sy),1)
                elif (mx-sx)<-2 and (my-sy)<-2:
                    draw.ellipse(screen,draw_col,(mx,my,sx-mx,sy-my),1)
                elif (mx-sx)<-2 and (my-sy)>2:
                    draw.ellipse(screen,draw_col,(mx,sy,sx-mx,my-sy),1)
                elif (mx-sx)>2 and (my-sy)<-2:
                    draw.ellipse(screen,draw_col,(sx,my,mx-sx,sy-my),1)

                            
            elif tool=="filled rectangle" and mb[0]==1: #A filled version of the rectangle
                screen.blit(screencopy,(0,0))
                draw.rect(screen,draw_col,(sx,sy,mx-sx,my-sy))
                
    
            elif tool=="filled ellipse" and mb[0]==1: #A filled version of the ellipse
                screen.blit(screencopy,(0,0))
                if (mx-sx)>2 and (my-sy)>2:
                    draw.ellipse(screen,draw_col,(sx,sy,mx-sx,my-sy))
                elif (mx-sx)<-2 and (my-sy)<-2:
                    draw.ellipse(screen,draw_col,(mx,my,sx-mx,sy-my))
                elif (mx-sx)<-2 and (my-sy)>2:
                    draw.ellipse(screen,draw_col,(mx,sy,sx-mx,my-sy))
                elif (mx-sx)>2 and (my-sy)<-2:
                    draw.ellipse(screen,draw_col,(sx,my,mx-sx,sy-my))

                
               

            elif tool=="eyedrop" and mb[0]==1:
                screen.set_clip(box_rect)
                draw_col=screen.get_at((mx,my)) #Gets the colour inside the canvas.
                draw.rect(screen,(draw_col),box_rect) #Displays the colour on the box that shows the current colour.

            elif tool=="fill" and mb[0]==1:
                color_at = screen.get_at((mx,my)) 
                coords=[(mx,my)]
                #Creates a list using the coordinates we got.
                if draw_col!=color_at:
                    while len(coords):
                        x,y=coords.pop() #Gets the last coordinates in the list. 
                        if screen.get_at((x,y)) == color_at and canvas.collidepoint((x,y)): #Makes sure the fill occurs in the canvas,
                            screen.set_at((x,y),draw_col) #Fills one pixel
                            coords.append((x-1,y))  
                            coords.append((x+1,y))
                            coords.append((x,y-1))
                            coords.append((x,y+1))
                            #Adds the coordinates to fill them unless they are a different colour than what the rest of the pixels originally were.
                       
                       
                
                    
                    
                    

            elif tool=="line" and mb[0]==1:
                screen.blit(screencopy,(0,0)) #Shows the line being dragged.
                draw.line(screen,draw_col,(sx,sy),(mx,my),size2) #Draws the line.

         
                

    elif page==page2:
        #Selecting stamps
        if sharingan_rect.collidepoint(mx,my) and mb[0]==1:
            
            screen.set_clip(orange_rect)
            stamp="sharingan"
            #Creates a yellow background for the stamps by redrawing all of them and adding a yellow rectangle for the selected stamp
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),dark_rect)
            
            draw.rect(screen,(255,255,255),sharingan_rect)
            draw.rect(screen,(255,255,255),headband_rect)
            draw.rect(screen,(255,255,255),rinnegan_rect)
            draw.rect(screen,(255,255,255),kunai_rect)
            draw.rect(screen,(255,255,255),byakugan_rect)
            draw.rect(screen,(255,255,255),shuriken_rect)
            draw.rect(screen,(255,255,255),rasengan_rect)
            draw.rect(screen,(255,255,255),chidori_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
            draw.line(screen,(0,0,0),(75,138),(125,138),7)

            screen.blit(headband_pic,(-115,70))
            screen.blit(rinnegan_pic,(0,155))
            screen.blit(kunai_pic,(-212,24))
            screen.blit(byakugan_pic,(-48,182))
            screen.blit(shuriken_pic,(-40,260))
            screen.blit(rasengan_pic,(-213,153))
            screen.blit(chidori_pic,(-20,289))
            screen.blit(rightarrow,(0,400))
            #The yellow rectangle.
            draw.rect(screen,(255,255,0),sharingan_rect)
            screen.blit(sharingan_pic,(-410,-330))
            screen.set_clip(None)
            
                
                
        elif headband_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="headband"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),dark_rect)
    
            draw.rect(screen,(255,255,255),sharingan_rect)
            draw.rect(screen,(255,255,255),headband_rect)
            draw.rect(screen,(255,255,255),rinnegan_rect)
            draw.rect(screen,(255,255,255),kunai_rect)
            draw.rect(screen,(255,255,255),byakugan_rect)
            draw.rect(screen,(255,255,255),shuriken_rect)
            draw.rect(screen,(255,255,255),rasengan_rect)
            draw.rect(screen,(255,255,255),chidori_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
            draw.line(screen,(0,0,0),(75,138),(125,138),7)


            screen.blit(sharingan_pic,(-410,-330))
            screen.blit(rinnegan_pic,(0,155))
            screen.blit(kunai_pic,(-212,24))
            screen.blit(byakugan_pic,(-48,182))
            screen.blit(shuriken_pic,(-40,260))
            screen.blit(rasengan_pic,(-213,153))
            screen.blit(chidori_pic,(-20,289))
            screen.blit(rightarrow,(0,400))

            draw.rect(screen,(255,255,0),headband_rect)
            screen.blit(headband_pic,(-115,70))
            
            
        elif rinnegan_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="rinnegan"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),dark_rect)
           
            draw.rect(screen,(255,255,255),sharingan_rect)
            draw.rect(screen,(255,255,255),headband_rect)
            draw.rect(screen,(255,255,255),rinnegan_rect)
            draw.rect(screen,(255,255,255),kunai_rect)
            draw.rect(screen,(255,255,255),byakugan_rect)
            draw.rect(screen,(255,255,255),shuriken_rect)
            draw.rect(screen,(255,255,255),rasengan_rect)
            draw.rect(screen,(255,255,255),chidori_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
            draw.line(screen,(0,0,0),(75,138),(125,138),7)

            screen.blit(sharingan_pic,(-410,-330))
            screen.blit(headband_pic,(-115,70))
            screen.blit(kunai_pic,(-212,24))
            screen.blit(byakugan_pic,(-48,182))
            screen.blit(shuriken_pic,(-40,260))
            screen.blit(rasengan_pic,(-213,153))
            screen.blit(chidori_pic,(-20,289))
            screen.blit(rightarrow,(0,400))

            draw.rect(screen,(255,255,0),rinnegan_rect)
            screen.blit(rinnegan_pic,(0,155))
            
        elif kunai_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="kunai"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),dark_rect)
           
            draw.rect(screen,(255,255,255),sharingan_rect)
            draw.rect(screen,(255,255,255),headband_rect)
            draw.rect(screen,(255,255,255),rinnegan_rect)
            draw.rect(screen,(255,255,255),kunai_rect)
            draw.rect(screen,(255,255,255),byakugan_rect)
            draw.rect(screen,(255,255,255),shuriken_rect)
            draw.rect(screen,(255,255,255),rasengan_rect)
            draw.rect(screen,(255,255,255),chidori_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
            draw.line(screen,(0,0,0),(75,138),(125,138),7)

            screen.blit(sharingan_pic,(-410,-330))
            screen.blit(headband_pic,(-115,70))
            screen.blit(rinnegan_pic,(0,155))
            screen.blit(byakugan_pic,(-48,182))
            screen.blit(shuriken_pic,(-40,260))
            screen.blit(rasengan_pic,(-213,153))
            screen.blit(chidori_pic,(-20,289))
            screen.blit(rightarrow,(0,400))

            draw.rect(screen,(255,255,0),kunai_rect)
            screen.blit(kunai_pic,(-212,24))
            
        elif byakugan_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="byakugan"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),dark_rect)
        
            draw.rect(screen,(255,255,255),sharingan_rect)
            draw.rect(screen,(255,255,255),headband_rect)
            draw.rect(screen,(255,255,255),rinnegan_rect)
            draw.rect(screen,(255,255,255),kunai_rect)
            draw.rect(screen,(255,255,255),byakugan_rect)
            draw.rect(screen,(255,255,255),shuriken_rect)
            draw.rect(screen,(255,255,255),rasengan_rect)
            draw.rect(screen,(255,255,255),chidori_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
            draw.line(screen,(0,0,0),(75,138),(125,138),7)

            screen.blit(sharingan_pic,(-410,-330))
            screen.blit(headband_pic,(-115,70))
            screen.blit(rinnegan_pic,(0,155))
            screen.blit(kunai_pic,(-212,24))
            screen.blit(shuriken_pic,(-40,260))
            screen.blit(rasengan_pic,(-213,153))
            screen.blit(chidori_pic,(-20,289))
            screen.blit(rightarrow,(0,400))

            draw.rect(screen,(255,255,0),byakugan_rect)
            screen.blit(byakugan_pic,(-48,182))
            
        elif shuriken_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="shuriken"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),dark_rect)
     
            draw.rect(screen,(255,255,255),sharingan_rect)
            draw.rect(screen,(255,255,255),headband_rect)
            draw.rect(screen,(255,255,255),rinnegan_rect)
            draw.rect(screen,(255,255,255),kunai_rect)
            draw.rect(screen,(255,255,255),byakugan_rect)
            draw.rect(screen,(255,255,255),shuriken_rect)
            draw.rect(screen,(255,255,255),rasengan_rect)
            draw.rect(screen,(255,255,255),chidori_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
            draw.line(screen,(0,0,0),(75,138),(125,138),7)

            screen.blit(sharingan_pic,(-410,-330))
            screen.blit(headband_pic,(-115,70))
            screen.blit(rinnegan_pic,(0,155))
            screen.blit(kunai_pic,(-212,24))
            screen.blit(byakugan_pic,(-48,182))
            screen.blit(rasengan_pic,(-213,153))
            screen.blit(chidori_pic,(-20,289))
            screen.blit(rightarrow,(0,400))

            draw.rect(screen,(255,255,0),shuriken_rect)
            screen.blit(shuriken_pic,(-40,260))
            
        elif rasengan_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="rasengan"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),dark_rect)
            
            draw.rect(screen,(255,255,255),sharingan_rect)
            draw.rect(screen,(255,255,255),headband_rect)
            draw.rect(screen,(255,255,255),rinnegan_rect)
            draw.rect(screen,(255,255,255),kunai_rect)
            draw.rect(screen,(255,255,255),byakugan_rect)
            draw.rect(screen,(255,255,255),shuriken_rect)
            draw.rect(screen,(255,255,255),rasengan_rect)
            draw.rect(screen,(255,255,255),chidori_rect)
            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
            draw.line(screen,(0,0,0),(75,138),(125,138),7)

            screen.blit(sharingan_pic,(-410,-330))
            screen.blit(headband_pic,(-115,70))
            screen.blit(rinnegan_pic,(0,155))
            screen.blit(kunai_pic,(-212,24))
            screen.blit(byakugan_pic,(-48,182))
            screen.blit(shuriken_pic,(-40,260))
            screen.blit(chidori_pic,(-20,289))
            screen.blit(rightarrow,(0,400))

            draw.rect(screen,(255,255,0),rasengan_rect)
            screen.blit(rasengan_pic,(-213,153))
            
        elif chidori_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="chidori"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),dark_rect)
         
            draw.rect(screen,(255,255,255),sharingan_rect)
            draw.rect(screen,(255,255,255),headband_rect)
            draw.rect(screen,(255,255,255),rinnegan_rect)
            draw.rect(screen,(255,255,255),kunai_rect)
            draw.rect(screen,(255,255,255),byakugan_rect)
            draw.rect(screen,(255,255,255),shuriken_rect)
            draw.rect(screen,(255,255,255),rasengan_rect)
            draw.rect(screen,(255,255,255),chidori_rect)
            
            
            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
            draw.line(screen,(0,0,0),(75,138),(125,138),7)

            screen.blit(sharingan_pic,(-410,-330))
            screen.blit(headband_pic,(-115,70))
            screen.blit(rinnegan_pic,(0,155))
            screen.blit(kunai_pic,(-212,24))
            screen.blit(byakugan_pic,(-48,182))
            screen.blit(shuriken_pic,(-40,260))
            screen.blit(rasengan_pic,(-213,153))
            screen.blit(rightarrow,(0,400))

            draw.rect(screen,(255,255,0),chidori_rect)
            screen.blit(chidori_pic,(-20,289))
            
            
        if canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            stamps=True
            #Blitting pictures to place them in appropriate positions.
            if stamp=="headband" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                screen.blit(headband_pic,(mx-120,my-100))
            elif stamp=="sharingan" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                screen.blit(sharingan_pic,(mx-520,my-490))
            elif stamp=="kunai" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                screen.blit(kunai_pic,(mx-250,my-200))
            elif stamp=="rinnegan" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                screen.blit(rinnegan_pic,(mx-100,my-100))
            elif stamp=="shuriken" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                screen.blit(shuriken_pic,(mx-50,my-50))
            elif stamp=="byakugan" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                screen.blit(byakugan_pic,(mx-150,my-150))
            elif stamp=="rasengan" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                screen.blit(rasengan_pic,(mx-250,my-250))
            elif stamp=="chidori" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                screen.blit(chidori_pic,(mx-100,my-130))


    elif page==page3:
        #Selecting stamps. Same process as before with the yellows backgrounds.
        if toad_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="toad"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),black_rect)
            draw.rect(screen,(255,255,255),toad_rect)
            draw.rect(screen,(255,255,255),snake_rect)
            draw.rect(screen,(255,255,255),slug_rect)
            draw.rect(screen,(255,255,255),gamakichi_rect)
            draw.rect(screen,(255,255,255),kyuubi_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
    
            screen.blit(snake_pic,(-380,30))
            screen.blit(slug_pic,(-250,80))
            screen.blit(gamakichi_pic,(-185,180))
            screen.blit(kyuubi_pic,(-130,255))
            screen.blit(leftarrow,(-10,445))

            draw.rect(screen,(255,255,0),toad_rect)
            screen.blit(toad_pic,(-340,-305))
            
        elif snake_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="snake"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),black_rect)
            draw.rect(screen,(255,255,255),toad_rect)
            draw.rect(screen,(255,255,255),snake_rect)
            draw.rect(screen,(255,255,255),slug_rect)
            draw.rect(screen,(255,255,255),gamakichi_rect)
            draw.rect(screen,(255,255,255),kyuubi_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
        
            screen.blit(toad_pic,(-340,-305))
            screen.blit(slug_pic,(-250,80))
            screen.blit(gamakichi_pic,(-185,180))
            screen.blit(kyuubi_pic,(-130,255))
            screen.blit(leftarrow,(-10,445))

            draw.rect(screen,(255,255,0),snake_rect)
            screen.blit(snake_pic,(-380,30))
            
        elif slug_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="slug"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),black_rect)
            draw.rect(screen,(255,255,255),toad_rect)
            draw.rect(screen,(255,255,255),snake_rect)
            draw.rect(screen,(255,255,255),slug_rect)
            draw.rect(screen,(255,255,255),gamakichi_rect)
            draw.rect(screen,(255,255,255),kyuubi_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
        
            screen.blit(toad_pic,(-340,-305))
            screen.blit(snake_pic,(-380,30))
            screen.blit(gamakichi_pic,(-185,180))
            screen.blit(kyuubi_pic,(-130,255))
            screen.blit(leftarrow,(-10,445))

            draw.rect(screen,(255,255,0),slug_rect)
            screen.blit(slug_pic,(-250,80))
            
        elif gamakichi_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="gamakichi"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),black_rect)
            draw.rect(screen,(255,255,255),toad_rect)
            draw.rect(screen,(255,255,255),snake_rect)
            draw.rect(screen,(255,255,255),slug_rect)
            draw.rect(screen,(255,255,255),gamakichi_rect)
            draw.rect(screen,(255,255,255),kyuubi_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
        
            screen.blit(toad_pic,(-340,-305))
            screen.blit(snake_pic,(-380,30))
            screen.blit(slug_pic,(-250,80))
            screen.blit(kyuubi_pic,(-130,255))
            screen.blit(leftarrow,(-10,445))

            draw.rect(screen,(255,255,0),gamakichi_rect)
            screen.blit(gamakichi_pic,(-185,180))
            
        elif kyuubi_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            stamp="kyuubi"
            draw.rect(screen,(255,128,64),orange_rect)
            draw.rect(screen,(0,0,0),black_rect)
            draw.rect(screen,(255,255,255),toad_rect)
            draw.rect(screen,(255,255,255),snake_rect)
            draw.rect(screen,(255,255,255),slug_rect)
            draw.rect(screen,(255,255,255),gamakichi_rect)
            draw.rect(screen,(255,255,255),kyuubi_rect)

            draw.rect(screen,(255,255,255),tools_rect)
            draw.rect(screen,(255,255,255),stamps_rect)
            screen.blit(stamps_pic,(75,88))
            screen.blit(tools_pic,(20,95))
        
            screen.blit(toad_pic,(-340,-305))
            screen.blit(snake_pic,(-380,30))
            screen.blit(slug_pic,(-250,80))
            screen.blit(gamakichi_pic,(-185,180))
            screen.blit(leftarrow,(-10,445))

            draw.rect(screen,(255,255,0),kyuubi_rect)
            screen.blit(kyuubi_pic,(-130,255))

        if canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            stamps=True
            if stamp=="toad" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                resize=transform.scale(toad_pic,(size,size1)) #Resizes the image
                screen.blit(resize,(mx-size//2,my-size1//2)) #Blits the image so it can properly be resized when the size is changed.
               
            elif stamp=="snake" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                resize=transform.scale(snake_pic,(size,size1))
                screen.blit(resize,(mx-size//2,my-size1//2))
               
            elif stamp=="slug" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                resize=transform.scale(slug_pic,(size,size1))
                screen.blit(resize,(mx-size//2,my-size1//2))
        
            elif stamp=="gamakichi" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                resize=transform.scale(gamakichi_pic,(size,size1))
                screen.blit(resize,(mx-size//2,my-size1//2))
             
            elif stamp=="kyuubi" and mb[0]==1:
                screen.blit(screencopy,(0,0))
                resize=transform.scale(kyuubi_pic,(size,size1))
                screen.blit(resize,(mx-size//2,my-size1//2))
                

        
        

    elif page==page4:
        #Music plays when user clicks on the image.
        if akatsuki_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            for i in music:
                draw.rect(screen,(255,128,64),i,4)
            draw.rect(screen,(0,0,0),akatsuki_rect,5)
            mixer.music.load("Music/akatsuki.mp3")
            mixer.music.play()
        elif fox_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            for i in music:
                draw.rect(screen,(255,128,64),i,4)
            draw.rect(screen,(0,0,0),fox_rect,5)
            mixer.music.load("Music/demon fox.mp3")
            mixer.music.play()
        elif jinchuuriki_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            for i in music:
                draw.rect(screen,(255,128,64),i,4)
            draw.rect(screen,(0,0,0),jinchuuriki_rect,5)
            mixer.music.load("Music/jinchuuriki.mp3")
            mixer.music.play()
        elif theme_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            for i in music:
                draw.rect(screen,(255,128,64),i,4)
            draw.rect(screen,(0,0,0),theme_rect,5)
            mixer.music.load("Music/Heaven.mp3")
            mixer.music.play()
        elif orochimaru_rect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(orange_rect)
            for i in music:
                draw.rect(screen,(255,128,64),i,4)
            draw.rect(screen,(0,0,0),orochimaru_rect,5)
            mixer.music.load("Music/orochimaru.mp3")
            mixer.music.play()

    if click:
        #Description box
        screen.set_clip(blue_rect)
        description_txt=posfont2.render("Description",True,(255,0,0))
        screen.blit(cover4,(160,120))
        draw.rect(screen,(0,0,255),blue_rect)
        screen.blit(description_txt,(160,120))

    if page==page0:
        screen.set_clip(description_rect)
        description_txt=descriptionfont.render("This box gives you a description of",True,(0,0,255))#First line of text
        description_txt2=descriptionfont.render("everthing that happens in this paint",True,(0,0,255))#Second line of text
        description_txt3=descriptionfont.render("project",True,(0,0,255))#Third line of text.
        #screen.blit(cover3,(160,140))
        draw.rect(screen,(255,0,0),description_rect)
        #Blits all the text to the screen.
        screen.blit(description_txt,(160,140))
        screen.blit(description_txt2,(160,155))
        screen.blit(description_txt3,(160,170))

    #Text for all the tools.
                        
    if tool=="pencil":
        screen.set_clip(description_rect)
        pencil_txt=descriptionfont.render("The pencil tool allows you to freely",True,(0,0,255))
        pencil_txt2=descriptionfont.render("draw inside the canvas",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(pencil_txt,(160,140))
        screen.blit(pencil_txt2,(160,155))

    elif tool=="eraser":
        screen.set_clip(description_rect)
        eraser_txt=descriptionfont.render("The eraser tool allows you to erase",True,(0,0,255))
        eraser_txt2=descriptionfont.render("images,backgrounds,drawings,etc.",True,(0,0,255))
        eraser_txt3=descriptionfont.render("It is very useful for erasing small",True,(0,0,255))
        eraser_txt4=descriptionfont.render("details",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(eraser_txt,(160,140))
        screen.blit(eraser_txt2,(160,155))
        screen.blit(eraser_txt3,(160,170))
        screen.blit(eraser_txt4,(160,185))

    elif tool=="spraypaint":
        screen.set_clip(description_rect)
        spray_txt=descriptionfont.render("The spraypaint tool allows you to",True,(0,0,255))
        spray_txt2=descriptionfont.render("replicate a spraypaintcan by",True,(0,0,255))
        spray_txt3=descriptionfont.render("continously filling the screen with",True,(0,0,255))
        spray_txt4=descriptionfont.render("small dots.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(spray_txt,(160,140))
        screen.blit(spray_txt2,(160,155))
        screen.blit(spray_txt3,(160,170))
        screen.blit(spray_txt4,(160,185))

    elif tool=="brush":
        screen.set_clip(description_rect)
        brush_txt=descriptionfont.render("A brush is a larger version of the",True,(0,0,255))
        brush_txt2=descriptionfont.render("pencilthat is much thicker.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(brush_txt,(160,140))
        screen.blit(brush_txt2,(160,155))

    elif tool=="rectangle":
        screen.set_clip(description_rect)
        rectangle_txt=descriptionfont.render("Allows you to drag and place a",True,(0,0,255))
        rectangle_txt2=descriptionfont.render("rectangle.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(rectangle_txt,(160,140))
        screen.blit(rectangle_txt2,(160,155))

    elif tool=="ellipse":
        screen.set_clip(description_rect)
        ellipse_txt=descriptionfont.render("Allows you to drag and place an",True,(0,0,255))
        ellipse_txt2=descriptionfont.render("ellipse",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(ellipse_txt,(160,140))
        screen.blit(ellipse_txt2,(160,155))

    elif tool=="filled rectangle":
        screen.set_clip(description_rect)
        frectangle_txt=descriptionfont.render("Allows you to drag and place a",True,(0,0,255))
        frectangle_txt2=descriptionfont.render("filled rectangle.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(frectangle_txt,(160,140))
        screen.blit(frectangle_txt2,(160,155))

    elif tool=="filled ellipse":
        screen.set_clip(description_rect)
        fellipse_txt=descriptionfont.render("Allows you to drag and place a",True,(0,0,255))
        fellipse_txt2=descriptionfont.render("filled ellipse.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(fellipse_txt,(160,140))
        screen.blit(fellipse_txt2,(160,155))

    elif tool=="eyedrop":
        screen.set_clip(description_rect)
        drop_txt=descriptionfont.render("Changes the colour when you click",True,(0,0,255))
        drop_txt2=descriptionfont.render("on the canvas area.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(drop_txt,(160,140))
        screen.blit(drop_txt2,(160,155))

    elif tool=="line":
        screen.set_clip(description_rect)
        line_txt=descriptionfont.render("Allows you to drag and place a line.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(line_txt,(160,140))

    elif tool=="fill":
        screen.set_clip(description_rect)
        fill_txt=descriptionfont.render("Fills shapes and objects on the",True,(0,0,255))
        fill_txt2=descriptionfont.render("canvas.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(fill_txt,(160,140))
        screen.blit(fill_txt2,(160,155))

    elif tool=="trash":
        screen.set_clip(description_rect)
        trash_txt=descriptionfont.render("Clears the page.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(trash_txt,(160,140))

    elif tool=="undo":
        screen.set_clip(description_rect)
        undo_txt=descriptionfont.render("Allows you to remove your previous",True,(0,0,255))
        undo_txt2=descriptionfont.render("actions",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(undo_txt,(160,140))
        screen.blit(undo_txt2,(160,155))

    elif tool=="redo":
        screen.set_clip(description_rect)
        redo_txt=descriptionfont.render("Pressed undo too many times.",True,(0,0,255))
        redo_txt2=descriptionfont.render("Use the redo features to go back",True,(0,0,255))
        redo_txt3=descriptionfont.render("to your original screen.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(redo_txt,(160,140))
        screen.blit(redo_txt2,(160,155))
        screen.blit(redo_txt3,(160,170))
    

    #Text for all the stamps.
        
    if stamp=="headband":
        screen.set_clip(description_rect)
        headband_txt=descriptionfont.render("What village are you from? Choose your",True,(0,0,255))
        headband_txt2=descriptionfont.render("your headband to represent that",True,(0,0,255))
        headband_txt3=descriptionfont.render("village!",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(headband_txt,(160,140))
        screen.blit(headband_txt2,(160,155))
        screen.blit(headband_txt3,(160,170))

    if stamp=="sharingan":
        screen.set_clip(description_rect)
        sharingan_txt=descriptionfont.render("Awaken your sharingan to gain",True,(0,0,255))
        sharingan_txt2=descriptionfont.render("power and one day you will evolve to get",True,(0,0,255))
        sharingan_txt3=descriptionfont.render("a mangekyou sharingan.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(sharingan_txt,(160,140))
        screen.blit(sharingan_txt2,(160,155))
        screen.blit(sharingan_txt3,(160,170))

    if stamp=="kunai":
        screen.set_clip(description_rect)
        kunai_txt=descriptionfont.render("Use your kunai, one of the most",True,(0,0,255))
        kunai_txt2=descriptionfont.render("important ninja tools that can be",True,(0,0,255))
        kunai_txt3=descriptionfont.render("dangerous when used properly.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(kunai_txt,(160,140))
        screen.blit(kunai_txt2,(160,155))
        screen.blit(kunai_txt3,(160,170))

    
    if stamp=="rinnegan":
        screen.set_clip(description_rect)
        rinnegan_txt=descriptionfont.render("The extremely dangerous jutsu that",True,(0,0,255))
        rinnegan_txt2=descriptionfont.render("was originally held by the sage of",True,(0,0,255))
        rinnegan_txt3=descriptionfont.render("the six paths.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(rinnegan_txt,(160,140))
        screen.blit(rinnegan_txt2,(160,155))
        screen.blit(rinnegan_txt3,(160,170))

    if stamp=="shuriken":
        screen.set_clip(description_rect)
        shuriken_txt=descriptionfont.render("Another ninja tool that is quite",True,(0,0,255))
        shuriken_txt2=descriptionfont.render("commonly used. It can be effective",True,(0,0,255))
        shuriken_txt3=descriptionfont.render("when used correctly.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(shuriken_txt,(160,140))
        screen.blit(shuriken_txt2,(160,155))
        screen.blit(shuriken_txt3,(160,170))

    if stamp=="byakugan":
        screen.set_clip(description_rect)
        byakugan_txt=descriptionfont.render("This jutsu was passed on by the",True,(0,0,255))
        byakugan_txt2=descriptionfont.render("Hyuuga clan. It is very effective",True,(0,0,255))
        byakugan_txt3=descriptionfont.render("during hand to hand combat.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(byakugan_txt,(160,140))
        screen.blit(byakugan_txt2,(160,155))
        screen.blit(byakugan_txt3,(160,170))

    if stamp=="rasengan":
        screen.set_clip(description_rect)
        rasengan_txt=descriptionfont.render("An extremely hard jutsu to learn but",True,(0,0,255))
        rasengan_txt2=descriptionfont.render("it can be verypowerful and",True,(0,0,255))
        rasengan_txt3=descriptionfont.render("dangerous when you have",True,(0,0,255))
        rasengan_txt4=descriptionfont.render("mastered it.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(rasengan_txt,(160,140))
        screen.blit(rasengan_txt2,(160,155))
        screen.blit(rasengan_txt3,(160,170))
        screen.blit(rasengan_txt4,(160,185))

    if stamp=="chidori":
        screen.set_clip(description_rect)
        chidori_txt=descriptionfont.render("A lightning blade that can pierce",True,(0,0,255))
        chidori_txt2=descriptionfont.render("through almost anything.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(chidori_txt,(160,140))
        screen.blit(chidori_txt2,(160,155))

    if stamp=="toad":
        screen.set_clip(description_rect)
        toad_txt=descriptionfont.render("Hey! I am the boss toad around",True,(0,0,255))
        toad_txt2=descriptionfont.render("here! Call me Gambuta.",True,(0,0,255))
        draw.rect(screen,(255,0,0),description_rect)
        screen.blit(toad_txt,(160,140))
        screen.blit(toad_txt2,(160,155))

    if stamp=="snake":
        screen.set_clip(description_rect)
        snake_txt=descriptionfont.render("Hiss! Hiss! I am orochimaru's first",True,(0,0,255))
        snake_txt2=descriptionfont.render("pet, the legendary Manda.",True,(0,0,255))
        draw.rect(screen,(255,0,0,),description_rect)
        screen.blit(snake_txt,(160,140))
        screen.blit(snake_txt2,(160,155))

    if stamp=="slug":
        screen.set_clip(description_rect)
        slug_txt=descriptionfont.render("I am one of Tsunade's slugs that",True,(0,0,255))
        slug_txt2=descriptionfont.render("has tremendous healing abilities.",True,(0,0,255))
        draw.rect(screen,(255,0,0,),description_rect)
        screen.blit(slug_txt,(160,140))
        screen.blit(slug_txt2,(160,155))

    if stamp=="gamakichi":
        screen.set_clip(description_rect)
        gamakichi_txt=descriptionfont.render("Yo! I am Gambuta's son. Don't",True,(0,0,255))
        gamakichi_txt2=descriptionfont.render("underestimate me!",True,(0,0,255))
        draw.rect(screen,(255,0,0,),description_rect)
        screen.blit(gamakichi_txt,(160,140))
        screen.blit(gamakichi_txt2,(160,155))

    if stamp=="kyuubi":
        screen.set_clip(description_rect)
        kyubi_txt=descriptionfont.render("ROAR! Don't come near me or I will",True,(0,0,255))
        kyubi_txt2=descriptionfont.render("eat you up. Why do I have to be",True,(0,0,255))
        kyubi_txt3=descriptionfont.render("sealed inside this Naruto idiot.",True,(0,0,255))
        draw.rect(screen,(255,0,0,),description_rect)
        screen.blit(kyubi_txt,(160,140))
        screen.blit(kyubi_txt2,(160,155))
        screen.blit(kyubi_txt3,(160,170))
                  
        
    bx=mx
    by=my

    
    display.flip()
font.quit()
quit()
