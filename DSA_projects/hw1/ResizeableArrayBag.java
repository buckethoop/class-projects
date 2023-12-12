package project1;

import java.util.Arrays;

public class ResizeableArrayBag<T> implements BagInterface<T>
{
	private T[] bag;
	private static final int DEFAULT_CAPACITY = 25;
	private int numberOfEntries;
	private boolean integrityOK = false;
	private static final int MAX_CAPACITY = 10000;
	
	//default constructor
	public ResizeableArrayBag() 
	{
		this(DEFAULT_CAPACITY);
	}
	
	//constructor
	public ResizeableArrayBag(int desiredCapacity)
	{
		if(desiredCapacity <= MAX_CAPACITY)
		{
			@SuppressWarnings("unchecked")
			T[] tempBag = (T[])new Object[desiredCapacity];
			bag = tempBag;
			numberOfEntries = 0;
			integrityOK = true;
		}
		
		else
			throw new IllegalStateException("Attempt to create a bag whose "
											+ "capacity exceeds allowed maximum.");
	}
	
	//gets the current number of entries in the bag
	public int getCurrentSize()
	{
		return numberOfEntries;
	}
	//sees whether this bag is empty
	public boolean isEmpty()
	{
		return numberOfEntries == 0;
	}
	//adds a new entry to this bag
	public boolean add(T newEntry) 
	{
		checkIntegrity();
		
		if(isFull())
		{
			doubleCapacity();
		}
		
		bag[numberOfEntries] = newEntry;
		numberOfEntries++;
		
		return true;
	}
	//removes one unspecified entry from this bag, if possible
	public T remove()
	{
		checkIntegrity();
		T result = removeEntry(numberOfEntries - 1);
		return result;
	}
	//removes one occurrence of a given entry from this bag, if possible
	public boolean remove (T anEntry)
	{
		checkIntegrity();
		int index = getIndexOf(anEntry);
		T result = removeEntry(index);
		return anEntry.equals(result);
	}
	//removes all entries from this bag
	public void clear()
	{
		while(isEmpty())
			remove();
	}
	//counts the number of times a given entry appears in this bag
	public int getFrequencyOf(T anEntry)
	{
		checkIntegrity();
		int counter = 0;
		for(int index = 0; index < numberOfEntries; index++)
		{
			if(anEntry.equals(bag[index]))
				counter++;
		}
		
		return counter;
	}
	//tests whether this bag contains a given entry
	public boolean contains(T anEntry)
	{
		checkIntegrity();
		return getIndexOf(anEntry) > -1;
	}
	
	//checks to see if array bag is full 
	public boolean isFull()
	{
		return numberOfEntries == bag.length;
	}
	//returns a bag that consists of all contents in two collections
	public BagInterface<T> union(BagInterface<T> otherBag)
	{
		//create result bag that will contain the union
		BagInterface<T> last =  new ResizeableArrayBag<>();
		T[] first = this.toArray();
		//adds each item in first array to last
		for(T item: first)
			last.add(item);
		
		T[] second = otherBag.toArray();
		//adds each item in second array to last
		for(T item: second)
			last.add(item);
		
		return last;
		
	}
	//returns a bag that consists of the entries that occur in both collections
	public BagInterface<T> intersection(BagInterface<T> otherBag)
	{
		BagInterface<T> last = new ResizeableArrayBag<>();
		BagInterface<T> result = new ResizeableArrayBag<>();
		
		T[] first = this.toArray();
		//adds each element in first array to temporary bag
		for(T item: first)
			last.add(item);
		
		T[] second = otherBag.toArray();
		for(T item: second) //iterates through the second array
			if(last.contains(item)) //checks to see if temp array contains elements in second array
				result.add(item); //if this is true the element is added to the result array
		
		return result;
	}
	
	//returns a bag that consists of the entries left in one collection after
	//removing the entries the occur in the second collection
	public BagInterface<T> difference(BagInterface<T> otherBag)
	{
		BagInterface<T> last = new ResizeableArrayBag<>();
		T[] first = this.toArray();
		//adds each element in the first array to the last array
		for(T item : first)
			last.add(item);
		
		T[] second = otherBag.toArray();
		for(T item : second) //iterates through second array
			if(last.contains(item)) //checks to see if temp array contains elements in second array
				last.remove(item);  //if this is true the element is removed from the last array
		
		return last;
	}
	
	//throws an exception if the object is not initialized
	private void checkIntegrity()
	{
		if(!integrityOK)
			throw new SecurityException("ArrayBag object is corrupt.");
	}
	//throws an exception if the client requests a capacity that is too large
	private void checkCapacity(int capacity)
	{
		if(capacity > MAX_CAPACITY)
			throw new IllegalStateException("Attempt to create a bag whose" 
		                                    + "capacity exceed allowed" 
					                        + "maximum of" + MAX_CAPACITY);
	}
	//doubles the size of the array bag
	private void doubleCapacity()
	{
		int newLength = 2 * bag.length;
		checkCapacity(newLength);
		bag = Arrays.copyOf(bag, newLength);
	}
	//locates a given entry within the array bag
	private int getIndexOf(T anEntry)
	{
		int where = -1;
		boolean found = false;
		int index = 0;
		
		while(!found && (index < numberOfEntries))
		{
			if(anEntry.equals(bag[index]))
			{
				found = true;
				where = index;
			}
			index++;
		}
		
		//if where > -1, anEntry is in the array bag, and it 
		//equals bag[where]; otherwise, anEntry is not in the array
		return where;
	}
	//removes a given entry in this bag if possible 
	private T removeEntry(int givenIndex)
	{
		T result = null;
		
		if(!isEmpty() && (givenIndex >= 0))
		{
			result = bag[givenIndex];
			bag[givenIndex] = bag[numberOfEntries - 1];
			bag[numberOfEntries - 1] = null;
			numberOfEntries--;
		}
		
		return result;
	}
	//retrieves all entries that are in this bag
	public T[] toArray()
	{
		@SuppressWarnings("unchecked")
		T[] result = (T[])new Object[numberOfEntries];
		
		for(int index = 0; index < numberOfEntries; index++)
			result[index] = bag[index];
		
		return result;
	}

}
