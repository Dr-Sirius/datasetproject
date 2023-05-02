import csv
import PySimpleGUI as sg
import wikipedia as wiki
from wikipedia import PageError

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False



def scrubber(csv_file):
  #Checks to see if string is == to int or float and converts it

  for red in csv_file:
    for i, v in enumerate(red):
      red[i] = red[i].replace('""',"").strip()
      try:
        if red[i].isdecimal == True:
          red[i] = float(red[i])
          
        else:
          red[i] = int(red[i])
      except:
          pass
  
  #converts string into boolean 
  
  for red in csv_file:
    for i, v in enumerate(red):
      try:
        red[i] = eval(red[i])
      except:
        if red[i] == "":
          red[i] = None
        else:
          pass

def appender(csv_file,append_data=False):
  with open(f"{csv_file}.csv","a") as f:
    data = csv.writer(f,delimiter=",")
    data.writerow(append_data)


def search(contents,input):
  inquary = None
  print(input)
  
  for red in contents:
    if input.lower() in red[0].lower():
      inquary = red
 
  
  print(inquary)
  return inquary
    
def sort(content,header,sort_param,key=None):
  
  if sort_param == "-ABC-":
    content = sorted(content,key= lambda item:item[0])
    return content
  if sort_param == "-ZYX-":
    content = sorted(content,key = lambda item:item[0])
    content.sort(reverse=True,key=lambda item:item[0])
    return content
  
  if sort_param == "-SORT-":
    get_in = header.index(key[0])
    if key[1] == False:
      content = sorted(content,key= lambda item:item[get_in])
      return content
    if key[1] == True:
      content = sorted(content,key = lambda item:item[get_in])
      content.sort(reverse=True,key=lambda item:item[get_in])
      return content
    
    
def only_nums(header,content):
  num_list = []
  hed_list = []
  
  for i,v in enumerate(content[0]):
    if str(v).isdigit():
      num_list.append(i)
    elif is_float(str(v)):
      num_list.append(i)
    
  for i,v in enumerate(num_list):
    print(v)
    hed_list.append(header[v])
    
  return hed_list



def master_math(header,content,num_headers,key,field,zero=False):
  if field not in num_headers:
    return "Sorry that is not an acceptable field"
  else:
    hed_index = header.index(field)
    math = []
    for red in content:
      if len(red) == len(header):
        print(red)
        if zero == False:
          if str(red[hed_index]).isdigit():
            math.append(red[hed_index])
          elif is_float(str(red[hed_index])):
            math.append(red[hed_index])
        if zero == True:
          if str(red[hed_index]).isdigit() and red[hed_index] != 0:
            math.append(red[hed_index])
          elif is_float(str(red[hed_index])) and red[hed_index] != 0.0:
            math.append(red[hed_index])
      else:
        pass
    if key == "-ADD-":
      answer = sum(math)
    if key == "-SUB-":
      return sub(math)
    if key == "-MULTI-":
      answer = multiply(math)
    if key == "-DIV-":
      answer = div(math)
    if key == "-DIZ-":
      answer = div_no_deci(math)
    return answer
    
  
def sub(listy):
  answer = listy[0]
  del listy[0]
  for red in listy:
    answer -= red
  
  return answer
  
def multiply(listy):
  answer = listy[0]
  del listy[0]
  for red in listy:
    
    answer *= red
  
  return answer


def div(listy):
  answer = listy[0]
  del listy[0]
  for red in listy:
    try:
      answer /= red
    except Exception as e:
      
      answer = e
      break
  return answer

def div_no_deci(listy):
  answer = listy[0]
  del listy[0]
  for red in listy:
    try:
      answer //= red
    except Exception as e:
      
      answer = e
      break
  
  return answer

def just_field(content,field_op=0):
  field = []
  for red in content:
    try:
      
      field.append(red[field_op])
    except:
      pass
  return field


def wiki_search(field,summary=False,link=False,result_select=0,jr=True):
  data = []
  results = wiki.search(field)
  
  if jr == True:
    data.append(results)
  if jr == False:
    
    try:
      if summary==False:
        page = wiki.page(results[result_select],redirect=True)
        
        contents = page.content
        print(contents)
        
        data.append(contents)
        if link==True:
          data.append(page.url)
        

        
      if summary == True:
        page = wiki.page(results[result_select],redirect=True)
        page_summary = page.summary
        data.append(page_summary)
        if link==True:
          data.append(page.url)
        
    except PageError:
      
      data = "Sorry an error occured please try again"
    
       
  return data