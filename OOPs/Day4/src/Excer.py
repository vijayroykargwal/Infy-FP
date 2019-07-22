'''
Created on Mar 8, 2019

@author: vijay.pal01
'''
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        val=super().m1()+30
        return val
class C(B):
    def m1(self):
        val=self.m1()+20
        return val
obj=C()
print(obj.m1())