package graphalgs;

import java.util.Random;



public class Graphs{
	public static int[][] arrayGenerator(int n, int threshold)
	{
		int graph[][] = new int[n][n];
		int min = 1;
		int max = 100;
		int random;
		
		Random rand = new Random();
		for(int i=0; i<graph.length;i++)
		{
			for(int j=0;j<graph.length;j++)
			{
				random = rand.nextInt(max - min)+min;
				if(random < threshold)
				{
					random = rand.nextInt(max-min) + min;
					graph[i][j] = random;
				}
				else
					graph[i][j]=999999;
			}
		}
		
		for(int i=0; i<graph.length;i++)
		{
			graph[i][i]=0;
		}

	return graph;
	}
	
	
	
}	
