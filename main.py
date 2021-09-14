'''
main.py: Project MapQuest_API
Created on Aug 24, 2021

@author: lon
'''
import out
import maps
import gui

'''
CLI Gets user input of location number. User inputs the locations.
Locations are appended to a list.
'''
def inputlocations():   
    
    #CLI code
    while True:
        try: 
            locnum = int(input('Enter the amount of destinations (including starting point: '))
    
    
            if locnum < 2:
                print('Enter a number 2 or greater.')        
                pass
            elif locnum >= 2:
                break
        except:
            print('Something weird happened, try again.')
            pass
    
    print('Enter one address per line:')
    
    loclist = []
    
    for i in range(0, locnum):
        loc = input()
    
        loclist.append(loc)
    
    return loclist

'''
GUI add to list
'''
def gui_inputlist(values, inputlist):
    list1 = inputlist
        
    list1.append(values)
            
    return list1

'''
CLI Gets user input of output number. User inputs the outputs that they want.
Outputs are appended to a list.
'''
def outputrequest():
    while True:   
        try:   
            outputnum = int(input('Input the amount of output requests: '))   
            if outputnum < 1:
                print('Enter a number from 1 through 5.')   
                pass   
            elif outputnum >= 1 and outputnum <= 5:
                break
        except:   
            print('Something weird happened. Try again.')   
            pass   
               
    
    print('Options for output: STEPS, TOTALDISTANCE, TOTALTIME, LATLONG, ELEVATION')
       
    outputlist = []   

    for i in range(0, outputnum):   
        while True:
            try:
                output = input()
                
                checkoutput = ['steps','totaldistance', 'totaltime', 'latlong', 'elevation']
                
                if output.casefold() in checkoutput:
                    outputlist.append(output.upper())
                    
                    #print(outputlist)
                    break
                else:
                    print('Incorrect output request, try again.')
                    pass
            except:
                print('Something weird happened, try again.')
                pass
        
    return outputlist

'''
Passes in list of outputs and loops through each output in order to retrieve information for
the user.
'''
def outputinfo(output_list, json_file):
    for output in output_list:
        if output == 'STEPS':
            for i in out.STEPS().info(json_file):
                print(i)
            #out.STEPS().info(json)
        elif output == 'TOTALDISTANCE':
            print(next(out.TOTALDISTANCE().info(json_file)))
        elif output == 'TOTALTIME':
            print(next(out.TOTALTIME().info(json_file)))
        elif output == 'LATLONG':
            for i in out.LATLONG().info(json_file):
                print(i)
        elif output == 'ELEVATION':
            ejsonlist = out.LATLONG().latlnglist(json_file)
            ejson = maps.elevurl(ejsonlist)
            
            for i in out.ELEVATION().info(ejson):
                print(i)
                
    print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.')
    
def main():
    # locations_list = inputlocations()
    # json = maps.directurl(locations_list)
    # output_list = outputrequest()
    #
    # outputinfo(output_list, json)
    
    gui.mainwindow()
    
if __name__ == "__main__":
    main()