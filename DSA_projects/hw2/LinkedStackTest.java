package project2;

public class LinkedStackTest
{
	public static void main (String[] args)
	{
		//infix expression to be converted
		//works with and without spaces
		
		String infix = "a * b / ( c - a ) + d * e";		
		
		System.out.println(convertToPostfix(infix));
	}
	//sets a precedence for each operator
	public static int getPrecedence(char ch)
	{
		switch(ch)
		{
		case '^':
			return 3;
		case '*':
		case '/':
			return 2;
		case '+':
		case '-':
			return 1;
		}
		return -1;
	}
	
	// Converts an infix expression to an equivalent postfix expression.
	public static String convertToPostfix(String infix)
	{
		StackInterface<Character> operatorStack = new LinkedStack<>();
		String postfix = new String("");
		int count = 0;
		
		while (count < infix.length())
		{
			char nextCharacter = infix.charAt(count);
			switch(nextCharacter)
			{
				//pushes nextCharacter to the operatorStack for case ^
				case '^' :
					operatorStack.push(nextCharacter);
					break;
				//Appends nextCharacter to postfix as long as operatorStack isn't empty and precedence for nextCharacter is 
				//less than or equal to precedence of the top item of the operatorStack 
				case '+' : 
				case '-' : 
				case '*' : 
				case '/' :
					while (!operatorStack.isEmpty() && getPrecedence(nextCharacter) <= getPrecedence(operatorStack.peek()))
					{
						//Append operatorStack.pop() to postfix
						postfix += operatorStack.pop();
					}
					operatorStack.push(nextCharacter);
					break;
				//pushes '(' on operatorStack
				case '(' :
					operatorStack.push(nextCharacter);
					break;
				case ')' : // Stack is not empty if infix expression is valid
					while (!operatorStack.isEmpty() && operatorStack.peek() != '(')
					{
						//Append topOperator to postfix
						postfix += operatorStack.pop();
					}
					operatorStack.pop();
					break;
				default: 
					if(Character.isLetterOrDigit(nextCharacter))
						postfix += nextCharacter;
					break; // Ignore unexpected characters
		}
		
		++count;
	}
	//pops all operators from operatorStack
	while (!operatorStack.isEmpty())
	{
		postfix += operatorStack.pop();
	}
	//returns a converted infix expression
	return postfix;
	}
}
