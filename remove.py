class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0 
        temp=head 
        while temp: 
            c+=1
            temp=temp.next 
        temp=head 
       
        while temp: 
            c-=1
            if c==n: 
                temp.next=temp.next.next 
                break
            if c<n: 
                head=temp.next 
                break

            
            temp=temp.next
        return head