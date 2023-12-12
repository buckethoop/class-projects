package project1;

public class LinkedBag<T> implements BagInterface<T> 
{
	private Node firstNode; 
	private int numberOfEntries;
	
	//default constructor
	public LinkedBag()
	{
		firstNode = null;
		numberOfEntries = 0;
	}
	
	//gets the number of entries currently in this bag
	public int getCurrentSize()
	{
		return numberOfEntries;
	}

	//sees whether this bag is empty 
	public boolean isEmpty()
	{
		return numberOfEntries == 0;
	}

	public boolean add(T newEntry) 
	{
		//adds to beginning of chain
		Node newNode = new Node(newEntry);
		// make new node reference rest of chain
		newNode.next = firstNode;
		
		firstNode = newNode; //new node is at beginning of chain
		numberOfEntries++;
		
		return true;
	}

	//removes unspecified entry from this bag, if possible 
	public T remove() 
	{
		T result = null;
		if(firstNode != null)
		{
			result = firstNode.getData();
			firstNode = firstNode.getNextNode(); // removes first node from chain
			numberOfEntries--;
		}
		return result;
	}

	//removes one occurrence of a given entry from this bag, if possible
	public boolean remove(T anEntry) 
	{
		boolean result = false;
		Node nodeN = getReferenceTo(anEntry);
		
		if(nodeN != null)
		{
			//replaces located entry with entry in first node
			nodeN.setData(firstNode.getData());
			//removes first node
			firstNode = firstNode.getNextNode();
			numberOfEntries--;
			result = true;
		}
		
		return result;
	}
	
	//locates a given entry within this bag
	//returns a reference to the node containing the entry
	//if located, or null otherwise
	private Node getReferenceTo(T anEntry)
	{
		boolean found = false;
		Node currentNode = firstNode;
		
		while(!found && (currentNode != null))
		{
			if(anEntry.equals(currentNode.getData()))
				found = true;
			else
				currentNode = currentNode.getNextNode();
		}
		return currentNode;
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
		int frequency = 0;
		int counter = 0;
		Node currentNode = firstNode;
		
		while((counter < numberOfEntries) && (currentNode != null))
		{
			if(anEntry.equals(currentNode.getData()))
				frequency++;
				
			counter++;
			currentNode = currentNode.getNextNode();
		}
		
		return frequency;
	}

	//tests whether this bag contains a given entry
	public boolean contains(T anEntry) 
	{
		boolean found = false;
		Node currentNode = firstNode;
		while(!found && (currentNode != null))
		{
			if(anEntry.equals(currentNode.getData()))
				found = true;
			else
				currentNode = currentNode.getNextNode();
		}
		return found;
	}

	//retrieves all entries that are in this bag
	public T[] toArray() 
	{
		//cast is safe because the new array contains null entries
		@SuppressWarnings("unchecked")
		T[] result = (T[])new Object[numberOfEntries]; //unchecked cast
		
		int index = 0;
		Node currentNode = firstNode;
		
		while((index < numberOfEntries) && (currentNode != null))
		{
			result[index] = currentNode.getData();
			index++;
			currentNode = currentNode.getNextNode();
		}
		return result;
	}
	
	//returns the union of two bags
	public BagInterface<T> union(BagInterface<T> otherBag)
	{
		//create result bag that will contain the union
		BagInterface<T> last = new LinkedBag<>();
		T[] first = this.toArray();
		//adds each item in first array to last
		for(T item : first)
			last.add(item);
		
		T[] second = otherBag.toArray();
		//adds each item in second array to last
		for(T item : second)
			last.add(item);
		
		return last;
	}

	//returns the intersection of two bags
	public BagInterface<T> intersection(BagInterface<T> otherBag)
	{
		//creates bag to hold elements from first bag that will be compared with second array
		BagInterface<T> temp = new LinkedBag<>();
		//creates bag that will contain the intersection
		BagInterface<T> result = new LinkedBag<>();
		
		T[] first = this.toArray();
		//adds each element in first array to temporary bag
		for(T item: first)
			temp.add(item);
		
		T[] second = otherBag.toArray();
		
		for(T item: second) //iterates through the second array
			if(temp.contains(item)) //checks to see if temp array contains elements in second array
				result.add(item);   //if this is true the element is added to the result array
		
		return result;
	}

	//returns a bag that consists of the entries left in one collection after
	//removing the entries the occur in the second collection
	public BagInterface<T> difference(BagInterface<T> otherBag)
	{
		BagInterface<T> last = new LinkedBag<>();
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
	
	private class Node
	{
		private T data; //entry in bag
		private Node next; //link to next node
		
		//default constructor
		private Node(T dataPortion)
		{
			this(dataPortion, null);
		}
		//constructor
		private Node(T dataPortion, Node nextNode)
		{
			data = dataPortion;
			next = nextNode;
		}
		//accessor method
		private T getData()
		{
			return data;
		}
		//mutator method
		private void setData(T newData)
		{
			data = newData;
		}
		//accessor method
		private Node getNextNode()
		{
			return next;
		}
		//mutator method
		private void setNextNode(Node nextNode) 
		{
			next = nextNode;
		}
	}

}
