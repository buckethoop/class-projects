import java.util.*;

class MatrixMultiplication

{

	static int n;
	
	public static void main(String[] args)
	
	{
    	long startTime = System.nanoTime();
		Scanner input = new Scanner(System.in);
		System.out.println("Enter value for n to create (n * n dimension Matrix):");
		n = input.nextInt(); 
		int i = 0;
		int j = 0;
		
		int [][]A = new int[n][n];
		int [][]B = new int[n][n];
		int [][]C = new int[n][n];
		
		Random random = new Random();
        int min = -9;
        int max = 9;
		
		
		for(i=0;i<n;i++) 
		{
			for(j=0;j<n;j++)
			{
				A[i][j] = random.nextInt(max-min) + min;
			}
		}
		
		
		for(i=0;i<n;i++) 
		{
			for(j=0;j<n;j++)
			{
				B[i][j] = random.nextInt(max-min) + min;	
			}
		}
		
		C = mult(A,B); 
		
		long endTime = System.nanoTime();
		System.out.println("Result Matrix:");
		
		print(C,n);		
		input.close();
		System.out.println("Execution time (in nanoseconds): "+(endTime-startTime));
		
	}
			
		public static void copyToWhole(int[][] from, int[][] to, int startRow, int startCol)
		{
			for (int i = 0; i < from.length; i++)
				for (int j = 0; j < from.length; j++)
					to[i+startRow][j+startCol] = from[i][j];
		}
				
		public static void copyToPart(int[][] from, int[][] to, int startRow, int startCol)
		{
			for (int i = 0; i < to.length; i++) 
				for (int j = 0; j < to.length; j++) 
					to[i][j] = from[i+startRow][j+startCol];
		} 
		
		
		public static int[][] add(int[][] a, int[][] b)
		{
			int result[][] = new int[a.length][a.length];
		
			for (int i = 0; i < a.length; i++) 
			{
				for (int j = 0; j < a.length; j++)
					result[i][j] = a[i][j] + b[i][j];
			}
		
			return result;
		
		} 
		
		public static void print(int matrix[][], int row_col_size) 
	    { 
	        for (int i = 0; i < row_col_size; i++) 
	        { 
	            for (int j = 0; j < row_col_size; j++) 
	            {
	                System.out.print(matrix[i][j] + " "); 
	            }
	  
	            System.out.println(); 
	        } 
	    }
		
		public static int[][] mult(int[][] a, int[][] b)
		
		{
			int n = a.length;
			
			int[][] result = new int[n][n]; 
			
			if (n == 1)
				result[0][0] = a[0][0] * b[0][0];
			
			else 
			{ 
				int[][] A11 = new int[n/2][n/2];
				int[][] A12 = new int[n/2][n/2];
				int[][] A21 = new int[n/2][n/2];
				int[][] A22 = new int[n/2][n/2];
				int[][] B11 = new int[n/2][n/2];
				int[][] B12 = new int[n/2][n/2];
				int[][] B21 = new int[n/2][n/2];
				int[][] B22 = new int[n/2][n/2];
				
				copyToPart(a, A11, 0, 0);
				copyToPart(a, A12, 0, n/2);
				copyToPart(a, A21, n/2, 0);
				copyToPart(a, A22, n/2, n/2);
				
				copyToPart(b, B11, 0, 0);
				copyToPart(b, B12, 0, n/2);
				copyToPart(b, B21, n/2, 0);
				copyToPart(b, B22, n/2, n/2);
				
				int[][] C11 = add( mult(A11, B11), mult(A12, B21) );
				int[][] C12 = add( mult(A11, B12), mult(A12, B22) );
				int[][] C21 = add( mult(A21, B11), mult(A22, B21) );
				int[][] C22 = add( mult(A21, B12), mult(A22, B22) );
				
				copyToWhole(C11, result, 0, 0);
				copyToWhole(C12, result, 0, n/2);
				copyToWhole(C21, result, n/2, 0);
				copyToWhole(C22, result, n/2, n/2);
			}
			return result;
		} 
}