#Authors: Ayah League and Matthew Cheser
#Date: 5/18/21
#Sort Project: Inserttion (Ayah) and (Matthew)

.data



.text


jal Insert_Sort
		
printArray:
	lw $a0, 0($t0)             		#load the array at index 
	li $v0, 1				#syscall to print integer
	syscall

	li $v0, 4				#syscall to print string
	la $a0, spacemsg			#set spacemsg to br printed
	syscall
	
	addi $t0,$t0,4             		#move the array to next index         
	addi $t1,$t1,1                 	 	#set t1 = 1    
	slt $t2,$s1,$t1                	 	#set t2 = s1 if s1 < t1   
	beq $t2,$zero,printArray 		#if t2 = 0, go to print array
            
	li $v0,10           			#syscall to exit program                
	syscall

addintegertoarray:

	li $v0, 4                     		#syscall to print string
	la $a0, msg1                		#put msg1 as the string to be printed
	syscall

	li $v0, 5				#syscall to take in an int
	syscall

	move $t3,$v0                        	#t3 = v0
	addi $t1, $zero, 0              	#t1 = 0
	sll $t1,$t0,2       			#shift left                
	sw $t3, array($t1)      		#store t3 into array          
	addi $t0, $t0, 1                      	#t0 = t0 + 1
	slt $t1, $s1, $t0                     	#set t1 = s1, if s1 < t0
	beq $t1, $zero, addintegertoarray	#if t1 = 0, go to addintegertoarray
	
Insert_Sort:
	addi $t0, $0, 1		#i =1
	
	Outside_of_loop:
		beq $t0, $a1, fin
	
		#Holds a[i]
		sll $t3, $t0, 2		# t4 = i * 4
		add $t3, $t3, $a0
		lw $t3, 0($t3)		#val = $t4 = a[i]
	
		#for(j = i -1); j >= 0 && a[j] > val; j--)
		addi $t1, $t0, -1
	
	in:
		slt $t2, $t1, $0	#t2 = 1 if j < 0
		bne $t2, $0, out
	
		#a[j] > val
		sll $t4, $t1, 2
		add $t4, $t4, $a0
		lw $t4, 0($t4)
		slt $t5, $t4, $t3	#$t5 = 1 if $t4 < val
		bne $t5, $0, out
		
		# a[j +1] = a[j]
		addi $t6, $t1, 1
		sll $t6, $t6, 2
		add $t6, $t6, $a0
		sw $t4, 0($t6)
		addi $t1, $t1, -1
	
		j in
	
	out:
		# a[j+1] = val
		addi $t7, $t1, 1
		sll $t7, $t7, 2
		add $t7, $t7, $a0
		sw $t3, 0($t7)
		addi $t0, $t0, 1
		j Outside_of_loop
	
	fin:
	jr $ra