#Authors: Ayah 
#Date: 5/18/21

.data
Array: .word 4 14 24 21 3 6 2


.text
la $a0, Array
addi $a1, $0, 7		#length
jal Insert_Sort
	
li $v0, 10
syscall
	
Insert_Sort:
	addi $t0, $0, 1		# i = 1
	
	Outside_of_loop:
		beq $t0, $a1, fin
	
		#Holds a[i]
		sll $t3, $t0, 2		# t4 = i * 4
		add $t3, $t3, $a0
		lw $t3, 0($t3)		#val = $t4 = a[i]
	
		addi $t1, $t0, -1	# j = i - 1
	
	#for(j = i -1); j >= 0 && a[j] > val; j--)
	in:	
	
		slt $t2, $t1, $0	#t2 = 1 if j < 0
		bne $t2, $0, out	#jump out of inner loop if j isn't >= 0 
	
		#a[j] > val
		sll $t4, $t1, 2
		add $t4, $t4, $a0
		lw $t4, 0($t4)
		slt $t5, $t4, $t3	#$t5 = 1 if $t4 < val
		bne $t5, $0, out	#jump out of inner loop if a[j] isn't > val
		
		# a[j + 1] = a[j]
		addi $t6, $t1, 1	
		sll $t6, $t6, 2
		add $t6, $t6, $a0
		sw $t4, 0($t6)
		
		addi $t1, $t1, -1	# j--
		
		j in
	
	
	out:
		# a[j+1] = val
		addi $t7, $t1, 1
		sll $t7, $t7, 2
		add $t7, $t7, $a0
		sw $t3, 0($t7)
		
		addi $t0, $t0, 1	# i++
		
		j Outside_of_loop
	
	fin:
	jr $ra