import PySimpleGUI as psg
from playsound import playsound
biskuvi_png = 'biskuvi.png'
krema_png = 'krema.png'
#140 55

psg.LOOK_AND_FEEL_TABLE['Dark_Minimalist'] = {'BACKGROUND': '#212324', 
                                        'TEXT': '#FFFFFF', 
                                        'INPUT': '#454545', 
                                        'TEXT_INPUT': '#FFFFFF', 
                                        'SCROLL': '#FFFFFF', 
                                        'BUTTON': ('#FFFFFF', '#454545'), 
                                        'PROGRESS': ('#FFFFFF', '#FFFFFF'), 
                                        'BORDER': 0, 'SLIDER_DEPTH': 0,  
                                        'PROGRESS_DEPTH': 0, } 
psg.theme('Dark_Minimalist')

layout = [[psg.Button(' ', visible=False), psg.Text('OREO JENERATÖRÜ' + 80*' '), psg.Button('X', button_color=('#FFFFFF', '#212324'))],
          [psg.Text('1. katman:'), psg.DropDown(['Bisküvi', 'Krema'], key='katman1'), psg.Text('2. katman:'), psg.DropDown(['Bisküvi', 'Krema'], key='katman2'), psg.Text('3. katman:'), psg.DropDown(['Bisküvi', 'Krema'], key='katman3')],
          [psg.Text('4. katman:'), psg.DropDown(['Bisküvi', 'Krema'], key='katman4'), psg.Text('5. katman:'), psg.DropDown(['Bisküvi', 'Krema'], key='katman5'), psg.Text('6. katman:'), psg.DropDown(['Bisküvi', 'Krema'], key='katman6')],
          [psg.Text('7. katman:'), psg.DropDown(['Bisküvi', 'Krema'], key='katman7'), psg.Text('8. katman:'), psg.DropDown(['Bisküvi', 'Krema'], key='katman8'), psg.Text('9. katman:'), psg.DropDown(['Bisküvi', 'Krema'], key='katman9')],
          [psg.Button('Oluştur')],
          [psg.Text(40*' '), psg.Image(key='img1')],
          [psg.Text(40*' '), psg.Image(key='img2')],
          [psg.Text(40*' '), psg.Image(key='img3')],
          [psg.Text(40*' '), psg.Image(key='img4')],
          [psg.Text(40*' '), psg.Image(key='img5')],
          [psg.Text(40*' '), psg.Image(key='img6')],
          [psg.Text(40*' '), psg.Image(key='img7')],
          [psg.Text(40*' '), psg.Image(key='img8')],
          [psg.Text(40*' '), psg.Image(key='img9')]]
 
main_window = psg.Window('main_menu', layout, size=(500,700), grab_anywhere=True, no_titlebar=True)

while True:
    event, values = main_window.read()
    katman1 = values['katman1']
    katman2 = values['katman2']
    katman3 = values['katman3']
    katman4 = values['katman4']
    katman5 = values['katman5']
    katman6 = values['katman6']
    katman7 = values['katman7']
    katman8 = values['katman8']
    katman9 = values['katman9']

    if event == 'X':
        break

    if katman1 == 'Bisküvi':
        main_window['img1'].update(filename=biskuvi_png)
        playsound('o.mp3')
    if katman1 == 'Krema':
        main_window['img1'].update(filename=krema_png)
        playsound('re.mp3')

    if katman2 == 'Bisküvi':
        main_window['img2'].update(filename=biskuvi_png)
        playsound('o.mp3')
    if katman2 == 'Krema':
        main_window['img2'].update(filename=krema_png)
        playsound('re.mp3')

    if katman3 == 'Bisküvi':
        main_window['img3'].update(filename=biskuvi_png)
        playsound('o.mp3')
    if katman3 == 'Krema':
        main_window['img3'].update(filename=krema_png)
        playsound('re.mp3')

    if katman4 == 'Bisküvi':
        main_window['img4'].update(filename=biskuvi_png)
        playsound('o.mp3')
    if katman4 == 'Krema':
        main_window['img4'].update(filename=krema_png)
        playsound('re.mp3')

    if katman5 == 'Bisküvi':
        main_window['img5'].update(filename=biskuvi_png)
        playsound('o.mp3')
    if katman5 == 'Krema':
        main_window['img5'].update(filename=krema_png)
        playsound('re.mp3')
        
    if katman6 == 'Bisküvi':
        main_window['img6'].update(filename=biskuvi_png)
        playsound('o.mp3')
    if katman6 == 'Krema':
        main_window['img6'].update(filename=krema_png)
        playsound('re.mp3')
        
    if katman7 == 'Bisküvi':
        main_window['img7'].update(filename=biskuvi_png)
        playsound('o.mp3')
    if katman7 == 'Krema':
        main_window['img7'].update(filename=krema_png)
        playsound('re.mp3')

    if katman8 == 'Bisküvi':
        main_window['img8'].update(filename=biskuvi_png)
        playsound('o.mp3')
    if katman8 == 'Krema':
        main_window['img8'].update(filename=krema_png)
        playsound('re.mp3')

    if katman9 == 'Bisküvi':
        main_window['img9'].update(filename=biskuvi_png)
        playsound('o.mp3')
    if katman9 == 'Krema':
        main_window['img9'].update(filename=krema_png)
        playsound('re.mp3')