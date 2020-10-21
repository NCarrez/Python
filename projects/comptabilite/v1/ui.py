### ----------------------------------------------------------------------------------------
### FILE CREATED AND OWNED BY NICOLAS CARREZ
### Publishing this file under any other name is forbidden
### Publishing this file without agreement is forbidden
### Publishing a copy of the file or code without mentioning the initial author is forbidden
### For more informations please contact n.carrez.code@gmail.com
### ----------------------------------------------------------------------------------------
import os, sys

file_path = os.path.dirname(os.path.abspath(__file__))
if not (file_path in sys.path):
    sys.path.append(file_path)


#-Create UI Using tkinter
import tkinter

#--Packing tkinter widgets
class pack_type():
    PACK = 0
    GRID = 1
def __pack_widget__(widget_to_pack, p_dict=None):
    p_type = p_dict.get('type',None)
    if(p_type == pack_type.PACK):
        return widget_to_pack.pack(
            fill  =p_dict.get('fill',None)          if p_dict != None else None, 
            expand=p_dict.get('expand',None)        if p_dict != None else None, 
            side  =p_dict.get('side',None)          if p_dict != None else None
            )
    elif(p_type == pack_type.GRID):
        return widget_to_pack.grid(
            row        =p_dict.get('row',None)      if p_dict != None else None, 
            column     =p_dict.get('column',None)   if p_dict != None else None, 
            rowspan    =p_dict.get('rowspan',None)  if p_dict != None else None, 
            columnspan =p_dict.get('colspan',None)  if p_dict != None else None
            )
    pass

#--Building tkinter widgets
class widget_type():
    LABEL = 0
    ENTRY = 1
    BUTTON = 2
    SPINBOX = 3

def __build_widget__(w_dict=None):
    if(w_dict == None):
        return None
    w_type = w_dict.get('type',None)
    del w_dict['type']
    if(w_type   == widget_type.LABEL):
        return __build_label__(w_dict)
    elif(w_type == widget_type.ENTRY):
        return __build_entry__(w_dict)
    elif(w_type == widget_type.BUTTON):
        return __build_button__(w_dict)
    elif(w_type == widget_type.SPINBOX):
        return __build_spinbox__(w_dict)
    pass

def __build_label__(w_dict=None):
    return tkinter.Label(**w_dict)  
    pass

def __build_entry__(w_dict=None):
    return tkinter.Entry(**w_dict)
    pass

def __build_button__(w_dict=None):
    return tkinter.Button(**w_dict)
    pass

def __build_spinbox__(w_dict=None):
    return tkinter.Spinbox(**w_dict)
    pass
    
    
def _add_widget_(widget_dict=None, pack_dict=None):
    return __pack_widget__(
        widget_to_pack=__build_widget__(
            w_dict=widget_dict
            ), 
        p_dict=pack_dict
        )
    pass

#-Create App Using tkinter
class MainApp():
    ### Tkinter App Skeleton 
    def __init__(self, app_name=None):
        self.m_window = tkinter.Tk()
        self.m_window.title(app_name)
        self.build_frame()
        self.__loop__()
    
    def __loop__(self):
        self.m_window.mainloop()   

    ###Tkinter App building
    def build_frame(self):
        ###Using dict to build widgets
        ###one dict for the widget, the other for packing
        _add_widget_(
            {'type':0,'text':'Valeur'}, #Widget Info
            {'type':0,'side':'left'}    #Packing Info
            )
        self.m_w_value = _add_widget_({'type':1}, {'type':0,'side':'left'})
        _add_widget_({'type':0,'text':'Categorie'}, {'type':0,'side':'left'})
        self.m_w_type  = _add_widget_({'type':3,'values':('ajout','retrait')}, {'type':0,'fill':'both','expand':'yes','side':'left'})
        _add_widget_({'type':0,'text':'Nom'}, {'type':0,'side':'left'})
        self.m_w_name  = _add_widget_({'type':1}, {'type':0,'side':'left'})
        self.m_w_button = _add_widget_({'type':2,'text':'Ok!'}, {'type':0,'side':'left'})



if __name__ == "__main__":
    my_app = MainApp()
    pass