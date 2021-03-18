

public class rotateMatrix {
    public static void main(String[] args) {
        int[][] input = {{1,2,3},{4,5,6},{7,8,9}};
        layerSolution(input, 3);
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(input[i][j] + " ");
            }
            System.out.println("");

        }

    }

    public static  void layerSolution(int[][] arr, int n){
        int[] temp;
        int mid = n/2;
        for (int l=  0;  l<  n  / 2;  l++)
        {
            int first= l;
            int last =  n  - 1  -l;
            for(int i  = l; i  < last; i++) {
                int offset =  i-first;
                int top =  arr[first][i];
                arr[first][i] = arr[last-offset][first];
                arr[last-offset][first] = arr[last][last- offset];
                arr[last][last - offset] = arr[i][last];;
                arr[i][last] = top;
            }

        }
    }


}
