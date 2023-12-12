 #Author: Ayah
 #Date: 4/13/21
 #Description: simple code for while loop
 #The code will read an integer and print this integer
 #the code will exit only if the integer is -1
 
 .data
 message1: .asciiz "\nPlease enter your integer: "
 message2: .asciiz "Your integer is: "
 message3: .asciiz "Goodbye!"
 
 .text
 main:
 
 	#display the message to enter integer i
 	li $v0,4
 	la $a0, message1
 	syscall 
 
 	#Read the integer i
 	li $v0, 5 
 	syscall
 	move $s0, $v0		#here the register value is in $s0
 	
 	start_loop:
 		beq $s0, -1, exit_loop
 		#print the message2
 		li $v0,4
 		la $a0, message2
 		syscall
 		
 		#print integer value
 		li $v0, 1
 		move $a0, $s0
 		syscall
 		
 		#ask for new integer
 		li $v0,4
 		la $a0, message1
 		syscall
 		
 		#Read the new integer i
 		li $v0, 5 
 		syscall
 		move $s0, $v0		#here the register value is in $s0
 		j start_loop
 		
 	exit_loop:
 		#print the message3
 		li $v0,4
 		la $a0, message3
 		syscall
 		
 		li $v0,10
 		syscall
 		
 		
 		
 		
 		
 		
 		
 		
 		