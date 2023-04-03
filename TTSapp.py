import PySimpleGUI as sg
import pyttsx3

TTS_ENGINE = pyttsx3.init()
VOICES = TTS_ENGINE.getProperty('voices')



layout = [    [sg.Text('Select voice:',text_color='black',background_color='red'),
               sg.Radio('Male', 'RADIO1', default=True, key='male',background_color='gold'),
               sg.Radio('Female', 'RADIO1', key='female',background_color='green')],
     [sg.Text('Enter text to speak:',text_color='black',background_color='gold',)],
          
    [sg.InputText(key='input'),sg.Button('Speak',button_color='blue')],
   
    
]

window = sg.Window('TEXT TO SPEECH CONVETOR', layout,background_color='blue')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        if values['male']:
            TTS_ENGINE.setProperty('voice', VOICES[0].id)
        elif values['female']:
           TTS_ENGINE.setProperty('voice', VOICES[1].id) 
    
        TTS_ENGINE.say(text)
        TTS_ENGINE.runAndWait()

window.close()