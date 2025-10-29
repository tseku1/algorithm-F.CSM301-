package lab3.java;

public class AlgorithmsDemo {
    public static int[] insertionSort(int[] arr) {
        for(int i = 1; i < arr.length; i++){      // C1 * n
            int key = arr[i];                     // C2 * (n-1)
            int j = i - 1;                        // C3 * (n-1)
            while (j >= 0 && arr[j] > key){       // C4 * (n(n-1))/2
                arr[j+1] = arr[j];                // C5 * (n(n-1))/2
                j--;                              // C6 * (n(n-1))/2
            }                                     
            arr[j+1] = key;                       // C7 * (n-1)
        }                                       
        return arr;                               // C8
        }

    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {                              // C1
            int mid = (left + right) / 2;                // C2 logn

            mergeSort(arr, left, mid);                   // рекурс
            mergeSort(arr, mid + 1, right);              // рекурс

            merge(arr, left, mid, right);                // C3 * n
        }
    }

    public static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;                         // C4
        int n2 = right - mid;                            // C5

        int[] L = new int[n1];                           // C6 * n1
        int[] R = new int[n2];                           // C7 * n2

        for (int i = 0; i < n1; i++) {                   // C8 * n1
            L[i] = arr[left + i];                        // C9 * n1
        }
        for (int j = 0; j < n2; j++) {                   // C10 * n2
            R[j] = arr[mid + 1 + j];                     // C11 * n2
        }

        int i = 0, j = 0, k = left;                      // C12

        while (i < n1 && j < n2) {                       // C13 * (n1+n2)
            if (L[i] <= R[j]) {                          // C14 
                arr[k++] = L[i++];                       // C15 
            } else {
                arr[k++] = R[j++];                       // C16 
            }
        }

        while (i < n1) {                                 // C17 * n1
            arr[k++] = L[i++];                           // C18 * n1
        }

        while (j < n2) {                                 // C19 * n2
            arr[k++] = R[j++];                           // C20 * n2
        }
    }

    public static int binarySearch(int[] arr, int left, int right, int x) {
        while (left <= right) {                          // C1 * log n
            int mid = left + (right - left) / 2;         // C2 * log n

            if (arr[mid] == x)                           // C3 * log n
                return mid;                              // C4 (амжилттай хайлт)

            if (arr[mid] < x)                            // C5 * log n
                left = mid + 1;                          // C6 * log n
            else
                right = mid - 1;                         // C7 * log n
        }
    return -1;                                       // C8
}

}
