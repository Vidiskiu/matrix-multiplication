import sys

def newline():
	print ""

def matrixDisplay(matrix,row,column):
	for i in range(0, row):
		for j in range(0, column):
			print matrix[i][j], "\t",
		print "\n"

def matrixInput(matrix,row,column):
	for i in range(0, row):
		for j in range(0, column):
			print "Row ", i+1, " Column ", j+1," : ",
			matrix[i][j] = int(raw_input())

def matrixMultiplication(matrix1,row_A,col_A,matrix2,row_B,col_B,matrix3):
	for i in range(0, row_A):
		for j in range(0, col_B):
			for k in range(0, col_A):
				matrix3[i][j] += matrix1[i][k]*matrix2[k][j]

newline()
print "Enter Row & Column of matrix A :"
row_A = int(raw_input())
col_A = int(raw_input())
print "Enter Row & Column of matrix B :"
row_B = int(raw_input())
col_B = int(raw_input())

if(col_A!=row_B):
	print "Make sure that Column of A = Row of B"
	sys.exit()

A = [([0] * col_A) for i in range(row_A)]
B = [([0] * col_B) for i in range(row_B)]
C = [([0] * col_B) for i in range(row_A)]

newline()
print "Enter data of matrix A : "
matrixInput(A,row_A,col_A)

print "Enter data of matrix B : "
matrixInput(B,row_B,col_B)

matrixMultiplication(A,row_A,col_A,B,row_A,col_B,C)

newline()
print "MATRIX A\n"
matrixDisplay(A,row_A,col_A)

print "MATRIX B\n"
matrixDisplay(B,row_B,col_B)

print "MATRIX C\n"
matrixDisplay(C,row_A,col_B)