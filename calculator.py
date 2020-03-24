#!/usr/bin/env python
# coding: utf-8

# ## calculator Program

# In[1]:


from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
    
def btnClearDisplay():
    global operator
    opeartor=""
    text_Input.set("")
    
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
root=Tk()
root.title("calculator")
operator=""
text_Input=StringVar()
txtDisplay=Entry(root,font=('arial',20,'bold'), textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue", justify='right').grid(columnspan=5)
#theLabel.pack()
btn7=Button(root, padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(root, padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=1,column=2)
addition=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=1,column=3)

btn4=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=2,column=2)
multiplication=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=2,column=3)

btn1=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=3,column=2)
subtraction=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=3,column=3)

btn0=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=4,column=0)
btndot=Button(root,padx=18,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text=".",bg="powder blue",command=lambda:btnClick(".")).grid(row=4,column=1)
equal=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="=",bg="powder blue",command=btnEqualsInput).grid(row=4,column=2)
division=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=4,column=3)

btnc=Button(root, padx=14,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="c",bg="powder blue",command=btnClearDisplay).grid(row=5,column=0)
btnpersantage=Button(root,padx=14,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="%",bg="powder blue",command=lambda:btnClick("%")).grid(row=5,column=1)
btnpower=Button(root, padx=14,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="^",bg="powder blue",command=lambda:btnClick("^")).grid(row=5,column=2)
btndel=Button(root, padx=14,pady=16,bd=8,fg="black",font=('arial',30,'bold'),text="x",bg="powder blue",command=lambda:btnClick("x")).grid(row=5,column=3)



root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




