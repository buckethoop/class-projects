package project1;

import java.util.Arrays;

public class LinkedBagTest 
{
	public static void main(String[] args)
	{
		//creation of bag1
		BagInterface<String> bag1 = new LinkedBag<>();
		//creation of bag2
		BagInterface<String> bag2 = new LinkedBag<>();
		
		//adds 5 string elements to bag 1 
		bag1.add("A");
		bag1.add("B");
		bag1.add("C");
		bag1.add("D");
		bag1.add("E");
		//adds 5 string elements to bag 2
		bag2.add("C");
		bag2.add("D");
		bag2.add("E");
		bag2.add("F");
		bag2.add("G");
		
		//prints the union of bags 1 and 2
		System.out.println(Arrays.toString(bag1.union(bag2).toArray()));
		//prints the intersection of bags 1 and 2
		System.out.println(Arrays.toString(bag1.intersection(bag2).toArray()));
		//prints the difference of bags 1 and 2
		System.out.println(Arrays.toString(bag1.difference(bag2).toArray()));
		//prints the difference of bags 2 and 1
		System.out.println(Arrays.toString(bag2.difference(bag1).toArray()));

	}
}
