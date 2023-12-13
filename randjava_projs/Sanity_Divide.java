
public class Sanity_Divide extends MatrixMultiplication
{
	public static void main(String[] args)
	{
		long startTime = System.nanoTime();
		int a[][] = {{2,0,-1,6},{3,7,8,0},{-5,1,6,-2},{8,0,2,7}};
    	int b[][] = {{0,1,6,3},{-2,8,7,1},{2,0,-1,0},{9,1,6,-2}};
    	
    	int result[][] = MatrixMultiplication.mult(a,b);
    	MatrixMultiplication.print(result, a.length);
    	long endTime = System.nanoTime();
    	System.out.println("Execution time (in nanoseconds): " + (endTime - startTime));
	}
}
