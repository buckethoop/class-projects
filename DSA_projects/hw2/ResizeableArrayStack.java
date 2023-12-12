package project2;

import java.util.Arrays;
import java.util.EmptyStackException;

public final class ResizeableArrayStack <T> implements StackInterface <T>
{
	private T[] stack;
	private int topIndex;
	private boolean integrityOK = false; 
	private static final int DEFAULT_CAPACITY = 50;
	private static final int MAX_CAPACITY = 10000;
	
	public ResizeableArrayStack()
	{
		this(DEFAULT_CAPACITY);
	}
	
	public ResizeableArrayStack(int initialCapacity)
	{
		integrityOK = false; 
		checkCapacity(initialCapacity);
		
		@SuppressWarnings("unchecked")
		T[] tempStack = (T[]) new Object[initialCapacity];
		stack = tempStack;
		topIndex = -1;
		integrityOK = true;
	}

	public void push(T newEntry) 
	{
		checkIntegrity();
		ensureCapacity();
		stack[topIndex + 1] = newEntry;
		topIndex++;
	}

	public T pop() 
	{
		checkIntegrity();
		if(isEmpty())
			throw new EmptyStackException();
		else
		{
			T top = stack[topIndex];
			stack[topIndex] = null;
			topIndex--;
			return top;
		}
	}

	public T peek() 
	{
		checkIntegrity();
		if(isEmpty())
			throw new EmptyStackException();
		else 
			return stack[topIndex];
	}

	public boolean isEmpty() 
	{
		return topIndex < 0;
	}

	public void clear()
	{
		checkIntegrity();
		while(topIndex > -1)
		{
			stack[topIndex] = null;
			topIndex--; 
		}
	}
	//double size of array if full
	private void ensureCapacity()
	{
		if(topIndex >= stack.length - 1)
		{
			int newLength = 2 * stack.length;
			checkCapacity(newLength);
			stack = Arrays.copyOf(stack, newLength);
		}
	}
	
	private void checkCapacity(int capacity)
	{
		if(capacity > MAX_CAPACITY)
			throw new IllegalStateException("Attempt to create a stack whose" 
		                                    + "capacity exceed allowed" 
					                        + "maximum of" + MAX_CAPACITY);
	}
	
	private void checkIntegrity()
	{
		if(!integrityOK)
			throw new SecurityException("ArrayBag object is corrupt.");
	}

}
