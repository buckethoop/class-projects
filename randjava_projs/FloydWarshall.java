package graphalgs;

import java.util.Scanner;

public class FloydWarshall extends Graphs
{
	
	  final static int INF = 999999;

	  void floydWarshall(int graph[][]) {
	    int n = graph.length;
		int matrix[][] = new int[n][n];
	    int i, j, k;

	    for (i = 0; i < n; i++)
	      for (j = 0; j < n; j++)
	        matrix[i][j] = graph[i][j];

	    for (k = 0; k < n; k++) {
	      for (i = 0; i < n; i++) {
	        for (j = 0; j < n; j++) {
	          if (matrix[i][k] + matrix[k][j] < matrix[i][j])
	            matrix[i][j] = matrix[i][k] + matrix[k][j];
	        }
	      }
	    }
	    printMatrix(matrix);
	  }

	  void printMatrix(int matrix[][]) {
	    int n = matrix.length;
		for (int i = 0; i < n; ++i) {
	      for (int j = 0; j < n; ++j) {
	        if (matrix[i][j] == INF)
	          System.out.print("INF ");
	        else
	          System.out.print(matrix[i][j] + "  ");
	      }
	      System.out.println();
	    }
	  }

	  public static void main(String[] args) 
	  {
		long startTime = System.nanoTime();
    	int n, threshold;    
        
    	Scanner input = new Scanner(System.in);
        System.out.print("Enter the number n for number of verticies:");
        n = input.nextInt();
        
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a threshold: ");
		threshold = in.nextInt();
		  
		FloydWarshall a = new FloydWarshall();
	    a.floydWarshall(arrayGenerator(n,threshold));
	    
	    long endTime = System.nanoTime();
        System.out.println("Execution time (in nanoseconds): " + (endTime - startTime));
        input.close();
        in.close();
	  }
	
}
