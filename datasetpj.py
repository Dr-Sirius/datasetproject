import csv,fun
import PySimpleGUI as sg
from tkinter import font





with open("user_settings.csv","r") as f:
  default_settings = list(csv.reader(f))[0]

current_theme = default_settings[0]
current_font = (default_settings[1],default_settings[2])
current_csv = default_settings[3]


with open(f"{current_csv}") as file:
  contents = list(csv.reader(file))
  file.close()

fun.scrubber(contents)

header = contents[0]
del contents[0]

search_quary = []





num_content = fun.only_nums(header=header,content=contents)

font_list = sg.Text.fonts_installed_list()
math_keys = ["-ADD-","-SUB-","-MULTI-","-DIV-","-DIZ-"]
sort_keys = ["-ABC-","-ZYX-","-SPSO-"]

def main(theme=current_theme,font=current_font):
  
  sg.theme(theme)
  g = sg.FileBrowse("open csv",file_types=(("CSV Files","*.csv"),))
  
  menu_bar = [
    [sg.Menu([['File', ["open csv","New CSV"]], ['Edit', ['Edit theme',[sg.theme_list()],"Edit Font",[font_list] ]]],  key='-CUST MENUBAR-')]
  ]


  #Main set of reused buttons
  main_button = [
    *[[sg.Text("",visible=True)]for i in range(2) ],
    
    [sg.Button('Exit'),sg.Button('return',visible=False,key="-RE-"),sg.Submit(key="-SUBM-",visible=False)]
  ]

  #Table Layout used in Layout4
  l4_table=[
    [sg.Table(headings=header,values=[],key="-SEQU-",hide_vertical_scroll=True)],
  ]


  #Main Menu
  layout1 = [
    [sg.Text('Main Menu')],
            [sg.Button("ADD VALUE"),sg.Button("Show CSV"),sg.Button("Value Search"),sg.Button("Sort CSV"),sg.Button("Math Funcs"),sg.Button("More Info")],
    
    
  ]


  #Show inputs to append data to CSV
  layout2 = [
    [sg.Text('Please Enter the respective field and click submit when done!')],
            *[[sg.Input(key='-IN-'),sg.Text(header[i]),sg.Text(f"Ex. {contents[0][i]}")]for i in range(len(header))],
            
          
  ]

  #Show contents of CSV in table format
  layout3 = [
    [sg.Table(headings=header,values=contents,auto_size_columns=True,expand_x=True,expand_y=True,row_height=22,num_rows=20,vertical_scroll_only=False)],
    
    
  ]
            
  #Returns table with the searched data
  layout4 = [
    [sg.Text("Please enter the name of the game you are trying to find!")],
    [sg.Input(key="-INSE-"),sg.Submit("Search",key="-SE-")],
    [sg.Table(headings=header,values=[],key="-SEQU-",row_height=15,num_rows=20,vertical_scroll_only=False,visible=False)],
    [sg.Button("Clear",visible=False,key="-CLEAR-")]
  ]  
    
    

  #Sorts CSV data by Alphanumeric and using specific data field
  layout5 = [
    #[sg.Column(layout=l5_table,size=(800,400))],
    [sg.Table(headings=header,values=contents,key="-DO-",auto_size_columns=True,expand_x=True,expand_y=True,row_height=15,num_rows=25,vertical_scroll_only=False)],
    [sg.HSep()],
    [sg.Button("Reset",key="-L5RE-"),sg.Button("Sort ABC",key="-ABC-"),sg.Button("Sort ZYX",key="-ZYX-"),sg.Button("Sort Specific Value",key="-SPSO-")],
    [sg.HSep()],
    [sg.Input(visible=False,key="-SPIN-"),sg.Button("Sort",visible=False,key="-SORT-"),sg.Checkbox("Sort ZYX",visible=False,key="-CBOX-")]
  ]


  #performs mathmatical operations on data field
  layout6 = [
    [sg.Table(headings=header,values=contents,key="-MATB",auto_size_columns=True,expand_x=True,expand_y=True,row_height=15,num_rows=15,vertical_scroll_only=False)],
    [sg.Text("Fields that support Math Operands:")],
    [sg.Column(layout=[[sg.Text(text=(num_content))],[sg.Text("")]],scrollable=True)],
    [sg.HSep()],
    [sg.Input(key="-MAIN-"),sg.Button("Add Values",key="-ADD-"),sg.Button("Sub Values",key="-SUB-"),sg.Button("Multiply Values",key="-MULTI-"),sg.Button("Div Values",key="-DIV-"),sg.Button("Div No Deci",key="-DIZ-")],
    [sg.Text("Answer ="),sg.Text(text="",key="-ANSR-",text_color="cyan"),sg.Checkbox("Remove Zero Values",key="-ZE-")]
    
  ]

  #Searches Wikipedia for More Info
  layout7 = [
    [sg.Text(text="Choose a field from the box"),sg.Input(key="-FESE-",visible=True),sg.Button("Field Select",key="-FESB-",visible=True)],
    [sg.Multiline(default_text=header,expand_x=True,expand_y=True,size=(400,15),key="-IKIW-")],
    [sg.HSep()],
    [sg.Input(key="-INWI-"),sg.Button("Search Wiki",key="-WIKI-"),sg.Checkbox("Only Summary",key="-SUM-"),sg.Checkbox("Include Link",key="-LINK-")],
    [sg.Text("Resullts select"),sg.Input(size=(5,5),key="-REINP-"),sg.Button("Select",key="-RESULT-")],
    [sg.Text(key="-CHEESE-"),sg.Button("Reset",key="-L7RE-")]
  ]


  # ----------- Create actual layout using Columns and a row of Buttons
  layout = [
    [sg.Column(menu_bar,key="-BAR-"),
    sg.Column(layout1, key='-COL1-'), 
    sg.Column(layout2, visible=False, key='-COL2-',scrollable=True,vertical_scroll_only=True), 
    sg.Column(layout3, visible=False, key='-COL3-'),
    sg.Column(layout4,key='-COL4-',visible=False,element_justification="center"),
    sg.Column(layout5,key="-COL5-",visible=False,scrollable=False),
    sg.Column(layout6,key="-COL6-",visible=False),
    sg.Column(layout7,key="-COL7-",visible=False)],

    [sg.Column(main_button)],[sg.Text("AN ERROR OCCURED",key="-TEXT-",visible=False)],[sg.Multiline(default_text="",visible=False,k="-ERROR-",size=(100,100))]
          ]
  window = sg.Window('Swapping the contents of a window', layout,size=(800,600),finalize=True,element_justification="center",resizable=True,font=font)
  return window

window = main()

layout = 1  # The currently visible layout
while True:
  with open("user_settings.csv","r") as f:
    default_settings = list(csv.reader(f))[0]
    f.close()
  current_theme = default_settings[0]
  current_font = (default_settings[1],default_settings[2])
  try:
    event, values = window.read()
    print(event)
    if event != "-ERRROR-":
      window["-ERROR-"].update()
      window["-ERROR-"].update(visible=False)
      window["-TEXT-"].update(visible=False)

      
    if event in (None, 'Exit'):
        break
    if event == 'ADD VALUE':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)
        window['-RE-'].update(visible=True)
        window["-SUB-"].update(visible=True)
      
    if event == "-RE-":
        window[f'-COL{layout}-'].update(visible=False)
        window["-RE-"].update(visible=False)
        window["-SUB-"].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)
      
    if event == "Show CSV":
      window[f'-COL{layout}-'].update(visible=False)
      layout = 3
      window[f'-COL{layout}-'].update(visible=True)
      window['-RE-'].update(visible=True)
      
    if event == "-SUBM-":
      append_data = []
      for i in values.items():
        if i[1] == "":
          append_data.append(None)
        else:
          append_data.append(i[1])
      print(append_data)
      fun.appender("video_games",append_data)
      
    if event == "Value Search":
      window[f'-COL{layout}-'].update(visible=False)
      layout = 4
      window[f'-COL{layout}-'].update(visible=True)
      window['-RE-'].update(visible=True)

    if event == "-SE-":
      search_quary.append(fun.search(contents,values["-INSE-"]))
      print(search_quary)
      window["-SEQU-"].update(visible=True)
      window["-SEQU-"].update(values=search_quary)
      window["-CLEAR-"].update(visible=True)

    if event == "-CLEAR-":
      window["-SEQU-"].update(visible=False)
      window["-SEQU-"].update(values=[])
      search_quary=[]
      window["-CLEAR-"].update(visible=False)
    
    if event == "Sort CSV":
      window[f'-COL{layout}-'].update(visible=False)
      layout = 5
      window[f'-COL{layout}-'].update(visible=True)
      window['-RE-'].update(visible=True)
    
    
    if event in sort_keys:
      if event == "-SPSO-":
        window["-CBOX-"].update(visible=True)
        window["-SPIN-"].update(visible=True)
        window["-SORT-"].update(visible=True)
        
      else:
        window["-DO-"].update(values=fun.sort(contents,header,event))
    
    if event == "-L5RE-":
      window["-DO-"].update(values=contents)
      window["-CBOX-"].update(visible=False)
      window["-SPIN-"].update(visible=False)
      window["-SORT-"].update(visible=False)
    
    if event == "-SORT-":
      window["-DO-"].update(values=fun.sort(contents,header,event,key=[values["-SPIN-"],values["-CBOX-"]]))
    
    if event == "Math Funcs":
      window[f'-COL{layout}-'].update(visible=False)
      layout = 6
      window[f'-COL{layout}-'].update(visible=True)
      window['-RE-'].update(visible=True)
      
    if event in math_keys:
      answer = fun.master_math(header,contents,num_content,event,field=values["-MAIN-"],zero=values["-ZE-"])
      window["-ANSR-"].update(answer)
    
    if event == "More Info":
      window[f'-COL{layout}-'].update(visible=False)
      layout = 7
      window[f'-COL{layout}-'].update(visible=True)
      window['-RE-'].update(visible=True)
      
    if event == "-WIKI-":
      wiki_search = values["-INWI-"]
      data = fun.wiki_search(values["-INWI-"],summary="-SUM-",link="-LINK-",result_select=0,jr=True)
      window["-IKIW-"].update(data)
    
    if event == "-RESULT-":
      data = fun.wiki_search(wiki_search,summary=values["-SUM-"],link=values["-LINK-"],result_select=int(values["-REINP-"]),jr=False)
      window["-IKIW-"].update(*data)
      if values["-LINK-"] == True:
        window["-CHEESE-"].update(data[1])
      
    if event == "-L7RE-":
      window["-IKIW-"].update("")
    
    if event == "-FESB-":
      field_in = header.index(values["-FESE-"])
      window["-IKIW-"].update(fun.just_field(contents,field_in))

    if event == "open csv":
      chese = sg.popup_get_file("cheese",no_window=True,file_types=(("CSV Files",".csv"),))
      with open("user_settings.csv","w") as f:
        data = csv.writer(f,delimiter=",")
        data.writerow([current_theme,current_font[0],current_font[1],chese])
      current_csv = chese
      window.close()
      with open(f"{current_csv}") as file:
        contents = list(csv.reader(file))

      fun.scrubber(contents)
      header = contents[0]
      del contents[0]
      window = main(theme=current_theme,font=current_font)
      
      

    if event in sg.theme_list():
      with open("user_settings.csv","w") as f:
        data = csv.writer(f,delimiter=",")
        data.writerow([event,current_font[0],current_font[1],current_csv])
      theme = event
      window.close()
      window = main(theme=theme,font=current_font)

    
    if event in font_list:
      with open("user_settings.csv","w") as f:
        data = csv.writer(f,delimiter=",")
        data.writerow([current_theme,event,current_font[1],current_csv])
      window.close()
      window = main(theme=current_theme,font=(event,11))
    

   
      
      
  except Exception as e:
    window["-ERROR-"].update(e)
    window["-ERROR-"].update(visible=True)
    window["-TEXT-"].update(visible=True)
    event = "-ERRROR-"
      
      
     
window.close()

