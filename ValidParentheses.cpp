class Solution {
public:
    bool isValid(string s) {
        stack<int> sta;
        for(int i=0; i< s.length();i++)
        {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[')
            {
                sta.push(s[i]);
            }
            else if( s[i] == ')' || s[i] == '}' || s[i] == ']')
            {
                if( sta.empty() == false && s[i] == ')' && sta.top() == '(' )
                {
                    sta.pop();
                }
                else if( sta.empty() == false && s[i] == '}' && sta.top() == '{')
                {
                    sta.pop();
                }
                else if( sta.empty() == false && s[i] == ']' && sta.top() == '[')
                {
                    sta.pop();
                }
                else
                {
                    return false;
                }
            }
            
        }
        if(sta.empty() == false)
        {
            return false;
        }
        return true;
        
    }
};