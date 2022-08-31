// Just Copy paste this solution on Leetcode!

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		// Declare unordered multimap to store the elements in vector and its indexes 
        unordered_multimap<int,int> vect;
		// Declare the vector to store the result
        vector<int> result(2,0);
		
		// Map the input vector into an unordered multimap
        for(int i=0; i<nums.size(); i++){
           vect.insert(pair<int,int>(nums[i],i));
        }
		
        // Search every element in the vector 
        for(int j=0; j<nums.size(); j++){
			// Find the other number of answer’s pair by subtracting that element from target value
            auto iter = vect.find(target - nums[j]);
			
			// If the number is found and they are not write indexes into the result vector and terminate the loop
            if((iter != vect.end() && (j != (*iter).second))){
                result[0] = j;
                result[1] = (*iter).second;
                break;
            }
        }
        return result;
    }
};