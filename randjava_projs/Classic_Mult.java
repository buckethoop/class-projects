import java.util.Random;
import java.util.Scanner;

public class Classic_Mult
{
    
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
     
    public static int[][] mult(int a[][], int b[][], int n) 
    { 
        int i, j, k;   
         
        int C[][] = new int[n][n]; 
  
        // Multiply the two matrices 
        for (i = 0; i < n; i++) 
        { 
            for (j = 0; j < n; j++) 
            { 
                for (k = 0; k < n; k++) 
                    C[i][j] += a[i][k] * b[k][j]; 
            } 
        }   
        
        System.out.println("\nResultant Matrix:"); 
        print(C,n);
        return C;
    }   
   
    public static void main(String[] args) 
    {
    	long startTime = System.nanoTime();
    	int n;    
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number n for size of the two matrices:");
        n = input.nextInt();   
        int A[][] = new int[n][n];   
        int B[][] = new int[n][n];   
        
        Random random = new Random();
        int min = -9;
        int max = 9;
        
        for (int i = 0; i < n; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                A[i][j] = random.nextInt(max-min) + min;
            }
        }
        System.out.println("");
        
        
        for (int i = 0; i < n; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                B[i][j] = random.nextInt(max-min) + min;
            }
        }            
   
        mult(A, B, n);    
        long endTime = System.nanoTime();
        System.out.println("Execution time (in nanoseconds): " + (endTime - startTime));
        input.close();
    }
}
