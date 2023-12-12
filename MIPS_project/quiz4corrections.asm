#author: Ayah
#date: 4/6/2021
#description: Quiz 4 corrections
#Translate the c code to MIPS
# if (f==g)
#	A[4] = f + g;
# else if (f==h)
#	A[4] = A[h] + f;
#    else
#	 A[i] = g - h;
# the variables f, g, h, i, and j are assigned to registers $s0, $s1, $s2, $s3, and $s4, respectively
# Assume that the base of the address of the arrays A is in register $s6.
.data
f: .word 12
g: .word 3
h: .word 6
i: .word 4
t: .word 2
A: .space 100

.text
main:
	lw $s0, f
	lw $s1, g
	lw $s2, h
	lw $s3, i
	lw $s4, t
	la $s6, A
	
	bne $s0, $s1, elseif		# if f<>g go to elseif
	add $t0, $s0, $s1		#t0 = f + g
	sw $t0, 16($s6)			# A[4] = f + g
	j exit				#exit the code
	elseif:
		bne $s0, $s2, else	# if f<>h go to else
		# Read A[h]
		sll $t0, $s2, 2		# $t0 = h+4 (offset of A[h])
		add $t1, $t0, $s6	# new base address to avoid using register as offset
		lw $t2, 0($t1)		# t2 = A[h]
		#Add A[h] and f
		add $t3, $t2, $s0 	#$t3 = A[h] + f
		sw $t3, 16($s6) 	# A[4] = A[h] + f
		j exit
		else:
			sub $t4, $s1, $s2	# $t4 = g-h
			sll $t0, $s3, 2 	#$t0 = i * 4 (offset A[i])
			add $t1, $t0, $s6	# $t1 is a new base @
			sw $t4, 0($t1)		#A[i] = g-h
			
	exit:
		li $v0, 10
		syscall 