from Tkinter import *
from tkMessageBox import *
 
 
def answer(msg):
    showerror("Answer", msg)
    
    
def Validator(s):
    try: 
        if int(s) > 0 and int(s) < 10 :
              return True
        else:
              return False;
    except ValueError:
        return False
 
 
 
def isSafe(Matrix, i , j, number):
	for x in range(9):
		if Matrix[x][j] == number:
			return False;
	
	for y in range(9):
		if Matrix[i][y] == number:
			return False;
		
	boxX = i-i%3;
	boxY = j-j%3;
	for x in range(boxX, boxX+3):
		for y in range(boxY, boxY+3):
			if Matrix[x][y] == number:
				return False;
	
	Matrix[i][j] = number;
	return True;		
 
 
def SolveSudoku(Matrix, i, j):
	
	if j == 9:
		return True;
	elif i == 9:
		return SolveSudoku(Matrix,0, j+1);
 
 
	if Matrix[i][j] == 0 :
		for number in range(1,10):
			if isSafe(Matrix,i,j,number) and SolveSudoku(Matrix,i+1,j):
				return True;
			else:
				Matrix[i][j] = 0;
	else:
		return SolveSudoku(Matrix,i+1,j);
	
	return False;	
 
 
 
 
rows = []
for i in range(9):
    cols = []
    for j in range(9):
        e = Entry(relief=RIDGE, width = 6)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '' )
        cols.append(e)
    rows.append(cols)
 
def onPress():
        Matrix = [[0 for x in range(9)] for x in range(9)] ;
    
       	x = 0;		
 
	for row in rows:
		y = 0;
		for col in row:
			if Validator(col.get()):
				Matrix[x][y] = int(col.get());
			elif col.get() == "": 
				Matrix[x][y] = 0 ;
			else:
				command = answer("Please enter values [1-9]");
				return;
			y = y +1;
 
		x = x + 1;
 
 #Check if all given inputs are correct
 
	for x in range(9):
		for y in range(9):
			if Matrix[x][y]>0 :
				temp = Matrix[x][y];
				Matrix[x][y] = 0;
				if not isSafe(Matrix, x, y, temp):
					print "Wrong Input";
					command = answer("Sorry, no answer available");
					return;
 
    
        for x in range(9):
                for y in range(9):
                        print Matrix[x][y],
                print
   
        if SolveSudoku(Matrix, 0, 0):
                for x in range(9):
                        for y in range(9):
                                print Matrix[x][y],
                        print
 
		x = 0;
		for row in rows:
			y = 0;
			for col in row:
				col.delete(0, END)	    
				col.insert(END,str(Matrix[x][y]))
				y = y +1;
 
			x = x + 1;
	else:
		 print "No sol"
		 command = answer("Sorry, no answer available")
 
 
def onClearPress():
	for row in rows:
		for col in row:
			col.delete(0, END)
 
 
 
 
Button(text='Solve', command=onPress).grid()
Button(text='Clear', command=onClearPress).grid()
mainloop() 