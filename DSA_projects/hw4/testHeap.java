import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class testHeap
{
	public static void main(String[] args)
	{
		//access input from file
		int arr[] = new int[100];
		try 
		{
			int i = 0;
			File in = new File("src/data.txt");
			Scanner src = new Scanner(in);
			//add elements to the array has long as there are numbers in the file 
			while(src.hasNextInt())
			{
				arr[i++] = src.nextInt();
			}
			src.close();
		} catch(FileNotFoundException e){
			System.out.println("An error occurred.");
			e.printStackTrace();
		}
		//creates new heap
		heap seqinsert = new heap();
		int count = seqinsert.sequentialHeap(arr);
		
		try
		{
			PrintWriter print = new PrintWriter("src/output.txt");
			print.write("Heap built using sequential insertions: ");
			//first 10 elements in heap
			for(int i = 0; i < 10; i++)
			{
				print.write(seqinsert.get(i) + ",");
			}
			
			print.write("...\n");
			print.write("Number of swaps in the heap creation: " + count + "\n");
			print.write("Heap after 10 removals: ");
			//10 removals from the heap
			for(int i=0; i<10;i++)
			{
				seqinsert.remove();
			}
			//prints heap after ten removals
			for(int i=0; i<10;i++)
			{
				print.write(seqinsert.get(i) + ",");
			}
			
			print.write("...\n\n");
			
			//creates another heap
			heap optimal = new heap();
			count = optimal.optimalHeap(arr);
			
			print.write("Heap built using optimal method: ");
			//print first 10 elements in heap
			for(int i = 0; i < 10; i++)
			{
				print.write(optimal.get(i) + ",");
			}
			
			print.write("...\n");
			print.write("Number of swaps in the heap creation: " + count + "\n");
			print.write("Heap after 10 removals: ");
			//performs 10 removals on the heap
			for(int i=0; i<10;i++)
			{
				optimal.remove();
			}
			//prints heap after 10 removals
			for(int i=0; i<10;i++)
			{
				print.write(optimal.get(i) + ",");
			}
			
			print.write("...\n\n");
			print.close();
		}catch(FileNotFoundException e){
			System.out.println("File not opened for writing");
		}
		
	}
	
}