#Author: Ayah
#date: 4/15/21
#Description: implement the code below

# n = prompt("enter the value to calculate the sum up to: ")
#total = 0;		#Initial the total variable for sum
#for(i=0; i < n; i++)
#{
#	total = total + i
#}
# print ("Total = " + total);

.data
input_prompt: .asciiz "Enter the value to calculate the sum up to: "
output_prompt: .asciiz "\n The total is: "
choice: .asciiz "\nTo exit enter -1 to continue enter another number: "

.text
main:
	first_loop:
		#print the choice message
		li $v0, 4
		la $a0, choice
		syscall
		
		#read the choice value and put in $t0
		li $v0, 5
		syscall 
		move $s0, $v0
		
		beq $s0, -1, exit_loop2
		
		# print the input prompt
		li $v0, 4
		la $a0, input_prompt
		syscall
	
		#read the value and put in $t0
		li $v0, 5
		syscall 
		move $t0, $v0
	
		li $t1, 0		#assign $t1 to total variable and initialize to 0
		li $t2, 0		#assign $t2 to i variable and initialize to 0
		
		for_loop:
			add $t1, $t1, $t2	#total = total + i
			addi $t2, $t2, 1	#i++
			blt $t2, $t0, for_loop	# if i < n go to for_loop
	
		exit_loop1:
			#print the output prompt
			li $v0, 4
			la $a0, output_prompt
			syscall
		
			#print the total value
			li $v0, 1
			move $a0, $t1
			syscall
		j first_loop
		
	exit_loop2:
		#syscall to exit
		li $v0, 10
		syscall
		
		
		
		
		
		
		
		
	