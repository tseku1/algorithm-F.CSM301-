package lab2.java;

public class Sort {

    public static int[] insertionSort(int[] arr) {
       for(int i = 1; i < arr.length; i++){    // C1*n
         int key = arr[i];                     // C2*(n-1)
         int j = i - 1;                        // C3*(n-1)
         while (j >= 0 && arr[j] > key){       // C4*n(n-1) / 2
            arr[j+1] = arr[j];                 // C5 
            j--;                               // C6 
         }                                     //
         arr[j+1] = key;                       // C7
       }                                       //
       return arr;                             // C8 

       
    }

    public static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) return arr;
        int mid = arr.length / 2;
        int[] left = mergeSort(java.util.Arrays.copyOfRange(arr, 0, mid));
        int[] right = mergeSort(java.util.Arrays.copyOfRange(arr, mid, arr.length));
        return merge(left, right);
    }

    private static int[] merge(int[] left, int[] right) {
        int[] result = new int[left.length + right.length];
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) result[k++] = left[i++];
            else result[k++] = right[j++];
        }
        while (i < left.length) result[k++] = left[i++];
        while (j < right.length) result[k++] = right[j++];
        return result;
    }

    public static int binarySearch(int[] arr, int target, int low, int high) {
       if(low > high) return -1;
       int mid = (low+high) / 2;
       if(arr[mid] == target) return mid;
       else if (arr[mid] > target) return binarySearch(arr, target, low, mid-1);
       else return binarySearch(arr, target, mid+1, mid);
    }

    public static int findMax(int[] arr) {
        if (arr.length == 1) return arr[0];
        int mid = arr.length / 2;
        int leftMax = findMax(java.util.Arrays.copyOfRange(arr, 0, mid));
        int rightMax = findMax(java.util.Arrays.copyOfRange(arr, mid, arr.length));
        return Math.max(leftMax, rightMax);
    }
}
