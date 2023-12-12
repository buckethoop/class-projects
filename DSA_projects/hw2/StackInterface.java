package project2;

public interface StackInterface<T> 
{
	//adds new entry to top of stack
	public void push(T newEntry);
	//removes and returns stacks top entry
	public T pop();
	//retrieves stacks top entry
	public T peek();
	//detects if stack is empty
	public boolean isEmpty();
	//removes all entries from stack
	public void clear();
}
