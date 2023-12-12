#Author: Ayah League
#Date: 4/29/21
#Description: Translate the following C code to MIPS
#int fib(int n)
#{
#    // Stop condition
#    if (n == 0)
#        return 0;
# 
#    // Stop condition
#    if (n == 1 || n == 2)
#        return 1;
# 
#    // Recursion function
#    else
#        return (fib(n - 1) + fib(n - 2));
#}
#main()
#{
#    // get n from user.
#    cout<<"Please enter n: ";
#    cin>> n;
# 
#    // Output is series of Fibonacci
#    cout<<"Fibonacci series of 5 numbers is: ";
# 
#    // for loop to print the fiboancci series.
#    for (int i = 0; i < n; i++)
#    {
#        cout<<fib(i)<<" ";
#    }
# 
#}

# n is saved in $a0

.data
getn: .asciiz "Please enter n: "
output: .asciiz "Fibonacci series of n is: "


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
 	
 	#Call fibonnacci 
 	move $a0, $t2
 	move $v0, $t2
 	jal fib
 	move $t3, $v0
 	
 	#Print prompt output
 	li $v0, 4
 	la $a0, output
 	syscall
 	
 	# for loop
 	li $t0, 0		#i is assigned to $t0
 	for_loop:
 		beq $t0, $s0, exit
 		move $a0, $t0		# i is argument for fib(i)
 		jal fib			#call fib(i)
 		move $a0, $v0		#save fib(i) in $a0
 		
 		# print fib value
 		li $v0, 1
 		syscall	
 		addi $t0, $t0, 1	# i++
 		j for_loop
	exit:
		li $v0, 10
		syscall
	
fib:
	#push needed values on the stack
	addi $sp, $sp, -12 
	sw $ra, 0($sp)     
	sw $a0, 4($sp)
	sw $s2, 8($sp)
	
	#body
	beq $a0, $0, Zero			#if n = 0 go to L1
	ble $a0, 2, One				#if n = 1 or 2 go to L2

	#call fib(i-1)
	addi $a0, $a0, -1
	jal fib
	move $s2, $v0				#s2 = fib(i-1)
	
	lw $a0, 4($sp)
	
	#call fib(i-2)
	move $a0, $s2
	addi $a0, $a0, -2			# n-2
	jal fib					# fib(n-2)
	
	#fib(i-1) + fib(i-2)
	add $v0, $s2, $a0			# return fib(i-1) + fib(i-2)
	
	#pop result from stack
	lw $s0, 8($sp)     
	lw $ra, 0($sp)    
	addi $sp, $sp, 12
	jr $ra
	
	Zero:
		lw $s0, 8($sp)     
		lw $ra, 0($sp)    
		addi $sp, $sp, 12
		li $v0, 0			#return 0
		jr $ra
	
	One:
		lw $s0, 8($sp)     
		lw $ra, 0($sp)    
		addi $sp, $sp, 12
		li $v0, 1			#return 1
 		jr $ra
	
	#pop saved values from stack 
 	addi $sp, $sp, 16
	
	#carries out the rest of the else 
	add $v0, $t0, $t1		# (fib(n - 1) + fib(n - 2))	
	beqz $ra, exit
	jr $ra











