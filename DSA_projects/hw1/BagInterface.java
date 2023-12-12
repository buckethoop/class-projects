package project1;

public interface BagInterface<T> 
{
	//gets the current number of entries in the bag
	public int getCurrentSize();
	//sees whether this bag is empty
	public boolean isEmpty();
	//adds a new entry to this bag
	public boolean add(T newEntry);
	//removes one unspecified entry from this bag, if possible
	public T remove();
	//removes one occurrence of a given entry from this bag, if possible
	public boolean remove(T anEntry);
	//removes all entries from this bag
	public void clear();
	//counts the number of times a given entry appears in this bag
	public int getFrequencyOf(T anEntry);
	//tests whether this bag contains a given entry
	public boolean contains(T anEntry);
	//retrieves all entries that are in this bag
	public T[] toArray();
	//returns a bag that consists of all contents in two collections
	BagInterface<T> union(BagInterface<T> otherBag);
	//returns a bag that consists of the entries that occur in both collections
	BagInterface<T> intersection(BagInterface<T> otherBag);
	//returns a bag that consists of the entries left in one collection after
	//removing the entries the occur in the second collection
	BagInterface<T> difference(BagInterface<T> otherBag);
}
