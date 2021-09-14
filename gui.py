'''
Created on Aug 28, 2021

@author: lon
'''
import PySimpleGUI as sg
import main

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
    
    return values

'''
GUI for input error window
'''
def errorpopup():
    
    sg.popup('Incorrect input, try again.')

'''
GUI interactions to retrieve user address input
'''
def inputlocation_addressgui():
    #window contents
    loclist = []
    layout = [[sg.Text('Enter one address at a time:', key = '-output-'), sg.Button('Quit')],
            [sg.Input(key = '-input-', size = (30, 1)), sg.Button('add', key = '-add-')],
            [sg.InputCombo(loclist, key = '-combo-', size = (30, 1))]]
    
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
            loclist = main.gui_inputlist(values['-input-'], loclist)
            #loclist.append(values['-input-'])
            #window['-combo-'].update(values=loclist)
            window['-input-'].update('')
            
        window['-combo-'].update(values=loclist)
        
    window.close()
    
    print(loclist)
    
'''
GUI
'''
def mainwindow():

    sg.SetOptions(element_padding = (0, 0))

    #menu definitions
    menu = [['File', ['Email', 'Print', 'Exit']],      
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
            ['Help', 'About'], ]  

    layout = [[sg.Menu(menu, tearoff = True)],
            [sg.Text('Enter one address at a time:', key = '-output-')],
            [sg.Input(key = '-input-', size = (30, 1)), sg.Button('add', key = '-add-')],
            [sg.Multiline(key = '-ml-'+sg.WRITE_ONLY_KEY, size = (30, 1))],
            [sg.Text('\nSelect trip outputs:')],
            [sg.Frame(layout = [
                [sg.Checkbox('Steps', key = 'STEPS'), sg.Checkbox('Total Distance', key = 'TOTALDISTANCE'), 
                 sg.Checkbox('Total Time', key = 'TOTALTIME'), sg.Checkbox('Coordinates', key = 'LATLONG'), 
                 sg.Checkbox('Elevation', key = 'ELEVATION')]], title = 'Options', relief = sg.RELIEF_SUNKEN)],
            [sg.Submit()]
            ]
    
    window = sg.Window('TripIt', layout, default_element_size = (40, 1), grab_anywhere = False)
    
    loclist = []
    outputlist = []
    
    while True:
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        
        if values['STEPS'] == True:
            outputlist.append('STEPS')
            print(outputlist)
        elif values['TOTALDISTANCE'] == True:
            outputlist.append('TOTALDISTANCE')
            print(outputlist)
        elif values['TOTALTIME'] == True:
            outputlist.append('TOTALTIME')
            print(outputlist)
        elif values['LATLONG'] == True:
            outputlist.append('LATLONG')
            print(outputlist)
        elif values['ELEVATION'] == True:
            outputlist.append('ELEVATION')
        
        if event == '-add-':
            window['-ml-'+sg.WRITE_ONLY_KEY].print(values['-input-'])
            loclist = main.gui_inputlist(values['-input-'], loclist)
            window['-input-'].update('')
        elif event == 'About':
            sg.popup('About this program', 'Version 1.0')
            
    window.close()
    
    print(loclist)
    print(outputlist)
