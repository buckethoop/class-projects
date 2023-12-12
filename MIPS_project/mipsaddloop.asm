 #Author: Ayah
 #Date: 4/13/21
 #Description: simple code for while loop
 #The code will read an integer and print this integer
 #the code will exit only if the integer is -1
 
 .data
 welcome: .asciiz "\n Welcome to add program. This code adds two integers. To exit type -1."
 message0: .asciiz "\nThe result of addition is: "
 
 message1: .asciiz "\nPlease enter your first number: "
 message2: .asciiz "\nPlease enter your second number: "
 message3: .asciiz "\nPlease enter -1 if you want to exit. "
 
 .text
 main:
 	start_loop:
 	#display the welcome message to enter integer i
 	li $v0,4
 	la $a0, welcome
 	syscall 
 
 	#display message three
 	li $v0,4
 	la $a0, message3
 	syscall 
 	
 	#Read the integer i
 	li $v0, 5 
 	syscall
 	move $s0, $v0		#here the register value is in $s0
 	
 		beq $s0, -1, exit_loop
 		
 		#print message1
 		li $v0,4
 		la $a0, message1
 		syscall
 		
 		#read first integer and put in $t0
 		li $v0, 5
 		syscall
 		move $t0, $v0		#the first number is in $t0
 		
 		#print message2
 		li $v0,4
 		la $a0, message2
 		syscall
 		
 		#print second integer and put in $t1
 		li $v0, 5
 		syscall
 		move $t1, $v0		#the first number is in $t1
 		
 		#Do addition
 		add $t2, $t0, $t1	#addition result saved in $t2
 		
 		#print message0
 		li $v0,4
 		la $a0, message0
 		syscall
 		
 		#print result
 		li $v0, 1
 		move $a0, $t2
 		syscall
 		
 		j start_loop
 		
 	exit_loop:	
 		li $v0,10
 		syscall
 		
 		
 		
 		
 		
 		
 		
 		
 		