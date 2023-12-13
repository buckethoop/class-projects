public class Sanity_Classic extends Classic_Mult
{
	public static void main(String[] args)
	{
		long startTime = System.nanoTime();
		int a[][] = {{2,0,-1,6},{3,7,8,0},{-5,1,6,-2},{8,0,2,7}};
    	int b[][] = {{0,1,6,3},{-2,8,7,1},{2,0,-1,0},{9,1,6,-2}};
    	
    	Classic_Mult.mult(a,b,a.length);
    	long endTime = System.nanoTime();
    	System.out.println("Execution time (in nanoseconds): " + (endTime - startTime));
	}
}
