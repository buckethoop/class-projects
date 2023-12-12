#Author: Ayah League
#Date: 5/7/21
#Description:
#Implement a recursive function in MIPS assembly code which implements the following recurrence relation:
#The user will enter the number n. The output is the value of A(n). 
#	A(n) = 1, n=1
#	A(n) = A(n-1) +1, if n is even
#	A(n) = A(n-1) × 2, if n is odd
# n > 0
# n is small enough so that A(n) does not overflow
# n stored in $a0

.data
getn: .asciiz "Please enter n: "
output: .asciiz "Answer is: "

.text
main:
	#Print prompt getn 
 	li $v0, 4
 	la $a0, getn
 	syscall
 	
 	#read n
 	li $v0, 5
 	syscall
 	move $s0, $v0
 	
 	#Call function
 	move $a0, $s0
 	jal A
 	move $s0, $v0		#save the return value in $s0 to avoid $v0 overwrite
 	
 	#Print prompt output
 	li $v0, 4
 	la $a0, output
 	syscall
 	
 	#Print answer
 	li $v0, 1
 	move $a0, $s0
 	syscall

 	li $v0, 10
 	syscall
 		
A:
	#push needed values on the stack
	addi $sp, $sp, -8 
	sw $ra, 0($sp)     
	sw $s0, 4($sp)

	li $v0, 1
	beq $a0, 1, base_case		#go to base case if n = 1
	
	#Call A(n-1)
	move $s0, $a0
	sub $a0, $a0, 1
	jal A
	
	#body
	#check even or odd
	and $s1, $s0, 1			#compares numbers bit by bit
	beq $s1, 0, Even
	beq $s1, 1, Odd
	
	base_case:
		#pop values from stack
		lw $ra, ($sp)
		lw $s0, 4($sp)
		add $sp, $sp, 8
		jr $ra
	
	Even:
		add $v0, $v0, 1		# A(n-1) + 1
		j base_case
	
	Odd:
 		mul $v0, $v0, 2		# A(n-1) * 2
 		j base_case
 		
 		
 		
 		
 		
 		
 		
 		