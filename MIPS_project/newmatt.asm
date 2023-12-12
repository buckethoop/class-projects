#Authors: Matthew Cheser
#Date: 5/12/21

.data
array: .space 100   
sizeOfArray: .asciiz "Enter size of your array: "
msg1: .asciiz "Enter integer to be saved in array: "
outputmsg: .asciiz "\nSorted Array: "
spacemsg: .asciiz " "

.text
main:
                  
	li $v0, 4				#syscall to print string
	la $a0, sizeOfArray 			#loads the string sizeOfArray into a0  
	syscall

	li $v0, 5				#syscall to read an integer, to serve as the size variable
	syscall

	move $s1, $v0               		 #move size variable into s1
	sub $s1, $s1, 1                		 #s1 = s1 - 1, to account for index

	jal addintegertoarray          		 #jump adding the integers to the array    

	la $a0,array  				#load the array in a0                      
	addi $a1,$s1,1   			#a1 = s1 + 1                   

	jal bubblesort                		#jump to bubble sort            

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

bubbleend:
	jr $ra					#jump back
