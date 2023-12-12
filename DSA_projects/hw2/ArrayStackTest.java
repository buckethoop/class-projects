package project2;

public class ArrayStackTest 
{
	public static void main (String[] args)
	{
		//postfix expression to be evaluated
		String postfix = "a b * c a - / d e * +";
		
		System.out.println(evaluatePostfix(postfix));
	}
	
	public static int evaluatePostfix(String postfix)
	{	// Evaluates a postfix expression.
		StackInterface<Integer> valueStack = new ResizeableArrayStack<>();
		int count = 0;
	
		//continues iterating as long as there are items left in the postfix expression
		while(count < postfix.length())
		{
			char nextCharacter = postfix.charAt(count);
		
			//checks to see if character is a part of the alphabet and assigns 
			//certain letters a value, ignores spaces
			if(Character.isAlphabetic(nextCharacter) || nextCharacter == ' ')
			{
				switch(nextCharacter)
				{
				//assigns value of 2 to a
				case 'a':
					valueStack.push(2);
					break;
				//assigns value of 3 to b
				case 'b':
					valueStack.push(3);
					break;
				//assigns value of 4 to c
				case 'c':
					valueStack.push(4);
					break;
				//assigns value of 5 to d
				case 'd':
					valueStack.push(5);
					break;
				//assigns value of 6 to e
				case 'e':
					valueStack.push(6);
					break;
				//skips any spaces in the expression
				default :
					break;
				}
			}
			
			else
			{
				int top1 = valueStack.pop();
				int top2 = valueStack.pop();
				
				switch (nextCharacter)
				{
				//takes two top most values in the stack,adds them
				//and pushes the result back onto the stack 
				case '+' : 
					valueStack.push(top2+top1);
					break;
				//takes two top most values in the stack,subtracts them
				//and pushes the result back onto the stack
				case '-' : 
					valueStack.push(top2-top1);
					break;
				//takes two top most values in the stack,multiplies them
				//and pushes the result back onto the stack
				case '*' : 
					valueStack.push(top2*top1);
					break;
				//takes two top most values in the stack,divides them
				//and pushes the result back onto the stack
				case '/' : 
					valueStack.push(top2/top1);
					break;
				//takes two top most values in the stack,raises top2 to the top1st power
				//and pushes the result back onto the stack
				case '^' :
					valueStack.push(top2^top1);
					break;
				default : 
			    	valueStack.push(top2);
			    	valueStack.push(top1);
					break; 
				}
			}
			//allows for the while loop to access the next character in the expression
			++count;
		}
		//returns top of the stack which holds the value of the postfix expression
		return valueStack.peek();
	}
}