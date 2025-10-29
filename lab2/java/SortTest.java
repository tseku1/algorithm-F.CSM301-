package lab2.java;

import org.junit.Test;
import static org.junit.Assert.*;

public class SortTest {
    @Test
    public void testInsertionSort() {
        int[] input = {5, 2, 4, 6, 1};
        int[] expected = {1, 2, 4, 5, 6};
        assertArrayEquals(expected, Sort.insertionSort(input));
    }

    @Test
    public void testMergeSort() {
        int[] input = {5, 2, 4, 6, 1};
        int[] expected = {1, 2, 4, 5, 6};
        assertArrayEquals(expected, Sort.mergeSort(input));
    }

    @Test
    public void testBinarySearchFound() {
        int[] sorted = {1, 2, 3, 4, 5};
        assertEquals(2, Sort.binarySearch(sorted, 3, 0, sorted.length - 1));
    }

    @Test
    public void testBinarySearchNotFound() {
        int[] sorted = {1, 2, 3, 4, 5};
        assertEquals(-1, Sort.binarySearch(sorted, 6, 0, sorted.length - 1));
    }

    @Test
    public void testFindMax() {
        int[] input = {1, 9, 3, 7};
        assertEquals(9, Sort.findMax(input));
    }
}
