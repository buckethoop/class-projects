package graphalgs;

import java.util.Scanner;

public class Dijkstras 
{
	public static class Dijkstra extends Graphs{

		  public static void dijkstra(int[][] graph, int source) {
		    int count = graph.length;
		    boolean[] visitedVertex = new boolean[count];
		    int[] dist = new int[count];
		    for (int i = 0; i < count; i++) {
		      visitedVertex[i] = false;
		      dist[i] = Integer.MAX_VALUE;
		    }

		    dist[source] = 0;
		    for (int i = 0; i < count; i++) {


		      int u = findMinDist(dist, visitedVertex);
		      visitedVertex[u] = true;

		      for (int v = 0; v < count; v++) {
		        if (!visitedVertex[v] && graph[u][v] != 0 && (dist[u] + graph[u][v] < dist[v])) {
		          dist[v] = dist[u] + graph[u][v];
		        }
		      }
		    }
		    for (int i = 0; i < dist.length; i++) {
		      System.out.println(String.format("Distance from %s to %s is %s", source, i, dist[i]));
		    }

		  }

		  private static int findMinDist(int[] distance, boolean[] visitedVertex) {
		    int minDist = Integer.MAX_VALUE;
		    int minDistVertex = -1;
		    for (int i = 0; i < distance.length; i++) {
		      if (!visitedVertex[i] && distance[i] < minDist) {
		        minDist = distance[i];
		        minDistVertex = i;
		      }
		    }
		    return minDistVertex;
		  }

		  public static int[][] dijkstraFormat(int graph[][])
			{
				for(int i=0;i<graph.length;i++)
					for(int j=0;j<graph.length;j++)
						if(graph[i][j]==999999)
							graph[i][j]=0;
				return graph;
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
	        
			int graph[][] = dijkstraFormat(arrayGenerator(n,threshold));
			
		    Dijkstra.dijkstra(graph, 0);
		    
		    long endTime = System.nanoTime();
	        System.out.println("Execution time (in nanoseconds): " + (endTime - startTime));
	        input.close();
	        in.close();
		  }
		}
	



}
