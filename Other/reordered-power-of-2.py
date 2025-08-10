class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
            def sort_digits(x: int) -> str:
                return ''.join(sorted(str(x)))
            
            target = sort_digits(n) # Sort n

            # check target with all 2's power till 2^30, as 2^30 > 10^9
            # 1 << i is bitwise left shift equivalent of 2**i
            for i in range(31):
                if sort_digits(1 << i) == target: 
                    return True 
            return False

# 869. Reordered Power of 2	
#  Range of i   1 << i time (seconds)	  2**i time (seconds)
# 0..30	        0.025	                  0.040
# 0..1000	      0.145	                  1.295

# Interpretation:
# For small i (like your 0..30 loop), the difference is tiny — both are microsecond-level fast.
# For larger i (up to 1000 here), 1 << i is about 9× faster because shifting is simpler than repeated multiplications.
