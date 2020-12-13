def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])


def reverse_array(arr, start, end):
  while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start+=1
    end-=1
