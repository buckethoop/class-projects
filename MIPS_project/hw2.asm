#Authors: Ayah League and Matthew Cheser (Group 5)
#Date: 4/22/21

#int array = {2,5,1, 9, 30, 4, 25, 10, 40, 56, 23, 17, 8, 3, 6}

#Description: Code sorts data in table from highest to lowest. 
#Data is then saved in memory where the 
#highest value is in the smallest memory location. 

.data
#Making the Array
Array: .word 2, 5, 1, 9, 30, 4, 25, 10, 40, 56, 23, 17, 8, 3, 6
size: .word 15

result: .asciiz "The sorted Array: "
spaces: .asciiz " "

.text
main: 
	la $t0, Array		#store base address for Array @ $t0
	lw $t1, size		#load size of the Array to $t1
	li $t2, 1		#set $s2 to be loop int starting at 1
	
	sort_loop1:
		la $t0, Array				#loads address of Array @ $t0
		bge $t2, $t1, sort_loop1_end		#if $t2 >= $t1, go to sort_loop1_end
		move $t3, $t2				#move $t2 to $t3
		
	sort_loop2:
		la $t0, Array				#loads address of Array @ $t0
		sll  $t5, $t3, 2			#$t5 = $t3 multiplied by 4
		add $t0, $t0, $t5			#new base address of $t5 value
		ble $t3, $0, sort_loop2_end		#if $t3 <= $0 then go to sort_loop2_end
		lw $t7, -4($t0) 			#load value into $t7
		lw $t6, 0($t0)				#load value into $t6
		bge $t7, $t6, sort_loop2_end		#if $t7 >= $t6 then go to sort_loop2_end
		lw $t4, -4($t0)				#load value into $t4
		sw $t6, -4($t0)				#store $t6 into memory location
		sw $t4, 0($t0)				#store $t4 into memory location
		subi $t3, $t3, 1			#$t3 = $t3 - 1
		j sort_loop2				#jump to sort_loop2
	
	sort_loop2_end:
		addi $t2, $t2, 1			#$t2 = $t2 + 1 / increases loop counter
		j sort_loop1				#jump to sort_loop1
	
	sort_loop1_end:
		li $v0, 4				#System call to print string
		la $a0, result				#Sets up for system call to print the 'result' string
		syscall					
	
	setArray:
		la   $t0, Array				#loads address of Array @ $t0
		lw   $t1, size				#loads size of Array @ $t1
		li   $t2, 0				#sets value of $t2 = 0 for intial int
		jal printArray				#jumps to printArray				
	
	printArray:
		bge   $t2, $t1, exit			#if $t2 >= $t1 then go to exit (tells if not properly sorted)
		li   $v0, 1				#System call to print an int
		lw   $a0, 0($t0)			#loads the int to be printed into $a0
		syscall					
		li   $v0, 4				#System call for string to be printed
		la   $a0, spaces			#loads string 'spaces' to be printed (puts a space in between ints
		syscall					
		addi   $t0, $t0, 4			#$t0 = $t0 + 4 (moves to next number in Array)
		addi   $t2, $t2, 1			#$t2 = $t2 + 1 (moves int to hold the current position in Array)
		j   printArray				#jumps back to start of printArray
	
	exit:
		li $v0, 10				#System call to exit
		syscall					
	



