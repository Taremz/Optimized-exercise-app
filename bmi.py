import healthsignup
import height
import weight
def calculate_bmi():
    kg = int(weight_tf.get())
    cm = int(height_tf.get())/100
    bmi = kg/(cm*cm)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('bmi-', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-computerscience', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-computerscience', f'BMI = {bmi} is Obese') 
    else:
        messagebox.showerror('bmi-computerscience', 'something went wrong!')   
        
ws = Tk()
ws.title('bmi-computerscience')
ws.geometry('400x300')
ws.config(bg='#686e70')

var = IntVar()


height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_button = Button(
    frame3,
    text='Reset',
    command=reset_entry
)
reset_button.pack(side=LEFT)

exit_button = Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_button.pack(side=RIGHT)

ws.mainloop()

