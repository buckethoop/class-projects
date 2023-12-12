#author: Ayah League
#date: 4/10/2021
#description: Quiz 6
#Making the MIPS code from Tuesday's class interactive.

.data
greeting: .asciiz "This is Ayah League and here is my solution for Quiz 6.\n"
Read_f: .asciiz "Please enter an integer for f: "
Read_g: .asciiz "Please enter an integer for g: "
Read_h: .asciiz "Please enter an integer for h: "
Read_i: .asciiz "Please enter an integer for i: "

Result1: .asciiz "The result of A[4] = f + g: "
Result2: .asciiz "The result of A[4] = A[h] + f: "
Result3: .asciiz "The result of A[i] = g-h: "

i: .word 12
A: .space 100

.text
main:
	lw $s3, i
	la $s6, A
	
	#Print greeting
	la $a0, greeting
	li $v0, 4
	syscall
	
	#Print prompt for f
	la $a0, Read_f
	li $v0, 4
	syscall
	
	#Read the f
	li $v0, 5
	syscall
	move $s0, $v0
	
	#Print the prompt to get g
	la $a0, Read_g
	li $v0, 4
	syscall
	
	#Read the g
	li $v0, 5
	syscall
	move $s1, $v0
	
	bne $s0, $s1, elseif		# if f<>g go to elseif
	add $t0, $s0, $s1		#t0 = f + g
	sw $t0, 16($s6)			# A[4] = f + g
	
	#Print the result
	la $a0, Result1		#prompt is the string to be printed
	li $v0, 4		#4 is the syscall code to print string
	syscall			#print the string in $a0
	
	move $a0, $t0
	li $v0, 1		#1 is the sycall code for printing an integer
	syscall			#print the integer
	j exit				#exit the code
	
	elseif:
		#Print prompt for h
		la $a0, Read_h
		li $v0, 4
		syscall
	
		#Read the h
		li $v0, 5
		syscall
		move $s2, $v0
		
		bne $s0, $s2, else	# if f<>h go to else
		# Read A[h]
		sll $t0, $s2, 2		# $t0 = h+4 (offset of A[h])
		add $t1, $t0, $s6	# new base address to avoid using register as offset
		lw $t2, 0($t1)		# t2 = A[h]
		#Add A[h] and f
		add $t3, $t2, $s0 	#$t3 = A[h] + f
		sw $t3, 16($s6) 	# A[4] = A[h] + f
		
		#Print the result
		la $a0, Result2		#prompt is the string to be printed
		li $v0, 4		#4 is the syscall code to print string
		syscall			#print the string in $a0
	
		move $a0, $t3
		li $v0, 1		#1 is the sycall code for printing an integer
		syscall			#print the integer
		j exit				#exit the code
		
		else:
			#Print prompt for i
			la $a0, Read_i
			li $v0, 4
			syscall
	
			#Read the i
			li $v0, 5
			syscall
			move $s3, $v0
			
			
			sll $t0, $s3, 2 	#$t0 = i * 4 (offset A[i])
			add $t1, $t0, $s6	# $t1 is a new base @
			sub $t4, $s1, $s2	# $t4 = g-h
			sw $t4, 0($t1)		#A[i] = g-h
			
			#Print the result
			la $a0, Result3		#prompt is the string to be printed
			li $v0, 4		#4 is the syscall code to print string
			syscall			#print the string in $a0
	
			move $a0, $t4
			li $v0, 1		#1 is the sycall code for printing an integer
			syscall			#print the integer
			
		
	exit:
		li $v0, 10
		syscall 