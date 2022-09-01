class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
       
        int max = 0,start = 0, end = 1;
        
        while (end < prices.size())
        {
            if(prices[start]<prices[end])
            {
                max =  std::max(max,prices[end]-prices[start]);
                //(max>prices[end])? max : prices[end]-prices[start];
            }
            else
            {
                start = end;
            }
            end++;
        }
        return max;
        
    }
};