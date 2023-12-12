#author: Ayah
#date: 4/8/2021
#description: examples for sycalls

.data
prompt: .asciiz "The Integer value is: "
greeting: .asciiz "Hello Class CS2640, that is my code of MIPS\n"
stars: .asciiz "******************************************\n"
first_N: .asciiz "Please enter your first number: "
second_N: .asciiz "Please enter your second number: "
.text
main:
	la $a0, stars
	li $v0, 4
	syscall
	
	la $a0, greeting	#greeting is the string to be printed
	li $v0, 4		#4 is the syscall code to print string
	syscall			#print the string in $a0
	 
	
	#Print prompt for first number
	la $a0, first_N
	li $v0, 4
	syscall
	
	#Read the first number
	li $v0, 5
	syscall
	move $t0, $v0
	
	#Print the prompt to get the second number
	la $a0, second_N
	li $v0, 4
	syscall
	
	#Read the second number
	li $v0, 5
	syscall
	move $t1, $v0
	
	#Add the two numbers
	add $t2, $t0, $t1
	
	#Print the result
	la $a0, prompt		#prompt is the string to be printed
	li $v0, 4		#4 is the syscall code to print string
	syscall			#print the string in $a0
	
	move $a0, $t2
	li $v0, 1		#1 is the sycall code for printing an integer
	syscall			#print the integer