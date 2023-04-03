import PySimpleGUI as sg
import qrcode


layout = [
    [sg.Text('Enter text to encode ',text_color='black',background_color='white',)],
    [sg.InputText(key='INPUT'),sg.Button('Generate',button_color='blue')],
    [sg.Image(key='image')]

]

window = sg.Window('GENRATOR FOR QRCODE', layout,background_color='gold')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Generate':
        text = values['INPUT']
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")
        window['image'].update('qrcode.png')

window.close()