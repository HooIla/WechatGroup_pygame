import pygame
from pygame import surface

pygame.init()
pygame.mixer.init()
bg_size = (820,560)

screen = pygame.display.set_mode(bg_size)   #游戏主界面的尺寸
pygame.display.set_caption("The Guardians") #游戏窗体显示游戏名字
clock = pygame.time.Clock() #控制频率
start_screen = pygame.Surface(screen.get_size())    #开始界面的画布
start_screen2 = pygame.Surface(screen.get_size())   #选关界面的画布
about_screen = pygame.Surface(screen.get_size())    #关于界面的画布
help_screen = pygame.Surface(screen.get_size())     #帮助界面的画布

start_screen = start_screen.convert()   
start_screen2 = start_screen2.convert()             
about_screen2 = about_screen.convert()
help_screen = help_screen.convert()

pygame.mixer.music.load("./source/vol/bg_music.mp3")    #加载音乐
pygame.mixer.music.set_volume(0.1)                  #设置背景音乐音量
pygame.mixer.music.play(loops=-1)                   #播放音乐，-1为无线循环

#按键音效
touch_sound1 = pygame.mixer.Sound("./source/vol/touch2.mp3")
touch_sound2 = pygame.mixer.Sound("./source/vol/touch.mp3")
#设置按键音效音量
touch_sound1.set_volume(0.05)
touch_sound2.set_volume(0.05)
#加载各种图片
bg = pygame.image.load("./source/pic/interface/bg.png").convert_alpha()
bg_about = pygame.image.load("./source/pic/interface/bg_about2.png").convert_alpha()
name = pygame.image.load("./source/pic/interface/name.png").convert_alpha()
play1 = pygame.image.load("./source/pic/interface/play11.png").convert_alpha()
play2 = pygame.image.load("./source/pic/interface/play21.png").convert_alpha()
vol1 = pygame.image.load("./source/pic/interface/vol1.png").convert_alpha()
vol2 = pygame.image.load("./source/pic/interface/vol2.png").convert_alpha()
help1 = pygame.image.load("./source/pic/interface/help1.png").convert_alpha()
help2 = pygame.image.load("./source/pic/interface/help2.png").convert_alpha()
about1 = pygame.image.load("./source/pic/interface/about1.png").convert_alpha()
about2 = pygame.image.load("./source/pic/interface/about2.png").convert_alpha()
about3 = pygame.image.load("./source/pic/interface/about3.png").convert_alpha()
return1 = pygame.image.load("./source/pic/interface/return1.png").convert_alpha()
return2 = pygame.image.load("./source/pic/interface/return2.png").convert_alpha()
level11 = pygame.image.load("./source/pic/level/level11.png").convert_alpha()
level12 = pygame.image.load("./source/pic/level/level12.png").convert_alpha()
level21 = pygame.image.load("./source/pic/level/level21.png").convert_alpha()
level22 = pygame.image.load("./source/pic/level/level22.png").convert_alpha()
level31 = pygame.image.load("./source/pic/level/level31.png").convert_alpha()
level32 = pygame.image.load("./source/pic/level/level32.png").convert_alpha()


global vol_TF,surfaces
vol_TF = True
surfaces = {'n1': True, 'n2': False, 'n3': False, 'n4': False}
#n1为T——主界面
#n2为T——选关界面
#n3为T——关于界面（设计人员介绍）
#n4为T——帮助界面（游戏规则）
def set_sur(sur_str):
    for sur in surfaces:
        if sur != sur_str:
            surfaces[sur] = False
        else:
            surfaces[sur] = True
#主界面
while True:
    while surfaces["n1"]:
        clock.tick(30)  #刷新率30
        screen.blit(start_screen,(0,0))
        buttons = pygame.mouse.get_pressed()    #鼠标按键
        x1, y1 = pygame.mouse.get_pos()         #获取当前鼠标位置坐标

        #判断鼠标是否悬停在play按钮上面，产生'动态'按钮效果，以及相应的按键效果
        if play1.get_rect(x=300,y=350).collidepoint(pygame.mouse.get_pos()):
            start_screen.blit(play2,(300,350))
            if buttons[0]:
                touch_sound1.play()
                set_sur('n2')   #更改n2为T

        elif about1.get_rect(x=610,y=5).collidepoint(pygame.mouse.get_pos()):
        #判断鼠标是否悬停在'!'按钮上面，产生'动态'按钮效果，以及相应的按键效果
            start_screen.blit(about2,(610,5))
            if buttons[0]:
                touch_sound2.play()
                set_sur('n3')   #更改n3为T

        elif help1.get_rect(x=680,y=5).collidepoint(pygame.mouse.get_pos()):
        #判断鼠标是否悬停在'?'按钮上面，产生'动态'按钮效果，以及相应的按键效果
            start_screen.blit(help2,(680,5))
            if buttons[0]:
                touch_sound2.play()
                set_sur('n4')   #更改n3为T

        else:
            start_screen.blit(bg,(0,0))
            start_screen.blit(name,(20,0))
            start_screen.blit(help1,(680,5))
            start_screen.blit(about1,(610,5))
            start_screen.blit(play1,(300,350))
            if vol_TF:
                #背景音乐播放
                start_screen.blit(vol1,(750,5))
                pygame.mixer.music.unpause()
            else:
                #背景音乐暂停
                start_screen.blit(vol2,(750,5))
                pygame.mixer.music.pause()
        pygame.display.update()

        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出")
                pygame.quit()
                exit()
            if vol1.get_rect(x=750,y=5).collidepoint(pygame.mouse.get_pos()):
                if vol_TF:
                    #音乐按钮播放
                    start_screen.blit(vol1,(750,5))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        vol_TF = False
                else:
                    #音乐暂停播放
                    start_screen.blit(vol2,(750,5))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        vol_TF = True

    while surfaces["n2"]:   #选关界面
        clock.tick(30)
        screen.blit(start_screen2,(0,0))
        start_screen2.blit(bg,(0,0))
        start_screen2.blit(return1,(20,10))
        start_screen2.blit(level11,(190,250))
        start_screen2.blit(level21,(360,250))
        start_screen2.blit(level31,(530,250))

        buttons = pygame.mouse.get_pressed()
        x2, y2 = pygame.mouse.get_pos()

        if return1.get_rect(x=20,y=10).collidepoint(pygame.mouse.get_pos()):
        #判断鼠标是否悬停在'返回'按钮上面，产生'动态'按钮效果，以及相应的按键效果
            start_screen2.blit(return2,(20,10))
            if buttons[0]:
                touch_sound2.play()
                set_sur('n1')
        elif level11.get_rect(x=190,y=250).collidepoint(pygame.mouse.get_pos()):
            #第一关
            if buttons[0]:
                touch_sound1.play()
                #TODO:  这里调用第一关
            start_screen2.blit(level12,(190,250))
        elif level21.get_rect(x=360,y=250).collidepoint(pygame.mouse.get_pos()):
            #第二关
            if buttons[0]:
                touch_sound1.play()
                #TODO:  这里调用第二关
            start_screen2.blit(level22,(360,250))
        elif level31.get_rect(x=530,y=250).collidepoint(pygame.mouse.get_pos()):
            #第三关
            if buttons[0]:
                touch_sound1.play()
                #TODO:  这里调用第三关
            start_screen2.blit(level32,(530,250))
        pygame.display.update()

        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出")
                pygame.quit()
                exit()
        
    while surfaces["n3"]:   #关于界面
        clock.tick(30)
        screen.blit(about_screen,(0,0))
        about_screen.blit(bg_about,(0,0))
        about_screen.blit(return1,(20,10))
        about_screen.blit(about3,(220,0))
        buttons = pygame.mouse.get_pressed()
        x3, y3 = pygame.mouse.get_pos()

        if return1.get_rect(x=20,y=10).collidepoint(pygame.mouse.get_pos()):
        #判断鼠标是否悬停在'返回'按钮上面，产生'动态'按钮效果，以及相应的按键效果
            about_screen.blit(return2,(20,10))
            if buttons[0]:
                touch_sound2.play()
                set_sur('n1')
        pygame.display.update()

        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出")
                pygame.quit()
                exit()

    while surfaces["n4"]:   #帮助界面   里面还没写游戏规则，等我知道了我们的游戏的规则就加上去
        clock.tick(30)
        screen.blit(help_screen,(0,0))
        help_screen.blit(bg_about,(0,0))
        help_screen.blit(return1,(20,10))
        buttons = pygame.mouse.get_pressed()
        x4, y4 = pygame.mouse.get_pos()

        if return1.get_rect(x=20,y=10).collidepoint(pygame.mouse.get_pos()):
        #判断鼠标是否悬停在'返回'按钮上面，产生'动态'按钮效果，以及相应的按键效果
            help_screen.blit(return2,(20,10))
            if buttons[0]:
                touch_sound2.play()
                set_sur('n1')
        pygame.display.update()

        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出")
                pygame.quit()
                exit()