#Author: Ayah
#Date:
#Description:

#input n
#input m
#sum = 0
# for (int i = 1; i <= 5; ++i)
#{
#	System.out.println("Outer loop iteration " + i);
#
#	for (int j = 1; j <=2; ++j)
#	{
#		System.out.println("i = " + i + "; j = " + j);
#	}
#}
#print sum

.data
input_n: .asciiz "\nPlease enter n: "
input_m: .asciiz "\nPlease enter m: "
output_sum: .asciiz "\nThe sum is: "


.text
main:
	#print the input n message
	li $v0, 4
	la $a0, input_n
	syscall
		
	#read the n
	li $v0, 5
	syscall 
	move $s0, $v0
	
	#print the input m message
	li $v0, 4
	la $a0, input_m
	syscall
		
	#read the m
	li $v0, 5
	syscall 
	move $s1, $v0

	li $s2, 0	#assign s2 to some variable
	li $t0, 0	#assign t0 to i
	
	for_i_loop:
		li $t1, 0	#assign t1 to j
		
		for_j_loop:
			add $s2, $s2, $t1	#sum = sum +j
			addi $t1, $t1, 1		#j++
			blt $t1, $s1, for_j_loop
			
		add $t0, $t0, 1
		blt $t0, $s0, for_i_loop
	exit:
		#print the output n message
		li $v0, 4
		la $a0, output_sum
		syscall
	
		#print the total value
		li $v0, 1
		move $a0, $s2
		syscall
		
		#syscall to exit
		li $v0, 10
		syscall
	
	
	
	













