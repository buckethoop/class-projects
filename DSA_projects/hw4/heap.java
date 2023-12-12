public class heap
{
	private int data[];
	int count = 0;
	
	public heap()
	{
		data = new int[100];
	}
	
	//heap created one by one (sequentially)
	public int sequentialHeap(int entries[])
	{
		int count = 0;
		for(int i = 0; i<entries.length; i++)
		 {
			 data[i] = entries[i];
			 int j = (i-1)/2;
			 int k = i;
			 
			 while(k != 0)
			 {
				 if(data[k] > data[j])
				 {
					 int temp = data[k];
					 data[k] = data[j];
					 data[j] = temp;
					 count++;
				 }
				 k = j;
				 j = (k-1)/2;
			 }
		 }
		 return count;
	}
	
	public int remove()
	{
		int len = data.length;
		
		int lastElement = data[len-1];
		
		data[0] = lastElement;
		
		//decreases heap size by one
		len = len-1;
		//make root node a heap
		makeHeap(len,0);
		return len;
	}
	
	//converts nodes to heaps
	public void makeHeap(int n, int i)
	{
		int largest = i;
		int left = 2 * i +1;
		int right = 2 * i +2;
		
		if(left < n && data[left] > data[largest])
			largest = left;
		
		if(right < n && data[right] > data[largest])
			largest = right;
		
		if(largest != i)
		{
			int swap = data[i];
			data[i] = data[largest];
			data[largest] = swap;
			count++;
			//recursive call to make subtree a heap
			//if largest is not the root
			makeHeap(n,largest);
		}
	}
	
	//optimal version to create heap
	public int optimalHeap(int entries[])
	{
		//copies entries onto data field that will be used for the heap
		for(int i = 0; i < entries.length; i++)
			data[i] = entries[i];
		
		int count = 0;
		int s;
		//creation of the heap
		for(int i = data.length / 2; i >= 0; i--)
		{
			int j = 2 * i + 1;
			int k = i;
			
			while (j < data.length)
			{
				if((j+1) < data.length && data[j] < data[j+1])
					j++;
				
				if(data[k] >= data[j])
					break;
				
				s = data[k];
				data[k] = data[j];
				data[j] = s;
				k = j;
				j = 2*k +1;
				count++;
			}
		}
		return count;
	}
	
	public int get(int index)
	{
		return data[index];
	}

}