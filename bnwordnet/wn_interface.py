import tkinter as tk

class KeyBoard:
  def __init__(self,master):
    frame=tk.Frame(master,width=600,height=200,relief='raised')
    frame.pack(fill='both')
    
    frame1=tk.Frame(frame,width=600,height=200,relief='raised',bg='grey')
    frame1.pack(fill='both')
    
    self.button=tk.Button(frame1,width=2,bg='white')
    self.button.grid(row=0,column=0,padx=1,pady=1)
    
    self.button1=tk.Button(frame1,text='\u09E7',width=2,bg='white',activebackground='white',command=self.key_button1)
    self.button1.grid(row=0,column=1,padx=1,pady=1)
    
    self.button2=tk.Button(frame1,text='\u09E8',width=2,bg='white',command=self.key_button2)
    self.button2.grid(row=0,column=2,padx=1,pady=1)
    
    self.button3=tk.Button(frame1,text='\u09E9',width=2,bg='white',command=self.key_button3)
    self.button3.grid(row=0,column=3,padx=1,pady=1)
    
    self.button4=tk.Button(frame1,text='\u09EA',width=2,bg='white',command=self.key_button4)
    self.button4.grid(row=0,column=4,padx=1,pady=1)
    
    self.button5=tk.Button(frame1,text='\u09EB',width=2,bg='white',command=self.key_button5)
    self.button5.grid(row=0,column=5,padx=1,pady=1)

    self.button6=tk.Button(frame1,text='\u09EC',width=2,bg='white',command=self.key_button6)
    self.button6.grid(row=0,column=6,padx=1,pady=1)
    
    self.button7=tk.Button(frame1,text='\u09ED',width=2,bg='white',command=self.key_button7)
    self.button7.grid(row=0,column=7,padx=1,pady=1)
    
    self.button8=tk.Button(frame1,text='\u09EE',width=2,bg='white',command=self.key_button8)
    self.button8.grid(row=0,column=8,padx=1,pady=1)
    
    self.button9=tk.Button(frame1,text='\u09EF',width=2,bg='white',fg='blue',command=self.key_button9)
    self.button9.grid(row=0,column=9,padx=1,pady=1)
    
    self.button10=tk.Button(frame1,text='\u09E6',width=2,bg='white',command=self.key_button10)
    self.button10.grid(row=0,column=10,padx=1,pady=1)
    
    self.button11=tk.Button(frame1,text='-',width=2,bg='white',command=self.key_button11)
    self.button11.grid(row=0,column=11,padx=1,pady=1)
    
    self.button12=tk.Button(frame1,text='\u09C3',width=2,bg='white',command=self.key_button12)
    self.button12.grid(row=0,column=12,padx=1,pady=1)
    
    self.button13=tk.Button(frame1,text='\\',width=2,bg='white',command=self.key_button13)
    self.button13.grid(row=0,column=13,padx=1,pady=1)
    
    self.button_14=tk.Button(frame1,text='Del',width=2,bg='white',command=self.key_button_14)
    self.button_14.grid(row=0,column=14,padx=1,pady=1)

#********************ROW-2********************************#

    self.r1_button1=tk.Button(frame1,width=5,text='Tab',justify=tk.LEFT,bg='white',command=self.key_r2_button1)
    self.r1_button1.grid(row=1,column=0,sticky='W',padx=1,pady=1,columnspan=2)
    
    self.r1_button2=tk.Button(frame1,text='\u09CC',width=2,bg='white',command=self.key_r2_button2)
    self.r1_button2.grid(row=1,column=2,sticky='W',padx=1,pady=1)
    
    self.r1_button3=tk.Button(frame1,text='\u09C8',width=2,bg='white',command=self.key_r2_button3)
    self.r1_button3.grid(row=1,column=3,sticky='W',padx=1,pady=1)
    
    self.r1_button4=tk.Button(frame1,text='\u09BE',width=2,bg='white',command=self.key_r2_button4)
    self.r1_button4.grid(row=1,column=4,sticky='W',padx=1,pady=1)
    
    self.r1_button5=tk.Button(frame1,text='\u09C0',width=2,bg='white',command=self.key_r2_button5)
    self.r1_button5.grid(row=1,column=5,padx=1,sticky='W',pady=1)
    
    self.r1_button6=tk.Button(frame1,text='\u09C2',width=2,bg='white',command=self.key_r2_button6)
    self.r1_button6.grid(row=1,column=6,padx=1,stick='W',pady=1)
    
    self.r1_button7=tk.Button(frame1,text='\u09AC',width=2,bg='white',command=self.key_r2_button7)
    self.r1_button7.grid(row=1,column=7,padx=1,sticky='W',pady=1)
    
    self.r1_button8=tk.Button(frame1,text='\u09B9',width=2,bg='white',command=self.key_r2_button8)
    self.r1_button8.grid(row=1,column=8,padx=1,sticky='W',pady=1)
    
    self.r1_button9=tk.Button(frame1,text='\u0997',width=2,bg='white',command=self.key_r2_button9)
    self.r1_button9.grid(row=1,column=9,padx=1,sticky='W',pady=1)
    
    self.r1_button10=tk.Button(frame1,text='\u09A6',width=2,bg='white',command=self.key_r2_button10)
    self.r1_button10.grid(row=1,column=10,padx=1,sticky='W',pady=1)
    
    self.r1_button11=tk.Button(frame1,text='\u099C',width=2,bg='white',command=self.key_r2_button11)
    self.r1_button11.grid(row=1,column=11,padx=1,sticky='W',pady=1)
    
    self.r1_button12=tk.Button(frame1,text='\u09A1',width=2,bg='white',command=self.key_r2_button12)
    self.r1_button12.grid(row=1,column=12,padx=1,sticky='W',pady=1)
    
    self.r1_button13=tk.Button(frame1,text='',width=2,bg='white',command=self.key_r2_button13)
    self.r1_button13.grid(row=1,column=13)
    
    self.r1_button14=tk.Button(frame1,height=3,width=2,bg='white')
    self.r1_button14.grid(row=1,column=14,rowspan=2)
    
 #   self.r1_button13=tk.Button(frame1,text='\u0986')
 #   self.r1_button13.grid(row=1,column=13,padx=2,sticky='W',pady=3)
    

#********************ROW-3**********************************#
    
    self.r2_button1=tk.Button(frame1,width=7,bg='white',justify=tk.LEFT,text='Caps Lock')
    self.r2_button1.grid(row=2,column=0,padx=1,pady=1,columnspan=2,sticky='W')
    
    self.r2_button2=tk.Button(frame1,text='\u0986',width=2,bg='white')
    self.r2_button2.grid(row=2,column=2,padx=1,pady=1,sticky='W')
    
    self.r2_button3=tk.Button(frame1,text='\u09CB',width=2,bg='white',command=self.key_r4_button3)
    self.r2_button3.grid(row=2,column=3,padx=1,pady=1,sticky='W')
    
    self.r2_button4=tk.Button(frame1,text='\u09C7',width=2,bg='white',command=self.key_r4_button4)
    self.r2_button4.grid(row=2,column=4,padx=1,pady=1,sticky='W')

    self.r2_button5=tk.Button(frame1,text='\u09CD',width=2,bg='white',command=self.key_r4_button5)
    self.r2_button5.grid(row=2,column=5,padx=1,pady=1,sticky='W')  

    self.r2_button6=tk.Button(frame1,text='\u09BF',width=2,bg='white',command=self.key_r4_button6)
    self.r2_button6.grid(row=2,column=6,padx=1,pady=1,sticky='W')
    
    self.r2_button7=tk.Button(frame1,text='\u09C1',width=2,bg='white',command=self.key_r4_button7)
    self.r2_button7.grid(row=2,column=7,padx=1,pady=1,sticky='W')
    
    self.r2_button8=tk.Button(frame1,text='\u09AA',width=2,bg='white',command=self.key_r4_button8)
    self.r2_button8.grid(row=2,column=8,padx=1,pady=1,sticky='W')
    
    self.r2_button9=tk.Button(frame1,text='\u09B0',width=2,bg='white',command=self.key_r4_button9)
    self.r2_button9.grid(row=2,column=9,padx=1,pady=1,sticky='W')
    
    self.r2_button10=tk.Button(frame1,text='\u0995',width=2,bg='white',activebackground='green',command=self.key_r4_button10)
    self.r2_button10.grid(row=2,column=10,padx=1,pady=1,sticky='W')
    
    self.r2_button11=tk.Button(frame1,text='\u09A4',width=2,bg='white',command=self.key_r4_button11)
    self.r2_button11.grid(row=2,column=11,padx=1,pady=1,sticky='W')
    
    self.r2_button12=tk.Button(frame1,text='\u099A',width=2,bg='white',command=self.key_r4_button12)
    self.r2_button12.grid(row=2,column=12,padx=1,pady=1,sticky='W')
    
    self.r2_button13=tk.Button(frame1,text='\u099F',width=2,bg='white',command=self.key_r4_button13)
    self.r2_button13.grid(row=2,column=13,sticky='W')
    
#*****************************ROW-4**************************************#

    self.r3_button1=tk.Button(frame1,width=8,bg='white',justify='left',text='Shift',command=self.shift_key)
    self.r3_button1.grid(row=3,column=0,padx=1,pady=1,columnspan=2,sticky='W')
    
    self.r3_button2=tk.Button(frame1,text='\u09CE',width=2,bg='white',command=self.key_r5_button1)
    self.r3_button2.grid(row=3,column=2,padx=1,pady=1,sticky='W')
    
    self.r3_button3=tk.Button(frame1,text='\u0982',width=2,bg='white',command=self.key_r5_button2)
    self.r3_button3.grid(row=3,column=3,padx=1,pady=1,sticky='W')
    
    self.r3_button4=tk.Button(frame1,text='\u09AE',width=2,bg='white',command=self.key_r5_button3)
    self.r3_button4.grid(row=3,column=4,padx=1,pady=1,sticky='W')
    
    self.r3_button5=tk.Button(frame1,text='\u09A8',width=2,bg='white',command=self.key_r5_button4)
    self.r3_button5.grid(row=3,column=5,padx=1,pady=1,sticky='W')
    
    self.r3_button6=tk.Button(frame1,text='\u09AC',width=2,bg='white',command=self.key_r5_button5)
    self.r3_button6.grid(row=3,column=6,padx=1,pady=1,sticky='W')
    
    self.r3_button7=tk.Button(frame1,text='\u09B2',width=2,bg='white',command=self.key_r5_button6)
    self.r3_button7.grid(row=3,column=7,padx=1,pady=1,sticky='W')
    
    self.r3_button8=tk.Button(frame1,text='\u09B8',width=2,bg='white',command=self.key_r5_button7)
    self.r3_button8.grid(row=3,column=8,padx=1,pady=1,sticky='W')
    
    self.r3_button9=tk.Button(frame1,text='\u0986',width=2,anchor=tk.NE,bg='white',command=self.key_r5_button8)
    self.r3_button9.grid(row=3,column=9,padx=1,pady=1,sticky='W')
    
    self.r3_button10=tk.Button(frame1,text='\u0986',width=2,anchor=tk.NE,bg='white',command=self.key_r5_button9)
    self.r3_button10.grid(row=3,column=10,padx=1,pady=1,sticky='W')
    
    self.r3_button11=tk.Button(frame1,text='\u09DF',width=2,bg='white',command=self.key_r5_button10)
    self.r3_button11.grid(row=3,column=11,padx=1,pady=1,sticky='W')
    
    self.r3_button12=tk.Button(frame1,width=8,text='Shift',command=self.shift_key,bg='white')
    self.r3_button12.grid(row=3,column=12,padx=1,pady=1,sticky='W',columnspan=2)

    self.r3_button13=tk.Button(frame1,text='Del',anchor=tk.NE,width=2,bg='white',command=self.key_button_14)
    self.r3_button13.grid(row=3,column=14,padx=1,pady=1)

#******************************ROW-5*********************************************#
    
    self.r4_button1=tk.Button(frame1,text='Ctrl',width=2,anchor=tk.NE,bg='white')
    self.r4_button1.grid(row=4,column=0,padx=2,pady=3)
    
    self.r4_button2=tk.Button(frame1,text='Alt',width=2,bg='white')
    self.r4_button2.grid(row=4,column=2,padx=2,pady=3,sticky='W')
    
    self.r4_button3=tk.Button(frame1,width=36,bg='white',command=self.space)
    self.r4_button3.grid(row=4,column=3,padx=2,pady=3,sticky='W',columnspan=7)
    
    self.r4_button4=tk.Button(frame1,text='Alt',width=2,bg='white')
    self.r4_button4.grid(row=4,column=10,padx=2,pady=3,sticky='W')
    
    self.r4_button5=tk.Button(frame1,width=2,text='Ctrl',anchor=tk.SW,bg='white')
    self.r4_button5.grid(row=4,column=14,padx=2,pady=3,sticky='W')
  
  i=0
  
  def shift_key(self):
    if self.i==0:
      self.r3_button12.config(relief='sunken',bg='grey')
      self.r3_button1.config(relief='sunken',bg='grey')
      self.r2_button10.config(text='\u0996',fg='green')
      self.button9.config(text='(',fg='green')
      self.button10.config(text=')',fg='green')
      self.button11.config(text='\u0983',fg='green')
      self.button12.config(text='\u09E0',fg='green')
      self.button13.config(text='|',fg='green')
      self.r1_button11.config(text='\u09AC',fg='green')
      self.r1_button12.config(text='\u09A2',fg='green')
      self.r1_button10.config(text='\u09A7',fg='green')
      self.r1_button9.config(text='\u0998',fg='green')
      self.r1_button8.config(text='\u0999',fg='green')
      self.r1_button7.config(text='\u09AD',fg='green')
      self.r1_button2.config(text='\u0994',fg='green')
      self.r1_button3.config(text='\u0990',fg='green')
      self.r1_button4.config(text='\u09A6',fg='green')
      self.r1_button5.config(text='\u0988',fg='green')
      self.r1_button6.config(text='\u098A',fg='green')
      self.r2_button3.config(text='\u0993',fg='green')
      self.r2_button4.config(text='\u098F',fg='green')
      self.r2_button5.config(text='\u0985',fg='green')
      self.r2_button6.config(text='\u0987',fg='green')
      self.r2_button7.config(text='\u0989',fg='green')
      self.r2_button8.config(text='\u09AB',fg='green')
      self.r2_button9.config(text='\u09DD',fg='green')
      self.r2_button11.config(text='\u09A5',fg='green')
      self.r2_button12.config(text='\u099B',fg='green')
      self.r2_button13.config(text='\u09A0',fg='green')
      self.r3_button2.config(text='?',fg='green')
      self.r3_button4.config(text='\u09A3',fg='green')
      self.r3_button8.config(text='\u09B6',fg='green')
      self.r3_button11.config(text='\u09AF',fg='green')
      self.r3_button9.config(text='\u09B7',fg='green')
      self.r3_button10.config(text='|',fg='green')
      self.r1_button13.config(text='\u099E',fg='green')
      self.r3_button3.config(text='\u09FA',fg='green')
      self.i=1
    else:
      self.r3_button12.config(relief='raised',bg='white')
      self.r3_button1.config(relief='raised',bg='white')
      self.r2_button10.config(text='\u0995',fg='black')
      self.button9.config(text='\u09EF',fg='black')
      self.button10.config(text='\u09E6',fg='black')
      self.button11.config(text='-',fg='black')
      self.button12.config(text='\u09C3',fg='black')
      self.button13.config(text='\ ',fg='black')
      self.r1_button11.config(text='\u099C',fg='black')
      self.r1_button12.config(text='\u09A1',fg='black')
      self.r1_button10.config(text='\u09A6',fg='black')
      self.r1_button9.config(text='\u0997',fg='black')
      self.r1_button8.config(text='\u09B9',fg='black')
      self.r1_button7.config(text='\u09AC',fg='black')
      self.r1_button2.config(text='\u09CC',fg='black')
      self.r1_button3.config(text='\u09C8',fg='black')
      self.r1_button4.config(text='\u09BE',fg='black')
      self.r1_button5.config(text='\u09C0',fg='black')
      self.r1_button6.config(text='\u09C2',fg='black')
      self.r2_button3.config(text='\u09CB',fg='black')
      self.r2_button4.config(text='\u09C7',fg='black')
      self.r2_button5.config(text='\u09CD',fg='black')
      self.r2_button6.config(text='\u09BF',fg='black')
      self.r2_button7.config(text='\u09C1',fg='black')
      self.r2_button8.config(text='\u09AA',fg='black')
      self.r2_button9.config(text='\u09B0',fg='black')
      self.r2_button11.config(text='\u09A4',fg='black')
      self.r2_button12.config(text='\u099A',fg='black')
      self.r2_button13.config(text='\u099F',fg='black')
      self.r3_button2.config(text='\u09CE',fg='black')
      self.r3_button4.config(text='\u09AE',fg='black')
      self.r3_button8.config(text='\u09B8',fg='black')
      self.r3_button11.config(text='\u09DF',fg='black')
      self.r3_button9.config(text=',',fg='black')
      self.r3_button10.config(text='.',fg='black')
      self.r1_button13.config(text='',fg='black')
      self.r3_button3.config(text='\u0982',fg='black')
      self.i=0
  def space(self):
    Wordnet.search.insert('end',' ')
  
  def key_button1(self):
    Wordnet.search.insert('end','\u09E7')
  def key_button2(self):
    Wordnet.search.insert('end','\u09E8')
  def key_button3(self):
    Wordnet.search.insert('end','\u09E9')
  def key_button4(self):
    Wordnet.search.insert('end','\u09EA')
  def key_button5(self):
    Wordnet.search.insert('end','\u09EB')
  def key_button6(self):
    Wordnet.search.insert('end','\u09EC')
  def key_button7(self):
    Wordnet.search.insert('end','\u09ED')
  def key_button8(self):
    Wordnet.search.insert('end','\u09EE')
  def key_button9(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09EF')
    else:
      Wordnet.search.insert('end','(')
  def key_button10(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09E6')
    else:
      Wordnet.search.insert('end',')')
  def key_button11(self):
    if self.i==0:
      Wordnet.search.insert('end','-')
    else:
      Wordnet.search.insert('end','\u0983')
  def key_button12(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09C3')
    else:
      Wordnet.search.insert('end','\u098B')
  def key_button13(self):
    if self.i==0:
      Wordnet.search.insert('end','\\')
    else:
      Wordnet.search.insert('end','|')
  def key_button14(self):
    pass
    #add code for backspace.
#****************************************ROW-1******************************************************************#
  
  def key_r2_button1(self):
    pass
    #Add code for tab.
  def key_r2_button2(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09CC')
    else:
      Wordnet.search.insert('end','\u0994')
  def key_r2_button3(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09C8')
    else:
      Wordnet.search.insert('end','\u0990')
  def key_r2_button4(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09BE')
    else:
      Wordnet.search.insert('end','\u09A6')
  def key_r2_button5(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09C0')
    else:
      Wordnet.search.insert('end','\u0988')
  def key_r2_button6(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09C2')
    else:
      Wordnet.search.insert('end','\u09BA')
  def key_r2_button7(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09AC')
    else:
      Wordnet.search.insert('end','\u09AD')
  def key_r2_button8(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09B9')
    else:
      Wordnet.search.insert('end','\u0999')
  def key_r2_button9(self):
    if self.i==0:
      Wordnet.search.insert('end','\u0997')
    else:
      Wordnet.search.insert('end','\u0998')
  def key_r2_button10(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09A6')
    else:
      Wordnet.search.insert('end','\u09A7')
  def key_r2_button11(self):
    if self.i==0:
      Wordnet.search.insert('end','\u099C')
    else:
      Wordnet.search.insert('end','\u09AC')
  def key_r2_button12(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09A1')
    else:
      Wordnet.search.insert('end','\u09A2')
  def key_r2_button13(self):
    if self.i==0:
      Wordnet.search.insert('end','')
    else:
      Wordnet.search.insert('end','\u099E')
 
 #********************************************ROW-3*************************************************************#
 
  def key_r4_button3(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09CB')
    else:
      Wordnet.search.insert('end','\u0993')
  def key_r4_button4(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09C7')
    else:
      Wordnet.search.insert('end','\u098F')
  def key_r4_button5(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09CD')
    else:
      Wordnet.search.insert('end','\u0985')
  def key_r4_button6(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09BF')
    else:
      Wordnet.search.insert('end','\u0987')
  def key_r4_button7(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09C1')
    else:
      Wordnet.search.insert('end','\u0989')
  def key_r4_button8(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09AA')
    else:
      Wordnet.search.insert('end','\u09AB')
  def key_r4_button9(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09B0')
    else:
      Wordnet.search.insert('end','\u09DD')
  def key_r4_button10(self):
    if self.i==0:
      Wordnet.search.insert('end','\u0995')
    else:
      Wordnet.search.insert('end','\u0996')
  def key_r4_button11(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09A4')
    else:
      Wordnet.search.insert('end','\u09A5')
  def key_r4_button12(self):
    if self.i==0:
      Wordnet.search.insert('end','\u099A')
    else:
      Wordnet.search.insert('end','\u099B')
  def key_r4_button13(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09FF')
    else:
      Wordnet.search.insert('end','\u09A0')
     
  #*****************************************ROW-4****************************************************#
   
  def key_r5_button1(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09CE')
    else:
      Wordnet.search.insert('end','?')
  def key_r5_button2(self):
    if self.i==0:
      Wordnet.search.insert('end','\u0982')
    else:
      Wordnet.search.insert('end','\u09FA')
  def key_r5_button3(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09AE')
    else:
      Wordnet.search.insert('end','\u09A3')
  def key_r5_button4(self):
    Wordnet.search.insert('end','\u09A8')
  def key_r5_button5(self):
    Wordnet.search.insert('end','\u09AC')
  def key_r5_button6(self):
    Wordnet.search.insert('end','\u09B2')
 
  def key_button_14(self):
    length=len(Wordnet.search.get())
    Wordnet.search.delete(length-1)
  
  def key_r5_button7(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09B8')
    else:
      Wordnet.search.insert('end','\u09B6')
  def key_r5_button8(self):
    if self.i==0:
      Wordnet.search.insert('end',',')
    else:
      Wordnet.search.insert('end','\u09B7')
  def key_r5_button9(self):
    if self.i==0:
      Wordnet.search.insert('end','.')
    else:
      Wordnet.search.insert('end','|')
  def key_r5_button10(self):
    if self.i==0:
      Wordnet.search.insert('end','\u09DF')
    else:
      Wordnet.search.insert('end','\u09AF')

  #************************Keyboard****************************************#
class Wordnet_bn:
  
  def __init__(self,master):
    
 #************************TOP_LEVEL FRAME***********************************************************#   
    frame1=tk.Frame(master,width=600,height=100,relief='raised',bd=2)
    frame1.pack(fill='both')
    
    self.label=tk.Label(frame1,text='Search')
    self.label.pack(side='left')
    
    search_text=tk.StringVar()
    self.search=tk.Entry(frame1,bg='white',textvariable=search_text)
    self.search.pack(side='left')
    self.search.bind("<Return>",self.show_text)
   # self.button1=tkinter.Button(frame1,text='Search',command=self.show_text)
   # self.button1.pack(side='right')
  
#*************************MIDDLE_LEVEL FRAME*******************************************************#    
    frame2=tk.Frame(master,width=600,height=100,relief='raised',bd=2)
    frame2.pack(fill='both')
    
   # image_key=tk.PhotoImage(file="key",width=70,height=30)
    
    self.keyboard=tk.Button(frame2,width=10,text="Keyboard",command=self.Key)
    self.keyboard.pack(side='right')
    
    senses_text=tk.StringVar()
    self.senses=tk.Entry(frame2,bg='white',textvariable=senses_text)
    self.senses.pack(side='right')
    
    self.senses_label=tk.Label(frame2,text='Senses')
    self.senses_label.pack(side='right')

#**************************TEXT AREA***************************************************************#    
    
    frame=tk.Frame(master,width=600,height=300)
    
    scrollbar=tk.Scrollbar(frame,orient='vertical')
    self.text_area=tk.Listbox(frame,font='ariel',width=80,height=20,bg='white',yscrollcommand=scrollbar.set)
    scrollbar.configure(command=self.text_area.yview)
    scrollbar.pack(side='right',fill='y')
    self.text_area.pack(fill='both',expand=1)
    frame.pack(fill='both')
    
#**************************************************************************************************#
   
    frame_bottom=tk.Frame(master,width=600,height=20,relief='raised')
    frame_bottom.pack(side='bottom')
    
#**********************Bottom-Frame****************************************************************#    
    
  def redisplay(self,master1):
    redisp_button=tk.Button(master1,text='Redisplay')
    redisp_button.pack(side='right')
 
  def show_text(self,event):
    
    t=self.search.get()
    self.text_area.insert('end',t)
  
  def Key(self):
    key_root=tk.Tk()
    app=KeyBoard(key_root)
    key_root.title('VBK')
    key_root.mainloop()
    
root=tk.Tk()
Wordnet=Wordnet_bn(root)
root.title('Bengali Keyboard')
root.mainloop()
    
