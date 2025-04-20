void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    
  int zeroIdx=m;
  
  for(int j=0;j<nums2Size;j++)
  {
      nums1[zeroIdx]=nums2[j];
      zeroIdx++;
  }
  
  int minIdx;
  int temp;
  
  for(int k=0;k<nums1Size;k++)
  {
      minIdx=k;
      for(int l=k+1;l<nums1Size;l++)
      {
          if(nums1[minIdx]>nums1[l])
          {
              minIdx=l;
          }
      }
      
      temp=nums1[minIdx];
      nums1[minIdx]=nums1[k];
      nums1[k]=temp;
  }
  
}