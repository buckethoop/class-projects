import java.util.Scanner;
import java.util.Random;

public class Strassen 
{
	public int[][] mult(int[][]A, int[][]B)
	{
		int n = A.length;
		int[][]result = new int[n][n];
		
		if(n == 1)
			result[0][0] = A[0][0]*B[0][0];
		
		else
		{
			int[][] A_11 = new int[n / 2][n / 2];
		    int[][] A_12 = new int[n / 2][n / 2];
		    int[][] A_21 = new int[n / 2][n / 2];
		    int[][] A_22 = new int[n / 2][n / 2];
		    int[][] B_11 = new int[n / 2][n / 2];
		    int[][] B_12 = new int[n / 2][n / 2];
		    int[][] B_21 = new int[n / 2][n / 2];
		    int[][] B_22 = new int[n / 2][n / 2];
		    
		    split(A, A_11, 0, 0);
		    split(A, A_12, 0, n / 2);
		    split(A, A_21, n / 2, 0);
		    split(A, A_22, n / 2, n / 2);
		    
		    split(B, B_11, 0, 0);
		    split(B, B_12, 0, n / 2);
		    split(B, B_21, n / 2, 0);
		    split(B, B_22, n / 2, n / 2);
		    int[][] M1 = mult(add(A_11, A_22), add(B_11, B_22));
		    int[][] M2 = mult(add(A_21, A_22), B_11);
		    int[][] M3 = mult(A_11, subtract(B_12, B_22));
		    int[][] M4 = mult(A_22, subtract(B_21, B_11));
		    int[][] M5 = mult(add(A_11, A_12), B_22);
		    int[][] M6 = mult(subtract(A_21, A_11), add(B_11, B_12));
		    int[][] M7 = mult(subtract(A_12, A_22), add(B_21, B_22));
		    int[][] C_11 = add(subtract(add(M1, M4), M5), M7);
		    int[][] C_12 = add(M3, M5);
		    int[][] C_21 = add(M2, M4);
		    int[][] C_22 = add(subtract(add(M1, M3), M2), M6);
		    
		    join(C_11, result, 0, 0);
	     	join(C_12, result, 0, n / 2);
	     	join(C_21, result, n / 2, 0);
	     	join(C_22, result, n / 2, n / 2);
		}
		return result;
	}
	public int[][] subtract(int[][] A, int[][] B) 
	{
	    int n = A.length;
	    int[][] C = new int[n][n];

	    for (int i = 0; i < n; i++)
	      for (int j = 0; j < n; j++)
	        C[i][j] = A[i][j] - B[i][j];

	    return C;
	}
	
	public int[][] add(int[][] A, int[][] B) 
	{
	    int n = A.length;
	    int[][] C = new int[n][n];

	    for (int i = 0; i < n; i++)
	      for (int j = 0; j < n; j++)
	        C[i][j] = A[i][j] + B[i][j];

	    return C;

	}
	
	public void split(int[][] P, int[][] C, int iB, int jB) 
	{
	    for (int i1 = 0, i2 = iB; i1 < C.length; i1++, i2++)
	      for (int j1 = 0, j2 = jB; j1 < C.length; j1++, j2++)
	        C[i1][j1] = P[i2][j2];
	}

	public void join(int[][] C, int[][] P, int iB, int jB)
	{
		for(int i1 = 0, i2 = iB; i1 < C.length; i1++, i2++)
			for(int j1 = 0, j2 = jB; j1 < C.length; j1++, j2++)
				P[i2][j2] = C[i1][j1];
	}
	
	public void print(int [][] C, int size)
	{
		System.out.println("Matrix Result :\n");
		for (int i = 0; i < size; i++) 
        {
            for (int j = 0; j < size; j++)
                System.out.print(C[i][j] + " ");
            System.out.println();
        
        }
	}
	
	public static void main(String[] args)
    {
		long startTime = System.nanoTime();
        Strassen matrix = new Strassen();
        System.out.print("Enter the number n for size of the two matrices:");
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        
          
        int [][]a = new int[n][n];    
        int [][]b = new int[n][n];   
 
        Random r = new Random();
        int min = -9;
        int max = 9;
   
        
        for (int i = 0; i < n; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                a[i][j] = r.nextInt(max-min) + min;
            }
        }
        System.out.println("");
        
        for (int i = 0; i < n; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                b[i][j] = r.nextInt(max-min) + min;
            }
        }
 
        int C[][] = matrix.mult(a, b);
        matrix.print(C, n);
 
  
        System.out.println(
            "\nProduct of matrices A and  B : ");

        input.close();
        long endTime = System.nanoTime();
        System.out.println("Execution time (in nanoseconds): " + (endTime - startTime));
    }
}










