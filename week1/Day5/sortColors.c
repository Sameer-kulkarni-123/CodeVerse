void sortColors(int* nums, int numsSize) {

  int i, j, min_idx;

for (i = 0; i < numsSize-1; i++) {
  min_idx = i;
  for (j = i+1; j < numsSize; j++)
    if (nums[j] < nums[min_idx])
      min_idx = j;

  int temp = nums[min_idx];
  nums[min_idx] = nums[i];
  nums[i] = temp;
}
}
  
