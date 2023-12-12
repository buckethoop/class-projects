#Authors: Matthew Cheser and Ayah League
#Date: 5/12/21
#Sort Project: Insertion (Ayah) and Bubble(Matthew)

.data
array: .space 100   
sizeOfArray: .asciiz "Enter size of your array: "
msg1: .asciiz "Enter integer to be saved in array: "
outputmsg: .asciiz "\nSorted Array: "
spacemsg: .asciiz " "
choicemsg: .asciiz "Enter a 1 for Bubble Sort or a 2 for Insertion Sort: "

.text
main:      
	li $v0, 4				#syscall to print string
	la $a0, choicemsg 			#loads the string choicemsg into a0  
	syscall
	
	li $v0, 5				#syscall to read an integer
	syscall
	
	move $s2, $v0				#move choice number into register $s2
	
	li $v0, 4				#syscall to print string
	la $a0, sizeOfArray 			#loads the string sizeOfArray into a0  
	syscall

	li $v0, 5				#syscall to read an integer, to serve as the size variable
	syscall

	move $s1, $v0               		#move size variable into s1
	sub $s1, $s1, 1                		#s1 = s1 - 1, to account for index

	jal addintegertoarray          		#jump adding the integers to the array    

	la $a0,array  				#load the array in a0                      
	addi $a1,$s1,1   			#a1 = s1 + 1

	beq $s2, 1, ONE
	beq $s2, 2, TWO
	
	li $v0,4				#syscall to print string
	la $a0, outputmsg			#set outputmsg as the string to be printed
	syscall

	la $t0,array            		#load the array into t0            
	li $t1,0                  		#set t1 = 0 for loop counter        
	
	
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
    
	
bubblesort:
	li $t0, 0        			#load t0 = 0                    

	bubbleloop:

		addi $t0, $t0, 1                #t0 = t0 + 1   
		bgt $t0, $a1, bubbleend       	#if t0 > a1, go to bubbleend           
		move $t1, $a1             	#set t1 = a1
	
	bubbleinnerloop:

		bge $t0, $t1, bubbleloop    	#if t0 >= t1, go to bubbleloop         

		sub $t1,$t1,1              	#t1 = t1 - 1        
		sll $t4, $t1, 2             	#shift left        
		sub $t3, $t4, 4                 #t3 = t4 - 4
		add $t4, $t4, $a0       	#t4 = t4 + a0
		add $t3, $t3, $a0        	#t3 = t3 + a0             
		lw $t5, 0($t4)			#load values to be swapped
		lw $t6, 0($t3)			#load values to be swapped

bubbleswap:
	bgt $t5, $t6, bubbleinnerloop        	#if t5 > t6, go back and don't swap  
	sw $t5, 0($t3)                       	#swap t5 = t6
	sw $t6, 0($t4)				#swap t6 = t5
	j bubbleinnerloop			#jump back to bubbleinnerloop

bubbleend:                 		#set t1 = 0 for loop counter
	jr $ra					#jump back

#########################################
insertionsort:
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

ONE:
	jal bubblesort

TWO:
	jal insertionsort
	
	
	
	
	
	
	