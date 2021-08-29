'''
Created on Aug 28, 2021

@author: lon
'''
import PySimpleGUI as sg

'''
GUI for inputlocations to retrieve user int input
'''
def inputlocation_intgui():
    #window contents
    layout = [[sg.Text('Enter the amount of addresses:')],
              [sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    #creates window
    window = sg.Window('Test', layout)
    
    event, values = window.read()
        
    window.close()
    
    #return values
'''
GUI interactions to retrieve user address input
'''
def inputlocation_addressgui():
    #window contents
    loclist = []
    layout = [[sg.Text('Enter one address at a time:', key='-output-'), sg.Button('Quit')],
            [sg.Input(key='-input-', size=(20, None)), sg.Button('add', key='-add-')],
            [sg.InputCombo(loclist, key='-combo-')]]
    
    #creates window
    window = sg.Window('Test', layout)
    
    #Process events and get user input values
    while True:
        event, values = window.read()
        
        #user closes window/cancels
        if event == sg.WIN_CLOSED or event == '-output-': 
            break
        #adds value to loclist
        elif event == '-add-':
            loclist.append(values['-input-'])
            window['-combo-'].update(values=loclist)
            window['-input-'].update('')
        
    window.close()
    
    print(loclist)