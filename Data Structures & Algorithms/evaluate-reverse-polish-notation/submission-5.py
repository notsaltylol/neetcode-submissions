class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for s in tokens:
            if s == '+':
                b = int(st.pop())
                a = int(st.pop())
                st.append(a+b)
            elif s =='-':
                b = int(st.pop())
                a = int(st.pop())
                st.append(a-b)
            elif s =='*':
                b = int(st.pop())
                a = int(st.pop())
                st.append(a*b)
            elif s == '/':
                b = int(st.pop())
                a = int(st.pop())
                st.append(int(a/b))
            else:
                st.append(s)
            # print(st)
        return int(st.pop())