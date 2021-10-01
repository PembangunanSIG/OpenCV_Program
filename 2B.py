import PySimpleGUI as sg
import cv2


def foto(sumber):
    cv2.imwrite('hasil/PYSimpleGUI.png', sumber)

def webcam():
    ret, frame = cap.read()
    cv2.waitKey(25)
    return frame

layout = [
            [sg.Text('Aplikasi Kamera Sederhana', size=(40, 1), justification='center', font='Arial 20 bold', background_color='#FEA642', text_color='#42AFFE' )],
            [sg.Image(filename='', key='-WEBCAM-')],
            [sg.Button('Ambil Gambar', size=(20, 1), font='Arial 14 bold', button_color=('#42AFFE', '#E2C300')),
             sg.Button('Keluar', size=(10, 1), font='Arial 14 bold', button_color=('#42AFFE', '#E2C300'))]
         ]

window = sg.Window('Demo Application - Aplikasi Kamera',layout,background_color='#EFD64C').Finalize()

cap = cv2.VideoCapture(1)
while True:
    event, values = window.read(timeout=20)
    camera = webcam()
    if event == 'Ambil Gambar':
        foto(camera)
    elif event == 'Keluar'or event == sg.WIN_CLOSED:
        break
    imgbytes = cv2.imencode('.png', camera)[1].tobytes() 
    window['-WEBCAM-'].update(data=imgbytes)
